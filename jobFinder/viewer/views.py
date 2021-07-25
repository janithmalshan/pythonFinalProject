from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Job, Category, Skill


# Jobs
class ListJobs(ListView):
    template_name = 'jobs.html'
    model = Job
    context_object_name = 'jobs'


class DetailJob(DetailView):
    template_name = 'job_details.html'
    model = Job
    context_object_name = 'job'


class UpdateJob(UpdateView):
    template_name = 'job_update.html'
    model = Job
    success_url = reverse_lazy('jobs')
    fields = '__all__'


class AddJob(CreateView):
    template_name = 'job_add.html'
    model = Job
    success_url = reverse_lazy('jobs')
    fields = '__all__'


class DeleteJob(DeleteView):
    template_name = 'job_delete.html'
    model = Job
    success_url = reverse_lazy('jobs')
    context_object_name = 'job'


# Job category
class ListCategories(ListView):
    template_name = 'categories.html'
    model = Category
    context_object_name = 'categories'


class UpdateCategory(UpdateView):
    template_name = 'category_update.html'
    model = Category
    success_url = reverse_lazy('categories')
    fields = '__all__'


class AddCategory(CreateView):
    template_name = 'category_add.html'
    model = Category
    success_url = reverse_lazy('categories')
    fields = '__all__'


class DeleteCategory(DeleteView):
    template_name = 'category_delete.html'
    model = Category
    success_url = reverse_lazy('categories')
    context_object_name = 'category'


# Job category skills
class ListSkills(ListView):
    template_name = 'skills.html'
    model = Skill
    context_object_name = 'skills'


class UpdateSkill(UpdateView):
    template_name = 'skill_update.html'
    model = Skill
    success_url = reverse_lazy('skills')
    fields = '__all__'


class AddSkill(CreateView):
    template_name = 'skill_add.html'
    model = Skill
    success_url = reverse_lazy('skills')
    fields = '__all__'


class DeleteSkill(DeleteView):
    template_name = 'skill_delete.html'
    model = Skill
    success_url = reverse_lazy('skills')
    context_object_name = 'skill'
