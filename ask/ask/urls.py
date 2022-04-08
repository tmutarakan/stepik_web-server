"""ask URL Configuration

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
from django.contrib import admin
from django.conf.urls import url, include
from qa import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', views.main),
    url('login/', views.test),
    url('signup/', views.test),
    url('question/<int:pk>/', views.question, name='question'),
    url('ask/', views.test),
    url('popular/', views.popular),
    url('new/', views.test),
]
