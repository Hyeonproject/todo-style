import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.edit import BaseDeleteView, BaseCreateView
from django.views.generic.list import BaseListView

from todo.models import Todo


@method_decorator(ensure_csrf_cookie, name='dispatch')
class ApiTodoLV(BaseListView):
    model = Todo

    # def get(self, request, *args, **kwargs):
    #     tmpList = [
    #         {'id': 1, 'name': 'dHyeon', 'todo': '잘 만들기'},
    #         {'id': 2, 'name': 'd이동현', 'todo': 'Vue.js 연동으로 서비스를 만듭니다.'},
    #         {'id': 3, 'name': 'd이동현', 'todo': 'Vue.js 연동으로 그냥 만드네요.'},
    #         {'id': 4, 'name': 'd이동현', 'todo': 'Vue.js 고기반찬'},
    #     ]
    #     return JsonResponse(data=tmpList, safe=False)

    def render_to_response(self, context, **response_kwargs):
        todoList = list(context['object_list'].values())
        return JsonResponse(data=todoList, safe=False)


# @method_decorator(csrf_exempt, name='dispatch')
class ApiTodoDelV(BaseDeleteView):
    model = Todo

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse(data={}, status=204)


# @method_decorator(csrf_exempt, name='dispatch')
class APITodoCV(BaseCreateView):
    model = Todo
    fields = '__all__'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['data'] = json.loads(self.request.body)
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        newTodo = model_to_dict(self.object)
        print(f'newTodo: {newTodo}')
        return JsonResponse(data=newTodo, status=201)

    def form_invalid(self, form):
        return JsonResponse(data=form.errors, status=400)