def divisor(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 1:
            divisors.append(i)
    return divisors


def run():
    num = int(input('Please, write a number: '))
    print(divisor(num))
    print('The program is finished')


if __name__ == "__main__":
    run()
