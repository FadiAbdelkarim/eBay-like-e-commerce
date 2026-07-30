# eBay-like E-Commerce

A Django-based online auction platform where users can list items, place competitive bids, and win auctions — modeled after eBay's core marketplace experience.

## Overview

This project is a full-stack auction marketplace built with Django on the backend. It allows registered users to create listings for items they want to sell, browse and search listings by category, place bids on active auctions, track items of interest via a personal watchlist, and discuss listings through comments. Sellers can close their own auctions at any time, automatically declaring the highest bidder the winner. It's designed for anyone who wants a lightweight, self-hosted alternative to large marketplace platforms — whether for a hobby community, a local exchange, or as a foundation to build a more specialized auction site on top of.

## Features

- **User authentication** — registration, login, and logout
- **Create listings** — title, description, starting bid, optional image URL, optional category
- **Active listings page** — browse all currently open auctions in a card-based grid
- **Listing detail page** — full item details, current highest bid, and auction status
- **Bidding system** — place bids with server-side validation (must exceed the current highest bid or meet the starting bid)
- **Close auction** — sellers can end their own auction at any time; the highest bidder is declared the winner
- **Watchlist** — signed-in users can save and remove listings to revisit later
- **Categories** — browse listings filtered by category
- **Comments** — signed-in users can leave comments on any listing
- **Django Admin integration** — manage listings, bids, comments, and categories from the built-in admin panel

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (default, via Django ORM)
- **Frontend:** HTML, CSS (custom, no external UI framework)
- **Auth:** Django's built-in authentication system, extended via a custom `User` model

## Setup / Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/FadiAbdelkarim/eBay-like-e-commerce.git
   cd eBay-like-e-commerce
   ```

2. **Install dependencies**
   ```bash
   pip3 install django
   ```

3. **Apply database migrations**
   ```bash
   python3 manage.py makemigrations auctions
   python3 manage.py migrate
   ```

4. **(Optional) Create an admin account**
   ```bash
   python3 manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python3 manage.py runserver
   ```

6. Visit `http://127.0.0.1:8000/` in your browser.

## Project Structure

```
eBay-like-e-commerce/
├── auctions/                  # Main Django app
│   ├── migrations/            # Database migration files
│   ├── static/auctions/       # CSS
│   ├── templates/auctions/    # HTML templates
│   ├── admin.py                # Django admin registrations
│   ├── models.py               # User, Listing, Bid, Comment, Category models
│   ├── urls.py                 # App-level URL routing
│   └── views.py                # View logic
├── commerce/                  # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
└── manage.py
```

## License

This project is licensed under the [MIT License](LICENSE).
