from django import template

register = template.Library()

@register.filter
def format_phone(phone):
    return f'{phone[0:3]}-{phone[3:6]}-{phone[6:10]}'