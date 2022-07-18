from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.account.serializers import RegisterSerializer, LoginSerializer

User = get_user_model()


class RegisterApiView(APIView):
    def post(self, request):
        data = request.data
        serializaers = RegisterSerializer(data=data)

        if serializaers.is_valid(raise_exception=True):
            serializaers.save()
            message = f'Вы успешно зарегестрировались. '\
                      f'Вам отправлено письмо с активационным кодом'
            return Response(message, status=201)


class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'Аккаунт успешно активирован'}, status=200)
        except User.DoesNotExist:
            return Response({'msg': 'Неверный код!'}, status=400)


class LoginAPIView(ObtainAuthToken):
    serializer_class = LoginSerializer


