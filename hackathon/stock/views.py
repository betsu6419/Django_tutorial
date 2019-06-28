from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.conf import settings
from .models import Stock
from sklearn.linear_model import LinearRegression
import numpy as np
import datetime
import boto3
from decimal import Decimal



def Update_from_dDB():
    session = boto3.session.Session(
    region_name = settings.REGION_NAME,
    aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
    )
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table(settings.DYNAMODB_TABLE_NAME)#insert table name 
    response = table.scan()
    time =[]
    weight= []

    #dynamoDBからのデータ取得
    if(response['Count'] < 2):
        raise Exception('quantity of records is less than 2')#2以下だと機械学習できないのでエラー
    for i in range(response['Count']):
        time.append(int(response['Items'][i]['time']))

    for i in range(response['Count']):
        weight.append(int(response['Items'][i]['weight']))

    #ローカルDBへのデータ更新
    for i in range(response['Count']):
        print(i)
        print(datetime.datetime.fromtimestamp(time[i]))
        print(weight[i])
        obj,created = Stock.objects.update_or_create(
            date = datetime.datetime.fromtimestamp(time[i]),
            money = int(weight[i]),
            defaults = {'money':weight[i]}
        )

        print(obj)
        print(created)
        print("#########")
    
    

#一覧表示用のDjango標準ビュー(ListView)を承継して一覧表示用のクラスを定義
class StockListView(ListView):
   #利用するモデルを指定
   model = Stock
   #データを渡すテンプレートファイルを指定
   template_name = 'stock/stock_list.html'
   
   #(澤邉)ここでも更新したいけど使用上更新されない？
   Update_from_dDB()

   #家計簿テーブルの全データを取得するメソッドを定義
   def queryset(self):
       return Stock.objects.all()

def show_line_grahp(request):
   
   #全データ取得
   Update_from_dDB()

   stock_data = Stock.objects.all()
   date_list=[]
   for i in stock_data:
        date_list.append((i.date.strftime('%Y/%m/%d')[:10]))
        date_list.sort()
   x_label = list(set(date_list))
   x_label.sort(reverse=False)
    #日毎の最小質量のデータセットの生成
   daily_min_data =[]
   for i in range(len(x_label)):
       ln=[]
       for j in stock_data:
            if j.date.strftime('%Y/%m/%d')[:10]==x_label[i]:   
                ln.append(j.money)
       daily_min_data.append([x_label[i], min(ln)])
   ld=len(x_label)-1
   nowweight=daily_min_data[ld][1]

    
     #折れ線グラフのボーダーカラー色の設定      
   border_color=[['54,164,235,0.8']]  
   background_color=[['54,164,235,0.5']]
   return render(request,'stock/stock_line.html',{
       'x_label': x_label,
       'border_color': border_color,
       'background_color': background_color,
       'matrix_list': daily_min_data,
       'nowweight' : nowweight
                } )
   
def show_learn_grahp(request):
   Update_from_dDB

   #全データ取得
   stock_data = Stock.objects.all()
   date_list=[]
   for i in stock_data:
        date_list.append((i.date))
   redays= list(set(date_list))
   redays.sort(reverse=False)
    #日毎の最小質量のデータセットの生成
   daily_min_data =[]
   for i in range(len(redays)):
       ln=[]
       for j in stock_data:
            if j.date==redays[i]:   
                ln.append(j.money)
       daily_min_data.append([redays[i], min(ln)])
   mass=[]
   for i,j in daily_min_data:
       mass.append(j)
   t_2 = np.array(range(len(redays)))
   mass_2 = np.array(mass)
   lr = LinearRegression()
   t_2 = t_2.reshape(-1,1)
   mass_2 = mass_2.reshape(-1,1)
   lr.fit(t_2,mass_2)
   min_t = min(t_2)
   x = np.arange(min_t,min_t+1000,1).reshape(-1,1)
   y = lr.predict(x)
   j=0
   firstday=date_list[0]
   x_label=[]
   daily_min_data =[]
   while y[j]>0:
       dayj=firstday+datetime.timedelta(days=j)
       x_label.append(dayj.strftime('%Y/%m/%d')[:10])
       daily_min_data.append([dayj.strftime('%Y/%m/%d')[:10],y[j]])
       j+=1
   deadline=firstday+datetime.timedelta(days=j)
   deadline.strftime('%Y/%m/%d')[:10]
     #折れ線グラフのボーダーカラー色の設定      
   border_color=[['54,164,235,0.8']]  
   background_color=[['54,164,235,0.5']]
   return render(request,'stock/stock_learn.html',{
       'x_label': x_label,
       'border_color': border_color,
       'background_color': background_color,
       'matrix_list': daily_min_data,
       'deadline': deadline
                } )
   
  