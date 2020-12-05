from django.core.validators import RegexValidator
from .messages import VALIDATION_ERROR_MESSAGES


# for alphabets + numeric + special characters (-, ., $, "",)
BookNameValidator = RegexValidator(
    regex='^[A-Za-z\s\-_,\.:;()''""]+$',
    message=VALIDATION_ERROR_MESSAGES['INVALID_BOOK_NAME'],
    code='INVALID_BOOK_NAME'
)

BookAuthorValidator = RegexValidator(
    regex='^[A-Za-z\s\-_,\.:;()''""]+$',
    message=VALIDATION_ERROR_MESSAGES['INVALID_AUTHOR_NAME'],
    code='INVALID_AUTHOR_NAME'
)
