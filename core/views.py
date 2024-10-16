from django.http import JsonResponse
from django.shortcuts import render
from .models import Task, Event, Interaction, Contact
from .forms import NewContactForm, NewInteractionForm, NewTaskForm
from django.views.generic import TemplateView, ListView, DetailView, FormView, View

class HomePageView(TemplateView):
    template_name = 'home.html'

class TaskListView(ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['interactions'] = Interaction.objects.all()
    #     context['leads'] = Lead.objects.all()
    #     return context

class NewContactView(FormView):
    template_name = 'forms/new_contact.html'
    form_class = NewContactForm
    success_url = '/tasks/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class NewInteractionView(FormView):
    template_name = 'forms/new_interaction.html'
    form_class = NewInteractionForm
    success_url = '/tasks/'

    def form_valid(self, form):
        new_interaction = form.save()
        needs_follow_up = form.cleaned_data['needs_follow_up']

        if needs_follow_up:
            task_form = NewTaskForm(self.request.POST)
            if task_form.is_valid():
                new_task = task_form.save(commit=False)
                new_task.origin = new_interaction
                new_task.save()

        return super().form_valid(form)
    
class FormSnippetView(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        if q == 'task':
            form = NewTaskForm()
        
        if form:
            return render(request, 'forms/snippets/new_task_snippet.html', {'form': form})