from django.urls import path
from account.views import RegistrationView,ActivateView

urlpatterns = [
    path('account/registration/',RegistrationView.as_view(),name='register'),
    path('account/activate/<str:uid>/<str:token>/', ActivateView.as_view(), name='activate'),
]
