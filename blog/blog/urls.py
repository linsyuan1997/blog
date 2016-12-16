from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
     url(r'^admin/', admin.site.urls),
     url(r'^main/', include('main.urls', namespace='main')),
     url(r'^article/', include('article.urls', namespace='article')),
     url(r'^book/', include('book.urls', namespace='book')),     
     url(r'^.*', include('main.urls')),
     ]