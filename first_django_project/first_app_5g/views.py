from django.shortcuts import render
from django.http import HttpResponse

import json

def index(request):
    return HttpResponse("Hi World")

def background(request):
    background = ["5th Generation Mobile Networks (5G) module", "4 years Work experience with Endava company working with servers, backend and Cloud architecutre projects", "More than 90 IT courses of related topics with certificates taken", "Server administration and deployment of self created website project auragora.com"]
    return HttpResponse(json.dumps(background), content_type="application/json")

def email(request):
    return HttpResponse("armando.a.florescolet@campus.tu-berlin.de")

def mtknr(request):
    return HttpResponse("0406407")

def name(request):
    return HttpResponse("Armando Andres Flores Colet")

def programOfStudy(request):
    return HttpResponse("Bachelor Elektrotechnik")

def skills(request):
    skills = ["Linux", "Docker", "Virtual Machines", "Python", "Cloud Services", "GCloud", "Kubernetes", "PHP", "Javascript", "MySQL", "Api-Rest", "C/++", "Java", "Django", "Laravel", "CI/CD Pipelines", "Scripts","Git", "Curl", "TCP UDP and Socket protocols", "Grafana", "Prometheus"]
    return HttpResponse(json.dumps(skills), content_type="application/json")

def topics(request):
    topics = {1: "ML-based 5G System Prediction and Anomaly Detection", 2: "Measurements of performance metrics for the 5G core components", 3: "Intelligent Data Compression for Bandwidth Optimization"}
    return HttpResponse(json.dumps(topics), content_type="application/json")
    