from django.urls import reverse_lazy
from django.views.generic import DeleteView
from webapp.models import Photo


class PhotoDeleteView(DeleteView):
    template_name = 'photo/photo_delete.html'
    model = Photo
    context_object_name = 'photo'
    success_url = reverse_lazy('photo_home')

