from thinking_tests.current import current_case
from thinking_tests.decorators import case

accumulator = []

@case
def case1():
    accumulator.append(current_case())

@case
def case2():
    accumulator.append(current_case())