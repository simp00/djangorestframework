from rest_framework import status
from rest_framework.decorators import api_view,APIView
from rest_framework.response  import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
# @api_view(['GET',"POST"])
# def snippet_list(request,format=None):
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets,many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request,pk,format=None):
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method=='GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
class SnippetList(APIView):
    def get(self,request,format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class SnippetDetail(APIView):
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    def get(self, request,pk,format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    def put(self,request,pk,format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status = status.HTTP_204_NO_CONETNT)
