from rest_framework.serializers import ModelSerializer
from .models import Sinhvien, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validate_data):
        user = User(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        
        return user
        

class SinhvienSerializer(ModelSerializer):
    class Meta:
        model = Sinhvien
        fields = '__all__'
        
    