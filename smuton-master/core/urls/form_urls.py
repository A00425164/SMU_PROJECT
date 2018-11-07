from django.conf.urls import url
from ..views.form_views import SumbitFormView
from ..views.form_views import DynamicFormView1
from ..views.form_views import DynamicFormView2
from django.contrib.auth.decorators import login_required

#//var blocky ='{{ form.name.label }}{{ form.name }}<br>{{ form.scale.label }}{{ form.scale }}';
#//var blocky = '<div id="repblock">Criteria Name<input type="text" name="name" maxlength="255" required id="id_name"><br>Scale<select name="scale" required id="id_scale"><option value="" selected>---------</option><option value="1">1 to 5</option></select></div>';
            
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
