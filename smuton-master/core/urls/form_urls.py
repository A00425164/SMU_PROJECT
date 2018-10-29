from django.conf.urls import url
from ..views.form_views import SumbitFormView
from ..views.form_views import DynamicFormView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$',
        login_required(SumbitFormView.as_view()),
        name="hackathon_form"),
		
	 url(r'^dynamic/$',
         login_required(DynamicFormView.as_view()),
         name="DynamicFormPage1"),
]
