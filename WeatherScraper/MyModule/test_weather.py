# in terminal install pytest
# Instructions: pip install pytest, bs4
import pytest
from functions import clothing, weather_greeting

def test_clothing():
    anticipated_return = True

    clothing_true = clothing()

    assert anticipated_return == clothing_true

def test_weather_greeting():
    anticipated_return = True

    weather_true = weather_greeting()

    assert anticipated_return == weather_true
