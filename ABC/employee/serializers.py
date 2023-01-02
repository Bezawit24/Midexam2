from .models import students
from .models import empolyee
from .models import teachers
from rest_framework import serializers
class empSerializer(serializers.ModelSerializer):
       class Meta:
            model=empolyee
            fields='__all__' 