# Generated by Django 4.1.4 on 2023-03-01 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_post_content'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Count',
        ),
    ]