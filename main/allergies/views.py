import base64
import random
import csv
import os
import cv2
from .models import Allergies
from .forms import AllergiesForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
import numpy as np
from PIL import Image
from .food_predict import predict, utils
from main.settings import BASE_DIR

#辞書の読み込み
from django.core.files.storage import default_storage
storage = default_storage
storage.location = 'allergies/'
dic = {}
f = storage.open("allergy.csv",'r')
reader = csv.reader(f)
header = next(reader)
for row in reader:
    tmp = row[1:]
    dic[row[0]] = [int(s) for s in tmp]

class AllergiesCreateView(generic.CreateView):
    model = Allergies
    form_class = AllergiesForm
    success_url = reverse_lazy('allergies:home')

"""def my_predict(x):
    labels = []
    for i in range(x.size):
        a = random.random()
        if(a<=0.5):
            labels.append("sushi")
        else:
            labels.append("cup_cakes")
    return labels
"""
   

"""class Home(generic.TemplateView):
    model = Allergies
    template_name = 'allergies/home.html'

class home(generic.ListView):
    model = Allergies
    template_name = 'allergies/home.html'
    def queryset(self):
       return Allergies.objects.all()
"""
def home(request):
    object_list = []
    object_all= Allergies.objects.all()
    for object_tmp in object_all: 
        ob = []
        ob.append(object_tmp.name)
        if(object_tmp.bool_0 == True):
            ob.append("ある")
        elif(object_tmp.bool_0 == False):
            ob.append("ない")
        elif(object_tmp.bool_0 == None):
            ob.append("わからない")    
        
        if(object_tmp.bool_1 == True):
            ob.append("ある")
        elif(object_tmp.bool_1 == False):
            ob.append("ない")
        elif(object_tmp.bool_1 == None):
            ob.append("わからない")    
        
        if(object_tmp.bool_2 == True):
            ob.append("ある")
        elif(object_tmp.bool_2 == False):
            ob.append("ない")
        elif(object_tmp.bool_2 == None):
            ob.append("わからない")    
        if(object_tmp.bool_3 == True):
            ob.append("ある")
        elif(object_tmp.bool_3 == False):
            ob.append("ない")
        elif(object_tmp.bool_3 == None):
            ob.append("わからない")    
        
        if(object_tmp.bool_4 == True):
            ob.append("ある")
        elif(object_tmp.bool_4 == False):
            ob.append("ない")
        elif(object_tmp.bool_4 == None):
            ob.append("わからない")    
        
        if(object_tmp.bool_5 == True):
            ob.append("ある")
        elif(object_tmp.bool_5 == False):
            ob.append("ない")
        elif(object_tmp.bool_5 == None):
            ob.append("わからない")    
        if(object_tmp.bool_6 == True):
            ob.append("ある")
        elif(object_tmp.bool_6 == False):
            ob.append("ない")
        elif(object_tmp.bool_6 == None):
            ob.append("わからない")    
        
        if(object_tmp.bool_7 == True):
            ob.append("ある")
        elif(object_tmp.bool_7 == False):
            ob.append("ない")
        elif(object_tmp.bool_7 == None):
            ob.append("わからない")    
        
        if(object_tmp.bool_8 == True):
            ob.append("ある")
        elif(object_tmp.bool_8 == False):
            ob.append("ない")
        elif(object_tmp.bool_8 == None):
            ob.append("わからない")    
        if(object_tmp.bool_9 == True):
            ob.append("ある")
        elif(object_tmp.bool_9 == False):
            ob.append("ない")
        elif(object_tmp.bool_9 == None):
            ob.append("わからない")    
        
        if(object_tmp.bool_10 == True):
            ob.append("ある")
        elif(object_tmp.bool_10 == False):
            ob.append("ない")
        elif(object_tmp.bool_10 == None):
            ob.append("わからない")    
        
        if(object_tmp.bool_11 == True):
            ob.append("ある")
        elif(object_tmp.bool_11 == False):
            ob.append("ない")
        elif(object_tmp.bool_11 == None):
            ob.append("わからない")    
        
        object_list.append(ob)
    context ={
        'object_list':object_list
    }
    return render(request,"allergies/home.html",context)

