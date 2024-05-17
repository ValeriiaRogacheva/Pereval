from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import PerevalAdded
from .serializers import PerevalSerializer


class SubmitData(CreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            instance = serializer.save()
            response_data = {
                "status": 200,
                "message": "Запись о перевале успешно добавлена.",
                "id": instance.id
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except ValidationError as e:
            response_data = {
                "status": 400,
                "message": "Bad Request. Некорректные данные.",
                "errors": e.detail
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            response_data = {
                "status": 500,
                "message": "Internal Server Error",
                "errors": str(e)
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)