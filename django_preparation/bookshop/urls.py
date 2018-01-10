from django.conf.urls import url, include
from bookshop.views import AuthorView
from bookshop.views import ArticleView

urlpatterns = [
    url(r'^success/', AuthorView.as_view(), name='book'),
    url(r'^article/', ArticleView.as_view(), name='article'),
]


