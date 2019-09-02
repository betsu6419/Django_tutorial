import base64
import random
from django.shortcuts import render, redirect
from django.views import generic
import numpy as np
from PIL import Image
 
def predict(x):
    labels = []
    for i in range(x.size):
        a = random.random()
        if(a<=0.5):
            labels.append("プリン")
        else:
            labels.append("おこのみやき")
    return labels

dic = {"プリン":[1,0,1],"おこのみやき":[1,1,0]}
   

class Home(generic.TemplateView):
    template_name = 'allergies/home.html'
 
 
def upload(request):
    files = request.FILES.getlist("files[]")
    if request.method == 'POST' and files:
        array_list = []
        for file in files:
            img = Image.open(file)
            array = np.asarray(img)
            array_list.append(array)
 
        #x = np.array(array_list).reshape(len(array_list), 1, 28, 28)
        x = np.array(array_list)
        print(x)
        labels = predict(x)
        result = []
        for file, label in zip(files, labels):
            file.seek(0)
            src = base64.b64encode(file.read()).decode()
            # django2.0からは src = base64.b64encode(file.read()).decode()
            result.append((src, label))
        result2 = []
        for src,label in result:
            result2.append(dic[label])
            print(dic[label])
        context = {
            'result': result,
            'result2':result2,
        }
        return render(request, 'allergies/result.html', context)
    else:
        return redirect('home')