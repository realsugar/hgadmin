from django.core.validators import RegexValidator

# Letters, numbers, dashes, underscores, dots, +, !
def password_validator():
    return RegexValidator(regex='^[A-Za-z0-9\-_\.\+\!]+$',
                          message="Only letters, numbers, dashes, underscores, dots, ! and + allowed.")

# Letters, numbers, dashes, underscores, dots
def login_validator():
        return RegexValidator(regex='^[A-Za-z0-9\-_\.]+$',
                              message="Only letters, numbers, dashes, underscores and dots allowed.")

  