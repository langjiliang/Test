from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

from myapp.models import Order
from .models import MianShow, FootTypes, Goods, User, Cart, OrderGoods


# Create your views here.
def index(request):
    HttpResponse("hello")


def home(request):
    main_shows = MianShow.objects.all()
    data = {
        'main_shows': main_shows,
    }

    return render(request, 'main/home.html', context=data)


def market(request):
    food_types = FootTypes.objects.all()

    goods_lists = Goods.objects.all()[1:20]
    data = {
        'food_types': food_types,
        'goods_lists': goods_lists,
    }

    return render(request, 'main/market.html', context=data)


# 将加入到购物车中信息进行前端渲染
def cart(request):
    username = request.session.get('username')

    print(username)

    if username:

        user = User.objects.get(username=username)

        print(user)

        carts = Cart.objects.filter(user=user)

        data = {
            'carts': carts,
            'content': "商品存在"
        }

        price_num = 0

        print(carts)
        if carts.exists():

            for cart in carts:
                if cart.is_select == 1:
                    price_num = cart.goods_num * cart.goods.price + price_num

                    data['price'] = price_num

            print(data)
            return render(request, 'main/cart.html', context=data)
        else:
            data['carts'] = None
            data['content'] = "商品不存在"
            return render(request, 'main/cart.html', )


    else:
        return redirect(reverse('lang:login'))

    return render(request, 'main/cart.html')


def mine(request):
    username = request.session.get('username')

    print(username)

    data = {
        'flag': 0
    }

    if username:
        data['username'] = username
        data['flag'] = 1

    return render(request, 'main/mine.html', context=data)


# 对右侧数据通过标签页进行更改
def changeMenu(request, typeid):
    goods_lists = Goods.objects.filter(categoryid=typeid)

    food_types = FootTypes.objects.all()

    data = {
        'food_types': food_types,
        'goods_lists': goods_lists
    }

    return render(request, 'main/market.html', context=data)


# 注册页面
def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')

    else:
        username = request.POST.get('username')
        email = request.POST.get('useremail')
        password = request.POST.get('userpassword')

        password = make_password(password)
        # 将用户存进数据库中
        user = User()
        user.username = username
        user.emain = email
        user.password = password
        user.save()

        return render(request, 'user/login.html')


# 登陆页面
def login(request):
    return render(request, 'user/login.html')


# 对注册页面的名字进行判断是否符合

def judge_name(request):
    ajax_username = request.GET.get('username')

    username = User.objects.filter(username=ajax_username)

    username = username.first()

    print(username)

    data = {
        'status': 0
    }

    if username:

        data['status'] = 300

    else:

        data['status'] = 200
    return JsonResponse(data=data)


# 对注册页面的邮箱进行判断是否符合

def judge_email(request):
    ajax_email = request.GET.get('email')

    email = User.objects.filter(emain=ajax_email)

    email = email.first()

    data = {
        'status': 0
    }

    if email:

        data['status'] = 301

    else:

        data['status'] = 201

    return JsonResponse(data=data)


# 对登陆进行判断

def judge_login(request):
    name = request.GET.get("username")
    password = request.GET.get("password")

    user = User.objects.filter(username=name)

    if user.exists():
        user = user.first()
        # 进行密码的判断
        if check_password(password, user.password):
            request.session['username'] = name
            return redirect(reverse('lang:mine'))

        else:
            return render(request, 'user/login.html', {'info': '密码输入错误'})


    else:
        return render(request, 'user/login.html', {'info': '用户名不存在'})


# 退出页面
def sign_out(request):
    flag = request.GET.get('flag')
    flag = int(flag)
    if flag == 1:
        request.session.flush()
    return redirect(reverse('lang:mine'))


# 搜索物品

def search(request):
    goods_info = request.POST.get("goods_info")
    goods_lists = Goods.objects.filter(productlongname__icontains=goods_info)

    if goods_lists.count() > 60:
        goods_lists = goods_lists[1:60]
    data = {
        'flag': 0
    }

    if goods_lists.exists():
        data['flag'] = 1
        data['goods_lists'] = goods_lists
    else:
        data['flag'] = 0

    return render(request, 'user/search.html', context=data)


