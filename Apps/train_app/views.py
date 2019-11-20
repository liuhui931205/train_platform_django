# -*-coding:utf-8-*-
from django.views import View
import json
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse, FileResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models
# Create your views here.


class trainHistory(View):

    def get(self, request):
        # Code block for GET request
        pass

    def post(self, request):
        req_dict = json.loads(request.read())
        task_id = req_dict["task_id"]
        if task_id:
            task_indexs = models.TrainTask.objects.get(task_id=task_id)
        else:
            task_indexs = models.TrainTask.objects.all().select_related("data_desc","net_desc").order_by("-id")
            # blog_index.all()
        data = []
        for task in list(task_indexs):
            data.append(task.to_dict())
        resp = JsonResponse({"errno": 1, "data": data})

        return resp


class Index(View):

    def get(self, request):
        # Code block for GET request
        return render(request, "index.html")

    def post(self, request):
        req_dict = request.json
        print("ss")
