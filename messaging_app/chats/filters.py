# your_app/filters.py
import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    custom_field = django_filters.CharFilter(method='filter_custom_logic')

    class Meta:
        model = Message
        fields = ['message_id', 'message_body']

    def filter_custom_logic(self, queryset, name, value):
        if value == 'special_value':
            return queryset.filter(some_other_field__contains='keyword')
        return queryset