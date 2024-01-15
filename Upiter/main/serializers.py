from rest_framework import serializers
from .models import Users
import json
from django.core.serializers.json import DjangoJSONEncoder

def serialize_user_data(user_instance):

    serialized_data = json.dumps(user_instance, cls=DjangoJSONEncoder)
    return serialized_data

class UserImage(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'surname', 'phone', 'email', 'password', 'photo'] 