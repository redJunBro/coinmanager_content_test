from django.urls import include, path
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register('content',ContentViewSet)

# app_name = 'content'
#
# content_list = ContentViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# content_detail = ContentViewSet.as_view({
#     'get': 'retrieve',
#     'post': 'update1',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

urlpatterns = [
    # path('', include(router.urls)), # ( 뷰셋을 이용했던 url )
    path('<int:pk>/like', ContentLike.as_view(), name='post-like'),
    # path('', content_list, name='post-list'),
    # path('<int:pk>/', content_detail, name='post-detail'),
]