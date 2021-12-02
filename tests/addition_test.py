"""Testing Addition"""

from tests import read_csv
from tests import log_reporting as log
from calc.calculations.addition import Addition


def test_addition_two_values():
    """Testing addition method for two values"""
    path = "tests/test_data/addition/addition_2_values.csv"
    # read_two_columns function
    columns = read_csv.read_two_columns(path)

    for i in range(columns[2].size):
        # columns: value1, value2 and result
        # Arrange
        addition = Addition(columns[0][i], (columns[1][i],))
        # Act and Assert
        assert addition.get_result() == columns[2][i]
        log.report_log_info(path, i, "addition", addition.get_result())


def test_addition_three_values():
    """Testing addition method for three values"""
    path = "tests/test_data/addition/addition_3_values.csv"
    # read_three_columns function
    columns = read_csv.read_three_columns(path)

    for i in range(columns[3].size):
        # columns: value1, value2, value3 and result
        # Arrange
        addition = Addition(columns[0][i], (columns[1][i], columns[2][i]))
        # Act and Assert
        assert addition.get_result() == columns[3][i]
        log.report_log_info(path, i, "addition", addition.get_result())
