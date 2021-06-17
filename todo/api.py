from rest_framework import viewsets, permissions
from .models import Todo
from .serializers import Todoserializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Todoserializer