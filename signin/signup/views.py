from django.shortcuts import render
from django.contrib.auth.models import User,auth
import mysql.connector

# Create your views here.
def index(request):
        return render(request,'index.html')
def registration(request):
        # pass
        return render(request,'registration.html')

def register(request):
        
        
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        pw=request.POST['pw']
        cpw=request.POST['cpw']

        user=User.objects.create_user(username=username,password=pw,email=email,first_name=firstname,last_name=lastname)
        user.save();

        return render(request,'user_page.html',{'user':user}) 

def login_page(request):
        return render(request,'login_page.html')

def login(request):
        username=request.POST['username']
        password=request.POST['pw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
                return render(request,'user_page.html',{'user':user})

                
def store_data(request):


        mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='accounts'
        )

        cursor=mydb.cursor()
        name=request.GET['trynowbitch']
        sql="insert into signup_name (name) values (%s)"
        list=[name]
        val=(list)
        cursor.execute(sql,val)
        mydb.commit     
        return render(request,'show_data.html',{'name':val})