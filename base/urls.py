from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout', views.logout_view, name='logout'),
    path('operator/dashboard', views.dashboard, name="dashboard"),



    path('operator/setting', views.setting, name="setting"),
    path('operator/form', views.artikelTambah, name="form-statis"),
    path('operator/profil', views.profil, name="profil"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)