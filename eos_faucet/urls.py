from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from passcode.views import PassRequestViewSet
from faucet.views import AccountView

router = DefaultRouter()
router.register('pass-code', PassRequestViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', AccountView.as_view()),
    path('api/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
