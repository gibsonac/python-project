from django.conf.urls import url, include 
urlpatterns = [
    url(r'^', include('apps.app_1.urls')),
]