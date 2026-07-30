from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:listing_id>/", views.listing, name="listing"),
    path("listing/<int:listing_id>/watchlist/", views.watchlist, name="watchlist"),
    path("listing/<int:listing_id>/bid/", views.bid, name="bid"),
    path("listing/<int:listing_id>/close/", views.close, name="close"),
    path("listing/<int:listing_id>/comment/", views.comment, name="comment"),
    path("watchlist/", views.watchlist_page, name="watchlist_page"),
    path("categories/", views.categories, name="categories"),
    path("categories/<int:cat_id>/", views.categories_listings, name="categories_listings"),
    path("create/", views.create_listing, name="create_listing"),
]
