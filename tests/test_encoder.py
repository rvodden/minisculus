from copy import deepcopy

from hypothesis import given
from hypothesis.strategies import data, lists, text, DataObject
from pytest import raises

from minisculus import Encoder
from tests.search_strategies import wheels, valid_characters


class TestEncoder:
    @staticmethod
    def build_encoder(draw) -> Encoder:
        """Create an encoder with an arbitrary set of wheels"""
        wheels_list = draw(lists(wheels(), max_size=10))
        return Encoder(wheels_list)

    @given(
        data(), text().filter(lambda s: not (all(c in Encoder._alphabet for c in s)))
    )
    def test_encode_throws_error_when_invalid_string_provided(
        self, data: DataObject, string: str
    ):
        encoder: Encoder = self.build_encoder(data.draw)
        with raises(ValueError):
            encoder.encode(string)

    @given(data(), text(alphabet=Encoder._alphabet))
    def test_encode_returns_string_which_decodes_correctly(self, data, string: str):
        encoder: Encoder = self.build_encoder(data.draw)
        # the encoding process modifies internal state, so take
        # a deepcopy so that decoding can start with fresh state
        decoder: Encoder = deepcopy(encoder)
        encoded_string: str = encoder.encode(string)
        assert len(encoded_string) == len(string)
        assert string == decoder.decode(encoded_string)

    @given(data(), valid_characters())
    def test_encode_character_returns_character_which_decodes_correctly(
        self, data, string: str
    ):
        encoder: Encoder = self.build_encoder(data.draw)
        # the encoding process modifies internal state, so take
        # a deepcopy so that decoding can start with fresh state
        decoder: Encoder = deepcopy(encoder)
        encoded_value: str = encoder._encode_character(string)
        assert string == decoder._decode_character(encoded_value)

    @given(data(), text(alphabet=Encoder._alphabet, min_size=2))
    def test_encode_character_throws_exception_when_string_is_too_long(
        self, data, string: str
    ):
        under_test: Encoder = self.build_encoder(data.draw)
        with raises(ValueError):
            under_test._encode_character(string)
