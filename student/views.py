from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from student.models import *
from student.serializers import *
from rest_framework import status
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.viewsets import ViewSet
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
    
    def put(self,req,**kwargs):
        id = kwargs.get('pk')
        assignment = Assignment.objects.get(id=id)
        desr = AssignmentSerializer(data=req.data)
        if desr.is_valid():
            title = desr.validated_data.get('title')
            desc = desr.validated_data.get('description')
            sub_date = desr.validated_data.get('submission_date')
            assignment.title = title
            assignment.description = desc
            assignment.submission_date = sub_date
            assignment.save()
            return Response(data={'msg':'updated'})
        return Response(data=desr.errors)
    
# class TodoView(APIView):
#     def post(self,req):
#         desr = TodoSerializer(data=req.data)
#         # print(desr)
#         # to check data without validation
#         # print(desr.initial_data.get("title"))
#         if desr.is_valid():  
#             title = desr.validated_data.get('title')
#             desc = desr.validated_data.get('description')
#             sub = desr.validated_data.get('subject')
#             Todo.objects.create(title= title,description = desc, subject = sub)
#             return Response(data={'msg':'data created'})
#         return Response(data=desr.errors)
    
#     def get(self,req):
#         data=Todo.objects.all()
#         ser=TodoSerializer(data,many=True)
#         print(ser.data)
#         return Response(ser.data)
    
# class TodoEditView(APIView):
    def delete(self,req,**kwargs):
        id = kwargs.get('id')
        Todo.objects.get(id=id).delete()
        return Response(data={'msg':'deleted'})
    
    
    def put(self,req,**kwargs):
        id = kwargs.get('id')
        desr = TodoSerializer(data =req.data)
        todo = Todo.objects.get(id=id)
        if desr.is_valid():
            todo.title = desr.validated_data.get('title')
            todo.description = desr.validated_data.get('description')
            todo.subject = desr.validated_data.get('subject')
            todo.save()
            return Response(data={'msg':'updated'})
    
    
class TodoMSView(APIView):
    def get(self,req):
        qsr = Todo.objects.all()
        ser = TodoModelSerializer(qsr,many=True)
        return Response(data=ser.data)
    
    def post(self,req):
        desr = TodoModelSerializer(data=req.data)
        if desr.is_valid():
            desr.save()
            return Response(data=desr.data)
        return Response(data=desr.errors)

class TodoMSEditView(APIView):
    def get(self,req,**kwargs):
        todos = Todo.objects.get(id=kwargs.get('id'))
        ser = TodoModelSerializer(todos)
        # if todos.pk in
        return Response(data=ser.data)
        # return Response(data={'msg':'id not found'})

    def delete(self,req,**kwargs):
        id= kwargs.get('id')
        Todo.objects.get(id=id).delete()
        return Response(data={'msg':'deleted'})

    def put(self,req,**kwargs):
        todo = Todo.objects.get(id=kwargs.get('id'))
        desr = TodoModelSerializer(todo,data=req.data)
        if desr.is_valid():
            desr.save()
            return Response(data=desr.data)
        return Response(data=desr.errors)
    
class TeacherView(APIView):

    parser_classes=[FormParser,MultiPartParser]

    def get(self,req):
        teachers=Teacher.objects.all()
        ser=TeachreSerializer(teachers,many=True)
        return Response(data=ser.data)
    
    def post(self,req):
        desr = TeachreSerializer(data=req.data)
        if desr.is_valid():
            desr.save()
            return Response(data=desr.data)
        return Response(data=desr.errors)
    
class TeacherViewset(ViewSet):
    
    def list(self, request):

        teacher = Teacher.objects.all()
        print(request.query_params)
        if 'department' in request.query_params:
            teacher = teacher.filter(department= request.query_params.get('department'))
        ser = TeachreSerializer(teacher,many=True)
        return Response(data=ser.data)

    def create(self, request):

        desr = TeachreSerializer(data=request.data)
        if desr.is_valid():
            desr.save()
            return Response(data=desr.data)
        return Response(data=desr.errors)

    def retrieve(self, request, pk=None):

        teacher = Teacher.objects.get(id=pk)
        ser = TeachreSerializer(teacher)
        return Response(data=ser.data)

    def update(self, request, pk=None):
        teacher = Teacher.objects.get(id=pk)
        desr = TeachreSerializer(teacher,data=request.data)
        if desr.is_valid():
            desr.save()
            return Response(data=desr.data)
        return Response(data=desr.errors)
        
        
    def destroy(self, request, pk=None):
        teacher = Teacher.objects.get(id=pk).delete()
        return Response(data={'msg':'deleted'})
    