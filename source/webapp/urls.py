from django.urls import path
from webapp.photo_views.photo_home import HomePhotoView
from webapp.photo_views.photo_add import PhotoCreateView, PhotoChosenAddView
from webapp.photo_views.photo_detail import PhotoDetailView
from webapp.photo_views.photo_update import PhotoUpdateView
from webapp.photo_views.photo_delete import PhotoDeleteView, PhotoChosenDeleteView


urlpatterns = [
    path('', HomePhotoView.as_view(), name='photo_home'),
    path('photo/<int:pk>', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo_add'),
    path('photo/update/<int:pk>', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/delete/<int:pk>', PhotoDeleteView.as_view(), name='photo_delete'),
    path('photo/chosen/<int:pk>', PhotoChosenAddView.as_view(), name='photo_choose'),
    path('photo/chosen/delete/<int:pk>', PhotoChosenDeleteView.as_view(), name='photo_choose_delete')
]

