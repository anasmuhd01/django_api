from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
 
# Create your views here.

students = [
    {'id':1,'name':'Amal','age':20,'batch':'BCA'},
    {'id':2,'name':'Vimal','age':22,'batch':'BSC CS'},
    {'id':3,'name':'Arun','age':21,'batch':'BCA'},
    {'id':4,'name':'Athul','age':19,'batch':'BSC CS'},
]

@api_view(['GET'])
def FirstRequest(req):
    return Response(data={'msg':'first request hit'})

@api_view(['post'])
def PostExample(req):
    print(req.data)
    print(req.data.get('username'))
    return Response(data={'msg':'post hit'})


@api_view(['put'])
def PutExample(req):
    print(req.data)
    return Response(data={'msg':'put req hit'})

class StudentApiView(APIView):
    def get(self,req):
        return Response(data=students)
    def post(self,req):
        students.append(req.data)
        return Response(data=students)
    
class StudentEditView(APIView):

    def get(self,req,**kwargs):
         
        id = kwargs.get('id')
        student = list(filter(lambda item:item['id']==id)).pop()
        print(student)
        return Response(data=student)

    def put(self,req,**kwargs):

        global students
        id = kwargs.get('id')
        students = list(filter (lambda item:item['id']!= id ,students))
        students.append(req.data)
        return Response(data=students)
    
    def delete(self,req,**kwargs):

        global students
        id = kwargs.get('id')
        students = list(filter(lambda item:item['id'] != id,students))
        return Response(data=students)


class AssignmentView(APIView):
    def get(self,req):
        return Response(data={'data':'PUT msg'})