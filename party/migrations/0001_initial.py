# Generated by Django 2.0.5 on 2018-05-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('feedback', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gotcha',
            fields=[
                ('sl_no', models.AutoField(primary_key=True, serialize=False)),
                ('secret', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Oqp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.CharField(max_length=20)),
                ('question', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Sorry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sorry', models.TextField(max_length=1000)),
                ('to', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WishingWell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('crush_desc', models.TextField(max_length=1500)),
            ],
        ),
    ]
