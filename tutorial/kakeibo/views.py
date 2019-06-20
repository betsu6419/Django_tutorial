from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import Category,Kakeibo

class KakeiboListView(ListView):
    model = Kakeibo
    template_name = 'kakeibo/kakeibo_list.html'

    def queryset(self):
        return Kakeibo.objects.all()