from test_fixture.acc import ACCUMULATOR
from thinking_tests.adapter import ThinkingAdapter
from thinking_tests.protocol import CaseCoordinates
from thinking_tests.start import run_all

if __name__ == "__main__":
    result = run_all()

    assert [
        CaseCoordinates('test_fixture.x', 'case_x_1'), 
        CaseCoordinates('test_fixture.x', 'case_x_2'), 
        CaseCoordinates('test_fixture.y', 'case_y_1'), 
        CaseCoordinates('test_fixture.y', 'case_y_2'), 
        CaseCoordinates('test_fixture.y', 'case_y_3')
    ] == ACCUMULATOR

    assert result.testsRun == 5
    assert result.errors == []
    assert len(result.failures) == 1
    failure = result.failures[0][0]
    assert isinstance(failure, ThinkingAdapter)
    assert failure.case.coordinates == CaseCoordinates('test_fixture.y', 'case_y_3')