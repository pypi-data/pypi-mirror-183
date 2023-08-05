#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView


class SerializerError(Exception):
    """ serializer error

    """
    pass


class BaseAPIView(GenericAPIView):
    """ 视图基类

    """
    all_serializers = {}

    result_serializers_class = None

    def get_serializer_class(self):
        """ Return the class to use for the serializer."""

        serializer_class = self.all_serializers.get(str(self.request.method).lower())

        return serializer_class if serializer_class else self.serializer_class

    @staticmethod
    def check_validate(serializer):
        """ Check the serializer is valid."""
        if not serializer.is_valid():
            raise SerializerError(serializer.errors)

    def get(self, request):

        return HttpResponse('success')
