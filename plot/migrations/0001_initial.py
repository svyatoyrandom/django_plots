# Generated by Django 3.2.8 on 2021-11-03 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_update', models.DateField()),
                ('interval', models.IntegerField()),
                ('step', models.IntegerField()),
                ('function', models.TextField()),
            ],
        ),
    ]
