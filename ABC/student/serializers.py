from .models import students
from .models import empolyee
from .models import teachers
from rest_framework import serializers
class stuSerializer(serializers.ModelSerializer):
       class Meta:
            model=students
            fields='__all__'
class empSerializer(serializers.ModelSerializer):
       class Meta:
            model=empolyee
            fields='__all__' 
class teachSerializer(serializers.ModelSerializer):
       class Meta:
            model=teachers
            fields='__all__'