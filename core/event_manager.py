from typing import Callable, Dict, List

class EventManager:
    """A simple event manager for inter-component communication."""

    def __init__(self):
        self._events: Dict[str, List[Callable]] = {}

    def subscribe(self, event_type: str, callback: Callable):
        """Subscribe to an event."""
        if event_type not in self._events:
            self._events[event_type] = []
        self._events[event_type].append(callback)

    def unsubscribe(self, event_type: str, callback: Callable):
        """Unsubscribe from an event."""
        if event_type in self._events:
            self._events[event_type].remove(callback)

    def post(self, event_type: str, data: any = None):
        """Post an event to all subscribers."""
        if event_type in self._events:
            for callback in self._events[event_type]:
                callback(data)
