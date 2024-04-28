from django.urls import path 
from .views import RishabViewList,RishabDetailsList

urlpatterns = [
    path('info/',RishabViewList,name='Rishab-List'),
    path('info/<int:pk>',RishabDetailsList,name='Rishab-Details')
]