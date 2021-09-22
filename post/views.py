# import queue
# from rest_framework.filters import SearchFilter
# from django.shortcuts import render
# from rest_framework import viewsets
# from .serializer import *
# from .models import Post
# from rest_framework.response import Response
# from rest_framework.decorators import action


# class PostTsetViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     # filter_backends = [SearchFilter]
#     # search_fields = ['id']
#
#     # url : post/jinseong/
#     @action(detail=False)
#     def jinseong(self, request,pk):
#         serializer = self.get_serializer(self.queryset, many=True)
#         return Response(serializer.data)
#
#         # url : post/:hong/jinseong/
#     @action(detail=True)
#     def hong(self, request, pk):
#         qs = self.queryset.filter(id=pk)
#         serializer = self.get_serializer(qs, many=True)
#         return Response(serializer.data)

#     def list(self, request, *args, **kwargs):
#         print(self.action)
#         queryset = Post.objects.all()
#         serializer = PostSerializer(queryset)
#         serializer.is_valid(raise_exception=True)
#
#         return Response(serializer.data)
#
#     def create(self, request):
#         print('하위1',self.action)
#         pass
#
#     def retrieve(self, request, pk=None):
#         print('하위2', self.action)
#         pass
#
#     def update1(self, request, pk=None):
#         print('하위3', self.action)
#         pass
#
#     def partial_update(self, request, pk=None):
#         print('하위4', self.action)
#         pass
#
#     def destroy1(self, request, pk=None):
#         print('하위5', self.action)
#         pass

    # }
    #
    # @property
    # def get_serializer_class(self):
    #     print(self.action)
    #     if self.action in self.serializer_classes:  # action값에 list를 받아옮
    #         return self.serializer_classes[self.action]
    #     return self.serializer_classes['default']
    #
    # def list(self, request, *args, **kwargs):
    #     queryset = Post.objects.all()
    #     serializer = self.get_serializer_class()(queryset,many=True)
    #     serializer.is_valid(raise_exception=True)
    #
    #     return Response(serializer.data)