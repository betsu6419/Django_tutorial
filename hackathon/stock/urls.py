from django.urls import path
from . import views

app_name = 'stock'

urlpatterns = [
    path('stock_list/', views.StockListView.as_view(), name='stock_list'),
    path('line/', views.show_line_grahp, name='stock_line'),
    path('line/learn', views.show_learn_grahp, name='stock_learn'),
    ]