from ui.models import *
from django import template

register=template.Library()

@register.simple_tag(takes_context=True)
def navbarVariables(context):
    house = House.objects.all()
    comment = Comment.objects.filter(home=house, status=True)
    context['comment'] = comment


    commentsByDate = Comment.objects.all().order_by('-created_date')
    commentsByid = commentsByDate.order_by('-id')
    commentsList = []
    i = 0
    for comments in commentsByid:
        commentsList.append(comments)
        i += 1
        if i == 3:
            break
    context['commentsList'] = commentsList
