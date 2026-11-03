import csv
from datetime import date
from decimal import Decimal

from django.core.management.base import BaseCommand

from orders.models import Customer, Order


class Command(BaseCommand):
    help = "Import orders from a Shopify CSV export"

    def add_arguments(self, parser):
        parser.add_argument("csv_path")

    def handle(self, *args, **options):
        created = 0
        with open(options["csv_path"], newline="", encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                if not row["Email"]:
                    continue  # extra line item of the previous order

                address = (
                    f"{row['Shipping Address1']}, "
                    f"{row['Shipping City']}, "
                    f"{row['Shipping Zip']}"
                )
                customer, _ = Customer.objects.get_or_create(
                    email=row["Email"],
                    defaults={"name": row["Shipping Name"], "address": address},
                )
                order, was_created = Order.objects.get_or_create(
                    shopify_order_id=row["Name"],
                    defaults={
                        "customer": customer,
                        "order_date": date.fromisoformat(row["Created at"][:10]),
                        "price": Decimal(row["Total"]),
                    },
                )
                if was_created:
                    created += 1
        self.stdout.write(self.style.SUCCESS(f"Created {created} new orders"))