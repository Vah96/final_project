from rest_framework.serializers import ModelSerializer

from aphorisms.models import Aphorism


class AphorismSerializer(ModelSerializer):
    class Meta:
        model = Aphorism
        fields = ['id', 'text', 'author', 'tags']
        read_only_fields = ['author', ]
