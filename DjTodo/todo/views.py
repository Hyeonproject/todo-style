from django.views.generic import TemplateView, CreateView


class TodoVueOnlyTV(TemplateView):
    template_name = 'todo/todo_vue_only.html'

class TodoCV(CreateView):
    template_name = 'todo/todo_form.html'

