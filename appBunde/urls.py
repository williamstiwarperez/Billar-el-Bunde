from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from appBunde import views

router = routers.DefaultRouter()
router.register(r'appBunde',views.appBundeView,'appBunde')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path("docs/", include_docs_urls(title='appBunde API'))
]


