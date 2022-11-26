from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView
from webapp.models import Photo
from webapp.forms import PhotoForm


class PhotoUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'photo/photo_update.html'
    form_class = PhotoForm
    model = Photo
    context_object_name = 'photo'
    permission_required = 'webapp.change_photo'

    def get_success_url(self):
        return reverse('photo_home')

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user \
               or self.request.user.is_superuser

