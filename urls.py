
from django.contrib import admin
from django.urls import path
from calculator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:recipe>/', views.recipe_detail, name='recipe')
]