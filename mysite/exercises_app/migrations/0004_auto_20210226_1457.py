# Generated by Django 3.1.4 on 2021-02-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises_app', '0003_song_band'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='band',
            field=models.ManyToManyField(to='exercises_app.Band'),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]