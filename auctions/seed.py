from auctions.models import User, Category, Listing

# Get or create a user to own these listings (change username if needed)
creator, _ = User.objects.get_or_create(username="demo_seller", defaults={"email": "demo@example.com"})
creator.set_password("password123")
creator.save()

# Categories
electronics, _ = Category.objects.get_or_create(name="Electronics")
fashion, _ = Category.objects.get_or_create(name="Fashion")
home, _ = Category.objects.get_or_create(name="Home")
toys, _ = Category.objects.get_or_create(name="Toys")

listings = [
    {
        "title": "Vintage Polaroid Camera",
        "description": "Classic instant film camera, fully functional, comes with a pack of unused film.",
        "starting_bid": 45.00,
        "image_url": "https://images.unsplash.com/photo-1495707902641-75cac588d2e9?w=500",
        "category": electronics,
    },
    {
        "title": "Leather Messenger Bag",
        "description": "Handmade full-grain leather bag, fits a 15-inch laptop, brass hardware.",
        "starting_bid": 80.00,
        "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500",
        "category": fashion,
    },
    {
        "title": "Mechanical Keyboard - Blue Switches",
        "description": "87-key tenkeyless mechanical keyboard, hot-swappable switches, RGB backlight.",
        "starting_bid": 60.00,
        "image_url": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500",
        "category": electronics,
    },
    {
        "title": "Ceramic Plant Pot Set (3 pcs)",
        "description": "Minimalist matte ceramic pots in three sizes, drainage holes included, no saucers.",
        "starting_bid": 20.00,
        "image_url": "https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=500",
        "category": home,
    },
    {
        "title": "Wooden Chess Set",
        "description": "Hand-carved walnut and maple chess set, folding board doubles as storage case.",
        "starting_bid": 35.00,
        "image_url": "https://images.unsplash.com/photo-1528819622765-d6bcf132f793?w=500",
        "category": toys,
    },
    {
        "title": "Retro Bluetooth Speaker",
        "description": "Portable speaker with 12-hour battery life, vintage radio-inspired design.",
        "starting_bid": 30.00,
        "image_url": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500",
        "category": electronics,
    },
]

for data in listings:
    Listing.objects.get_or_create(
        title=data["title"],
        defaults={
            "description": data["description"],
            "starting_bid": data["starting_bid"],
            "image_url": data["image_url"],
            "category": data["category"],
            "creator": creator,
        }
    )

print(f"Seeded {len(listings)} listings.")