# Generated by Django 2.1.3 on 2019-11-20 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto_select',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(max_length=255, verbose_name='任务类型')),
                ('task_id', models.CharField(max_length=255, verbose_name='任务ID')),
                ('output_dir', models.CharField(max_length=255, verbose_name='输出目录')),
                ('gpus', models.CharField(max_length=255, verbose_name='GPU')),
                ('sele_ratio', models.CharField(max_length=255, verbose_name='挑选数量')),
                ('weights_dir', models.CharField(max_length=255, verbose_name='模型名')),
                ('track_file', models.CharField(max_length=255, verbose_name='外业文件')),
                ('task_file', models.CharField(max_length=255, verbose_name='外业ID')),
                ('isshuffle', models.CharField(max_length=255, verbose_name='随机')),
                ('status', models.CharField(max_length=255, verbose_name='任务状态')),
            ],
            options={
                'verbose_name': '挑选数据',
                'verbose_name_plural': '挑选数据',
                'db_table': 'auto_select',
            },
        ),
        migrations.CreateModel(
            name='CheckDatas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=255, verbose_name='任务ID')),
                ('task_name', models.CharField(max_length=255, verbose_name='任务名')),
                ('gpus', models.CharField(max_length=255, verbose_name='GPU')),
                ('weights_dir', models.CharField(max_length=255, verbose_name='模型名')),
                ('status', models.CharField(max_length=255, verbose_name='任务状态')),
            ],
            options={
                'verbose_name': '检查项挑错',
                'verbose_name_plural': '检查项挑错',
                'db_table': 'check_datas',
            },
        ),
        migrations.CreateModel(
            name='Confidence_Datas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_whole_con', models.CharField(max_length=255, verbose_name='原始整体置信度')),
                ('whole_con', models.CharField(max_length=255, verbose_name='整体置信度')),
                ('origin_cls_con', models.TextField(max_length=500, verbose_name='原始分类置信度')),
                ('model', models.TextField(max_length=500, verbose_name='模型')),
                ('trackpointid', models.TextField(max_length=500, verbose_name='轨迹点ID')),
                ('task_name', models.TextField(max_length=500, verbose_name='任务名')),
            ],
            options={
                'verbose_name': '数据置信度',
                'verbose_name_plural': '数据置信度',
                'db_table': 'confidence_datas',
            },
        ),
        migrations.CreateModel(
            name='LabelData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('time_info', models.CharField(max_length=255, verbose_name='入库时间')),
                ('trackpointid', models.CharField(max_length=255, verbose_name='轨迹点ID')),
                ('pacid', models.CharField(max_length=255, verbose_name='包ID')),
                ('imgrange', models.CharField(max_length=255, verbose_name='图片类别')),
                ('city', models.CharField(max_length=255, verbose_name='城市')),
                ('label_info', models.CharField(max_length=255, verbose_name='色板信息')),
                ('tag_info', models.TextField(max_length=4000, verbose_name='分类统计')),
            ],
            options={
                'verbose_name': '数据管理',
                'verbose_name_plural': '数据管理',
                'db_table': 'data_manage',
            },
        ),
        migrations.CreateModel(
            name='LabelProcess',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=255, verbose_name='任务ID')),
                ('version', models.CharField(max_length=255, verbose_name='任务包名')),
                ('name', models.CharField(max_length=255, verbose_name='输出目录')),
                ('types', models.CharField(max_length=255, verbose_name='任务类型')),
                ('color_info', models.CharField(max_length=255, verbose_name='色板')),
                ('status', models.CharField(max_length=255, verbose_name='任务状态')),
            ],
            options={
                'verbose_name': '任务包发布',
                'verbose_name_plural': '任务包发布',
                'db_table': 'label_process',
            },
        ),
        migrations.CreateModel(
            name='LineDownload',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=255, verbose_name='任务ID')),
                ('taskid_start', models.CharField(max_length=255, verbose_name='起始ID')),
                ('taskid_end', models.CharField(max_length=255, verbose_name='结束ID')),
                ('dest', models.CharField(max_length=255, verbose_name='输出目录')),
                ('status', models.CharField(max_length=255, verbose_name='任务状态')),
            ],
            options={
                'verbose_name': '在线下载',
                'verbose_name_plural': '在线下载',
                'db_table': 'linedown_datas',
            },
        ),
        migrations.CreateModel(
            name='OfflineImport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=255, verbose_name='任务ID')),
                ('roadelement', models.CharField(max_length=255, verbose_name='色板信息')),
                ('source', models.CharField(max_length=255, verbose_name='数据来源')),
                ('author', models.CharField(max_length=255, verbose_name='创始人')),
                ('annotype', models.CharField(max_length=255, verbose_name='标注类型')),
                ('datakind', models.CharField(max_length=255, verbose_name='数据类型')),
                ('city', models.CharField(max_length=255, verbose_name='城市')),
                ('imgoprange', models.CharField(max_length=255, verbose_name='图片操作范围')),
                ('status', models.CharField(max_length=255, verbose_name='任务状态')),
            ],
            options={
                'verbose_name': '离线上传',
                'verbose_name_plural': '离线上传',
                'db_table': 'offline_datas',
            },
        ),
        migrations.CreateModel(
            name='Schedulefrom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.CharField(max_length=255, verbose_name='任务状态ID')),
                ('task_id', models.CharField(max_length=255, verbose_name='任务ID')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('picid', models.CharField(max_length=255, verbose_name='包ID')),
                ('statue', models.CharField(max_length=255, verbose_name='任务状态')),
            ],
            options={
                'verbose_name': '数据管理进度',
                'verbose_name_plural': '数据管理进度',
                'db_table': 'progress',
            },
        ),
        migrations.CreateModel(
            name='TaskDivide',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=255, verbose_name='任务ID')),
                ('version', models.CharField(max_length=255, verbose_name='任务包名')),
                ('step', models.CharField(max_length=255, verbose_name='每包数量')),
                ('types', models.CharField(max_length=255, verbose_name='任务类型')),
                ('status', models.CharField(max_length=255, verbose_name='任务状态')),
            ],
            options={
                'verbose_name': '任务包生成',
                'verbose_name_plural': '任务包生成',
                'db_table': 'task_divide',
            },
        ),
    ]
