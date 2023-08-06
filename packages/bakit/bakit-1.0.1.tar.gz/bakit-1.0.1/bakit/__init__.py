'''
# BAKit
Built-in Alternative Kit

'''

from .Events import Event, Events
from .Queue import Queue
from .tasks_queue import TasksQueue
from .Copy import copy
from .Defer import defer

__version__ = "1.0.1"
__all__ = ["Event", "Events", "Queue", "tasks_queue", "copy"]