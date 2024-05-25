from django.views.generic.base import TemplateView

from .models import TodoItem

class ItemView(TemplateView):
    template_name = 'item.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = TodoItem.objects.get(kwargs['id'])
        return context


