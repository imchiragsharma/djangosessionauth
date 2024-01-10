from rest_framework import serializers
from account.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email","name","password","confirm_password"]

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_passowrd = attrs.get('confirm_password')
        if password != confirm_passowrd:
            return serializers.ValidationError("Passwords doesnot match")
        return attrs
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('User mail already exist')
        return value
    
    def create(self, validated_data):
        user = User.objects.create.user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
        )
        user.is_active = False
        user.save()

        return user
