from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User

from .forms import UserForm

class loginView(View):

    initial = {'key': 'value'}
    template_name = 'login.html'
    form_class = UserForm
    #import pdb; pdb.set_trace()
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                email = form.cleaned_data['email']
                print username
                user = User.objects.get(username=username)
                if user:
                    return HttpResponseRedirect('/bookshop/success/', {'user': user})
                else:
                    user = User.objects.create_user(username=username,
                                                    password=password, email=email)
                    return HttpResponse('/thanks for creating account')

        return render(request, self.template_name, {'form': form})


class homeView(View):

    def get(self, request):
         return render(request, 'home.html', {})


class newsView(View):

    def get(self, request):
         return render(request, 'news.html', {})


class logoutView(View):

    def get(self, request):
        return HttpResponse("<h1> You are logged Out!</h1>")