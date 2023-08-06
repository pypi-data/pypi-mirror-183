from typing import Callable, Dict, List

from client import app


class ListenManager:
    class Listener:
        def __init__(self, event_name: str):
            app().event(event_name)(self.on_event)
            self.listeners: List[Callable] = []

        def register(self, listener: Callable):
            self.listeners.append(listener)

        def unregister(self, listener: Callable):
            self.listeners.remove(listener)

        def on_event(self, event):
            for listener in self.listeners:
                listener(event)

    registered_listeners: Dict[str, Listener] = {
        "message": Listener("message"),
        "message_replied": Listener("message_replied"),
    }

    def __init__(self):
        raise RuntimeError("This class cannot create instance")

    @staticmethod
    def register_command(command_name: str, listener: Callable):
        app.command(command=command_name)(listener)

    @classmethod
    def register_event(cls, event_name: str, listener: Callable):
        if event_name in cls.registered_listeners.keys():
            cls.registered_listeners[event_name].register(listener)
        else:
            app.event(event_name)(listener)

    @classmethod
    def unregister_event(cls, listener: Callable):
        for registered_listener in cls.registered_listeners.values():
            if listener in registered_listener.listeners:
                registered_listener.unregister(listener)
