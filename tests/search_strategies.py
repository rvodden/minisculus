from hypothesis.strategies import SearchStrategy, integers, composite, one_of

from minisculus.wheel import SimpleWheel, StatefulWheel, Wheel


@composite
def simple_wheels(draw):
    min_value = draw(integers(), label="min_value")
    max_value = draw(integers(min_value=min_value + 1), label="max_value")
    factor = draw(
        integers(min_value=-9, max_value=9).filter(lambda x: x != 0), label="factor"
    )
    value = draw(integers(min_value=min_value, max_value=max_value), label="value")
    return SimpleWheel(min_value, max_value).set_factor(factor).set_value(value)


@composite
def stateful_wheels(draw):
    factor = draw(
        integers(min_value=-9, max_value=9).filter(lambda x: x != 0), label="factor"
    )
    return StatefulWheel().set_factor(factor)


def wheels() -> SearchStrategy[Wheel]:
    return one_of(simple_wheels(), stateful_wheels())
