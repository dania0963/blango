from rest_framework import serializers
from blog.models import Post

class AppointmentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        readonly = ["modified_at", "created_at"]