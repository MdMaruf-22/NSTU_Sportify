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
router.register(r'carrom', CarromViewSet)
router.register(r'handball', HandBallViewSet)
router.register(r'chess', ChessViewSet)
router.register(r'football', FootballViewSet)
router.register(r'cricket', CricketViewSet)
router.register(r'livescores', LiveScoreViewSet)
router.register(r'results', ResultViewSet)
router.register(r'standings', StandingViewSet)
router.register(r'notices',NoticeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]