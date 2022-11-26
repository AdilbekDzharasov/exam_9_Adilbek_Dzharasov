from django.urls import path
from api.views import get_token_view

urlpatterns = [
    path('token/', get_token_view, name='token')
]

