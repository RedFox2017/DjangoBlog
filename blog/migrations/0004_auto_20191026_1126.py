# Generated by Django 2.1.5 on 2019-10-26 03:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpicinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloginfo',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='authorinfo',
            name='au_password',
            field=models.CharField(default=django.utils.timezone.now, max_length=48, verbose_name='密码'),
            preserve_default=False,
        ),
    ]
