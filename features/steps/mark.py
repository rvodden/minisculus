from behave import given
from behave.runner import Context

from minisculus import MarkOne, MarkTwo


@given("a mark one machine with its wheel set to {}")
def a_mark_one_machine_with_its_wheel_set_to(context: Context, wheel_value: int):
    """
    Args:
        context: The feature context.
        wheel_value: The value of the wheel.
    """
    context.mark = MarkOne(wheel_value)


@given("a mark two machine with its wheels set to {} and {}")
def a_mark_two_machine_with_its_wheels_set_to_and(
    context: Context, wheel1_value: int, wheel2_value: int
):
    """
    Args:
        context: The feature context.
        wheel1_value: The value the first wheel should be set to.
        wheel2_value: The value the second wheel should be set to.
    """
    context.mark = MarkTwo(wheel1_value, wheel2_value)
