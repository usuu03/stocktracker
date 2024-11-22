from rest_framework import serializers
from .models import User
from tenants.models import Tenant


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    organization_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['organization_name', 'email', 'username', 'password', 'password2']

    def validate(self, attrs):
        # Check if passwords match
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        
        # Look up the organization by name
        try:
            attrs['organization'] = Tenant.objects.get(name=attrs['organization_name'])
        except Tenant.DoesNotExist:
            raise serializers.ValidationError({"organization_name": "Invalid organization name."})
        
        return attrs

    def create(self, validated_data):
        validated_data.pop('organization_name')  # Remove organization_name as it's not part of User model
        user = User.objects.create_user(
            organization=validated_data['organization'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
