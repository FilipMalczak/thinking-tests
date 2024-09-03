from thinking_modules.model import ModuleName

from test_fixture.acc import ACCUMULATOR
from thinking_tests.adapter import ThinkingAdapter
from thinking_tests.protocol import CaseCoordinates, TestStage
from thinking_tests.running.start import run_all

if __name__ == "__main__":

    result = run_all()
    assert [
        CaseCoordinates(ModuleName.of('test_fixture.x'), 'case_x_1', 10),
        CaseCoordinates(ModuleName.of('test_fixture.x'), 'case_x_2', 14),
        CaseCoordinates(ModuleName.of('test_fixture.y'), 'case_y_1', 13),
        CaseCoordinates(ModuleName.of('test_fixture.y'), 'case_y_2', 17),
        CaseCoordinates(ModuleName.of('test_fixture.y'), 'case_y_3', 21)
    ] == ACCUMULATOR

    assert result.testsRun == 5
    assert result.errors == []
    assert len(result.failures) == 1
    failure = result.failures[0][0]
    assert isinstance(failure, ThinkingAdapter)
    assert failure.case.coordinates == ACCUMULATOR[-1]
    run_exec_details = failure.case.execution_details[TestStage.RUN]
    assert run_exec_details.stdout == "to stdout\n"
    assert run_exec_details.stderr == "to stderr\n"
    #todo assert there are headers in all stage logs and stacktrace in teardown logs
