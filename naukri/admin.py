from django.contrib import admin
from django.apps import apps
from .models import Company,Job,Seeker
# Register your models here.
app = apps.get_app_config('naukri')

for name,model in app.models.items():
		admin.site.register(model)

