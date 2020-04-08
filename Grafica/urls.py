"""Grafica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework_swagger.views import get_swagger_view
from Test1 import views
from rest_framework.authtoken.views import ObtainAuthToken


schema_view = get_swagger_view(title="My api")

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
    
    re_path(r'^api/v1/', include('Test1.urls')),
    # re_path(r'^api/v1/test1/$', views.Test1List.as_view()),
    # re_path(r'^api/v1/test1/(?P<pk>\d+)$', views.Test1Detail.as_view()),
    re_path(r'^api/v1/login/', include('login.urls')),
    re_path(r'^api/v1/registration/', include('rest_auth.registration.urls')),
    re_path(r'^api/v1/swagger/', schema_view),

]
