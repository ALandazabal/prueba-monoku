# Generated by Django 3.1.7 on 2021-07-22 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_auto_20210424_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='song',
            name='subgenres',
        ),
        migrations.AddField(
            model_name='album',
            name='band',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapi.band'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='subgenre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapi.subgenre'),
            preserve_default=False,
        ),
    ]
