from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'representatives', RepresentativeViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'events', EventViewSet)
router.register(r'matchdetails', MatchDetailViewSet)
router.register(r'carom', CarromViewSet)