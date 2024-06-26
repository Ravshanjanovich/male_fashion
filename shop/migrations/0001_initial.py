# Generated by Django 5.0.6 on 2024-06-07 07:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Brending',
                'verbose_name_plural': 'Breinding',
                'db_table': 'Brending',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
                'db_table': 'Cate',
            },
        ),
        migrations.CreateModel(
            name='ColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='color')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
                'db_table': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='SizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
                'db_table': 'Size',
            },
        ),
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='tag name')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'db_table': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('short_desc', models.CharField(max_length=150, verbose_name='short description')),
                ('long_desc', models.TextField(verbose_name='long description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='price')),
                ('real_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='real price')),
                ('sale', models.BooleanField(default=False, verbose_name='sale')),
                ('discount', models.PositiveSmallIntegerField(default=0, verbose_name='discount')),
                ('main_image', models.ImageField(upload_to='media/shop_product/%Y/%m/%d', verbose_name='image')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='product', to='shop.brandmodel', verbose_name='brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='product', to='shop.category', verbose_name='category')),
                ('color', models.ManyToManyField(related_name='product', to='shop.colormodel', verbose_name='color')),
                ('size', models.ManyToManyField(related_name='product', to='shop.sizemodel', verbose_name='size')),
                ('tags', models.ManyToManyField(related_name='product', to='shop.tagmodel', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'ProductModel',
                'verbose_name_plural': 'ProductModels',
                'db_table': 'Products',
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='shop.productmodel', verbose_name='product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Wishlist',
                'verbose_name_plural': 'WishLists',
                'db_table': 'Wishlist',
                'unique_together': {('user', 'product')},
            },
        ),
    ]
