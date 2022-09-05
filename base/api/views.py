from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api'
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    serialized_rooms = RoomSerializer(Room.objects.all(), many=True)
    return Response(serialized_rooms.data)


@api_view(['GET'])
def getRoom(request, pk):
    serialized_room = RoomSerializer(Room.objects.get(pk=pk))
    return Response(serialized_room.data)