def customer_solve(result2,ob):
    list_ob = []
    if ob.bool_0 ==True or ob.bool_0 ==None:
        list_ob.append(1)
    else:
        list_ob.append(0)

    if ob.bool_1 ==True or ob.bool_1 ==None:
        list_ob.append(1)
    else:
        list_ob.append(0)
    if ob.bool_2 ==True or ob.bool_2 ==None:
        list_ob.append(1)
    else:
        list_ob.append(0)
   
    if ob.bool_3 ==True or ob.bool_3 ==None:
        list_ob.append(1)
    else:
        list_ob.append(0)
    if ob.bool_4 ==True or ob.bool_4 ==None:
        list_ob.append(1)
    else:
        list_ob.append(0)
    if ob.bool_5 ==True or ob.bool_5 ==None:
        list_ob.append(1)
    else:
        list_ob.append(0)
    if ob.bool_6 ==True or ob.bool_6 ==None:
        list_ob.append(1)
    else:
        list_ob.append(0)
    if ob.bool_7 ==True or ob.bool_7 ==None:
        list_ob.append(1)
    else:
        list_ob.append(0)
    if ob.bool_8 ==True or ob.bool_8 ==None:
        list_ob.append(1)
    else:
        list_ob.append(0)
    if ob.bool_9 ==True or ob.bool_9 ==None:
        list_ob.append(1)
    else:
        list_ob.append(0)
    if ob.bool_10 ==True or ob.bool_10 ==None:
        list_ob.append(1)
    else:
        list_ob.append(0)
    
    if ob.bool_10 ==True or ob.bool_11 ==None:
        list_ob.append(1)
    else:
        list_ob.append(0)

    result3 = []
    conclusion = 0
    for i in range(12):
        if result2[i] and list_ob[i] == 1:
            result3.append(1)
            conclusion = 1
        else:
            result3.append(0)
    return result3,conclusion
def upload(request):
    files = request.FILES.getlist("files[]")
    if request.method == 'POST' and files:
       
        array_list = []
        file_name = ""
        for file in files:
            img = Image.open(file)
            array = np.asarray(img)
            array_list.append(array)
            img.save(os.path.join(BASE_DIR,"allergies/images/image.jpg"))
 
        #x = np.array(array_list).reshape(len(array_list), 1, 28, 28)
        x = np.array(array_list)
        
        #img = cv2.imdecode(np.fromstring(request.FILES['files[]'], np.uint8), cv2.IMREAD_UNCHANGED)
        #img_array = process_image(img)
        
        path = os.path.join(BASE_DIR,'allergies/images/image.jpg')
        
        labels = []
        confidence = 0.99
        food,confidence = predict.predict(path)
        labels.append(food)
        #labels.append("sushi")
        #confidence = float(confidence*float(100))

        result = []
        for file, label in zip(files, labels):
            file.seek(0)
            src = base64.b64encode(file.read()).decode()
            # django2.0からは src = base64.b64encode(file.read()).decode()
            result.append((src, label))
        result2 = []
        for src,label in result:
            result2.append(dic[label])
            #print(dic[label])

        customer_name = request.POST["name"]
        result3 = []
        conclusion = 0     
        if Allergies.objects.filter(name=customer_name).exists():
            ob = Allergies.objects.filter(name = customer_name)[0]
            result3,conclusion = customer_solve(result2[0],ob)
        else:
            conclusion = 3
        
        print(labels)
        print(result2)
        print(result3)
        print(confidence)
        print(customer_name)
        print(conclusion)
        context = {
            'result': result,
            'result2':result2,
            'result3':result3,
            'confidence':confidence,
            'customer_name':customer_name,
            'conclusion':conclusion,
        }
        return render(request, 'allergies/result.html', context)
    else:
        return redirect('/allergies/')