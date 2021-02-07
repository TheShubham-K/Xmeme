from Xmeme.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('memes', memesViewset)