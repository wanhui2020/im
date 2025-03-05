from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q

from message.models import Message


def search_messages(user, query):
    search_vector = SearchVector('content')
    search_query = SearchQuery(query)
    return Message.objects.annotate(
        rank=SearchRank(search_vector, search_query)
    ).filter(
        Q(sender=user) | Q(receiver=user),
        rank__gte=0.3
    ).order_by('-rank')

def filter_messages(user, start_date=None, end_date=None, message_type=None):
    queryset = Message.objects.filter(
        Q(sender=user) | Q(receiver=user))
    if start_date:
        queryset = queryset.filter(timestamp__gte=start_date)
    if end_date:
        queryset = queryset.filter(timestamp__lte=end_date)
    if message_type:
        queryset = queryset.filter(message_type=message_type)
    return queryset