from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from webapp.models import Photo, Chosen
from webapp.forms import PhotoForm


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'photo/photo_add.html'
    form_class = PhotoForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=self.request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.author = request.user
            photo.save()
            return redirect('photo_home')
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})


class PhotoChosenView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        chosen, created = Chosen.objects.get_or_create(image=photo, user=request.user)
        if created:
            photo.save()
            return HttpResponse("good")
        else:
            return HttpResponseForbidden()

