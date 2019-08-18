from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.conf import settings
from .models import Stock ,Category
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
   category_list = []
    category_data = Category.objects.all().order_by('-category_name')
    for item in category_data:
        category_list.append(item.category_name)

   date_list=[]
   for i in stock_data:
        date_list.append((i.date.strftime('%Y/%m/%d')[:10]))
        date_list.sort()
   x_label = list(set(date_list))
   x_label.sort(reverse=False)

   #月毎＆カテゴリ毎の合計金額データを生成する。
    #カテゴリが登録されていない月の合計金額は０にセットする。
    #まず、全日付ｘ全カテゴリｘ合計金額「0]のリストを生成する。
    matrix_list =[]
    for item_label in x_label:
        for item_category in category_list:
            matrix_list.append([item_label, item_category, 0])

    #日毎の最小質量のデータセットの生成
    nowweight = []
    daily_min_data =[]
    for i,category in enumerate(category_list):
        for i in range(len(x_label)):
            ln=[]
            for j in stock_data:
                if j.category == category:
                    if j.date.strftime('%Y/%m/%d')[:10]==x_label[i]:   
                        ln.append(j.money)
            daily_min_data.append([x_label[i],category, ln[-1]])
        ld=len(x_label)-1
        nowweight.append(daily_min_data[ld][2])

    for x,category,weight in daily_min_data:
        for i data in enumerate(matrix_list):
            if data[0] == x and data[1] == category:
                matrix_list[i][2] = weight
    
     #折れ線グラフのボーダーカラー色の設定        #折れ線グラフのボーダーカラー色の設定      
    border_color_list=['254,97,132,0.8','54,164,235,0.8','0,255,65,0.8','255,241,15,0.8',\
                       '255,94,25,0.8','84,77,203,0.8','204,153,50,0.8','214,216,165,0.8',\
                       '33,30,45,0.8','52,38,89,0.8']
    border_color =[]
    for x,y in zip(category_list, border_color_list):
        border_color.append([x,y])
        
    background_color_list=['254,97,132,0.5','54,164,235,0.5','0,255,65,0.5','255,241,15,0.5',\
                           '255,94,25,0.5','84,77,203,0.5','204,153,50,0.5','214,216,165,0.5'\
                           '33,30,45,0.5','52,38,89,0.5']

    background_color =[]
    for x,y in zip(category_list, background_color_list):
        background_color.append([x,y])
    
   return render(request,'stock/stock_line.html',{
       'x_label': x_label,
       'category_list':category_list,
       'border_color': border_color,
       'background_color': background_color,
       'matrix_list': matrix_list,
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
       daily_min_data.append([redays[i], ln[-1]])
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

   
  
