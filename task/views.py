from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TaskModel
from .serializer import TaskSerializer
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

class TaskView(APIView):
  parser_classes = (MultiPartParser, FormParser)

  def get(self, request):
    # task = TaskModel.objects.filter(name_icontains="")
    tasks = TaskModel.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response({"message": "Task GET request sucessful", "data": serializer.data})
  
  def post(self, request):
    task_copy = request.data.copy()
    task_copy['user'] = request.user.id
    serializer = TaskSerializer(data=task_copy)    #serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message": "Post method sucessful"})
    else:
      return Response({"message": "Post request unsuccessful", "error": serializer.errors})
  
  def put(self, request, pk):
    try:
      data_in_base = TaskModel.objects.get(pk=pk)
    except TaskModel.DoesNotExist:
      return Response({"message": "Data doesn't exist."}, status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(data_in_base, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response({"message": "Put method sucessful"})
    else:
        return Response({"message": "Post request unsuccessful", "error": serializer.errors})


  def delete(self, request, pk):
    try:
      data_in_base = TaskModel.objects.get(pk=pk)
    except TaskModel.DoesNotExist:
      return Response({"message": "Data doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
    
    data_in_base.delete()
    return Response({"message": "Delete method sucessful"})