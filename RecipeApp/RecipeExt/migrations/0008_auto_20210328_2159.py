# Generated by Django 3.1.7 on 2021-03-28 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeExt', '0007_auto_20210328_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='author',
            new_name='chef',
        ),
    ]
