from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TaskModel
from .serializer import TaskSerializer

class TaskView(APIView):
  def get(self, request):
    # task = TaskModel.objects.filter(name_icontains="")
    tasks = TaskModel.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response({"message": "Task GET request sucessful", "data": serializer.data})
  
  def post(self, request):
    return Response({"message": "Post method sucessful"})
  
  def put(self, request):
    return Response({"message": "Put method sucessful"})
  
  def delete(self, request):
    return Response({"message": "Delete method sucessful"})