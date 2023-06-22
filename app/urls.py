from django.urls import path
from . import views
from django.conf import settings # new
from django.conf.urls.static import static # new




urlpatterns = [
    path("",  views.home, name="home_page"),
    path("admin/dashboard/",  views.dashboard, name="admin_dashboard"),
    path("login/",  views.login, name="login_page"),
    path("trader/dashboard",  views.traderview, name="trader_dashboard"),
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
