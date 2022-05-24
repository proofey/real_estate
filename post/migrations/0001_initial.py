# Generated by Django 4.0.4 on 2022-05-24 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=10, verbose_name='option')),
            ],
        ),
        migrations.CreateModel(
            name='ConstructionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Construction type')),
            ],
        ),
        migrations.CreateModel(
            name='Heating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Heating')),
            ],
        ),
        migrations.CreateModel(
            name='OfferType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Offer type')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Property type')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('location', models.CharField(max_length=50, verbose_name='Location')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('neighborhood', models.CharField(blank=True, max_length=60, verbose_name='Neighborhood')),
                ('square_meters', models.IntegerField(verbose_name='Square meters')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('more_information', models.TextField(verbose_name='More information')),
                ('for_contact', models.CharField(max_length=100, null=True, verbose_name='For contact')),
                ('main_picture', models.ImageField(default='default_property.jpg', upload_to='property_pictures', verbose_name='Main picture')),
                ('picture_1', models.ImageField(default='default_property.jpg', upload_to='property_pictures', verbose_name='Picture 1')),
                ('picture_2', models.ImageField(default='default_property.jpg', upload_to='property_pictures', verbose_name='Picture 2')),
                ('picture_3', models.ImageField(default='default_property.jpg', upload_to='property_pictures', verbose_name='Picture 3')),
                ('picture_4', models.ImageField(default='default_property.jpg', upload_to='property_pictures', verbose_name='Picture 4')),
                ('picture_5', models.ImageField(default='default_property.jpg', upload_to='property_pictures', verbose_name='Picture 5')),
                ('picture_6', models.ImageField(default='default_property.jpg', upload_to='property_pictures', verbose_name='Picture 6')),
                ('picture_7', models.ImageField(default='default_property.jpg', upload_to='property_pictures', verbose_name='Picture 7')),
                ('picture_8', models.ImageField(default='default_property.jpg', upload_to='property_pictures', verbose_name='Picture 8')),
                ('picture_9', models.ImageField(default='default_property.jpg', upload_to='property_pictures', verbose_name='Picture 9')),
                ('picture_10', models.ImageField(default='default_property.jpg', upload_to='property_pictures', verbose_name='Picture 10')),
                ('construction_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='post.constructiontype')),
                ('heating', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='post.heating')),
                ('offer_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='post.offertype')),
                ('property_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='post.propertytype')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
