# Generated by Django 2.1 on 2018-11-08 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FootTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.IntegerField(default=1)),
                ('typename', models.CharField(max_length=32)),
                ('childtypenames', models.CharField(max_length=255)),
                ('typesort', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'foodtypes',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField(default=1)),
                ('productimg', models.CharField(max_length=255)),
                ('productname', models.CharField(max_length=128)),
                ('productlongname', models.CharField(max_length=255)),
                ('isxf', models.BooleanField(default=False)),
                ('pmdesc', models.BooleanField(default=False)),
                ('specifics', models.CharField(max_length=64)),
                ('price', models.FloatField(default=0)),
                ('marketprice', models.FloatField(default=1)),
                ('categoryid', models.IntegerField(default=1)),
                ('childcid', models.IntegerField(default=1)),
                ('childcidname', models.CharField(max_length=128)),
                ('dealerid', models.IntegerField(default=1)),
                ('storenums', models.IntegerField(default=1)),
                ('productnum', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='MianShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackid', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=64)),
                ('img', models.CharField(max_length=255)),
                ('categoryid', models.IntegerField(default=1)),
                ('brandname', models.CharField(max_length=64)),
                ('img1', models.CharField(max_length=255)),
                ('childcid1', models.IntegerField(default=1)),
                ('productid1', models.IntegerField(default=1)),
                ('longname1', models.CharField(max_length=255)),
                ('price1', models.FloatField(default=1)),
                ('marketprice1', models.FloatField(default=0)),
                ('img2', models.CharField(max_length=255)),
                ('childcid2', models.IntegerField(default=1)),
                ('productid2', models.IntegerField(default=1)),
                ('longname2', models.CharField(max_length=255)),
                ('price2', models.FloatField(default=1)),
                ('marketprice2', models.FloatField(default=0)),
                ('img3', models.CharField(max_length=255)),
                ('childcid3', models.IntegerField(default=1)),
                ('productid3', models.IntegerField(default=1)),
                ('longname3', models.CharField(max_length=255)),
                ('price3', models.FloatField(default=1)),
                ('marketprice3', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'mainshow',
            },
        ),
    ]