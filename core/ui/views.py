from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import random
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from .forms import CommentForm
from ui.decorators import unauthenticated_user
from .forms import CreateUserForm
from ui.models import *
from django.contrib import messages



@unauthenticated_user
def registerPage(request):
    indate = datetime.now()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
    context = {'form': form, 'indate':indate}
    return render(request, 'register.html', context)


@unauthenticated_user
def loginPage(request):
    indate = datetime.now()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {'indate':indate}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    sliders = Sliders.objects.all()
    abouts = About.objects.all()
    features = FeaturesHome.objects.all()
    brands = BrandsItem.objects.all()
    houses = House.objects.all()
    services = Service.objects.all()
    agents = Agent.objects.all()
    blogs = Blog.objects.all()
    agentsByDate = Agent.objects.all().order_by('-inDate')
    agentsByid = agentsByDate.order_by('-id')
    agentList = []
    i = 0
    for agent in agentsByid:

        agentList.append(agent)
        i += 1
    housesByDate = House.objects.all().order_by('-inDate')
    housesByid = housesByDate.order_by('-id')
    houseList = []
    i = 0
    for house in housesByid:
        houseList.append(house)
        i += 1
        if i == 9:
            break

    context = {'sliders':sliders,'abouts':abouts,'features':features,'agents':agents,
               'agentList':agentList,'brands':brands,'services':services,
                'houseList':houseList, 'houses':houses, 'blogs':blogs}
    return render(request, 'index.html', context)

@login_required(login_url='login')
def contact(request):
    contacts = Contact.objects.all()
    if request.method=='POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        message= request.POST.get('message')
        dateOfMail = datetime.now()
        formatDate = dateOfMail.strftime("%Y-%m-%d %H:%M:%S")
        text = f"Yeni başvuru bilgileri adı:  {name}                      tarih:{formatDate} \n " \
               f"eposta adresi: {email}\r\n\n" \
               f" bu mesajı göndermiştir: {message}"
        textOfCustomer = f'Sayın {name} mesajınız bize başarıyla gönderildi'
        title = 'Yeni Başvuru Var!'
        titleOfCustomer = 'mesajınız bize ulaşmıştır!'

        hostEmail = settings.EMAIL_HOST_USER
        sent_to = [hostEmail]

        sendToCustomer = [email]
        print(sendToCustomer)
        print(hostEmail)

        try:
            send_mail(title, text, hostEmail, sent_to, fail_silently=False)
            send_mail(titleOfCustomer, textOfCustomer, hostEmail, sendToCustomer, fail_silently=False)
            messages.info(request, 'Mesajiniz başarılı bir şekilde gönderildi!')
        except:
            message.error(request, 'Bir hata uluştu lütfen tekrar deneyiniz!')

    context ={'contacts':contacts}
    return render(request, 'contact.html', context)

def about(request):
    about = About.objects.all()
    brands = BrandsItem.objects.all()
    services = Service.objects.all()
    agents = Agent.objects.all()
    context = {'about':about,'brands':brands,
               'services':services,'agents':agents}
    return render(request,'about.html', context)


def agent(request):
    agents = Agent.objects.all()
    brands = BrandsItem.objects.all()
    context = {'agents':agents, 'brands':brands}
    return render(request, 'agent.html', context)

def agentDetails(request,pk):
    agents = Agent.objects.get(id=pk)
    brands = BrandsItem.objects.all()
    # ********send message to agent********
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        dateOfMail = datetime.now()
        formatDate = dateOfMail.strftime("%Y-%m-%d %H:%M:%S")
        text = f"Yeni başvuru bilgileri adı:  {name}                      tarih:{formatDate} \n " \
               f"telefon numarası: {phone} \n "\
               f"eposta adresi: {email}\r\n\n" \
               f" bu mesajı göndermiştir: {message}"
        textOfCustomer = f'Sayın {name} mesajınız bize başarıyla gönderildi'
        title = 'Yeni Başvuru Var!'
        titleOfCustomer = 'mesajınız bize ulaşmıştır!'

        agentMail = agents.email
        sent_to = [agentMail]

        sendToCustomer = [email]
        print(sendToCustomer)

        try:
            send_mail(title, text, agentMail, sent_to, fail_silently=False)
            send_mail(titleOfCustomer, textOfCustomer, agentMail, sendToCustomer, fail_silently=False)
            messages.info(request, 'Mesajiniz başarılı bir şekilde gönderildi!')
        except:
            message.error(request, 'Bir hata uluştu lütfen tekrar deneyiniz!')
    context = {'agents':agents, 'brands':brands}
    return render(request, 'agentDetails.html', context)

