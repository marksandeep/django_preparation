from django.conf.urls import url, include
from loginapp.views import homeView, newsView, logoutView

urlpatterns = [

    url(r'^home/', homeView.as_view(), name='home'),
    url(r'^news/', newsView.as_view(), name='news'),
    url(r'^logout/', logoutView.as_view(), name='logout'),
]