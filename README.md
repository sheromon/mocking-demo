# Mocking Demo
Demo code for a study group session with Boston Python on the topic of mocking

This repository includes an example Python package and associated code for running tests with `pytest`. In the main branch, the test code is incomplete to allow people to experiment with completing it using `unittest.mock`. This code is intended for educational purposes only.

## References

* Python documentation for `unittest.mock`: https://docs.python.org/3/library/unittest.mock.html
* Open-Meteo weather api: https://open-meteo.com/


## Example Python Package
The example Python package `outfit-picker` uses `openmeteo-requests` to request a weather forecast with the maximum temperature for the day. Then some basic logic is used to pick clothing items based on the predicted temperature.

There are two version of the code, one written using a class (`classes.py`) and one written using functions (`functions.py`) to enable practice using `unittest.mock` with both styles of code.

## Tests

### Setup
To run the tests, it is recommended to first clone this repository, then install the Python package and dev requirements in a virtual environment.

With your desired virtual environment activated, install the Python package from source and install the dev requirements.

    pip install .
    pip install -r dev-requirements.txt

After the dependencies are installed, the test code can by run using `pytest`. Note: The tests on the `main` branch arte not expected to pass.

    pytest tests/

### Test Code
The test code in the main branch is incomplete so that you can experiment with completing it. 

* `test_exception_handling` has one test intended to verify that the code goes down the expected path when the request to openmeteo fails with the error `requests.exceptions.ConnectionError`.
* `test_outfit_logic_classes` has several tests that verify that the output changes depending on the max temperature, using the version of the `outfit-picker` code that was written using a class. This file has many tests that do essentially the same thing in different ways.
* `test_outfit_logic_functions` is the same as the above except using the version of the code written using functions.
* `test_parameters` has tests to verify that a function is gettting called with the expected arguments.

Although there is no single "right" answer for completing the code, there is a version in the `completed` branch of the git repository where all tests should pass. To get this version of the code, run `git checkout completed`.

To supplement the test code, here are some questions to consider.

1. Could the `outfit-picker` code have been written differently so that the code to test the outfit logic (in `test_outfit_logic_classes.py` and/or `test_outfit_logic_functions.py`) did not need to use mocking at all? How?
2. In `test_exception_handling`, `unittest.mock.patch` is used on `sys.stdout`. What does that do?
