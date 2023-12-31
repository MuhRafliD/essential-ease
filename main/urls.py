from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_item, get_Item_json, add_item_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    path('get-item-json/', get_Item_json, name='get_item_json'),
    path('add-item-ajax/', add_item_ajax, name='add_item_ajax')
]