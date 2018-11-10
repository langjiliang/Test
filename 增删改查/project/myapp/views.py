from django.shortcuts import render
from django.db.models import F,Q
# Create your views here.
import math
from .models import Phone
from django.http import HttpResponse
# def index(request):
#     # response = HttpResponse("{'person': {'name': 'xiaoming', 'age': 20}}", content_type="json")
#     stu=Student.objects.filter(pk=2)[0]
#     content = stu.content
#     return render(request,'index.html',{"student":content})
def index(request):
    return render(request,'index.html')


def putValue(request):
    getPhone=request.POST.get('phoneName')
    phones=Phone.objects.filter(Q(name__icontains=getPhone)|Q(content__icontains=getPhone))
    if phones:
        return render(request,'putValue.html',{"contents":phones})
    return HttpResponse("NO FOUND")

def add(request):
    return render(request,'add.html')

def dele(request):
    return render(request,'dele.html')

def change(request):
    phones=Phone.objects.all()
    return render(request, 'change.html',{"phones":phones})

def all(request,page):
    page=int(page)
    number=math.ceil(Phone.objects.count()/5)
    phones= Phone.objects.filter(isDelete=False)[(page-1)*5:page*5]
    if page==1:
        return render(request, 'all.html', {"phones": phones, "pageNext": page + 1, "pagePre": number})
    if page==number:
        return render(request, 'all.html', {"phones": phones, "pageNext": 1, "pagePre": number})
    if page>1:
        return render(request, 'all.html',{"phones":phones,"pageNext":page+1,"pagePre":page-1})


def dataDisplay(request):
    render(request,'dataDisplay')


# 添加数据
def addData(request):
    pname=request.POST.get('pname')
    pprice = request.POST.get('pprice')
    pcontent = request.POST.get('pcontent')
    phone=Phone.create(pname,pprice,pcontent)
    phone.save()
    return HttpResponse("succeed")
    # phones=Phone.objects.values()
    # return render(request,'dataDisplay.html',{'phones':phones})

# 删除数据
def deleByName(request):
    pname = request.POST.get('pname')
    phones = Phone.objects.filter(name=pname)
    print(phones)
    for phone in phones:

        phone.isDelete=True
        phone.save()

    for phone in phones:

        print(phone.isDelete)

        return HttpResponse("dele succeed")
    return HttpResponse("No Found")

# 修改数据
def changeByName(request):
    pnum=request.POST.get('num')
    pname=request.POST.get('name')
    pprice=request.POST.get('price')
    pcontent=request.POST.get('content')

    phone=Phone.objects.get(pk=pnum)
    phone.name=pname
    phone.price=pprice
    phone.content=pcontent
    phone.save()
    return HttpResponse(pnum)

