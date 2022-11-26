from django.views.generic import DetailView
from webapp.models import Photo


class PhotoDetailView(DetailView):
    template_name = "photo/photo.html"
    context_object_name = 'photo'
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['reviews'] = self.object.products.order_by("-created_at")
        return context

