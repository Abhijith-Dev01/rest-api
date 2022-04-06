from django.urls import path,include
from . views import articleList,articleDetail,ArticleAPIView,ArticleDetails,GenericAPIView,ArticleViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article',ArticleViewset,base_name='article')

urlpatterns =[
	path('viewset/',include(router.urls)),
	path('viewset/<int:pk>/',include(router.urls)),
	# path('article/',articleList),
	path('article/',ArticleAPIView.as_view()),
	path('generic/article/',GenericAPIView.as_view()),
	path('generic/article/<int:id>/',GenericAPIView.as_view()),
	# path('detail/<int:pk>/',articleDetail),
	path('detail/<int:id>/',ArticleDetails.as_view()),
]
