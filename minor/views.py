import os
from django.shortcuts import render
from .vari import calcVegIndex
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors
import skimage
import numpy as np 
matplotlib.style.use('ggplot')
np.random.seed(1)
#from .vari import calcVegIndex
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    return render(request , 'index.html')

def upload(request):
    if request.method == 'POST' and request.FILES['img']:
        myfile = request.FILES['img']
        extension = myfile.name.split('.')[1]
        photo_path = 'static/img/' 
        if os.path.exists(photo_path + 'test.png'):
            os.remove(photo_path+'test.png')
        elif os.path.exists(photo_path + 'test.jpg'):
            os.remove(photo_path+'test.jpg')
        elif os.path.exists(photo_path + 'test.jpeg'):
            os.remove(photo_path+'test.jpeg')
        fs = FileSystemStorage()
        fs.save(photo_path+'test.'+ extension, myfile)
    #main code
    algorithm=request.POST['algorithm']
    if algorithm=='vari':
        dense,sparse,barren=calcVegIndex(photo_path+'test.'+extension,extension,photo_path)
    else:
        dense,sparse,barren=calcVegIndex(photo_path+'test.'+extension,extension,photo_path,1)
      
    inputimg='img/test.'+extension
    outputimg='img/result.'+extension
    plotimg='img/plot.png'
    return render(request , 'output.html',{'outputimg':outputimg,'inputimg':inputimg,'dense':dense,'sparse':sparse,'barren':barren,'plotimg':plotimg})