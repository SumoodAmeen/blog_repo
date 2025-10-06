from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BlogModel


class RegisterSerializer(serializers.ModelSerializer):
    cpassword = serializers.CharField(write_only=True)
    class Meta:

        model = User
        fields = ['username','email','password','cpassword']
        extra_kwargs = {'password':{'write_only':True}}

    def validate(self,data):
        if data['password'] != data['cpassword']:
            serializers.ValidationError("Passwords do not match")
        return data

    def create(self,validated_data):
        validated_data.pop('cpassword')
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'



