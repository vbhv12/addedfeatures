# Generated by Django 3.0.7 on 2020-07-13 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_auto_20200713_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='tag',
        ),
        migrations.AddField(
            model_name='event',
            name='tag',
            field=models.CharField(blank=True, choices=[('Incomplete', 'Incomplete'), ('Complete', 'Complete')], default='blank', max_length=12, null=True),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
