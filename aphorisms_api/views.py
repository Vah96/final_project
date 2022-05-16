from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import permissions
from aphorisms.models import Aphorism
from .serializers import AphorismSerializer
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def aphorism_list(request):
    if request.method == 'GET':
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
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = AphorismSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Aphorism.objects.all().delete()
        return JsonResponse({'message': '{} Aphorisms were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def aphorism_detail(request, pk):
    # find tutorial by pk (id)
    try:
        aphorism = Aphorism.objects.get(pk=pk)
    except Aphorism.DoesNotExist:
        return JsonResponse({'message': 'The aphorism does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer = AphorismSerializer(aphorism)
        return JsonResponse(tutorial_serializer.data)
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
