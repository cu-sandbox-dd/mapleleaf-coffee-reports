# Maple Leaf Coffee – Daily Sales Report

Fictional coffee chain (all data is made up). This small Python tool reads a day's
point-of-sale export and prints a summary for the store manager:

- number of completed orders
- gross sales
- net sales (after discounts, **excluding refunded orders**)
- average order value

## Run it

```
pip install -r requirements.txt
python src/sales_report.py data/sample_sales.csv
```

## Run the tests

```
pytest
```

## Known issue
The store manager reports that net sales look too high on days with refunds.
