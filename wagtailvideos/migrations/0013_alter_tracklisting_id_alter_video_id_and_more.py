# Generated by Django 4.0.6 on 2022-07-09 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailvideos', '0012_remove_unique_constraint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracklisting',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='videotrack',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='videotranscode',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
