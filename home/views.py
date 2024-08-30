from django.views.generic import TemplateView

class Index(TemplateView):  # class name
    template_name = 'home/index.html'  # template name