from django.urls import path
from webapp.photo_views.photo_home import HomePhotoView
from webapp.photo_views.photo_add import PhotoCreateView
from webapp.photo_views.photo_detail import PhotoDetailView
from webapp.photo_views.photo_update import PhotoUpdateView
from webapp.photo_views.photo_delete import PhotoDeleteView


urlpatterns = [
    path('', HomePhotoView.as_view(), name='photo_home'),
    path('photo/<int:pk>', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo_add'),
    path('photo/update/<int:pk>', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/delete/<int:pk>', PhotoDeleteView.as_view(), name='photo_delete'),
    # path('products/<int:pk>/review/add/', ProductReviewAddView.as_view(), name='product_review_add'),
    # path('reviews/update/<int:pk>', ReviewUpdateView.as_view(), name='review_update'),
    # path('reviews/delete/<int:pk>', ReviewDeleteView.as_view(), name='review_delete')
]

