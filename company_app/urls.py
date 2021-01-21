from django.contrib import admin
from django.urls import path
import company_app.views as tv

urlpatterns = [
    path('delete_person/', tv.delete_person),
    path('all_big/', tv.all_big),
    path('bigdui/', tv.getbig),
    path('big_captain/', tv.get_big_captain),
    path('smalldui/', tv.get_small),
    path('small_person/',tv.get_small_person),
    path('new_small/',tv.add_small),
    path('new_big/',tv.add_big),
    path('person_info/',tv.get_person_info),
    path('edit_person_info/',tv.edit_person_info),
    path('new_person_info/',tv.new_person_info),

]
# django2.0之后
app_name = 'company_app'
