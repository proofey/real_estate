# Generated by Django 4.0.4 on 2022-05-24 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='balcony',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='balcony', to='post.availableoptions'),
        ),
        migrations.AddField(
            model_name='post',
            name='basement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='basement', to='post.availableoptions'),
        ),
        migrations.AddField(
            model_name='post',
            name='bathroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bathroom', to='post.availableoptions'),
        ),
        migrations.AddField(
            model_name='post',
            name='bedroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bedroom', to='post.availableoptions'),
        ),
        migrations.AddField(
            model_name='post',
            name='floor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='floor', to='post.availableoptions'),
        ),
        migrations.AddField(
            model_name='post',
            name='floors',
            field=models.IntegerField(blank=True, null=True, verbose_name='Floors'),
        ),
        migrations.AddField(
            model_name='post',
            name='garage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='garage', to='post.availableoptions'),
        ),
        migrations.AddField(
            model_name='post',
            name='garret',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='garret', to='post.availableoptions'),
        ),
        migrations.AddField(
            model_name='post',
            name='number_of_rooms',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='number_of_doors', to='post.availableoptions'),
        ),
        migrations.AddField(
            model_name='post',
            name='parking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='parking', to='post.availableoptions'),
        ),
    ]
