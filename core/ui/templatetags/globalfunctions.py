from django import template

from ui.models import House, Pictures

register = template.Library()
@register.simple_tag(takes_context=True)
def getProfileDefualtPic(context,houseId=''):
    house = House.objects.get(id=houseId)
    # allpic = Pictures.objects.filter(homeName=house,status=1)
    # allPicList = list(allpic)
    # defaultpic = False
    # for pic in allPicList:
    #     if pic.cover:
    #         defaultpic = pic
    #
    # if defaultpic is not True:
    #     defaultpic=allPicList[0]

    try:
        defaultpic = Pictures.objects.get(homeName=house,status=1,cover=1)

    except:
        defaultpic = Pictures.objects.filter(homeName=house, status=1)[0]

    context['defaultPic'] = defaultpic

    return ""

#
# def gethouseforsale(context,houseId=''):
#     house = House.objects.get(id=houseId)
#     try:
#         defaultpic = Pictures.objects.get(homeName=house,status=1,cover=1,)
#
#     except:
#         defaultpic = Pictures.objects.filter(homeName=house, status=1)[0]
#
#     context['defaultPic'] = defaultpic
#
#     return ""