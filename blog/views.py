from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from blog.models import BlogPaper


class BlogListView(ListView):
    model = BlogPaper
    template_name = "blog/home.html"
    context_object_name = "paper"

    def get_queryset(self):
        context = super().get_queryset().filter(is_active=True)
        return context


class BlogPaperNotActiveListView(ListView):
    model = BlogPaper
    template_name = "blog/not_active.html"
    context_object_name = "paper"

    def get_queryset(self):
        context = super().get_queryset().filter(is_active=False)
        return context


class BlogCreateView(CreateView):
    model = BlogPaper
    fields = ["title", "text", "preview", "is_active"]
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:home")


class BlogDetailView(DetailView):
    model = BlogPaper
    template_name = "blog/paper_detail.html"
    context_object_name = "paper"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.view_count += 1
        self.object.save(update_fields=["view_count"])
        return response


class BlogUpdateView(UpdateView):
    model = BlogPaper
    fields = ["title", "text", "preview", "is_active"]
    template_name = "blog/blog_form.html"

    def get_success_url(self):
        return reverse_lazy("blog:paper_detail", kwargs={"pk": self.object.pk})


class BlogDeleteView(DeleteView):
    model = BlogPaper
    template_name = "blog/blog_paper_delete.html"
    context_object_name = "paper"
    success_url = reverse_lazy("blog:home")
