from django.shortcuts import render, get_object_or_404
from django.db.models.query import  QuerySet
from .models import Post
from django.views.generic import  ListView, DetailView, CreateView
from blog.forms import CommentForm
from django.urls import reverse



class PostView(ListView):
    template_name = 'blog.html'


    def get_queryset(self):
        qs = Post.objects.order_by("-id")
        tag = self.request.GET.get("tag")
        if tag:
            qs = qs.filter(tag__name=tag)
        return qs

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog-deatils.html'


class CommentView(CreateView):
    def form_valid(self, form):
        print(form.instance)
        form.instance.post = get_object_or_404(Post, pk=self.kwargs.get("pk"))
        return super().form_valid(form)
    def get_success_url(self):
        return reverse("blogs:detail", kwargs={'pk':self.kwargs.get("pk")})

