from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BiReportConfig(AppConfig):
    name = 'report_diff.bi_report'
    verbose_name = _('BI REPORT')
