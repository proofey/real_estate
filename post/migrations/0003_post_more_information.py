# Generated by Django 4.0.4 on 2022-05-21 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_for_contact_post_main_picture_post_picture_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='more_information',
            field=models.TextField(default='More Information', verbose_name='More information'),
            preserve_default=False,
        ),
    ]
