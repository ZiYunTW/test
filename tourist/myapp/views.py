from django.shortcuts import render
from datetime import datetime
#在這定義函數

def sayhello(request,username):
    now = datetime.now
    return render(request,"sayhello.html",locals())
