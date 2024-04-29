from django.urls import path
from .views import AbhishekDetailsList,AbhishekViewList


urlpatterns = [
    path('check/', AbhishekViewList , name='Abhishek-View' ),
    path('check/<int:pk>', AbhishekDetailsList, name= 'Abhishek-Details')
]
