from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from bookshop.models import Reporter, Article

class AuthorView(View):

    template_name = 'article.html'

    def get(self, request):
        articles = Article.objects.all()
        return render_to_response(self.template_name, {'articles': articles})




class ArticleView(View):

    template_name = 'add_article.html'

    def get(self, request):
        print "sandeep is here"
        return render(request, 'add_article.html', {})