from decimal import Decimal
from django.db.models import Max
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Listing, Bid, Comment, Category


def index(request):
    listings = Listing.objects.filter(is_active = True)
    return render(request, "auctions/index.html", {
        "listings": listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def listing(request, listing_id):
    lis = Listing.objects.get(pk = listing_id)
    return render(request, "auctions/listing.html",{
        "listing":lis
    })


def watchlist(request, listing_id):
    listing = Listing.objects.get(pk = listing_id)
    if listing in request.user.watchlist.all():
        request.user.watchlist.remove(listing)
    else:
        request.user.watchlist.add(listing)
    return HttpResponseRedirect(reverse("listing", args=[listing_id]))


def bid(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    bid_amount = Decimal(request.POST.get("bid_amount"))

    if bid_amount > listing.current_price or (not listing.bid_set.exists() and bid_amount >= listing.starting_bid):
        Bid.objects.create(amount=bid_amount, bidder=request.user, listing=listing)
        return HttpResponseRedirect(reverse("listing", args=[listing_id]))
    else:
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "error": "Bid must be greater than the current price."
        })


def close(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    listing.is_active = False
    listing.save()
    return HttpResponseRedirect(reverse("listing", args=[listing_id]))


def comment(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    comment_text = request.POST.get("comment")
    Comment.objects.create(commenter=request.user, listing=listing, comment=comment_text)
    return HttpResponseRedirect(reverse("listing", args=[listing_id]))


def watchlist_page(request):
    watchlist = request.user.watchlist.all()
    return render(request, "auctions/watchlist.html", {
                "watchlist" : watchlist
            })



def categories(request):
    categories = Category.objects.all()
    return render(request, "auctions/categories.html", {
                    "categories" : categories
                })

def categories_listings(request, cat_id):
    category = Category.objects.get(pk=cat_id)
    listings = Listing.objects.filter(category=category, is_active=True)
    return render(request, "auctions/index.html", {
        "listings": listings,
        "category": category
    })

from django.contrib.auth.decorators import login_required

@login_required
def create_listing(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        starting_bid = request.POST.get("starting_bid")
        image_url = request.POST.get("image_url", "").strip()
        category_id = request.POST.get("category")

        if not title or not description or not starting_bid:
            return render(request, "auctions/create_listing.html", {
                "categories": Category.objects.all(),
                "error": "Title, description, and starting bid are required."
            })

        category = None
        if category_id:
            category = Category.objects.get(pk=category_id)

        listing = Listing.objects.create(
            title=title,
            description=description,
            starting_bid=starting_bid,
            image_url=image_url if image_url else None,
            category=category,
            creator=request.user
        )
        return HttpResponseRedirect(reverse("listing", args=[listing.id]))
    else:
        return render(request, "auctions/create_listing.html", {
            "categories": Category.objects.all()
        })