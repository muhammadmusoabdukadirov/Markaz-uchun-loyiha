from django import template

register = template.Library()

@register.filter
def get_star_rating(value):
    """Raqamdan yulduzcha hosil qiladi"""
    try:
        value = int(value)
    except (ValueError, TypeError):
        return ''
    return '★' * value + '☆' * (5 - value)
