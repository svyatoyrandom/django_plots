# Generated by Django 3.2.8 on 2021-11-18 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plot',
            old_name='function',
            new_name='plot_function',
        ),
        migrations.RemoveField(
            model_name='plot',
            name='date_update',
        ),
    ]
