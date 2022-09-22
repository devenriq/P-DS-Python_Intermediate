def run():
    # my_list = {i: i**3 for i in range(1, 100) if i % 3 != 0}
    # print(my_list)

    my_list = {i: i**(1/2) for i in range(1, 1001)}
    print(my_list)


if __name__ == '__main__':
    run()
