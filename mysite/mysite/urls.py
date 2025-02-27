"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from my_project import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.index),
    # path('index/', views.index_same),
    path('', views.index_same),
    path('index_similar/', views.index_similar),
    path('index_product/', views.index_product),
    path('index_same/', views.index_same),
    path('index_similar_url/', views.index_similar_url),
    path('index_product_url/', views.index_product_url),
    path('index_same_url/', views.index_same_url),
    path('same_put_in/',views.same_put_in),
    path('same_check/',views.same_check),
    path('same_update/',views.same_update),
    path('same_delete/',views.same_delete),
    path('similar_put_in/',views.similar_put_in),
    path('similar_check/',views.similar_check),
    path('similar_update/',views.similar_update),
    path('similar_delete/',views.similar_delete),
    path('product_put_in/',views.product_put_in),
    path('product_check/',views.product_check),
    path('product_update/',views.product_update),
    path('product_delete/',views.product_delete),
    path('same_put_in_url/', views.same_put_in_url),
    path('same_check_url/', views.same_check_url),
    path('same_update_url/', views.same_update_url),
    path('same_delete_url/', views.same_delete_url),
    path('similar_put_in_url/', views.similar_put_in_url),
    path('similar_check_url/', views.similar_check_url),
    path('similar_update_url/', views.similar_update_url),
    path('similar_delete_url/', views.similar_delete_url),
    path('product_put_in_url/', views.product_put_in_url),
    path('product_check_url/', views.product_check_url),
    path('product_update_url/', views.product_update_url),
    path('product_delete_url/', views.product_delete_url)
]
