"""Daily sales summary for Maple Leaf Coffee (fictional)."""
import csv
import sys


def load_orders(path):
    """Read the POS export into a list of dicts with numeric fields."""
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["quantity"] = int(r["quantity"])
        r["unit_price"] = float(r["unit_price"])
        r["discount_pct"] = float(r["discount_pct"] or 0)
    return rows


def line_total(order):
    """Value of one order line after its discount."""
    return order["quantity"] * order["unit_price"] * (1 - order["discount_pct"])


def gross_sales(orders):
    """Sum of quantity x price for every line, before discounts."""
    return round(sum(o["quantity"] * o["unit_price"] for o in orders), 2)


def net_sales(orders):
    """Sales after discounts. Refunded orders should not count."""
    return round(sum(line_total(o) for o in completed_orders(orders)), 2)


def completed_orders(orders):
    return [o for o in orders if o["status"] == "completed"]


def average_order_value(orders):
    done = completed_orders(orders)
    if not done:
        return 0.0
    return round(net_sales(done) / len(done), 2)


def main(path):
    orders = load_orders(path)
    print(f"Completed orders:    {len(completed_orders(orders))}")
    print(f"Gross sales:         ${gross_sales(orders):,.2f}")
    print(f"Net sales:           ${net_sales(orders):,.2f}")
    print(f"Average order value: ${average_order_value(orders):,.2f}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/sample_sales.csv")
