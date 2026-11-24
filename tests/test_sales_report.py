import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from sales_report import load_orders, net_sales, gross_sales, average_order_value  # noqa: E402

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "sample_sales.csv")


def test_gross_sales_includes_every_line():
    assert gross_sales(load_orders(DATA)) == 54.3


def test_net_sales_excludes_refunds_and_applies_discounts():
    assert net_sales(load_orders(DATA)) == 42.13


def test_average_order_value_uses_completed_orders_only():
    assert average_order_value(load_orders(DATA)) == 7.02
