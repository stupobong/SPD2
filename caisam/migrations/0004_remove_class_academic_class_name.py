# Generated by Django 4.2 on 2023-05-14 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caisam', '0003_alter_class_academic_class_academic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class_academic',
            name='class_name',
        ),
    ]
