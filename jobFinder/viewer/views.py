from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import Job


def jobs(request):
    return HttpResponse('Hello')


class ListJobs(ListView):
    template_name = 'jobs.html'
    model = Job
    context_object_name = 'jobs'


class DetailJob(DetailView):
    template_name = 'job_details.html'
    model = Job
    context_object_name = 'job'