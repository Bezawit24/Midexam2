from django.shortcuts import render
from .models import students
from .models import empolyee
from .models import teachers
from .serializers  import stuSerializer
from .serializers  import empSerializer
from .serializers  import teachSerializer
from  rest_framework import generics

# Create your views here.
class teachList(generics.ListCreateAPIView):
         queryset=teachers.objects.all()
         serializer_class=teachSerializer
class teachDel(generics.RetrieveUpdateDestroyAPIView):
          queryset=teachers.objects.all()
          serializer_class=teachSerializer