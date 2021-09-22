from rest_framework import serializers
from .models import Content

class ContentdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = (
            'id',
            'category',
            'author',
            'level',
            'viewcount',
            'content',
            'title',
            'created',
            'updated',
        )


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = (
                    'id',
                    'category',
                    'author',
                    'title',
                    'created',
                )
