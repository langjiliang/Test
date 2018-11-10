from django.db import models

# Create your models here.
class MianShow(models.Model):
    trackid = models.IntegerField(default=1)
    name = models.CharField(max_length=64)
    img = models.CharField(max_length=255)
    categoryid = models.IntegerField(default=1)
    brandname = models.CharField(max_length=64)
    img1 = models.CharField(max_length=255)
    childcid1 = models.IntegerField(default=1)
    productid1 = models.IntegerField(default=1)
    longname1=models.CharField(max_length=255)
    price1 = models.FloatField(default=1)
    marketprice1 = models.FloatField(default=0)
    img2 = models.CharField(max_length=255)
    childcid2 = models.IntegerField(default=1)
    productid2 = models.IntegerField(default=1)
    longname2 = models.CharField(max_length=255)
    price2 = models.FloatField(default=1)
    marketprice2 = models.FloatField(default=0)
    img3 = models.CharField(max_length=255)
    childcid3 = models.IntegerField(default=1)
    productid3 = models.IntegerField(default=1)
    longname3 = models.CharField(max_length=255)
    price3 = models.FloatField(default=1)
    marketprice3 = models.FloatField(default=0)

    class Meta:
        db_table = 'mainshow'

class FootTypes(models.Model):

    typeid=models.IntegerField(default=1)
    typename=models.CharField(max_length=32)
    childtypenames=models.CharField(max_length=255)
    typesort=models.IntegerField(default=0)

    class Meta:
        db_table='foodtypes'

class Goods(models.Model):


    productid = models.IntegerField(default=1)
    productimg = models.CharField(max_length=255)
    productname = models.CharField(max_length=128)
    productlongname = models.CharField(max_length=255)
    isxf = models.BooleanField(default=False)
    pmdesc = models.BooleanField(default=False)
    specifics = models.CharField(max_length=64)
    price = models.FloatField(default=0)
    marketprice = models.FloatField(default=1)
    categoryid = models.IntegerField(default=1)
    childcid = models.IntegerField(default=1)
    childcidname = models.CharField(max_length=128)
    dealerid = models.IntegerField(default=1)
    storenums = models.IntegerField(default=1)
    productnum = models.IntegerField(default=1)

    class Meta:
        db_table = 'goods'


class User(models.Model):
    username=models.CharField(max_length=32,unique=True)
    password=models.CharField(max_length=256)
    emain=models.CharField(max_length=64,unique=True)
    is_active=models.BooleanField(default=False)
    is_delete=models.BooleanField(default=False)

    class Meta:
        db_table='user'

class Cart(models.Model):

# 注意级联的时候在后面添加on_delete=models.CASCADE在可以级联成功，即级联删除
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)

    goods_num = models.IntegerField(default=1)
    is_select = models.BooleanField(default=True)

    class Meta:
        db_table = 'cart'

# 订单与订单商品是一对多的关系，一个订单包含多个商品，一个用户有多个订单，同时商品和订单商品也是一对多的关系

class Order(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    time = models.DateTimeField(auto_now=True)
    is_finish = models.IntegerField(default=0)

    class Meta:
        db_table = 'order'


class OrderGoods(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=1)
    goods_have = models.BooleanField(default=1)

    class Meta:
        db_table = 'ordergoods'