def divisor(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input('Please, write a number: ')
    assert num.isnumeric(), 'You must enter a number'
    print(divisor(int(num)))
    print('The program is finished')


if __name__ == "__main__":
    run()
