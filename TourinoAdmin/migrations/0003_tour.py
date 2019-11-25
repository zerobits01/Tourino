# Generated by Django 2.0.2 on 2019-11-25 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TourinoAdmin', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, unique=True)),
                ('price', models.DecimalField(decimal_places=7, max_digits=20)),
                ('description', models.TextField()),
                ('location', models.TextField(blank=True)),
                ('duration', models.IntegerField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('image_url', models.TextField()),
                ('online', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TourinoAdmin.TourinoAdmin')),
            ],
        ),
    ]