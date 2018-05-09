from django.urls import path,include

from . import views

app_name='party'

urlpatterns = [

    path(r'home/',views.index,name='index'),
    path(r'gotcha/',views.gotcha,name='gotcha'),
    path(r'oqp/',views.oqp,name='oqp'),
    path(r'wishingwell/',views.wishingwell,name='ww'),
    path(r'sorry/',views.sorry,name='sorry'),
]