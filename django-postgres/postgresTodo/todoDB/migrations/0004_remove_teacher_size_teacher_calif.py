# Generated by Django 4.2.1 on 2023-06-04 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoDB', '0003_alter_teacher_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='size',
        ),
        migrations.AddField(
            model_name='teacher',
            name='calif',
            field=models.IntegerField(default=6),
        ),
    ]
