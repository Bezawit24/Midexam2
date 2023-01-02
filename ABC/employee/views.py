from django.shortcuts import render
from .models import students
from .models import empolyee
from .models import teachers
from .serializers  import stuSerializer
from .serializers  import empSerializer
from .serializers  import teachSerializer
from  rest_framework import generics
class empList(generics.ListCreateAPIView):
         queryset=empolyee.objects.all()
         serializer_class=empSerializer
class empDel(generics.RetrieveUpdateDestroyAPIView):
          queryset=empolyee.objects.all()
          serializer_class=empSerializer