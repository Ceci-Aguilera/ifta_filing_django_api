from django.contrib import admin
from django.conf.urls import url,include
from .views import *

app_name = 'truck_management_app'

urlpatterns = [
    url(r'^new-entry/(?P<truck_id>[0-9]+)/$', NewEntryView.as_view(), name='new-entry-api'),
    url(r'^all-entries/(?P<owner_id>[0-9]+)/(?P<truck_id>[0-9]+)/$', ListAllQuarterEntry.as_view(), name='list-all-new-entries-api'),
    url(r'^calculate-quarter-taxes/(?P<owner_id>[0-9]+)/(?P<truck_id>[0-9]+)/$', CalculateQuarterTaxesView.as_view(), name='calculate-quarter-taxes-api'),
    url(r'^taxes-all-years/(?P<owner_id>[0-9]+)/(?P<truck_id>[0-9]+)/$', AllTimesTaxesYear.as_view(), name='taxes-all-years-api'),
    url(r'^year/(?P<owner_id>[0-9]+)/(?P<truck_id>[0-9]+)/(?P<year>[0-9]+)/$', YearTaxes.as_view(), name='year-api'),
    url(r'^quarter-tax/(?P<owner_id>[0-9]+)/(?P<truck_id>[0-9]+)/(?P<year>[0-9]+)/(?P<number>[0-9]+)/$', QuarterTaxes.as_view(), name='year-api'),
    url(r'^ifta-report-pdf/(?P<owner_id>[0-9]+)/(?P<truck_id>[0-9]+)/$', SendTaxesPDF.as_view(), name='ifta-report-pdf-test-api'),
    url(r'^truck-current-driver/(?P<id>[0-9]+)/$', CurrentTruck.as_view(), name='truck-current-driver-api'),
    url(r'^driver-quarter-entries/(?P<id>[0-9]+)/(?P<truck_id>[0-9]+)/$', CurrentDriverEntries.as_view(), name='driver-quarter-entries-api'),
    url(r'^delete-entry/(?P<id>[0-9]+)/(?P<truck_id>[0-9]+)/(?P<entry_id>[0-9]+)/$', DeleteEntry.as_view(), name='delete-entry-api'),
]
