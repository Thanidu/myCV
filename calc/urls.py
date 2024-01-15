from django.urls import path
from . import views
from .views import send_message


urlpatterns = [
	path('',views.index, name='index'),
	path('blog_single/',views.blog_single, name='blog_single'),
    path('project_details/',views.project_details, name='project_details'),
    path('send_message/', send_message, name='send_message'),
]