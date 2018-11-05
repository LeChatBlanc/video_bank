"""video_bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



from video_store.views import MovieListView, MovieDetailView, MovieUpdateView
from video_store.views import MovieCreateView, MovieDeleteView


urlpatterns = [
    url(r'^admin/', admin.site.urls),


    url(r'^login/$', auth_views.LoginView.as_view()),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/')),

    
    url(r'^$', MovieListView.as_view(), name='list-movie'),
    url(r'^movie/create/$', MovieCreateView.as_view(), name='create-movie'),
    url(r'^movie/(?P<slug>[-\w]+)/$', MovieDetailView.as_view(), name='detail-movie'),
    url(r'^movie/(?P<slug>[-\w]+)/update/$', MovieUpdateView.as_view(), name='update-movie'),
    url(r'^movie/(?P<slug>[-\w]+)/delete/$', MovieDeleteView.as_view(), name='delete-movie'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
