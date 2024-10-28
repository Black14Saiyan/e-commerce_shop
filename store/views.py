from django.shortcuts import render #type: ignore
from store.models import Product

# CHEMIN POUR RETOURNER LA PAGE INDEX
def index(request):
    # POUR RECUPERER LES ELEMENTS DU MODELE PRODUCT
    products = Product.objects.all()
    return render(request, 'store/index.html', context={"products" : products})
