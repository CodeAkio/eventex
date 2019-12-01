from django.contrib import admin
from django.urls import path, include

from core.views import home

urlpatterns = [
    path('', home, name='home'),
    path('inscricao/', include('subscriptions.urls')),
    path('admin/', admin.site.urls),
]
