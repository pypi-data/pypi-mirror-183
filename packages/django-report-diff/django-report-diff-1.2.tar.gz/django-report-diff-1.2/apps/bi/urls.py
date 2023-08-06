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

from apps.bi.views import BaseAPIView

app_name = 'report_diff_bi'


urlpatterns = [
    path('test/', BaseAPIView.as_view()),
]
