from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from tasks.models import TodoItem, Category, Priority
from datetime import datetime
from django.core.cache import cache


def index(request):
    categories = Category.objects.all()
    priorities = Priority.objects.all()
    return render(request, "tasks/index.html", {"categories": categories, "priorities": priorities})

def tasks_by_cat(request, cat_slug=None):
    user = request.user
    tasks = TodoItem.objects.filter(owner=user).all()
    cat = None
    if cat_slug:
        cat = get_object_or_404(Category, slug=cat_slug)
        tasks = tasks.filter(category__in=[cat])
    categories = Category.objects.all()
    return render(
        request,
        "tasks/list_by_cat.html",
        {"category": cat, "tasks": tasks, "categories": categories},
    )


class TaskListView(ListView):
    model = TodoItem
    context_object_name = "tasks"
    template_name = "tasks/list.html"


class TaskDetailsView(DetailView):
    model = TodoItem
    template_name = "tasks/details.html"

def get_cashed_time(request):
    timenow = datetime.now().strftime("%d-%m-%Y / %H:%M:%S")
    if not cache.get('cached_time'):
        cache.set('cached_time', timenow, 300)
    return render(request, "tasks/datetime_cache.html", {'current_time': timenow,
                                                'cached_time': cache.get('cached_time'), })