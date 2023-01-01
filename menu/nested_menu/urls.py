from django.urls import path

from nested_menu.views import IndexView

app_name = 'nested_menu'

urlpatterns = [
    path('menu/', IndexView.as_view(), name='index')
]
