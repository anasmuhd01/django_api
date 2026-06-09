from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from student.models import Assignment
from student.serializers import AssignmentSerializer
from rest_framework import status
 
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
    def post(self,req):
        desr = AssignmentSerializer(data=req.data)
        if desr.is_valid():
            title = desr.validated_data.get('title')
            desc = desr.validated_data.get('description')
            sub_date = desr.validated_data.get('submission_date')
            Assignment.objects.create(title = title, description = desc, submission_date= sub_date)
            return Response(data={'msg':'Data Added'})
        return Response(data={'msg':desr.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,req):
        data = Assignment.objects.all()
        ser = AssignmentSerializer(data,many=True)
        return Response(data=ser.data)
    
class AssignmentSpecificView(APIView):
    def get(self,req,**kwargs):
        id = kwargs.get('pk')
        data= Assignment.objects.get(id=id)
        ser = AssignmentSerializer(data)
        return Response(data=ser.data)
    
    def delete(self,req,**kwargs):
        id = kwargs.get('pk')
        Assignment.objects.get(id=id).delete()
        return Response(data={'msg':"deleted"})