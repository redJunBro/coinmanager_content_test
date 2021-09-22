import queue
from rest_framework.filters import SearchFilter
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from .serializer import *
from .models import Content
from rest_framework.response import Response
from rest_framework.decorators import action
from .permissions import *





class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all().order_by('created')
    serializer_class = ContentSerializer
    #authentication_classes = [IsAuthenticated]
    permission_classes = [
        IsAuthorOrReadonly
    ]

    # filter_backends = [SearchFilter]
    # search_fields = ['id']

    # url : post/jinseong/
    @action(detail=False)
    def jinseong(self, request,pk):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

        # url : post/:hong/jinseong/
    @action(detail=True)
    def hong(self, request, pk):
        qs = self.queryset.filter(id=pk)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    # def list(self, request, *args, **kwargs):
    #     print('하위2',self.action)
    #     queryset = Content.objects.all()
    #     serializer = ContentListSerializer(queryset, many=True)
    #     # serializer.is_valid(raise_exception=True)
    #     print(serializer.data)
    #     return Response(serializer.data)
    #
    # def create(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     serializer.save()
    #
    def retrieve(self, request, pk=None):
        queryset = Content.objects.all()
        content = get_object_or_404(queryset, pk=pk)
        serializer = ContentdetailSerializer(content)
        return Response(serializer.data)
    #
    # def update1(self, request, pk=None):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #
    # def partial_update(self, request, pk=None):
    #     print('하위4', self.action)
    #     pass
    #
    # def destroy1(self, request, pk=None):
    #     print('하위5', self.action)
    #     pass