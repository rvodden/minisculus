from hypothesis.strategies import SearchStrategy, integers, composite, one_of, text

from minisculus import Encoder
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


def valid_wheel_values() -> SearchStrategy[int]:
    return integers(min_value=0, max_value=9)


def valid_indexes() -> SearchStrategy[int]:
    return integers(min_value=0, max_value=len(Encoder._alphabet))


def valid_factors() -> SearchStrategy[int]:
    return integers(min_value=-9, max_value=9).filter(lambda x: x != 0)


def valid_characters() -> SearchStrategy[str]:
    return text(alphabet=Encoder._alphabet, min_size=1, max_size=1)
