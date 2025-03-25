from django.views.generic import ListView
from django.shortcuts import render

from .models import Foods


# Create your views here.
class FoodList(ListView):
    model = Foods
    template_name = 'home/food.html'
    context_object_name = 'foods'

    ordering = '-pk'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(FoodList, self).get_context_data()
        # context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Foods.objects.filter().count()
        return context

def landing(request):
    
    return render(
        request,
        'home/landing.html',
        {
            
        }
    )

def about(request):
    
    return render(
        request,
        'home/about.html',
        {
            
        }
    )

def chat(request):
    
    return render(
        request,
        'home/chat.html',
        {
            
        }
    )