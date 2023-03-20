**Question**

Write a python script using pandas that finds and prints:
- top seller n products in given date range (product name & quantity)
- top seller n stores in given date range (store name & quantity)
- top seller n brands in given date range (brand & quantity)
- top seller n cities in given date range (city & quantity)

On equality, print all of the rows.

**Input Data Format**

product.csv
- id: identifier of the product
- name: name of the product
- brand: brand of the product

store.csv
- id: identifier of the store
- name: name of the store
- city: city that the store is located in

sales.csv
- product: identifier of the product (id column in product.csv)
- store: identifier of the product (id column in product.csv)
- date: date of sale
- quantity: sales quantity of the specified product in the specified store

**Arguments**

Your script should take following arguments from command line:
- "--min-date": start of the date range. type:str, format:"YYYY-MM-DD", default:"2020-01-01"
- "--max-date": end of the date range. type:str, format:"YYYY-MM-DD", default:"2020-06-30"
- "--top": number of rows in the output. type:int, default:3

Expected command and output:
```
$ python3 solution.py --min-date 2020-02-01 --max-date 2020-06-30 --top 2
-- top seller product --
  name  quantity
 p-103        33
 p-102        24
 p-110        24
-- top seller store --
name  quantity
 s-3        42
 s-2        36
 s-7        36
-- top seller brand --
    brand  quantity
 yoyodyne       100
     acme        65
-- top seller city --
      city  quantity
    gotham       108
 coruscant        78
```
