from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'', include('docu.urls')),
    url(r'^api/', include('quickstart.urls')),
    #url(r'^docu/', include('docu.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'', include('hello.urls')),
]
