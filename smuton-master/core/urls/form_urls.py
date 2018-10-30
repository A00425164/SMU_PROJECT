from django.conf.urls import url
from ..views.form_views import SumbitFormView
from ..views.form_views import DynamicFormView1
from ..views.form_views import DynamicFormView2
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$',
        login_required(SumbitFormView.as_view()),
        name="hackathon_form"),
		
	 url(r'^dynamic1/$',
         login_required(DynamicFormView1.as_view()),
         name="DynamicFormPage1"),
         
    url(r'^dynamic2/$',
         login_required(DynamicFormView2.as_view()),
         name="DynamicFormPage2"),
  
]
