import sys

from thinking_modules.model import ModuleName

from test_fixture.acc import ACCUMULATOR
from thinking_tests.adapter import ThinkingAdapter
from thinking_tests.current import current_coordinates
from thinking_tests.decorators import case
from thinking_tests.protocol import CaseCoordinates
from thinking_tests.running.start import run_current_module


@case
def case_y_1():
    ACCUMULATOR.append(current_coordinates())

@case
def case_y_2():
    ACCUMULATOR.append(current_coordinates())

@case
def case_y_3():
    ACCUMULATOR.append(current_coordinates())
    print("to stdout")
    print("to stderr", file=sys.stderr)
    assert False


if __name__ == "__main__":
    result = run_current_module()

    assert [
        CaseCoordinates(ModuleName.of('__main__'), 'case_y_1', 13),
        CaseCoordinates(ModuleName.of('__main__'), 'case_y_2', 17),
        CaseCoordinates(ModuleName.of('__main__'), 'case_y_3', 21)
    ] == ACCUMULATOR

    assert result.testsRun == 3
    assert result.errors == []
    assert len(result.failures) == 1
    failure = result.failures[0][0]
    assert isinstance(failure, ThinkingAdapter)
    assert failure.case.coordinates == ACCUMULATOR[-1]