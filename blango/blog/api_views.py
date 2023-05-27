from http import HTTPStatus
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.api.serializers import AppointmentRequestSerializer
from blog.models import Post





@api_view(["GET", "POST"])
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return Response({"data": AppointmentRequestSerializer(posts,
        many=True).data})
    elif request.method == "POST":
        serializer = AppointmentRequestSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            return Response(
            status=HTTPStatus.CREATED,
            headers={"Location": reverse("api_post_detail",
            args=(post.pk,))},
            )
        return Response(serializer.errors,
        status=HTTPStatus.BAD_REQUEST)



@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=HTTPStatus.NOT_FOUND)
    if request.method == "GET":
        return Response(AppointmentRequestSerializer(post).data)
    elif request.method == "PUT":
        serializer = AppointmentRequestSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTPStatus.NO_CONTENT)
        return Response(serializer.errors,
        status=HTTPStatus.BAD_REQUEST)
    elif request.method == "DELETE":
        post.delete()
        return Response(status=HTTPStatus.NO_CONTENT)