
from .models import students
from .models import empolyee
from .models import teachers
from rest_framework import serializers
class teachSerializer(serializers.ModelSerializer):
       class Meta:
            model=teachers
            fields='__all__'