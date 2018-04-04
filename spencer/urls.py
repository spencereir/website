from django.conf.urls import url

from spencer.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
]
