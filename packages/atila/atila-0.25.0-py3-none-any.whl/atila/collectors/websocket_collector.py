from .grpc_collector import GRPCStreamCollector
from io import BytesIO
from rs4.protocols.sock.impl.ws import *
from rs4.protocols.sock.impl.ws.collector import Collector as BaseWebsocketCollector
import atila
import asyncio

class WebsocketCollector (BaseWebsocketCollector, GRPCStreamCollector):
    is_continue_request = True

    def __init__ (self, handler, request, *args):
        self.handler = handler
        self.request = request
        self.content_length = -1

        self.msgs = []
        self.rfile = BytesIO ()
        self.masks = b""
        self.has_masks = True
        self.buf = b""
        self.payload_length = 0
        self.opcode = None
        self.default_op_code = OPCODE_TEXT
        self.ch = self.channel = request.channel
        self.initialize_stream_variables ()

    def collect_incoming_data (self, data):
        if not data:
            # closed connection
            self.close ()
            return

        if self.masks or (not self.has_masks and self.payload_length):
            self.rfile.write (data)
        else:
            self.buf += data

    def start_collect (self):
        self.channel.set_terminator (2)
        self.first_data and self.continue_request ()

    def flush (self):
        if not self.proxy:
            return
        while self.msgs:
            self.queue.append (self.msgs.pop (0))
            self.callback ()
        if self.end_of_data:
            self.callback ()

    def close (self):
        if self.end_of_data:
            return
        self.channel.journal ('websocket spec.{}'.format (atila.WS_COROUTINE))
        GRPCStreamCollector.close (self)
        self.end_of_data = True

    def handle_message (self, msg):
        GRPCStreamCollector.handle_message (self, msg)
        self.flush ()


class WebsocketAsyncCollector (WebsocketCollector):
    is_continue_request = False

    def __init__ (self, handler, request, *args):
        super ().__init__ (handler, request, *args)
        self.mq = asyncio.Queue ()
        self.loop = asyncio.get_event_loop ()

    async def get (self):
        return await self.mq.get ()

    def set_channel (self, channel):
        self.ch = self.channel = channel
        self.channel.set_terminator (2)

    def start_collect (self):
        pass

    def handle_message (self, msg):
        self.loop.call_soon_threadsafe (self.mq.put_nowait, msg)

    def close (self):
        if self.closed:
            return
        self.loop.call_soon_threadsafe (self.mq.put_nowait, None)
        self.channel and self.channel.close ()
        self.closed = True
