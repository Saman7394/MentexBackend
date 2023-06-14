from django.urls import include, path
from rest_framework import routers
from authentication.views import UserViewSet, ChangePasswordView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # ...
    path('api/password/change/', ChangePasswordView.as_view(), name='change_password'),
    path('api/', include(router.urls)),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # ...
]
