from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'myapp/myapp_list.html'

class Index2View(generic.TemplateView):
    template_name = 'myapp/index2.html'