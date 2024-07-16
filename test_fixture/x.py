from test_fixture.acc import ACCUMULATOR
from thinking_tests.current import current_coordinates
from thinking_tests.decorators import case
from thinking_tests.protocol import CaseCoordinates
from thinking_tests.start import run_current_module


@case
def case_x_1():
    ACCUMULATOR.append(current_coordinates())

@case
def case_x_2():
    ACCUMULATOR.append(current_coordinates())



if __name__ == "__main__":
    result = run_current_module()

    assert [
        CaseCoordinates('__main__', 'case_x_1'),
        CaseCoordinates('__main__', 'case_x_2')
    ] == ACCUMULATOR

    assert result.testsRun == 2
    assert result.errors == []
    assert result.failures == []