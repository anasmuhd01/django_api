from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from

# Create your views here.
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
