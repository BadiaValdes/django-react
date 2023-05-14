from dal import autocomplete

from ..models import Position, ProductType, Brand

class ABrand(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Brand.objects.all()
        if(self.q):
            qs = qs.filter(name__contains=self.q)
        return qs

class APosition(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        return Position.objects.all()

class AProductType(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        return ProductType.objects.all()