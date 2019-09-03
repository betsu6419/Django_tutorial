from django.urls import path
from . import views
app_name = 'allergies'

urlpatterns = [
    # トップ画面
    path('', views.home, name='home'),
    path('upload', views.upload, name='upload'),
    path('create',views.AllergiesCreateView.as_view(),name = 'create')
]