from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from .models import Person, City
from .forms import PersonForm


class PersonListView(ListView):
    model = Person
    template_name = 'person/list.html'
    http_method_names = ['get']
	# muda o nome do product_list gerado por padrao pela classe
    context_object_name = 'object_list'
    paginate_by = 15

class PersonCreateView(CreateView):
    model = Person
    template_name = 'person/add.html'
    form_class = PersonForm


class PersonUpdateView(UpdateView):
    model = Person
    template_name = 'person/add.html'
    form_class = PersonForm


def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    context = {
        'cities': cities,
    }
    return render(request, 'includes/_city_dropdown_list_options.html', context)
