from django.shortcuts import render
from .models import students
from .models import empolyee
from .models import teachers
from .serializers  import stuSerializer
from .serializers  import empSerializer
from .serializers  import teachSerializer
from  rest_framework import generics
class stuList(generics.ListCreateAPIView):
         queryset=students.objects.all()
         serializer_class=stuSerializer
class stuDel(generics.RetrieveUpdateDestroyAPIView):
          queryset=students.objects.all()
          serializer_class=stuSerializer
class empList(generics.ListCreateAPIView):
         queryset=empolyee.objects.all()
         serializer_class=empSerializer
class empDel(generics.RetrieveUpdateDestroyAPIView):
          queryset=empolyee.objects.all()
          serializer_class=empSerializer
class teachList(generics.ListCreateAPIView):
         queryset=teachers.objects.all()
         serializer_class=teachSerializer
class teachDel(generics.RetrieveUpdateDestroyAPIView):
          queryset=teachers.objects.all()
          serializer_class=teachSerializer
# Create your views here.
