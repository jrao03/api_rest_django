from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Item
from .serializers import ItemSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

# Create your views here.
@api_view(['get'])
def get_item(request):
    items = Item.objects.all()
    nombre = request.query_params.get('name', None)
    departamento = request.query_params.get('department', None)

    if nombre:
        items = items.filter(name__icontains=nombre)

    if departamento:
        items = items.filter(department=departamento)

    paginator = StandardResultsSetPagination()
    pagina = paginator.paginate_queryset(items, request)

    serializer = ItemSerializer(pagina, many=True)
    return Response(serializer.data, status=200)

@api_view(['post'])
@permission_classes([IsAuthenticated])
def insert_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['put'])
@permission_classes([IsAuthenticated])
def update_item(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return Response({'error': 'Item not found'}, status=404)
    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)

@api_view(['patch'])
@permission_classes([IsAuthenticated])
def partial_update_item(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return Response({'error': 'Item not found'}, status=404)
    serializer = ItemSerializer(item, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)

@api_view(['delete'])
@permission_classes([IsAuthenticated])
def delete_item(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return Response({'error': 'Item not found'}, status=404)
    item.delete()
    return Response({'message': 'Item deleted successfully'}, status=204)
