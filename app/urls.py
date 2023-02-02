from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, ClientViewSet, ProductListDestroy, MarkViewSet, ClientListView

router = routers.DefaultRouter()
router.register(r'user',ClientViewSet)
router.register(r'product',ProductViewSet)
router.register(r'mark',MarkViewSet)
urlpatterns = [
    path('delete/',ProductListDestroy.as_view()),
    path('list/',ClientListView.as_view()),
    path('',include(router.urls))
]
