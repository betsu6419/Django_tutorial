from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Location
import io
import matplotlib.pyplot as plt
import numpy as np
class IndexView(LoginRequiredMixin, generic.ListView): # generic.ListViewを継承
    model = Location
    paginate_by = 5 
    ordering = ['-updated_at']
    template_name = 'monitor/index.html'
class DetailView(generic.DetailView):
    model = Location
    template_name = 'monitor/detail.html'
# グラフ作成
def setPlt(pk):
    
    # 折れ線グラフを出力
    # TODO: 本当はpkを基にしてモデルからデータを取得する。
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([20, 90, 50, 30, 100, 80, 10, 60, 40, 70])
    plt.plot(x, y)
# svgへの変換
def pltToSvg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s
def get_svg(request,  pk):
    setPlt(pk)       # create the plot
    svg = pltToSvg() # convert plot to SVG
    plt.cla()        # clean up plt so it can be re-used
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response
