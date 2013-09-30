from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView, FormView

from .models import Project


class HomeView(ListView):
    model = Project
    template_name = 'Portfolio/grid.html'

    def get_queryset(self):
        return Project.objects.all()