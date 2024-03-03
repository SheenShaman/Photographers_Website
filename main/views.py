from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from main.models import Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'image', 'is_published')
    # success_url = reverse_lazy('')


