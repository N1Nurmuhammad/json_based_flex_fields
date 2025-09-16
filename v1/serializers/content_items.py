from rest_framework import serializers

from v1.models import ContentItemModel


class ContentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentItemModel
        fields = ["data"]
