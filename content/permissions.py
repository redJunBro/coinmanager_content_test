from rest_framework import permissions
from .models import Content
SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAuthorOrReadonly(permissions.BasePermission):

    def has_object_permission(slef, request, views, obj):
    # 조회 요청은 항상 True
        if request.method in permissions.SAFE_METHODS:
            return True
        # PUT, DELETE 요청에 한해, 작성자에게만 허용
        return obj.author == request.user