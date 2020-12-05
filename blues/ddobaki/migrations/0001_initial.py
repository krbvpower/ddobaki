# Generated by Django 2.1.7 on 2019-04-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='get_ddobaki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=50)),
                ('stt', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='post_ddobaki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divided_stt', models.CharField(max_length=100)),
                ('color', models.BooleanField(default=True)),
            ],
        ),
    ]
