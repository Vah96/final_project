from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import permissions
from aphorisms.models import Aphorism
from .serializers import AphorismSerializer
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_aphorism_list(request):
    aphorisms = Aphorism.objects.all()

    text = request.GET.get('text', None)
    if text is not None:
        aphorisms = aphorisms.filter(text__icontains=text)

    tag_id = request.GET.get('tag_id', None)
    if tag_id is not None:
        aphorisms = aphorisms.filter(tags__id=tag_id)

    aphorisms_serializer = AphorismSerializer(aphorisms, many=True)
    return JsonResponse(aphorisms_serializer.data, safe=False)
    # 'safe=False' for objects serialization


@api_view(['POST', 'DELETE'])
@permission_classes((permissions.IsAuthenticated,))
def aphorism_list(request):
    if request.method == 'POST':
        # aphorism_data = JSONParser().parse(request.data)
        aphorism_serializer = AphorismSerializer(data=request.data)
        if aphorism_serializer.is_valid():
            aphorism_serializer.save(author=request.user)
            return JsonResponse(aphorism_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(aphorism_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Aphorism.objects.all().delete()
        return JsonResponse({'message': '{} Aphorisms were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT', 'DELETE'])
@permission_classes((permissions.IsAuthenticated,))
def aphorism_detail(request, pk):
    # find aphorism by pk (id)
    try:
        aphorism = Aphorism.objects.get(pk=pk, author=request.user)
    except Aphorism.DoesNotExist:
        return JsonResponse({'message': 'The aphorism does not exist or it is not your aphorism (you cant '
                                        'not update or delete other user aphorism)'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        aphorism_serializer = AphorismSerializer(aphorism)
        return JsonResponse(aphorism_serializer.data)
    elif request.method == 'PUT':
        aphorism_data = JSONParser().parse(request)
        aphorism_serializer = AphorismSerializer(aphorism, data=aphorism_data)
        if aphorism_serializer.is_valid():
            aphorism_serializer.save()
            return JsonResponse(aphorism_serializer.data)
        return JsonResponse(aphorism_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        aphorism.delete()
        return JsonResponse({'message': 'Aphorism was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
