"""jobFinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from viewer.views import ListJobs, DetailJob, UpdateJob, AddJob, DeleteJob, ListCategories, UpdateCategory, AddCategory, DeleteCategory, ListSkills, UpdateSkill, AddSkill, DeleteSkill

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs', ListJobs.as_view(), name='jobs'),
    path('jobs/<int:pk>', DetailJob.as_view(), name='job_details'),
    path('jobs/<int:pk>/update', UpdateJob.as_view(), name='job_update'),
    path('jobs/create', AddJob.as_view(), name='job_add'),
    path('jobs/<int:pk>/delete', DeleteJob.as_view(), name='job_delete'),
    path('categories', ListCategories.as_view(), name='categories'),
    path('categories/<int:pk>/update', UpdateCategory.as_view(), name='category_update'),
    path('categories/create', AddCategory.as_view(), name='category_add'),
    path('categories/<int:pk>/delete', DeleteCategory.as_view(), name='category_delete'),
    path('skills', ListSkills.as_view(), name='skills'),
    path('skills/<int:pk>/update', UpdateSkill.as_view(), name='skill_update'),
    path('skills/create', AddSkill.as_view(), name='skill_add'),
    path('skills/<int:pk>/delete', DeleteSkill.as_view(), name='skill_delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
