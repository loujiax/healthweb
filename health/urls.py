from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('vegetables.urls')),  # Keep
    path('admin/', admin.site.urls),  # Keep
    path('accounts/', include('django.contrib.auth.urls')),  # Keep

    url(r'^oauth/', include('social_django.urls', namespace='social')),  # Keep
 #   path('ads/', include('ads.urls')),  # Keep

]
