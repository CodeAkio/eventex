from django.urls import path

from subscriptions.views import new, detail

app_name = 'subscriptions'

urlpatterns = [
    path('', new, name='new'),
    path('<str:hashid>/', detail, name='detail'),
]