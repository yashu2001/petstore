from django.urls import path
from .import views
urlpatterns = [
    path('pets/<str:pet_id>',views.pets_api.as_view(),name='pets_api' ),
    path('getowner/',views.ownerlist.as_view(),name='ownerlist' ),
    path('petowner/<str:pet_id>/',views.petowner.as_view(),name='petowner' ),
     path('ownerpets/<str:o_id>/',views.ownerpets.as_view(),name='ownerpets' ),
]