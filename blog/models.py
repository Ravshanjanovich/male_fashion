from django.db import models
from shop.abstract import BaseModel
from django.utils.translation import gettext_lazy as _





class Author(BaseModel):
    full_name = models.CharField(max_length=100, verbose_name=_("full name"))
    image = models.ImageField(upload_to="author_image/", verbose_name=_("image"))


    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.full_name


class PostTag(BaseModel):
    name = models.CharField(max_length=40, verbose_name=_('name'))


    class Meta:
        verbose_name = _("PostTag")
        verbose_name_plural =_("PostTags")

    def __str__(self):
        return self.name


class Post(BaseModel):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    body = models.TextField(verbose_name=_("body"))
    main_image = models.ImageField(upload_to="post_image/", verbose_name=_("main image"))
    author = models.ForeignKey(Author, related_name="posts", verbose_name=_('author'), on_delete=models.RESTRICT)
    tag = models.ManyToManyField(PostTag, related_name='posts', verbose_name=_('tag'))


    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return f"{self.title[:100]}"


class Comment(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    email = models.EmailField(verbose_name=_("email"))
    phone = models.CharField(max_length=13, verbose_name=_('phone'))
    comment = models.TextField(verbose_name=_('comment'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", verbose_name=_("post"))


    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return f"{self.name}\n{self.comment[:50]}\n{self.email}"



