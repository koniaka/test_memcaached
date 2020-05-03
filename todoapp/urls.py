from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('', include('tasks.urls', namespace="tasks")),
    path('admin/', admin.site.urls),
    re_path(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
]

# if not settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path("__debug__/", include(debug_toolbar.urls))
#     ] + urlpatterns
