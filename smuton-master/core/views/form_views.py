from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django import forms
#from core.forms import DynamicForm
from django.template.context_processors import request
from test.test_array import ArraySubclassWithKwargs
#from django.views.generic.edit import FormView


class SumbitFormView(View):
    template_name = "core/InitialFormPage1.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
        #form = DynamicForm()
        #return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        
        #args = {'form': form, 'text': text}
        #return redirect(preview1.html)
        #if form.is_valid():
            #text = form.cleaned_data['post']
        return render(request, self.template_name)
        #return render(request, 'preview1.html', {'form': form})
        #return render(request, self.template_name, {'form': form})
        #return render(request, self.template_name).post(request, *args, **kwargs)

    
class PreviewFormView(View):
    template_name = "core/preview1.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name) 