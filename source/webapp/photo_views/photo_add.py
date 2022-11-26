from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from webapp.models import Photo
from webapp.forms import PhotoForm


class PhotoCreateView(CreateView):
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

