from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from BlogAPISecond.views import AuthorsViewSet, BlogsViewSet 

router = DefaultRouter()
router.register(r'authors', AuthorsViewSet)
router.register(r'blogs', BlogsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),  
]
