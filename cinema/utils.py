from django.db.models import Count

from .models import *

# class DataMixin:
#
#     def get_user_context(self, **kwargs):
#         context = kwargs
#         genrs = Genre.objects.annotate(Count('women'))
#
#         user_menu = menu.copy()
#         if not self.request.user.is_authenticated:
#             user_menu.pop(1)
#
#         context['menu'] = user_menu
#
#         context['genrs'] = genrs
#         if 'genrs_selected' not in context:
#             context['genrs_selected'] = 0
#         return context