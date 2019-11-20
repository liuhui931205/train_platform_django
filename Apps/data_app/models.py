# -*-coding:utf-8-*-
from django.db import models


class Auto_select(models.Model):

    id = models.AutoField("ID", primary_key=True)
    task_type = models.CharField("任务类型", max_length=255)
    task_id = models.CharField("任务ID", max_length=255)
    output_dir = models.CharField("输出目录", max_length=255)
    gpus = models.CharField("GPU", max_length=255)
    sele_ratio = models.CharField("挑选数量", max_length=255)
    weights_dir = models.CharField("模型名", max_length=255)
    track_file = models.CharField("外业文件", max_length=255)
    task_file = models.CharField("外业ID", max_length=255)
    isshuffle = models.CharField("随机", max_length=255)
    status = models.CharField("任务状态", max_length=255)

    class Meta:
        db_table = "auto_select"
        verbose_name = "挑选数据"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.task_type

    # def to_dict(self):
    #     select_dict = {
    #         'task_id': self.task_id,
    #         'task_type': self.task_type,
    #         'output_dir': self.output_dir,
    #         'gpus': self.gpus,
    #         'sele_ratio': self.sele_ratio,
    #         'weights_dir': self.weights_dir,
    #         'track_file': self.track_file,
    #         'task_file': self.task_file,
    #         'isshuffle': self.isshuffle,
    #         'status': self.status
    #     }
    #     return select_dict


class OfflineImport(models.Model):

    id = models.AutoField("ID", primary_key=True)
    task_id = models.CharField("任务ID", max_length=255)
    roadelement = models.CharField("色板信息", max_length=255)
    source = models.CharField("数据来源", max_length=255)
    author = models.CharField("创始人", max_length=255)
    annotype = models.CharField("标注类型", max_length=255)
    datakind = models.CharField("数据类型", max_length=255)
    city = models.CharField("城市", max_length=255)
    imgoprange = models.CharField("图片操作范围", max_length=255)
    status = models.CharField("任务状态", max_length=255)

    class Meta:
        db_table = "offline_datas"
        verbose_name = "离线上传"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "离线上传"

    # def to_dict(self):
    #     data_dict = {
    #         'id': self.id,
    #         'task_id': self.task_id,
    #         'roadelement': self.roadelement,
    #         'source': self.source,
    #         'author': self.author,
    #         'annotype': self.annotype,
    #         'datakind': self.datakind,
    #         'city': self.city,
    #         'imgoprange': self.imgoprange,
    #         'status': self.status
    #     }
    #     return data_dict


class LineDownload(models.Model):

    id = models.AutoField("ID", primary_key=True)
    task_id = models.CharField("任务ID", max_length=255)
    taskid_start = models.CharField("起始ID", max_length=255)
    taskid_end = models.CharField("结束ID", max_length=255)
    dest = models.CharField("输出目录", max_length=255)
    status = models.CharField("任务状态", max_length=255)

    class Meta:
        db_table = "linedown_datas"
        verbose_name = "在线下载"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "在线下载"

    # def to_dict(self):
    #     data_dict = {
    #         'task_id': self.task_id,
    #         'taskid_start': self.taskid_start,
    #         'taskid_end': self.taskid_end,
    #         'dest': self.dest,
    #         'status': self.status
    #     }
    #     return data_dict


class TaskDivide(models.Model):

    id = models.AutoField("ID", primary_key=True)
    task_id = models.CharField("任务ID", max_length=255)
    version = models.CharField("任务包名", max_length=255)
    step = models.CharField("每包数量", max_length=255)
    types = models.CharField("任务类型", max_length=255)
    status = models.CharField("任务状态", max_length=255)

    class Meta:
        db_table = "task_divide"
        verbose_name = "任务包生成"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.version

    # def to_dict(self):
    #     data_dict = {
    #         'task_id': self.task_id,
    #         'version': self.version,
    #         'step': self.step,
    #         'types': self.types,
    #         'status': self.status
    #     }
    #     return data_dict


