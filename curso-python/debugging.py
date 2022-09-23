def divisor(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input('Please, write a number: '))
        if num < 0:
            raise ValueError

        print(divisor(num))
        print('The program is finished')
    except ValueError:
        print('You must give a positive number')


if __name__ == "__main__":
    run()
