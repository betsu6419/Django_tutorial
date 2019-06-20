from django.shortcuts import render
from .forms import KakeiboForm
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import Category,Kakeibo

class KakeiboListView(ListView):
    model = Kakeibo
    template_name = 'kakeibo/kakeibo_list.html'

    def queryset(self):
        return Kakeibo.objects.all()

class KakeiboCreateView(CreateView):
    model = Kakeibo
    form_class = KakeiboForm
    success_url = reverse_lazy('kakeibo:create_done')

def create_done(request):
    return render(request,'kakeibo/create_done.html')