# Generated by Django 3.1.7 on 2021-03-28 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeExt', '0005_auto_20210328_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cook_time',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='total_time',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
