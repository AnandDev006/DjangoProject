"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path

from . import views

urlpatterns = [
    path( '', views.ArticleView.as_view(), name = 'home'),
    path( 'article/<int:pk>', views.ArticleDetailView.as_view(), name = 'article_page'),
    path( 'article/new', views.ArticleCreateView.as_view(), name = 'new_article'),
    path( 'article/<int:pk>/edit', views.ArticleEditView.as_view(), name = 'edit_article'),
    path( 'article/<int:pk>/delete', views.ArticleDeleteView.as_view(), name = 'delete_article'),
]
