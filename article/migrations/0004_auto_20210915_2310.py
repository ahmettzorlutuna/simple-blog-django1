# Generated by Django 3.2.6 on 2021-09-15 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_author',
            field=models.CharField(max_length=50, null=True, verbose_name='İsim'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=models.CharField(max_length=200, null=True, verbose_name='Yorum'),
        ),
    ]
