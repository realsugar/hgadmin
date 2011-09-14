from django.core.validators import RegexValidator, ValidationError
from models import Developer

# Letters, numbers, dashes, underscores, dots, +, !
def password_validator():
    return RegexValidator(regex='^[A-Za-z0-9\-_\.\+\!]+$',
                          message="Only letters, numbers, dashes, underscores, dots, ! and + allowed.")

# Letters, numbers, dashes, underscores, dots
def login_validator():
        return RegexValidator(regex='^[A-Za-z0-9\-_\.]+$',
                              message="Only letters, numbers, dashes, underscores and dots allowed.")

def developer_exists_validator(developer_login):
    if Developer.get_by_login(developer_login):
        raise ValidationError("Developer %s already exists!" % developer_login)
    return None