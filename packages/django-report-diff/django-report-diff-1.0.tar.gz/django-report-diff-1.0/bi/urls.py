#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      urls.py
   Description:
   Author:          dingyong.cui
   date：           2022/12/27
-------------------------------------------------
   Change Activity:
                    2022/12/27:
-------------------------------------------------
"""
from django.urls import path

from bi.views import BaseAPIView

urlpatterns = [
    path('test/', BaseAPIView.as_view()),
]
