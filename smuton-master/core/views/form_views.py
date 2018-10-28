from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class SumbitFormView(View):
    template_name = "core/InitialFormPage1.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class DynamicFormView(View):
    template_name = "core/DynamicFormPage1.html"
    
    def get(self, request, *args, **kwargs):
        form = DynamicForm()
        return render(request, self.template_name, {'form': form})