from django.urls import path
from blog.views import PostDetailView, PostView, CommentView


app_name = "blogs"

urlpatterns = [
   
    path('', PostView.as_view(), name='post'),
    path('<int:pk>/post/', PostDetailView.as_view(), name='detail'),
    path("<int:pk>/comment/", CommentView.as_view(), name='comment')

]