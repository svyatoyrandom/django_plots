from django.core.validators import BaseValidator
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

@deconstructible
class BracketValidator(BaseValidator):
    message = _('Чекни скобки')
    code = 'invalid brackets'
    def __init__(self):
        pass
    def __call__(self, value: str) -> None:
        open_brackets_cnt = 0
        close_bracket_cnt = 0
        for i in range(len(value)):
            if value[i] == ')':
                close_bracket_cnt += 1
            if value[i] == '(':
                open_brackets_cnt += 1
        if open_brackets_cnt != close_bracket_cnt:
            raise ValidationError(self.message, self.code, params={'value': value})