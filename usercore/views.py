import structlog

from rest_framework import serializers, viewsets

from .models import User

logger = structlog.get_logger(__name__)


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "age"]


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        logger.info("UserViewSet list called", size=str(len(self.queryset)))
        return super(UserViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        logger.info("Creating a new user", body=request.data)
        return super(UserViewSet, self).create(request, *args, **kwargs)
