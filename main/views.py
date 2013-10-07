import math
from django.shortcuts import redirect
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView, FormView

from .models import Project


class HomeView(ListView):
    model = Project
    template_name = 'Portfolio/grid.html'

    model_query = Project.objects.all().exclude(thumbnail='')

    def dispatch(self, *args, **kwargs):
        #Store stuff so we don't have to calculate them in each of these functions
        page = self.kwargs['page'] if 'page' in self.kwargs else 1
        self.page = int(page)

        self.numPages = int(math.ceil(self.model_query.count()/6.0))

        self.page_list = range(1,self.numPages+1)

        if self.page in self.page_list:
            return super(HomeView, self).dispatch(*args, **kwargs)

        #If the page is not in the range of possible pages, redirect to page 1
        return redirect('home_paginated', page=1)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['num_pages'] = self.numPages

        context['current_page'] = self.page

        context['prev_page'] = self.page-1 if self.page > 1 else 1
        context['next_page'] = self.page+1 if self.page < self.numPages else self.numPages

        context['page_list'] = self.page_list

        return context

    def get_queryset(self):
        offsetStart = 6*(self.page-1)
        offsetEnd = offsetStart+6

        return self.model_query.prefetch_related('tags', 'links').order_by('id')[offsetStart:offsetEnd]


class ProjectView(DetailView):
    model = Project
    template_name = 'Portfolio/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)

        projects = Project.objects.all().order_by('id')

        result = [(p.id, p.get_url) for p in projects]

        prev = None
        next = False
        i = -1
        for p in projects:
            if next:
                context['next_project'] = (p.id, p.get_url())
                break
            if p.id == self.object.id:
                if prev:
                    context['prev_project'] = (prev.id, prev.get_url())
                next = True

            prev = p
            i += 1

        if 'next_project' not in context:
            context['next_project'] = (self.object.id, self.object.get_url())
        if 'prev_project' not in context:
            context['prev_project'] = (self.object.id, self.object.get_url())

        context['project_links'] = result
        context['num_projects'] = len(result)

        context['grid_page'] = (i / 6)+1

        return context

    def get_object(self, queryset=None):
        return Project.objects.prefetch_related('pictures', 'tags', 'links').get(slug=self.kwargs['slug'])