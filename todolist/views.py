from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .models import TodoItem
from .forms import CreateTodoitemForm

class ItemView(TemplateView):
    template_name = 'item.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = TodoItem.objects.get(kwargs['id'])
        return context


def item_create_view(request):
    if request.method != 'POST':
        form = CreateTodoitemForm() 
        return render(request, 'genericform.html', {'form': form})
    
    form = CreateTodoitemForm(request.POST)

    if not form.is_valid():
        return HttpResponse('<h1>Error With Form Validation</h1>')

    data = form.cleaned_data

    item = TodoItem(name=data['name'], creator=request.user)
    item.save()
    return HttpResponseRedirect('') 

