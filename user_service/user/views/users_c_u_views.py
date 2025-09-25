from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny
from user.services.user_creation_updation_service import UserCreateOrUpdateService

class UsersViewCreatorUpdate(APIView):
     
     permission_classes = [AllowAny]
     
     def post(self, request):
          
          data = request.data
          cmd = request.query_params.get('cmd', None)
          
          pdata = {
               'data':data,
               'cmd':cmd
          }
          
          response = UserCreateOrUpdateService(pdata).manage()
          
          return Response(response.toJson())
     
     
class UsersViewGet(APIView):
     
     def get(self, request):
          
          data = request.data
          cmd = request.query_params.get('cmd', None)
          id = request.query_params.get('id', None)
          
          pdata = {
               'data':data,
               'cmd':cmd
          }
          
          response = UserCreateOrUpdateService(pdata).get(id)
          
          return Response(response.toJson())