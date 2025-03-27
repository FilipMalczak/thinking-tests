from abc import abstractmethod
from contextlib import contextmanager
from typing import Protocol, ContextManager

from thinking_tests.protocol import TestStage, ThinkingCase, ThinkingSuite


class TestAspect(Protocol):
    @abstractmethod
    def around_case(self, stage: TestStage, case: ThinkingCase) -> ContextManager: pass

    @contextmanager
    def around_suite(self, suite: ThinkingSuite) -> ContextManager:
        yield