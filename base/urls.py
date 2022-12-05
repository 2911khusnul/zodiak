from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout', views.logout_view, name='logout'),
    
    path('kritik-saran', views.kritikSaran, name="kritik-saran-post"),
    path('komentar', views.komentar, name="komentar"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)