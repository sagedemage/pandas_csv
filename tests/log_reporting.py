"""Log reporting program"""
import logging


def report_log_info(path, record_number, operation, result):
    """Log report info"""
    path_items = path.split("/")
    # Get the filename
    filename = path_items[len(path_items) - 1]
    message = filename + " " + str(record_number) + " " + operation + " " + str(result)
    logging.info(message)


def report_log_error(path, record_number):
    """Log report error"""
    path_items = path.split("/")
    # Get the filename
    filename = path_items[len(path_items) - 1]
    message = filename + " " + str(record_number)
    logging.error(message)
