from django.shortcuts import render
from .forms import KakeiboForm
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import Category,Kakeibo
from datetime import datetime

from .test import test
  
class KakeiboListView(ListView):
    model = Kakeibo
    template_name = 'kakeibo/kakeibo_list.html'

    def queryset(self):
        return Kakeibo.objects.all()
    
    def send(self):
        n = Kakeibo.objects.create(date = datetime.now)


class KakeiboCreateView(CreateView):
    model = Kakeibo
    form_class = KakeiboForm
    success_url = reverse_lazy('kakeibo:create_done')

def create_done(request):
    n = Kakeibo.objects.last()
    n.result = test(int(n.money))
    n.save()
    return render(request,'kakeibo/create_done.html')

class KakeiboUpdateView(UpdateView):
    model = Kakeibo
    form_class = KakeiboForm
    success_url = reverse_lazy('kakeibo:update_done')

def update_done(request):
    n = Kakeibo.objects.last()
    n.result = test(int(n.money))
    n.save()
    return render(request,'kakeibo/update_done.html')

class KakeiboDeleteView(DeleteView):
    model = Kakeibo
    success_url = reverse_lazy('kakeibo:delete_done')

def delete_done(request):
    return render(request,'kakeibo/delete_done.html')

