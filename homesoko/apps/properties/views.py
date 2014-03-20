from django.views.generic import TemplateView


class HomeList(TemplateView):
    template_name = "property_list.html"


class HomeDetail(TemplateView):
    template_name = "property_detail.html"
