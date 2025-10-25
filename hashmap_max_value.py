def main():
    my_dict = {'a': 10, 'b': 25, 'c': 15, 'd': 30}

    max_value = max(my_dict.values())
    keys_with_max_value = [k for k, v in my_dict.items() if v == max_value]

    print(f"Max value: {max_value}")  # Output: 30
    print(f"Keys with max value: {keys_with_max_value}")  # Output: ['d']

    # If values are objects or tuples
    my_dict = {
        'item1': {'price': 100, 'quantity': 5},
        'item2': {'price': 200, 'quantity': 3},
        'item3': {'price': 150, 'quantity': 8}
    }

    # Find key with maximum price
    key_with_max_price = max(my_dict, key=lambda k: my_dict[k]['price'])
    print(f"Key with max price: {key_with_max_price}")  # Output: item2

    # Find key with maximum quantity
    key_with_max_quantity = max(my_dict, key=lambda k: my_dict[k]['quantity'])
    print(f"Key with max quantity: {key_with_max_quantity}")  # Output: item3

if __name__ == "__main__":
    main()