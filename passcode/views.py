from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from passcode.models import PassRequest
from passcode.serializers import PassRequestSerializer


class PassRequestViewSet(viewsets.ModelViewSet):
    queryset = PassRequest.objects.all()
    serializer_class = PassRequestSerializer

    http_method_names = ['post', 'head']
    permission_classes = AllowAny,
