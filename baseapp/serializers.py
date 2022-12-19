from . models import Task
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    var_password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'var_password')

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username']
        )
        user.set_password(validated_data['var_password'])
        user.save()
        return user


class TaskSerializers(serializers.ModelSerializer):
    picture = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Task
        fields = ['id', 'task_name', 'task_desc', 'completed', 'date_created', 'picture']
