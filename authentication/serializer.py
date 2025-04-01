from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework.validators import ValidationError
from phonenumber_field.serializerfields import PhoneNumberField

class UserCreationSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8, write_only=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

    def validate(self, attrs):
        errors = {}

        # Check for duplicate username, email, and phone_number
        if User.objects.filter(username=attrs['username']).exists():
            errors['username'] = 'This Username already exists! Please enter another one.'

        if User.objects.filter(email=attrs['email']).exists():
            errors['email'] = 'This Email already exists! Please use another one.'

        if User.objects.filter(phone_number=attrs['phone_number']).exists():
            errors['phone_number'] = 'Phone Number already exists! Use another one.'

        # Password validation
        password = attrs.get('password')
        if len(password) < 8:
            errors['password'] = 'Password must be at least 8 characters long.'

        if not any(char.isdigit() for char in password):
            errors['password'] = 'Password must contain at least one digit.'

        if not any(char.isalpha() for char in password):
            errors['password'] = 'Password must contain at least one letter.'

        if errors:
            
            raise ValidationError({
                'Errors': 'Please fix the issues below.',  
                **errors  
            })
            
        return attrs


    def create(self, validated_data):
        """
        Hash the password before saving the user.
        """
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)