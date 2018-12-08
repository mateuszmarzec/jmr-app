from django.urls import path

from shortener.views import IndexView, RedirectView

urlpatterns = [
    path('', IndexView.as_view(), name='index-view'),
    path('<str:shortcut>', RedirectView.as_view(), name='redirect-view')
]
