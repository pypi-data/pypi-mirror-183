from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

class FormStatus(TextChoices):
    DRAFT = 'draft', _('Draft')
    PENDING = 'pending', _('Pending')
    PUBLISH = 'publish', _('Publish')
    SUSPEND = 'suspend', _('Suspend')

class FieldGenre(TextChoices):
    TEXT_INPUT = 'text_input', _('Text input')
    TEXT_AREA = 'text_area', _('Text area')
    NUMBER = 'number', _('Number')
    DROPDOWN = 'dropdown', _('Dropdown')
    DATE = 'date', _('Date')
    TIME = 'time', _('Time')
    DATETIME = 'datetime', _('Datetime')
    EMAIL = 'email', _('E-Mail')
    PASSWORD = 'password', _('Password')
    CHECKBOX = 'checkbox', _('Checkbox')
    MULTI_CHECKBOX = 'multi_checkbox', _('Multi checkbox')
    RADIO = 'radio', _('Radio')
    HIDDEN = 'hidden', _('Hidden')
    CAPTCHA = 'captcha', _('Captcha')
    UPLOAD_FILE = 'upload_file', _('Upload file')

    @classmethod
    def selectable_fields(cls):
        return [cls.DROPDOWN, cls.CHECKBOX, cls.RADIO, cls.MULTI_CHECKBOX]

class FormAPIManagerMethod(TextChoices):
    GET = 'get', _('GET')
    POST = 'post', _('POST')
    PUT = 'put', _('PUT')
    PATCH = 'patch', _('PATCH')
    DELETE = 'delete', _('DELETE')
    OPTION = 'option', _('OPTION')

class FormAPIManagerExecuteTime(TextChoices):
    PRE_LOAD = 'pre_load', _('Pre load')
    POST_LOAD = 'post_load', _('Post load')

class FieldPosition(TextChoices):
    INLINE = 'inline', _('In-line')
    INORDER = 'inorder', _('In-Order')
    BREAK = 'break', _('Break')

class FormDirection(TextChoices):
    LTR = 'ltr', _('LTR')
    RTL = 'rtl', _('RTL')

class FormTheme(TextChoices):
    INLINE = 'django_form_generator/fields/inline_fields.html', _('In-line Theme')
    INORDER = 'django_form_generator/fields/inorder_fields.html', _('In-order Theme')
    DYNAMIC = 'django_form_generator/fields/dynamic_fields.html', _('Dynamic Theme')