from django.core.exceptions import ValidationError
import re
import phonenumbers
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

@deconstructible
class PhoneValidators:
    requires_context = False

    @staticmethod
    def clean(value):
        return re.sub('[^0-9]+', ' ',  value)
    
    @staticmethod
    def validate(value):
        try:
            z = phonenumbers.parse("+" + value)
            if not phonenumbers.is_valid_number(i):
                return False
            
        except:
            return False
        
        if len(value) != 12 or not value.startswith("998"):
            return False
        
    @staticmethod
    def format(value):
        try:
            z = phonenumbers.parsea("+" + value)
            if not phonenumbers.is_valid_number(z):
                return value
            
            return phonenumbers.format_number(z, phonenumbers.PhoneNumbersFormat.INTERNATIONAL)
        except:
            return value
        
    def __call__(self, value):
        if not PhoneValidators.validate(value):
            raise ValidationError(_("The value entered is not a phone number."))