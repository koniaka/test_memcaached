from django.db.models.signals import m2m_changed, post_save, post_delete
from django.dispatch import receiver
from tasks.models import TodoItem, Category, Priority


def calculate_cats():
    categories = {}
    for cat in Category.objects.all():
        categories[cat.slug] = 0
    for task in TodoItem.objects.all():
        for cat in task.category.all():
            categories[cat.slug] += 1
    for slug, new_count in categories.items():
        Category.objects.filter(slug=slug).update(count=new_count)


def calculate_priors():
    priorities = {}
    for priority in Priority.objects.all():
        priorities[priority.name] = 0
    for task in TodoItem.objects.all():
        priorities[task.priority.name] += 1
    for priority, new_count in priorities.items():
        Priority.objects.filter(name=priority).update(count=new_count)


@receiver(m2m_changed, sender=TodoItem.category.through)
def task_cats(sender, instance, action, model, **kwargs):
    if action == "post_add":
        for cat in instance.category.all():
            slug = cat.slug
            new_count = 0
            for task in TodoItem.objects.all():
                new_count += task.category.filter(slug=slug).count()
            Category.objects.filter(slug=slug).update(count=new_count)
    elif action == "post_remove":
        calculate_cats()


@receiver(post_save, sender=TodoItem)
def post_save_items(sender, instance, action="post_save", model=TodoItem, **kwargs):
    calculate_cats()
    calculate_priors()


@receiver(post_delete, sender=TodoItem)
def post_delete_items(sender, instance, action="post_save", model=TodoItem, **kwargs):
    calculate_cats()
    calculate_priors()