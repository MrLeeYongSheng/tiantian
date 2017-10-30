from django.conf.urls import url
import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_handler/$', views.register_handler),
    url(r'^login/$', views.login),
    url(r'^login_handler/$',views.login_handler)
]