pens_pack = 5.80
markers_pack = 7.20
cleaner = 1.20

pens_packs_count = int(input())
market_packs_count = int(input())
cleaner_liters = float(input())
discount = int(input())

pen_packs_price = pens_pack * pens_packs_count
marker_packs_price = markers_pack * market_packs_count
cleaner_price = cleaner * cleaner_liters
price_sum = pen_packs_price + marker_packs_price + cleaner_price

price_with_discount = price_sum - (price_sum * (discount /100))

print (price_with_discount)
