from django.shortcuts import render
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='accounts'
)

cursor=mydb.cursor()

# Create your views here.
def store_data(request,cursor,mydb):
    name=request.get['name']
    sql="insert into accounts (name) values (%s)"
    val=(name)
    cursor.execute(sql,val)
    mydb.commit

    return render(request,'store_data.html')