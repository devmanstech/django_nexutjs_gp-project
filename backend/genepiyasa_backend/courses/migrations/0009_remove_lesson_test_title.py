# Generated by Django 3.0.2 on 2020-02-20 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_lesson_test_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='test_title',
        ),
    ]