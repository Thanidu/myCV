from django.contrib import admin
from .models import Publication, Experience, Education, Blog, Project,Message


# Register your models here.
admin.site.register(Publication)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Blog)
admin.site.register(Project)
admin.site.register(Message)