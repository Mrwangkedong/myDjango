from django.urls import path
import SoftMake.views as sv

urlpatterns = [
    path('index/',sv.GoIndex),
    path('GetAll/',sv.GetAll,name='getall_action')
]

app_name = 'soft_app'