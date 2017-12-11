from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View


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
                return HttpResponse('/thanks/')

        return render(request, self.template_name, {'form': form})