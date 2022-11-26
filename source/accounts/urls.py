from django.urls import path
from accounts.views import LoginView, logout_view, RegisterView, AccountDetailView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('create/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('account/detail/<int:pk>', AccountDetailView.as_view(), name='account_detail')
]

