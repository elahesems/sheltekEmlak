from django.urls import path
from ui import views

urlpatterns =[
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('service/',views.service,name="service"),
    path('service_details/<str:pk>/',views.serviceDetails,name="serviceDetails"),
    path('agent/',views.agent,name="agent"),
    path('agent_details/<str:pk>/',views.agentDetails,name="agentDetails"),
    path('properties/',views.propertiesHouse,name="propertiesHouse"),
    path('properties_details/<str:pk>/',views.propertiesDetails,name="propertiesDetails"),
    path('blog/',views.blog,name="blog"),
    path('blog_details/<str:pk>/',views.blogDetails,name="blogDetails"),
    path('features/',views.featuresHome,name="features"),
    path('404/',views.errors,name="errors"),


]