from .views import indexView ,aboutView, saveDataView, deleteView,updateViewPage
from django.urls import path

urlpatterns = [
    # path("",renderSomething, name = "render"),
    path("",indexView,name="index"),
    path("about",aboutView, name ="about"),
    path("save-data",saveDataView, name="save_data"),
    path("delete-note/<int:id>",deleteView, name="deleteView"),
    path("update-note/<int:id>",updateViewPage,name="updateViewPage"),
]