def propertiesHouse(request):
    houses = House.objects.all()
    brands = BrandsItem.objects.all()
    indate = datetime.now()
    context = {'houses':houses, 'brands':brands, 'indate':indate}
    return render(request,'properties.html', context)

@login_required(login_url='login')
def propertiesDetails(request,pk):
    house = House.objects.get(id=pk)
    housespic = Pictures.objects.filter(homeName=house)

    allHouse = House.objects.all()
    FeaturedProperty = random.choices(allHouse, k=3)
    #********send message to agent********
    if request.method=='POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        message= request.POST.get('message')
        dateOfMail = datetime.now()
        formatDate = dateOfMail.strftime("%Y-%m-%d %H:%M:%S")
        text = f"Yeni başvuru bilgileri adı:  {name}                      tarih:{formatDate} \n " \
               f"eposta adresi: {email}\r\n\n" \
               f" bu mesajı göndermiştir: {message}"
        textOfCustomer = f'Sayın {name} mesajınız bize başarıyla gönderildi'
        title = 'Yeni Başvuru Var!'
        titleOfCustomer = 'mesajınız bize ulaşmıştır inceledikten sonra paylaşilacaktır!'

        hostEmail = settings.EMAIL_HOST_USER
        sent_to = [hostEmail]


        sendToCustomer = [email]
        print(sendToCustomer)
        print(hostEmail)

        try:
            send_mail(title, text, hostEmail, sent_to, fail_silently=False)
            send_mail(titleOfCustomer, textOfCustomer, hostEmail, sendToCustomer, fail_silently=False)
            messages.info(request, 'Mesajiniz başarılı bir şekilde gönderildi!')
        except:
            message.error(request, 'Bir hata uluştu lütfen tekrar deneyiniz!')

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    comment = Comment.objects.filter(home=house, status=True)

    context={'house':house,'housespic':housespic, 'form':form,
             'FeaturedProperty':FeaturedProperty, 'comment':comment}
    return render(request, 'propertiesDetails.html', context)

def service(request):
    services = Service.objects.all()
    brands = BrandsItem.objects.all()
    context = {'services':services, 'brands':brands}
    return render(request, 'service.html', context)

def serviceDetails(request,pk):
    services = Service.objects.get(id=pk)
    houses = House.objects.filter(type='sale')
    brands = BrandsItem.objects.all()
    agents = Agent.objects.all()
    agentsByDate = Agent.objects.all().order_by('-inDate')
    agentsByid = agentsByDate.order_by('-id')
    agentList = []
    i = 0
    for agent in agentsByid:
        agentList.append(agent)
        i += 1
    context = {'services':services, 'houses':houses,
               'agents':agents, 'agentList':agentList,
               'brands':brands}
    return render(request, 'service-details.html', context)

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'blog.html',context)

def blogDetails(request,pk):
    blogs = Blog.objects.get(id=pk)
    agents = Agent.objects.get(id=pk)
    context = {'blogs':blogs, 'agents':agents}
    return render(request,'blogDetails.html',context)

def featuresHome(request):
    features = FeaturesHome.objects.all()
    brands = BrandsItem.objects.all()
    context = {'features':features,'brands':brands}
    return render(request,'features.html',context)


# def footer(request):
#     blogs = Blog.objects.all()
#     randBlogs = random.choices(blogs, k=3)
#     context = {'randBlogs':randBlogs}
#     return render(request, 'footer.html',context)



