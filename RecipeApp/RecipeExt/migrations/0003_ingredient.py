# Generated by Django 3.1.7 on 2021-03-28 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeExt', '0002_auto_20210328_0306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
