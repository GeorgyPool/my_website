from django.urls import path

from blog.apps import BlogConfig

from . import views

app_name = BlogConfig.name

urlpatterns = [
    path("blog/home/", views.BlogListView.as_view(), name="home"),
    path("blog/form_create/", views.BlogCreateView.as_view(), name="create"),
    path(
        "blog/paper_detail/<int:pk>/",
        views.BlogDetailView.as_view(),
        name="paper_detail",
    ),
    path("blog/form_update/<int:pk>/", views.BlogUpdateView.as_view(), name="update"),
    path(
        "blog/blog_paper_delete/<int:pk>/",
        views.BlogDeleteView.as_view(),
        name="delete",
    ),
    path(
        "blog/not_active/",
        views.BlogPaperNotActiveListView.as_view(),
        name="not_active",
    ),
]
