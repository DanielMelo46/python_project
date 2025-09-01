# messy data string
data = "transaction_id:001, customer_name: Alice, item=Laptop, price: $999; transaction_id=002, customer_name: Bob, item - Smartphone, price= $599; transaction_id:003, item=Tablet, price:299, discount-10%; transaction_id=004, customer_name=Charlie, item: Headphones, discount=5%"

# expected output
[
    {
        'transaction_id': '001',
        'customer_name': 'Alice',
        'item': 'Laptop',
        'price': '$999',
        'discount': None
    },
    {
        'transaction_id': '002',
        'customer_name': 'Bob',
        'item': 'Smartphone',
        'price': '$599',
        'discount': None
    },
    {
        'transaction_id': '003',
        'customer_name': None,
        'item': 'Tablet',
        'price': '299',
        'discount': '10%'
    },
    {
        'transaction_id': '004',
        'customer_name': 'Charlie',
        'item': 'Headphones',
        'price': None,
        'discount': '5%'
    }
]