from django import template
from django.template import loader

register = template.Library()

@register.simple_tag
def menu(json):
    template = loader.get_template("menu_container.html")
    
    if type(json) is str:
        return template.render({'elems':[]})    
    return template.render(json)




