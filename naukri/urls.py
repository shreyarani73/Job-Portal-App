from django.conf.urls import url
from . import views

app_name='naukri'

urlpatterns = [
     # /
    url(r'^$',views.index,name='index'),
    # login/
    url(r'^login/$', views.mylogin, name='mylogin'),
    # logout/
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', views.mylogout, name='mylogout'),
    # /<job_id>/
    url(r'^(?P<job_id>[0-9]+)/$',views.jobdetail,name='jobdetail'),
    # /<job_id>/apply/
    url(r'^(?P<job_id>[0-9]+)/apply/$',views.apply,name='newuser'),
    # /addjob
    url(r'^addjob/$',views.addnewjob,name='newjob'),
    # /addjob/addcompany
    url(r'^addcompany/$',views.addnewcompany,name='newcomp'),
]