from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout', views.logout_view, name='logout'),
    
    path('kritik-saran-post/', views.kritikSaran, name="kritik-saran-post"),
    path('komentar/', views.komentar, name="komentar"),
    path('register/', views.register, name="register"),
    path('zodiak/', views.zodiak, name="zodiak"),
    path('detail-zodiak/<str:nama_zodiak>', views.detailZodiak, name="detail-zodiak"),
    path('tentang/', views.tentang, name="tentang"),
    path('ramalan/', views.ramalan, name="ramalan"),
    path('kritik-saran/', views.kritikSaranPage, name="kritik-saran"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)