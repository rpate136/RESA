# Generated by Django 3.1.7 on 2021-03-28 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeExt', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chef',
            options={'ordering': ('first_name',)},
        ),
        migrations.AddField(
            model_name='chef',
            name='email',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chef',
            name='first_name',
            field=models.CharField(default='Sasha', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chef',
            name='last_name',
            field=models.CharField(default='Azad', max_length=50),
            preserve_default=False,
        ),
    ]
