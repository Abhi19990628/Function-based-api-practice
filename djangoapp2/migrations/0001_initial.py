# Generated by Django 5.0.4 on 2024-04-29 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abhishek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
    ]
