from django.shortcuts import render
from django.shortcuts import render
from pages.forms import ContactForm
from pages.models import Banner, MapsModel
from django.views.generic import TemplateView, CreateView
from blog.models import Post
from django.urls import reverse
from django.db.models.query import QuerySet


class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        data = super().get_context_data(**kwargs)
        data ['posts'] = Post.objects.order_by("-pk")[:3]
        data ['banners'] = Banner.objects.filter(is_active=True).order_by('-pk')
        return data 


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm


    def get_success_url(self):
        return reverse("pages:contact")

    def get_queryset(self):
        return MapsModel.objects.all()