from enum import Enum, auto
from functools import reduce
from typing import NewType, Callable, Iterable, Self, Optional


Handler = NewType('Handler', Callable[[any], any])


class HandlerKeeper:
    """
    Mixin class for conveniently getting handlers from an input collection and
    unlimited input arguments.
    """

    def __init__(self, handler_resource: Handler | Iterable[Handler], *handlers: Handler):
        self.handlers = (
            tuple(handler_resource)
            if isinstance(handler_resource, Iterable)
            else (handler_resource, )
        ) + handlers


class ReturnFlag(Enum):
    """
    Enum return method flags class.
    
    Describe the returned result from something (MultipleHandler).
    """

    first_received = auto()
    last_thing = auto()
    everything = auto()
    nothing = auto()


class MultipleHandler(HandlerKeeper):
    """
    Handler proxy class for representing multiple handlers as a single
    interface.

    Applies its handlers to a single resource.

    Return data is described using the ReturnFlag of the return_flag attribute.
    """

    def __init__(
        self,
        handler_resource: Handler | Iterable[Handler],
        *handlers: Handler,
        return_flag: ReturnFlag = ReturnFlag.first_received
    ):
        super().__init__(handler_resource, *handlers)
        self.return_flag = return_flag

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({', '.join(map(str, self.handlers))})"

    def __call__(self, resource: any) -> any:
        result_of_all_handlers = list()

        for handler in self.handlers:
            handler_result = handler(resource)

            if self.return_flag == ReturnFlag.everything:
                result_of_all_handlers.append(handler_result)

            if self.return_flag == ReturnFlag.first_received and handler_result is not None:
                return handler_result

        if self.return_flag == ReturnFlag.everything:
            return result_of_all_handlers

        if self.return_flag == ReturnFlag.last_thing:
            return handler_result


class ActionChain(HandlerKeeper):
    """
    Class that implements handling as a chain of actions of handlers.

    Each next handler gets the output of the previous one.
    Data returned when called is data exited from the last handler.

    If there are no handlers, spits out the input as output.
    """

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({' -> '.join(map(str, self.handlers))})"

    def __call__(self, resource: any) -> any:
        return reduce(
            lambda resource, handler: handler(resource),
            (resource, *self.handlers)
        )


class Brancher:
    """
    Class that implements branching handling of something according to a certain
    condition.

    Selects the appropriate handler based on the results of the
    condition_resource_checker.

    In case of a negative case and the absence of a negative case handler, returns
    None.
    """

    def __init__(
        self,
        positive_case_handler: Handler,
        condition_resource_checker: Callable[[any], bool],
        negative_case_resource: Optional[Handler] = None
    ):
        self.positive_case_handler = positive_case_handler
        self.condition_resource_checker = condition_resource_checker
        self.negative_case_resource = negative_case_resource

    @property
    def negative_case_handler(self) -> Handler:
        return (
            self.negative_case_resource
            if self.negative_case_resource is not None
            else lambda _: None
        )

    @negative_case_handler.setter
    def negative_case_handler(self, negative_case_resource: Optional[Handler]) -> None:
        self.negative_case_resource = negative_case_resource

    def __repr__(self) -> str:
        return "{class_name}({positive_case_handler} if {condition_checker}{else_part})".format(
            class_name=self.__class__.__name__,
            positive_case_handler=self.positive_case_handler,
            condition_checker=self.condition_resource_checker,
            else_part=(
                f' else {self.negative_case_handler}'
                if self.negative_case_resource is not None
                else str()
            )
        )

    def __call__(self, resource: any) -> any:
        return (
            self.positive_case_handler
            if self.condition_resource_checker(resource)
            else self.negative_case_handler
        )(resource)


class EventAdapter:
    """
    Adapter class for combining the Handler interface with callable entities
    that do not require input data.
    """

    def __init__(self, event: Callable[[], any]):
        self.event = event

    def __repr__(self) -> str:
        return f"<Event {self.event}>"

    def __call__(self, _: any) -> any:
        return self.event()


class HandlingNode:
    """
    Class that allows to handle a resource but not return the results of its
    handling to continue the chain of handling this resource.
    """

    def __init__(self, handler: Handler):
        self.handler = handler

    def __repr__(self) -> str:
        return f"<Handling node {self.handler}>"

    def __call__(self, resource: any) -> any:
        self.handler(resource)
        return resource


class ErrorRaiser:
    """Adapter class for raising an error using calling."""

    def __init__(self, error: Exception):
        self.error = error

    def __repr__(self) -> str:
        return f"<Riser of \"{self.error}\">"

    def __call__(self) -> None:
        raise self.error


class Mapper:
    """
    Map adapter class.

    Works just like map with the exception of returning already saved results.
    Can be replaced by partial(map, handler).
    """

    def __init__(self, handler: Handler):
        self.handler = handler

    def __repr__(self) -> str:
        return f"<Mapper of {self.handler}>"

    def __call__(self, collection: Iterable) -> tuple:
        return tuple(self.handler(item) for item in collection)


class CollectionExpander:
    """Class for getting a collection with additional elements."""
    
    def __init__(self, adding_items: Iterable):
        self.adding_items = adding_items

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} of [{', '.join(map(str, self.adding_items))}]>"

    def __call__(self, collection: Iterable) -> tuple:
        return (*collection, *self.adding_items)


def return_(resource: any) -> any:
    """Stub function for handling emulation."""

    return resource