# Generated by Django 4.0.2 on 2022-03-30 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='rpiData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=200, null=True)),
                ('saturation', models.IntegerField()),
                ('temperature', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
