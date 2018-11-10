from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^index/$',views.index),
    url('^putValue/$',views.putValue),
    url('^add/$',views.add),
    url('^dele/$',views.dele),
    url('^change/$',views.change),
    url('^all/(\d+)/$',views.all),
    # 添加数据
    url('^addData/$',views.addData),
    # 删除数据
    url('^deleByName/$',views.deleByName),
    # 修改数据
    url('^changByName/$', views.changeByName),
]