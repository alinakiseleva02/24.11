from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from .forms import RequestForm
from .models import Doctor, Service, Request

class ServicesView(ListView):
    model = Service
    template_name = 'services.html'
    context_object_name = 'services'
    paginate_by = 2

class NewRequestView(FormView):
    form_class = Request
    template_name = 'new_request.html'
    success_urls = reverse_lazy('request-form')

    def form_valid(self, form):
        request = form.save(commit=False)
        request.status = 'new'
        request.save()
        return seper().form_valid(form)
        
class RequestFormView(ListView):
    model = Request
    template_name = 'request_form.html'
    context_object_name = 'requests'

class DoctorsView(ListView):
    model = Doctor
    template_name = 'doctors.html'
    context_object_name = 'doctors'
    paginate_by = 2

class RequestsView(ListView):
    model = Request
    template_name = 'requests.html'
    context_object_name = 'requests'
    paginate_by = 2
