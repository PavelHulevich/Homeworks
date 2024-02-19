from articles.models import Article
from articles.models import Comment
from category.models import Category
from django.core.management.base import BaseCommand
from faker import Faker
import random
import string
from order.models import Order
from order.models import OrderItem
from order.models import Product
from order.models import ShippingAddress
from order.models import Tag
from ...models import User
from ...models import UserProfile
from django.utils import timezone
fake = Faker()


class Command(BaseCommand):
    help = 'Populates the database with fake data'

    def handle(self, *args, **kwargs):
        self.generate_users()
        self.generate_user_profiles()
        self.generate_articles()
        self.generate_comments()
        self.generate_categories()
        self.generate_orders_and_products()
        self.generate_tags()
        self.generate_shipping_addresses()

    def generate_users(self, num_users=20):
        for _ in range(num_users):
            username = fake.user_name()
            email = fake.email()
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            User.objects.create(username=username, email=email, password=password)

    def generate_user_profiles(self):
        for user in User.objects.all():
            bio = fake.paragraph()
            avatar = fake.image_url()
            UserProfile.objects.create(user=user, bio=bio, avatar=avatar)

    def generate_articles(self, num_articles=20):
        for _ in range(num_articles):
            title = fake.sentence()
            content = fake.text()
            author = random.choice(User.objects.all())
            Article.objects.create(title=title, content=content, author=author)

    def generate_comments(self, num_comments=20):
        for _ in range(num_comments):
            article = random.choice(Article.objects.all())
            author = random.choice(User.objects.all())
            text = fake.text()
            created_at = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone())
            Comment.objects.create(article=article, author=author, text=text, created_at=created_at)

    def generate_categories(self, num_categories=20):
        for _ in range(num_categories):
            name = fake.word()
            description = fake.sentence()
            parent = random.choice(Category.objects.all()) if Category.objects.exists() else None
            Category.objects.create(name=name, description=description, parent=parent)

    def generate_tags(self, num_tags=20):
        for _ in range(num_tags):
            name = fake.word()
            tag = Tag.objects.create(name=name)
            products = random.sample(list(Product.objects.all()), k=random.randint(1, 5))
            tag.products.set(products)

    def generate_orders_and_products(self, num_orders=20, products_per_order=3):
        for _ in range(num_orders):
            customer = random.choice(User.objects.all())
            total_price = round(random.uniform(50, 200), 2)
            order = Order.objects.create(customer=customer, total_price=total_price)
            for _ in range(products_per_order):
                name = fake.word()
                description = fake.sentence()
                price = round(random.uniform(10, 50), 2)
                product = Product.objects.create(name=name, description=description, price=price)
                quantity = random.randint(1, 5)
                total_price = round(quantity * price, 2)
                OrderItem.objects.create(order=order, product=product, quantity=quantity, total_price=total_price)

    def generate_shipping_addresses(self):
        for user in User.objects.all():
            address = fake.address()
            city = fake.city()
            country = fake.country()
            zip_code = fake.zipcode()
            ShippingAddress.objects.create(user=user, address=address, city=city, country=country, zip_code=zip_code)
