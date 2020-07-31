from django.shortcuts import render
import logging
from .models import Members, Activity_Periods
from .serializer import MembersSerializer, ActivitySerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

logger = logging.getLogger(__name__)


class MembersViewSet(viewsets.ModelViewSet):
    serializer_class = MembersSerializer
    queryset = Members.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

    def _validate_int(self, member_id):
        if member_id is not None:
            try:
                member_id = int(member_id)
            except ValueError:
                raise (
                    {
                        "error_message": "Given member_id ({param_value}) param NOT VALID".format(param_value=member_id),
                        "cause": "type param value should be integer"
                    }
                )
        return member_id

    def list(self, request, *args, **kwargs):
        logging.info("Retrieving All Members")
        queryset = self.filter_queryset(self.get_queryset())
        if self.request.query_params.get("real_name"):
            real_name = self.request.query_params.get("real_name")
            particular_member = Members.objects.get(real_name=real_name).id
            logging.info("Retrieving Details of : {real_name}".format(real_name=real_name))

            particular_member = self._validate_int(particular_member)
            logging.debug(
                "Of Particular Member: {particular_member}".format(particular_member=particular_member))
            if particular_member is not None:
                queryset = queryset.filter(id=particular_member)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        logger.info("List Done")
        return Response(serializer.data)


class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity_Periods.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

    def _validate_int(self, member_id):
        if member_id is not None:
            try:
                member_id = int(member_id)
            except ValueError:
                raise (
                    {
                        "error_message": "Given member_id ({param_value}) param NOT VALID".format(param_value=member_id),
                        "cause": "type param value should be integer"
                    }
                )
        return member_id

    def list(self, request, *args, **kwargs):
        logging.info("Retrieving All Activity Periods")
        queryset = self.filter_queryset(self.get_queryset())
        if self.request.query_params.get("real_name"):
            real_name = self.request.query_params.get("real_name")
            particular_member = Members.objects.get(real_name=real_name).id
            logging.info("Retrieving Periods of : {real_name}".format(real_name=real_name))
        else:
            particular_member = self.request.query_params.get("id")

        particular_member = self._validate_int(particular_member)
        logging.debug(
            "Of Particular Member: {particular_member}".format(particular_member=particular_member))
        if particular_member is not None:
            queryset = queryset.filter(member=particular_member)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        logger.info("List Done")
        return Response(serializer.data)
