import sys
import logging

# Function to extract error details
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script [{0}] at line [{1}]: {2}".format(
        filename, exc_tb.tb_lineno, str(error)
    )
    return error_message  # ✅ Corrected return statement

# Custom Exception Class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)  # ✅ Fixed variable reference

    def __str__(self):
        return self.error_message

