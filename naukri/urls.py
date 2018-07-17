from django.conf.urls import url
from . import views
from .views import *
app_name='naukri'

urlpatterns = [
    # /
    url(r'^$',views.index,name='index'),
    # /<job_id>/
    url(r'^(?P<job_id>[0-9]+)/$',views.jobdetail,name='jobdetail'),
    # /<job_id>/apply/
    url(r'^(?P<job_id>[0-9]+)/apply/$',views.apply,name='newuser'),
    # /addjob
    url(r'^addjob/$',views.addnewjob,name='newjob'),
    # /addjob/addcompany
    url(r'^addcompany/$',views.addnewcompany,name='newcomp'),
]