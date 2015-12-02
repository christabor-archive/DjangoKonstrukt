from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='classy')
@stringfilter
def classy(value):
    """Converts random value to class CamelCase
    style for model generation.
    e.g. My random model name => MyRandomModelName
    """
    return ''.join(
        [val[:1].upper() + val[1:] for val in value.split(' ')])
