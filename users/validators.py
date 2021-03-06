from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

only_letters = RegexValidator(r'^[A-ZÁÉÍÓÚÑÇÄËÏÖÜa-zñáéíóúäëïöüç\s]*$',
                              u'Only letters allowed.')
alphaSpaces = RegexValidator(r'^[a-zA-Z]+$', 'Only letters and spaces are allowed in the Location Name.')
nums = RegexValidator(r'^[0-9]*$',
                      'Only numbers allowed.')
alfan = RegexValidator(r'^[A-ZÁÉÍÓÚÑÇÄËÏÖÜa-zñáéíóúäëïöüç\,.-s0-9]*$',
                       u'Only numbers and/or letters are allowed.')


def positive_price(value):
    """ 
    0 is allowed for possibles offers in future
    """
    if value < 0:
        msg = u"Price must be over or = 0"
        raise ValidationError(msg)