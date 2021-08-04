from django.conf.urls import url
from basicapp import views

#TEMPLATE URLS!

app_name = 'basicapp'

urlpatterns=[
    url(r'^register/$',views.register,name='register')
    ]
