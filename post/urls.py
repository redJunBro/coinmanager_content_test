# from django.urls import include, path
# from rest_framework import routers
# from .views import *
#
# # router = routers.DefaultRouter()
# # router.register('post',PostViewSet)
#
# app_name = 'post'
#
# post_list = PostTsetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# post_detail = PostTsetViewSet.as_view({
#     'get': 'retrieve',
#     'post': 'update1',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# urlpatterns = [
#     # path('', include(router.urls)),# ( 뷰셋을 이용했던 url )
#     path('', post_list, name='post-list'),
#     path('<int:pk>/', post_detail, name='post-detail'),
# ]
