def run():
    my_list = [1, "hello", True, 4.32]
    my_dic = {"first-name": "Enrique", "last-name": "Palomino"}

    super_list = [
        {"first-name": "Enrique", "last-name": "Palomino"},
        {"first-name": "Diana", "last-name": "Palomares"},
        {"first-name": "alguien", "last-name": "algo"},
        {"first-name": "Rosa", "last-name": "Torres"},
        {"first-name": "Ramiro", "last-name": "Ramirez"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "integer_nums": [-1, -2, 19, 3, 5, 0, 2],
        "floating_nums": [1.13, 231.412, 2.35, 231.34]
    }

    for key, value in super_dict.items():
        print(key, '-', value)

    for values in super_list:
        for key, value in values.items():
            print(key, '-', value)


if __name__ == '__main__':
    run()
