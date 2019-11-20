# -*-coding:utf-8-*-
from django.db import models


class NetworkDescribe(models.Model):
    id = models.CharField("ID", max_length=100, primary_key=True)
    task_id = models.CharField("任务ID", max_length=255)
    net_name = models.CharField("网络名称", max_length=255)
    src_network = models.TextField("网络目录", max_length=500)
    net_describe = models.TextField("网络描述", max_length=500)
    type = models.CharField("网络类型", max_length=100)
    status = models.CharField("任务状态", max_length=100)

    class Meta:
        db_table = "network_describe"
        verbose_name = "网络"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.net_name

    def to_net_dict(self):
        net_desc_dict = {
            'id': self.id,
            'task_id': self.task_id,
            'status': self.status,
            'net_name': self.net_name,
            'net_describe': self.net_describe,
            'type': self.type
        }
        return net_desc_dict


class Datas(models.Model):
    id = models.CharField("ID", max_length=100, primary_key=True)
    task_id = models.CharField("任务ID", max_length=255)
    data_name = models.CharField("数据名称", max_length=255)
    data_type = models.CharField("数据类型", max_length=100)
    images_type = models.CharField("图片类型", max_length=100)
    type = models.CharField("数据类别", max_length=100)
    train = models.CharField("训练集占比", max_length=100)
    val = models.CharField("验证集占比", max_length=100)
    test = models.CharField("测试集占比", max_length=100)
    sour_data = models.TextField("原始数据", max_length=500)
    data_describe = models.TextField("数据描述", max_length=500)
    status = models.CharField("任务状态", max_length=100)
    machine_id = models.CharField("机器ID", max_length=100)

    class Meta:
        db_table = "datas"
        verbose_name = "数据"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.data_name

    def to_data_dict(self):
        data_desc_dict = {
            'id': self.id,
            'task_id': self.task_id,
            'data_type': self.data_type,
            'train': self.train,
            'val': self.val,
            'test': self.test,
            'machine_id': self.machine_id,
            'sour_data': self.sour_data,
            'status': self.status,
            'data_name': self.data_name,
            'data_describe': self.data_describe,
            'type': self.type
        }
        return data_desc_dict


class TrainTask(models.Model):

    id = models.CharField("ID", max_length=100, primary_key=True)
    task_id = models.CharField("任务ID", max_length=255)
    task_name = models.CharField("任务名", max_length=255)
    network_path = models.TextField("网络目录", max_length=500)
    task_describe = models.TextField("任务描述", max_length=500)
    image_type = models.CharField("图片类型", max_length=100)
    data_path = models.TextField("数据目录", max_length=500)
    category_num = models.CharField("训练类别", max_length=100)
    iter_num = models.CharField("全量迭代", max_length=100)
    learning_rate = models.CharField("初始学习率", max_length=100)
    batch_size = models.CharField("批大小", max_length=100)
    steps = models.CharField("步长", max_length=100)
    gpus = models.CharField("GPU", max_length=100)
    model = models.CharField("模型目录", max_length=255)
    start_date = models.DateTimeField("开始时间")
    end_date = models.DateTimeField("结束时间")
    net_desc = models.ForeignKey(NetworkDescribe, on_delete=models.CASCADE, verbose_name='网络描述')
    data_desc = models.ForeignKey(Datas, on_delete=models.CASCADE, verbose_name='数据描述')
    machine_id = models.CharField("机器ID", max_length=100)
    type = models.CharField("训练类型", max_length=100)
    weights = models.TextField("初始权重文件", max_length=500)
    parallel_bool = models.CharField("分布式", max_length=100, default="0")
    status = models.CharField("训练状态", max_length=100)

    class Meta:
        db_table = "train_task"
        verbose_name = "训练"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.task_name

    def to_dict(self):
        desc_dict = {
            'id': self.id,
            'task_id': self.task_id,
            'task_name': self.task_name,
            'network_path': self.network_path,
            'category_num': self.category_num,
            'data_path': self.data_path,
            'iter_num': self.iter_num,
            'learning_rate': self.learning_rate,
            'steps': self.steps,
            'batch_size': self.batch_size,
            'gpus': self.gpus,
            'model': self.model,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'net_desc': self.net_desc.net_describe,
            'task_desc': self.task_describe,
            'data_desc': self.data_desc.data_describe,
            'status': self.status,
            'data_name': self.data_desc.data_name,
            'machine_id': self.machine_id,
            'type': self.type,
            'weights': self.weights,
            'image_type': self.image_type,
            "parallel_bool": self.parallel_bool
        }
        return desc_dict
