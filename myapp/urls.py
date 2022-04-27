from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('', home,name='home'),
    path('user_signup', user_signup,name='user_signup'),
    path('visualization_view', visualization_view,name='visualization_view'),
    path('input_view', input_view,name='input_view'),
]
