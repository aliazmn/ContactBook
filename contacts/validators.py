from django.db.models import CharField
from django.core.validators import RegexValidator


class PhoneValidator (CharField):
    
    def __init__(self, max_length = 16, *args, **kwargs):
        phone_regex = RegexValidator(regex=r'^(\+98|0)?9\d{9}$', 
                                     message="Phone number must be entered in the format: '+98**********'. Up to 11 digits allowed.")
        kwargs["validators"] = [phone_regex]
        super().__init__(*args, max_length = max_length, **kwargs)
    

class HomePhone (CharField):
    def __init__(self, max_length = 16, *args, **kwargs):
        phone_regex = RegexValidator(regex=r'^(\+98|0)\d{10}$', 
                                        message="Phone number must be entered in the format: '+98**********'. Up to 11 digits allowed.")
        kwargs["validators"] = [phone_regex]
        super().__init__(*args, max_length = max_length, **kwargs)
