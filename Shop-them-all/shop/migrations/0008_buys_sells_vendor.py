# Generated by Django 2.2.1 on 2019-05-29 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20190529_0139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sells',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_product', models.IntegerField()),
                ('id_vendor', models.IntegerField()),
            ],
            options={
                'unique_together': {('id_product', 'id_vendor')},
            },
        ),
        migrations.CreateModel(
            name='Buys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_product', models.IntegerField()),
                ('id_user', models.IntegerField()),
            ],
            options={
                'unique_together': {('id_product', 'id_user')},
            },
        ),
    ]
