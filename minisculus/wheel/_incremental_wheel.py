from minisculus.wheel._incremental_factor_wheel import IncrementalFactorWheel


class IncrementalWheel(IncrementalFactorWheel):
    """A wheel which functions by incrementing the character by the set value."""

    def __init__(self, min_value: int = 0, max_value: int = 9) -> None:
        super().__init__(min_value, max_value)
        self.factor = 1
