#from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from core.forms import DynamicForm
from django.template.context_processors import request


class SumbitFormView(View):
    template_name = "core/InitialFormPage1.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def dynamicformpage1(self, request, *args, **kwargs):
        return render(request, 'DynamicFormPage1.html')
    
class DynamicFormView(View):
    template_name = "core/DynamicFormPage1.html"
    
    def get(self, request, *args, **kwargs):
        form = DynamicForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = DynamicForm(request.POST)
        
        if form.is_valid():
            data = request.POST.copy()
            form = DynamicForm()
            
        if request.method == 'POST':
            form = DynamicForm(request.POST)
            
        
        args = {'form': form, 'data':data}
        print(request.POST)
        return render(request, self.template_name, args)
        #return render(request, self.template_name, answer)
        #return super(DynamicFormView, self).post(request, *args, **kwargs)