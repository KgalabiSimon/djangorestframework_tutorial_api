from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from snippets import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


# Create a router and register our viewsets with it.

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)