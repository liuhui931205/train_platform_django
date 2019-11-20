# Generated by Django 2.1.3 on 2019-11-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluate_Models',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=255, verbose_name='任务ID')),
                ('sour_dir', models.TextField(max_length=500, verbose_name='源目录')),
                ('gpus', models.CharField(max_length=100, verbose_name='GPU')),
                ('dest_dir', models.TextField(max_length=500, verbose_name='目标目录')),
                ('single_gpu', models.CharField(max_length=100, verbose_name='进程')),
                ('model', models.TextField(max_length=500, verbose_name='模型')),
                ('status', models.CharField(max_length=100, verbose_name='状态')),
                ('host', models.CharField(max_length=100, verbose_name='机器ID')),
            ],
            options={
                'verbose_name': '模型',
                'verbose_name_plural': '模型',
            },
        ),
        migrations.CreateModel(
            name='Released_Models',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=255, verbose_name='任务ID')),
                ('tasks_name', models.CharField(max_length=255, verbose_name='任务名称')),
                ('version', models.CharField(max_length=255, verbose_name='模型目录')),
                ('model_name', models.CharField(max_length=255, verbose_name='模型名')),
                ('env', models.CharField(max_length=255, verbose_name='环境')),
                ('adcode', models.CharField(max_length=100, verbose_name='地区ID')),
                ('desc', models.TextField(max_length=500, verbose_name='模型描述')),
                ('time', models.DateTimeField(verbose_name='发布时间')),
                ('type', models.CharField(max_length=255, verbose_name='模型类别')),
                ('status', models.CharField(max_length=100, verbose_name='发布状态')),
            ],
            options={
                'verbose_name': '模型',
                'verbose_name_plural': '模型',
            },
        ),
    ]
