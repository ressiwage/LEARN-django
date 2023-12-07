from django.shortcuts import render
from .models import Option
from django.http import HttpResponse
from django.template import loader
from json import dumps

def treeify(lst, filter_=lambda x:True): #list<dict>
    list_root = filter(lambda x:x['level'] == 1,lst)
    def recursive(item, list_):
        if filter_(item)!=True:
            return None
        item_copy = dict(**item)
        for i in list_:
            if i['parent'] == item_copy['id']:
                item_copy['all_childs'] = item_copy.get('all_childs', [])+[i]

        item_copy['all_childs'] = [recursive(j, list_) for j in item_copy.get('all_childs', [])]
        item_copy['all_childs'] = list(filter(lambda x:x!=None, item_copy['all_childs']))
        return item_copy
    result = [recursive(i, lst) for i in list_root]
    result = list(filter(lambda x:x!=None, result))
    return result

def index(request):
    list_ = [i.__dict__ for i in Option.objects.all()]
    for i,_ in enumerate(list_):
        list_[i].pop('_state')
    
    template = loader.get_template("index.html")    
    context={'context':{'elems':treeify(list_, lambda x:x['level']<=1)}}
    print(context)
    return HttpResponse(template.render(context, request))

def page(request, id):

    list_ = [i.__dict__ for i in Option.objects.all()]
    for i,_ in enumerate(list_):
        list_[i].pop('_state')
    this_option = [i for i in list_ if i['id'] == id][0]
    template = loader.get_template("index.html")    
    context={'context':{'elems':treeify(list_, lambda x:x['level']<=this_option['level'] or x['parent'] == this_option['id'])}}
    print(context)
    return HttpResponse(template.render(context, request))