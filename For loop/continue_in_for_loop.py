for i in range(1,11):
    if i % 2 != 0:

        print(i)

#continue
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)

# while
n = 0

while n < 10:
    print(n)
    n+= 1


products = ['iphone', 'ipad', 'macbook']
regions = ['USA', 'China', 'India']
revenue = [20, 23, 45, 18, 17, 12, 12, 9, 5]

i=0

for product in products:
    for region in regions:
        rev = revenue[i]
        i = i + 1
        print(f"{product} {region} revenue:",rev)













