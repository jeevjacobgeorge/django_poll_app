
from django.contrib import admin
from django.urls import include, path
from polls import views
from api import views as api_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include("polls.urls")),
    path("", views.IndexView.as_view(), name="index"),
    path('studinfo/<int:pk>',api_views.student_detail),
    path('studinfo/',api_views.student_list),
    path('stucreate/', api_views.student_create),
    path('studapi/', api_views.student_api),
   
]