# 将market页面的数据加入到购物车中
def add_to_cart(request):
    print("我进入到添加函数")
    goods_id = request.GET.get('goods_id')
    goods = Goods.objects.get(id=goods_id)
    print("物品的id为")
    print(goods_id)
    # 先进行用户是否登录的判断
    username = request.session.get('username')

    print("用户名为")
    print(username)

    data = {
        'status': 500,
        'goods_num': 0
    }

    if username:

        user = User.objects.get(username=username)

        cart = Cart.objects.filter(user=user).filter(goods=goods)

        if cart.exists():

            cart = cart.first()
            cart.goods_num = cart.goods_num + 1
            data['goods_num'] = cart.goods_num
            data['status'] = 200
            cart.save()

        else:

            cart = Cart()

            cart.user = user
            cart.goods = goods
            cart.goods_num = 1
            data['goods_num'] = 1
            data['status'] = 200
            cart.save()
    else:
        data['status'] = 500

    return JsonResponse(data=data)


# 点击减号的时候将数据从购物中减少
def sub_from_cart(request):
    goods_id = request.GET.get('goods_id')

    goods = Goods.objects.get(id=goods_id)

    username = request.session.get('username')

    data = {
        'status': 500,
        'goods_num': 0
    }

    if username:

        user = User.objects.get(username=username)

        cart = Cart.objects.filter(user=user).filter(goods=goods)

        if cart.exists():

            cart = cart.first()

            data['status'] = 200

            if cart.goods_num > 1:

                cart.goods_num = cart.goods_num - 1
                cart.save()
                data['goods_num'] = cart.goods_num
                print("该数据存在")
                print(cart.goods_num)

            else:

                # cart.goods_num=0
                cart.delete()
                data['status'] = 400

        else:
            data['status'] = 500

    # print("最终数据为")
    # print(cart.goods_num)
    # data
    return JsonResponse(data=data)


# 对小球进行判断
def judge_ball(request):
    username = request.session.get('username')
    # print("断点1")
    # print(username)
    user = User.objects.filter(username=username)

    user = user.first()

    data = {}
    # print(user)
    # print("断点2")
    if user:

        cart_id = request.GET.get('cart_id')

        flag = request.GET.get('flag')

        cart = Cart.objects.get(id=cart_id)

        if flag == '1':
            cart.is_select = True

            cart.save()

        if flag == '0':
            cart.is_select = False

            cart.save()

        carts = Cart.objects.filter(user=user)

        # 获取被选择的金额
        price = 0

        for c_cart in carts:
            if c_cart.is_select == True:
                price = c_cart.goods_num * c_cart.goods.price + price

        print("这些商品总价为")
        print(price)
        data['price'] = price

        return JsonResponse(data=data)
    else:

        data['status'] = 500
        return JsonResponse(data=data)


# 对数据进行下单操作

def place_an_order(request):
    username = request.session.get('username')

    user = User.objects.filter(username=username)

    data = {
        'order_id': 0,
        'status': 500
    }

    if user.exists():

        user = user.first()

        carts = Cart.objects.filter(user=user).filter(is_select=True)

        if carts.exists():

            order = Order()

            order.user = user

            price = 0

            for cart in carts:

                price = cart.goods_num * cart.goods.price + price

            order.price = price

            order.save()

            for cart in carts:
                # 将数据加入到order_goods中
                print("将数据加入到order_goods中")
                ordergoods = OrderGoods()

                ordergoods.order = order

                ordergoods.goods = cart.goods

                ordergoods.goods_num = cart.goods_num

                ordergoods.save()
                print(ordergoods)

            data['order_id'] = order.id

            data['status'] = 200

            return JsonResponse(data=data)

        else:
        # 用户未加入购物车
            data['status'] = 300

            return JsonResponse(data=data)

    else:
    # 用户未登录

        return JsonResponse(data=data)


# 进行商品的展示

def show_order(request):
    order_id = request.GET.get('order_id')

    orders = Order.objects.filter(id=order_id)

    if orders.exists():
        order = orders.first()

        order_goods_lists = OrderGoods.objects.filter(order=order)

        print("物品展示")
        print(order.price)

        print(order_goods_lists)

        return render(request, 'show_order/show_order.html', {'order_goods_lists': order_goods_lists,'price':order.price})

    return request(request, 'show_order/show_order.html', {'data': "商品数据不存在"})
