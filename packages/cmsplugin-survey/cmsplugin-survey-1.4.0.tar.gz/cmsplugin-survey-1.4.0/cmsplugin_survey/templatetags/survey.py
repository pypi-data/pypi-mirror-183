from django import template

from ..models import Answer

register = template.Library()


@register.filter
def answer(answer_id):
    try:
        return answer_id and Answer.objects.get(id=answer_id.value)
    except Answer.DoesNotExist:
        return None
