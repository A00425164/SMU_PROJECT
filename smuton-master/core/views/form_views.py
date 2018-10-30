#from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from core.forms import DynamicForm
from django.template.context_processors import request
from core import models
#from django.views.generic.edit import CreateView

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Criteria
from ..forms import CriteriaForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404

class SumbitFormView(View):
    template_name = "core/InitialFormPage1.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def dynamicformpage1(self, request, *args, **kwargs):
        return render(request, 'DynamicFormPage1.html')
    
class DynamicFormView1(View):#CreateView? Check all available views  try
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
        models.Criteria.objects.all()
        models.Scale.objects.all()
        print(request.POST)
        return render(request, self.template_name, args)
        #return render(request, self.template_name, answer)
        #return super(DynamicFormView, self).post(request, *args, **kwargs)
        
class DynamicFormView2(CreateView):#CreateView? Check all available views  try
    template_name = "core/DynamicFormPage2.html"
    model = Criteria
    form_class = DynamicForm
    success_url = reverse_lazy("dynamic2")
    
    
    def __init__(self, **kwargs):
        return super(DynamicFormView2, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(DynamicFormView2, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DynamicFormView2, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DynamicFormView2, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(DynamicFormView2, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DynamicFormView2, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DynamicFormView2, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DynamicFormView2, self).get_initial()

    def form_invalid(self, form):
        return super(DynamicFormView2, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DynamicFormView2, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DynamicFormView2, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(DynamicFormView2, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DynamicFormView2, self).get_template_names()

    def get_success_url(self):
        return reverse("core:criteria_detail", args=(self.object.pk,))

    
#     def get(self, request, *args, **kwargs):
#         form = DynamicForm()
#         return render(request, self.template_name, {'form': form})
#     
#     def post(self, request, *args, **kwargs):
#         form = DynamicForm(request.POST)
#         
#         if form.is_valid():
#             data = request.POST.copy()
#             form = DynamicForm()
#             
#         if request.method == 'POST':
#             form = DynamicForm(request.POST)
            
        
#         args = {'form': form, 'data':data}
#         models.Criteria.objects.all()
#         models.Scale.objects.all()
#         print(request.POST)
#         return render(request, self.template_name, args)
