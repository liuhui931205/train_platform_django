# -*-coding:utf-8-*-
from django.db import models


class Released_Models(models.Model):

    id = models.AutoField("ID", primary_key=True)
    task_id = models.CharField("任务ID", max_length=255)
    tasks_name = models.CharField("任务名称", max_length=255)
    version = models.CharField("模型目录", max_length=255)
    model_name = models.CharField("模型名", max_length=255)
    env = models.CharField("环境", max_length=255)
    adcode = models.CharField("地区ID", max_length=100)
    desc = models.TextField("模型描述", max_length=500)
    time = models.DateTimeField("发布时间")
    type = models.CharField("模型类别", max_length=255)
    status = models.CharField("发布状态", max_length=100)

    class Meta:
        db_table = "released_models"
        verbose_name = "模型发布"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tasks_name

    # def to_models_dict(self):
    #     model_dict = {
    #         'id': self.id,
    #         'task_id': self.task_id,
    #         'tasks_name': self.tasks_name,
    #         'version': self.version,
    #         'model_name': self.model_name,
    #         'env': self.env,
    #         'adcode': self.adcode,
    #         'desc': self.desc,
    #         'time': self.time,
    #         'type': self.type,
    #         'status': self.status
    #     }
    #     return model_dict


class Evaluate_Models(models.Model):


    id = models.AutoField("ID", primary_key=True)
    task_id = models.CharField("任务ID", max_length=255)
    sour_dir = models.TextField("源目录", max_length=500)
    gpus = models.CharField("GPU", max_length=100)
    dest_dir = models.TextField("目标目录", max_length=500)
    single_gpu = models.CharField("进程", max_length=100)
    model = models.TextField("模型", max_length=500)
    status = models.CharField("状态", max_length=100)
    host = models.CharField("机器ID", max_length=100)

    class Meta:
        db_table = "evaluate_models"
        verbose_name = "模型评估"
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return self.tasks_name

    # def to_model_dict(self):
    #     model_dict = {
    #         'id': self.id,
    #         'task_id': self.task_id,
    #         'sour_dir': self.sour_dir,
    #         'gpus': self.gpus,
    #         'dest_dir': self.dest_dir,
    #         'single_gpu': self.single_gpu,
    #         'model': self.model,
    #         'status': self.status,
    #         "host": self.host
    #     }
    #     return model_dict