class LabelProcess(models.Model):

    id = models.AutoField("ID", primary_key=True)
    task_id = models.CharField("任务ID", max_length=255)
    version = models.CharField("任务包名", max_length=255)
    name = models.CharField("输出目录", max_length=255)
    types = models.CharField("任务类型", max_length=255)
    color_info = models.CharField("色板", max_length=255)
    status = models.CharField("任务状态", max_length=255)

    class Meta:
        db_table = "label_process"
        verbose_name = "任务包发布"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.version

    # def to_dict(self):
    #     data_dict = {
    #         'task_id': self.task_id,
    #         'version': self.version,
    #         'name': self.name,
    #         'types': self.types,
    #         'color_info': self.color_info,
    #         'status': self.status,
    #     }
    #     return data_dict


class CheckDatas(models.Model):

    id = models.AutoField("ID", primary_key=True)
    task_id = models.CharField("任务ID", max_length=255)
    task_name = models.CharField("任务名", max_length=255)
    gpus = models.CharField("GPU", max_length=255)
    weights_dir = models.CharField("模型名", max_length=255)
    status = models.CharField("任务状态", max_length=255)

    class Meta:
        db_table = "check_datas"
        verbose_name = "检查项挑错"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.task_name

    # def to_dict(self):
    #     data_dict = {
    #         'task_id': self.task_id,
    #         'task_name': self.task_name,
    #         'weights_dir': self.weights_dir,
    #         'status': self.status
    #     }
    #     return data_dict


class Confidence_Datas(models.Model):
    id = models.AutoField("ID", primary_key=True)
    origin_whole_con = models.CharField("原始整体置信度", max_length=255)
    whole_con = models.CharField("整体置信度", max_length=255)
    origin_cls_con = models.TextField("原始分类置信度", max_length=500)
    model = models.TextField("模型", max_length=500)
    trackpointid = models.TextField("轨迹点ID", max_length=500)
    task_name = models.TextField("任务名", max_length=500)


    class Meta:
        db_table = "confidence_datas"
        verbose_name = "数据置信度"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.task_name

    # def to_dict(self):
    #     data_dict = {
    #         'origin_whole_con': self.origin_whole_con,
    #         'whole_con': self.whole_con,
    #         'origin_cls_con': self.origin_cls_con,
    #         'trackpointid': self.trackpointid,
    #         'model': self.model,
    #         'task_name': self.task_name
    #     }
    #     return data_dict


class LabelData(models.Model):

    id = models.AutoField("ID", primary_key=True)
    time_info = models.CharField("入库时间", max_length=255)
    trackpointid = models.CharField("轨迹点ID", max_length=255)
    pacid = models.CharField("包ID", max_length=255)
    imgrange = models.CharField("图片类别", max_length=255)
    city = models.CharField("城市", max_length=255)
    label_info = models.CharField("色板信息", max_length=255)
    tag_info = models.TextField("分类统计", max_length=4000)

    class Meta:
        db_table = "data_manage"
        verbose_name = "数据管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.trackpointid

    # def to_dict(self):
    #     data_dict = {
    #         'time_info': self.time_info,
    #         'trackpointid': self.trackpointid,
    #         'imgrange': self.imgrange,
    #         'city': self.city,
    #         'pacid': self.pacid,
    #         'label_info': self.label_info,
    #         'tag_info': self.tag_info
    #     }
    #     return data_dict


class Schedulefrom(models.Model):

    id = models.AutoField("ID", primary_key=True)
    id_code = models.CharField("任务状态ID", max_length=255)
    task_id = models.CharField("任务ID", max_length=255)
    start_time = models.DateTimeField("开始时间")
    end_time = models.DateTimeField("结束时间")
    picid = models.CharField("包ID", max_length=255)
    statue = models.CharField("任务状态", max_length=255)

    class Meta:
        db_table = "progress"
        verbose_name = "数据管理进度"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.statue

    # def to_dict(self):
    #     data_dict = {
    #         "id_code": self.id_code,
    #         'task_id': self.task_id,
    #         'picid': self.picid,
    #         'start_time': self.start_time,
    #         "end_time": self.end_time,
    #         'statue': self.statue
    #     }
    #     return data_dict