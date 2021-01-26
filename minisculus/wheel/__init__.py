"""Wheels are elements of the MARK machines which take ints and return ints."""

from minisculus.wheel._simple_wheel import SimpleWheel
from minisculus.wheel._stateful_wheel import StatefulWheel
from minisculus.wheel._wheel import Wheel
from minisculus.wheel._wheel_chain import WheelChain

__all__ = ["SimpleWheel", "StatefulWheel", "Wheel", "WheelChain"]
