from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),

    re_path(r'^problems/$', views.problem_list, name='problem_list'),
    re_path(r'^problems/upload/$', views.upload_problem, name='upload_problem'),
    path('problems/submit/<int:pk>/', views.submit_problem, name='submit_problem'),
    path('problems/delete/<int:pk>/', views.delete_problem, name='delete_problem'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


