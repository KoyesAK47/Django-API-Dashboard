from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets
from .models import CustomUser
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer, GroupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def serialize_user(user):
    serializer = UserSerializer(user)
    return Response(serializer.data)

def index(request):
    return render(request, 'user/index.html')

def profile(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        context = {
            'user': user
        }
        return render(request, 'user/profile.html', context)
    except CustomUser.DoesNotExist:
        return HttpResponse("User not found", status=404)

def delete_user(request, user_id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponse("Access denied. Admin privileges required.", status=403)
    
    try:
        user_to_delete = CustomUser.objects.get(id=user_id)
        
        # Prevent deletion of current user or superuser
        if user_to_delete == request.user:
            return HttpResponse("Cannot delete your own account", status=400)
        
        if user_to_delete.is_superuser and not request.user.is_superuser:
            return HttpResponse("Cannot delete superuser account", status=403)
        
        if request.method == 'POST':
            username = user_to_delete.username
            user_to_delete.delete()
            # Redirect to user list with success message
            from django.shortcuts import redirect
            from django.contrib import messages
            messages.success(request, f'User "{username}" has been successfully deleted.')
            return redirect('/user/')
        
        # Show confirmation page
        context = {
            'user_to_delete': user_to_delete
        }
        return render(request, 'user/delete_confirm.html', context)
        
    except CustomUser.DoesNotExist:
        return HttpResponse("User not found", status=404)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Temporarily allow any for testing

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]  # Temporarily allow any for testing
