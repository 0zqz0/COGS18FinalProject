"""Test for my functions.
"""

from functions import start_quiz, location, quiz_choice, ending, rate, end_quiz

def test_start_quiz():
    
    assert callable(start_quiz)

def test_location():
    
    assert callable(location)

def test_quiz_choice():
    
    assert callable(quiz_choice)

def test_ending():
    
    assert callable(ending)
    assert ending(1) == "\n Your score for this small quiz is 1. Thanks for your participation.\n"

def test_rate():
    
    assert callable(rate)
    
def test_end_quiz():
    
    assert callable(end_quiz)
