from django.shortcuts import render
from django.http import JsonResponse
from backend.models import Photographer, Client, PhotoshootSession

# Create your views here.


def searchPhotographers(request):
    if(not (request.GET.get('base_price') and request.GET.get('city'))):
        if (request.GET.get('base_price')):
            price = request.GET.get('base_price')
            photographer_list = Photographer.objects.filter(
                base_price__lte=price)

            if(len(photographer_list) == 0):
                errString = 'No photographers with base price $' + \
                    request.GET.get('base_price')
                context = {'error_message': errString}
                return render(request, 'search.html', context)
            else:
                context = {'success_message': 'list retreived',
                           'list': photographer_list}
                return render(request, 'search.html', context)
        if (request.GET.get('city')):
            search_city = request.GET.get('city')
            photographer_list = Photographer.objects.filter(
                city=search_city)
            if(len(photographer_list) == 0):
                errString = 'No photographers in city: ' + \
                    request.GET.get('city')
                context = {'error_message': errString}
                return render(request, 'search.html', context)
            else:
                context = {'list': photographer_list,
                           'success_message': 'list retreived'}
                return render(request, 'search.html', context)
    else:
        price = request.GET.get('base_price')
        search_city = request.GET.get('city')
        photographer_list = Photographer.objects.filter(
            base_price__lte=price, city=search_city)
        if(len(photographer_list) == 0):
            errString = 'No photographers with city ' + \
                request.GET.get('city') + ' and base price $' + \
                request.GET.get('base_price')
            context = {'error_message': errString}
            return render(request, 'search.html', context)
        else:
            context = {'list': photographer_list,
                       'success_message': 'list retreived'}
            return render(request, 'search.html', context)

    if request.is_ajax():
        data = list(Photographer.objects.filter(
            id=request.GET.get('id')).values('first_name', 'last_name', 'city', 'address1', 'address2', 'base_price', 'telephone', 'email'))
        return JsonResponse(data, safe=False)

    return render(request, 'search.html')
