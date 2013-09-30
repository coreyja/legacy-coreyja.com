import math
from django.shortcuts import redirect
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView, FormView

from .models import Project


class HomeView(ListView):
    model = Project
    template_name = 'Portfolio/grid.html'

    def dispatch(self, *args, **kwargs):
        #Store page and numPages so we don't have to calculate them every time
        self.numPages = int(math.ceil(Project.objects.count()/6.0))

        page = self.kwargs['page'] if 'page' in self.kwargs else 1
        self.page = int(page)

        self.page_list = range(1,self.numPages+1)

        if self.page in self.page_list:
            return super(HomeView, self).dispatch(*args, **kwargs)

        #If the page is not in the range of possible pages, redirect to home
        return redirect('home')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['num_pages'] = self.numPages

        context['current_page'] = self.page

        context['prev_page'] = self.page-1 if self.page > 1 else 1
        context['next_page'] = self.page+1 if self.page < self.numPages else self.numPages-1

        context['page_list'] = self.page_list

        return context

    def get_queryset(self):
        offsetStart = 6*(self.page-1)
        offsetEnd = offsetStart+6

        return Project.objects.all().order_by('id')[offsetStart:offsetEnd]
