# Generated by Django 3.1.5 on 2021-03-05 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nutriscore', models.CharField(max_length=1)),
                ('url', models.CharField(max_length=1000)),
                ('barcode', models.CharField(max_length=20, unique=True)),
                ('ingredient', models.CharField(max_length=3000)),
                ('url_image', models.CharField(max_length=1000, null=True)),
                ('nutriment', models.CharField(max_length=5000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='researches.category')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='researches.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='researches.product')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]