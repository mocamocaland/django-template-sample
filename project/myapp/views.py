from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'myapp/myapp_list.html'

class Index2View(generic.TemplateView):
    template_name = 'myapp/index2.html'


class TestView(generic.TemplateView):
    template_name = 'myapp/test.html'
