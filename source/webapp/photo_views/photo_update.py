from django.urls import reverse
from django.views.generic import UpdateView
from webapp.models import Photo
from webapp.forms import PhotoForm


class PhotoUpdateView(UpdateView):
    template_name = 'photo/photo_update.html'
    form_class = PhotoForm
    model = Photo
    context_object_name = 'photo'

    def get_success_url(self):
        return reverse('photo_home')

