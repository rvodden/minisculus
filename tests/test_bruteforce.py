from datetime import timedelta

from hamcrest import assert_that, is_
from hypothesis import given, settings
from hypothesis.strategies import data, text, DataObject, integers

from minisculus import Encoder, MarkFour
from minisculus import BruteForce


class TestBruteForce:

    # This test is slow, so up the deadline and crank the examples down for CI.
    @settings(deadline=timedelta(milliseconds=500), max_examples=10)
    @given(
        text(min_size=10, max_size=256, alphabet=Encoder._alphabet),
        integers(min_value=0, max_value=9),
        integers(min_value=0, max_value=9),
        data(),
    )
    def test_brute_force(
        self, message: str, wheel1_value: int, wheel2_value: int, data: DataObject
    ):
        # generate clues:
        number_of_clues = data.draw(integers(min_value=1, max_value=2))
        min_clue_length = 4
        clues = []
        for number_of_clues in range(number_of_clues):
            start_character = data.draw(
                integers(min_value=0, max_value=len(message) - min_clue_length - 1)
            )
            end_character = data.draw(
                integers(
                    min_value=start_character + min_clue_length, max_value=len(message)
                )
            )
            clues.append(message[start_character:end_character])
        mark_four = MarkFour(wheel1_value, wheel2_value)
        encoded_message = mark_four.encode(message)

        solutions, decoded_message = BruteForce.brute_force(encoded_message, clues)
        assert_that(decoded_message, is_(message))
