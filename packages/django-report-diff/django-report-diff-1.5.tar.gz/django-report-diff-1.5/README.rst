===========
Report Diff
===========

Quick start
-----------

1. Add "report-diff" to your INSTALLED_APPS settings like this::

    INSTALLED_APP = [
        ...
        'report-diff',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^report-diff/', include('polls.urls')),

