from django.urls import path
from . import views

# path('route string', name of view function, name="string name of route")
# # example
# path('artists/', views.Artist_List.as_view(), name="artist_list")


# this is like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('artists/', views.ArtistList.as_view(), name="artist_list"),
    path('artists/new/', views.ArtistCreate.as_view(), name="artist_create"),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name="artist_detail"),
    path('artists/<int:pk>/update',views.ArtistUpdate.as_view(), name="artist_update"),
    path('artists/<int:pk>/delete',views.ArtistDelete.as_view(), name="artist_delete_confirmation"),
    path('artists/<int:pk>/songs/new/', views.SongCreate.as_view(), name="song_create"),
    path('playlists/<int:pk>/songs/<int:song_pk>/', views.PlaylistSongAssoc.as_view(), name="playlist_song_assoc"),
    path('songs/', views.SongList.as_view(), name="song_list"),
] 
