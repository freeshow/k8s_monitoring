import json

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    if request.method == "POST":
        concat = request.POST
        post_body = request.body
        json_body = json.loads(post_body)
        print("concat: ", concat)
        print("json_body: ", json_body)


def node_alert(request):
    if request.method == "POST":
        concat = request.POST
        post_body = request.body
        json_body = json.loads(post_body)
        print("concat: ", concat)
        print("json_body: ", json_body)


def pod_alert(request):
    if request.method == "POST":
        concat = request.POST
        post_body = request.body
        json_body = json.loads(post_body)
        print("concat: ", concat)
        print("json_body: ", json_body)
