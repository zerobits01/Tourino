# Generated by Django 2.0.2 on 2019-11-27 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TourinoAdmin', '0005_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TourinoAdmin.TourinoAdmin'),
        ),
    ]
