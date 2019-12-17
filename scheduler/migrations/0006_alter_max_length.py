# Generated by Django 2.2.2 on 2019-12-17 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_added_result_ttl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronjob',
            name='callable',
            field=models.CharField(max_length=4096, verbose_name='callable'),
        ),
        migrations.AlterField(
            model_name='cronjob',
            name='queue',
            field=models.CharField(max_length=32, verbose_name='queue'),
        ),
        migrations.AlterField(
            model_name='repeatablejob',
            name='callable',
            field=models.CharField(max_length=4096, verbose_name='callable'),
        ),
        migrations.AlterField(
            model_name='repeatablejob',
            name='queue',
            field=models.CharField(max_length=32, verbose_name='queue'),
        ),
        migrations.AlterField(
            model_name='scheduledjob',
            name='callable',
            field=models.CharField(max_length=4096, verbose_name='callable'),
        ),
        migrations.AlterField(
            model_name='scheduledjob',
            name='queue',
            field=models.CharField(max_length=32, verbose_name='queue'),
        ),
    ]