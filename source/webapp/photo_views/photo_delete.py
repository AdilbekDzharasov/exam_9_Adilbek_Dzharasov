from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView
from webapp.models import Photo
from webapp.models import Chosen


class PhotoDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'photo/photo_delete.html'
    model = Photo
    context_object_name = 'photo'
    success_url = reverse_lazy('photo_home')
    permission_required = 'webapp.delete_photo'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user \
               or self.request.user.is_superuser


class PhotoChosenDeleteView(View):

    def post(self, request, *args, **kwargs):
        image = get_object_or_404(Photo, pk=kwargs.get('pk'))
        user = request.user
        Chosen.objects.filter(image=image, user=user).delete()
        return redirect('photo_home')

