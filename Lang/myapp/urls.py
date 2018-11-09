from django.contrib import admin
from django.conf.urls import url

from . import views

app_name='myapp'

urlpatterns = [
    url('^index/', views.index ,name='index'),
    # 四个基础的展示页
    url('^home/', views.home, name='home'),
    url('^market/', views.market, name='market'),
    url('^cart/', views.cart, name='cart'),
    url('^mine/', views.mine, name='mine'),

    # 对右侧数据通过标签页进行更改
    url('^changeMenu/(?P<typeid>\d+)/', views.changeMenu,name='changeMenu'),

    # 登陆注册页面
    url('^register/', views.register, name='register'),
    url('^login/', views.login, name='login'),

    # 注册信息进行判断
    url('^judge_name/', views.judge_name, name='judge_name'),
    url('^judge_email/', views.judge_email, name='judge_email'),

    # 对登录信息进行判断
    url('^judge_login/', views.judge_login, name='judge_login'),

    # mine中进行退出
    url('^sign_out/', views.sign_out, name='sign_out'),

    # 搜索物品
    url('^search/', views.search, name='search'),

    # 将market中的物品添加到购物车和减操作
    url('^add_to_cart/', views.add_to_cart, name='add_to_cart'),
    url('^sub_from_cart/', views.sub_from_cart, name='sub_from_cart'),

    # 对小球进行判断

    url('^judge_ball/', views.judge_ball, name='judge_ball'),

]
