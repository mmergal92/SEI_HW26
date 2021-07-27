from django.urls import path
from . import views
from .views import ClassList

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('class/', ClassList.as_view(), name="scienceclass_list"),
    # path('class/', views.ClassList.as_view(), name="scienceclass_list"),
    path('class/<int:scienceclass_id>/', views.ClassList.as_view(), name="scienceclass_details"),
    # path('class/<int:class_id>/', views.class_detail, name="detail"),
    path('class/create/', views.ClassCreate.as_view(), name="scienceclass_form"),
    path('class/<int:pk>/update/', views.ClassUpdate.as_view(), name="scienceclass_update"),
    path('class/<int:pk>/delete/', views.ClassDelete.as_view(), name="scienceclass_delete"),
]