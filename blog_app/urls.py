from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import BlogView,RegisterView,CreateBlogView, DetailView, DeleteView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authenticate/', RegisterView.as_view()),
    path('home/', BlogView.as_view()),
    path('create_blog/', CreateBlogView.as_view()),
    path('details/<int:pk>/', DetailView.as_view()),
    path('manage/<int:pk>/', DeleteView.as_view()),
]