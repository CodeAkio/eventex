from django.urls import path

from subscriptions.views import new, DescriptionDetail

app_name = 'subscriptions'

urlpatterns = [
    path('', new, name='new'),
    path('<str:hashid>/', DescriptionDetail.as_view(), name='detail'),
]
