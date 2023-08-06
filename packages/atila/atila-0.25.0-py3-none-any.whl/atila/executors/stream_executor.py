from . import ws_executor
import inspect
import threading

class Executor (ws_executor.Executor):
    def respond_async (self, was, task):
        ws_executor.deallocate_was (was)

    async def handle_async_stream (self, context, wsfunc):
        context.stream = await context.stream.open ()
        if hasattr (context.stream, 'aiochannel'):
            if self.env ["wsgi.route_options"]['grpc.input_stream']:
                some = wsfunc (context, context.stream)
            else:
                pr = await context.stream.receive ()
                some = wsfunc (context, pr)
        else:
            some = wsfunc (context, **self.env.get ("stream.params", {}))

        if inspect.isasyncgen (some):
            async for m in some:
                await context.stream.send (m)
        else:
            r = await some
            r and await context.stream.send (r)
        context.stream.close ()

    def __call__ (self):
        self.was = self.env ["skitai.was"]
        current_app, wsfunc = self.env.get ("stream.handler")
        self.is_async_executor_running ()
        coro = self.handle_async_stream (self.env ['skitai.was'], wsfunc)
        return self.add_async_task (coro, pooling = False)