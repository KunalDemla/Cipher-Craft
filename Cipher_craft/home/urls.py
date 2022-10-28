from . import views
from django.urls import path
# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index , name='home_page'),
    path('about/',views.about, name='about_page'),
    path('faqs/',views.faqs,name='faqs_page'),
    path('feedback/',views.feedback,name='feedback_page'),
]