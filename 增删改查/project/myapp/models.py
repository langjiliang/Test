from django.db import models

# Create your models here.
# class Student(models.Model):
#     content = models.CharField(max_length=50)
    # @classmethod
    # def create(cls):
    #     stu=cls(content=scontent)

class Phone(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    content = models.CharField(max_length=50)
    isDelete=models.BooleanField(default=False)

    @classmethod
    def create(cls,pname,pprice,pcontent):
        phone=cls(name=pname,price=pprice,content=pcontent)
        return phone

