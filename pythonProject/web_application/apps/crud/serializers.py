from rest_framework import serializers
from apps.crud.models import Tutorial



class TutorialSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(required=True)
    published = serializers.BooleanField()

    def validate_title(self, value):
        """
        Check that the blog post is about Django.
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value
        pass
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')