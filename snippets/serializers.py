from rest_framework import serializers


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField()
    linenos = serializers.BooleanField()
    language = serializers.CharField()
    style = serializers.CharField()
