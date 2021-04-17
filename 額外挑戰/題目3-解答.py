def count_products(data):
    products = {}
    for d in data:
        name, count = d.split(' ')
        count = int(count)
        if name in products:
            products[name] += count
        else:
            products[name] = count
    return products