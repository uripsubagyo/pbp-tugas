from django.urls import path
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import show_json_mywatchlist
from mywatchlist.views import show_json_id_mywatchlist
from mywatchlist.views import show_xml_mywatchlist
from mywatchlist.views import show_xml_id_mywatchlist
from mywatchlist.views import show_html_mywatchlist, show_html_id_mywatchlist

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html', show_html_mywatchlist, name='show_html_mywatchlist'),
    path('html/<int:id>', show_html_id_mywatchlist, name='show_html_id_mywatchlist'),
    path('json/', show_json_mywatchlist, name='show_json_mywatchlist'),
    path('json/<int:id>', show_json_id_mywatchlist, name='show_json_id_mywatchlist'),
    path('xml/', show_xml_mywatchlist, name='show_xml_mywatchlist'),
    path('xml/<int:id>', show_xml_id_mywatchlist, name='show_xml_id_mywatchlist'),

]

