# Generated by Django 3.1.7 on 2021-04-19 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwordgeneratorapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cardNumber', models.IntegerField()),
                ('date', models.CharField(max_length=5)),
                ('securityCode', models.IntegerField()),
            ],
        ),
    ]
