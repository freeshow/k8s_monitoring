import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.


def index(request):
    if request.method == "POST":
        post_body = request.body
        json_body = json.loads(post_body)
        print("json_body: ", json_body)
        return JsonResponse({"json_body": json_body}, safe=False)


def node_alert(request):
    if request.method == "POST":
        post_body = request.body
        json_body = json.loads(post_body)
        print("json_body: ", json_body)
        return JsonResponse({"json_body": json_body}, safe=False)


def pod_alert(request):
    if request.method == "POST":
        post_body = request.body
        json_body = json.loads(post_body)
        print("json_body: ", json_body)
        return JsonResponse({"json_body": json_body}, safe=False)
