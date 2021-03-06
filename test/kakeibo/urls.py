from django.urls import path
from . import views
app_name = 'kakeibo'

urlpatterns = [
    # トップ画面
    path('', views.IndexView.as_view(), name='index'),
    # 詳細画面
    path('monitor/<int:pk>/', views.DetailView.as_view(), name='detail'),
    # グラフ描画
    path('monitor/<int:pk>/plot/', views.get_svg, name='plot'),
]