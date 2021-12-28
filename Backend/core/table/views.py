from rest_framework.generics import ListAPIView

from .serializers import TableSerializer
from .models import Table
from .pagination import TablePagination

class TableListView(ListAPIView):
    serializer_class = TableSerializer
    pagination_class = TablePagination

    def get_queryset(self):
        qs = Table.objects.all()
        column = self.request.GET.get('column', None)
        condition = self.request.GET.get('condition', None)
        value = self.request.GET.get('value', None)
        if column == 'name':
            if condition == 'equal':
                qs = qs.filter(name=value)
            elif condition == 'contains':
                qs = qs.filter(name__icontains=value)
        elif column == 'amount':
            if condition == 'equal':
                qs = qs.filter(amount=value)
            elif condition == 'greater':
                qs = qs.filter(amount__gt=value)
            elif condition == 'lower':
                qs = qs.filter(amount__lt=value)
        elif column == 'distance':
            if condition == 'equal':
                qs = qs.filter(distance=value)
            elif condition == 'greater':
                qs = qs.filter(distance__gt=value)
            elif condition == 'lower':
                qs = qs.filter(distance__lt=value)
        return qs


    