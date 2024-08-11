import markdown
from django import template

register = template.Library()


@register.filter
def markdown_html(text):
    return markdown.markdown(text)
