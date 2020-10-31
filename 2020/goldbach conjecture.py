def stop_def():
    while True:
        input("program is stopped")

def prime_number_def(prime_number, object_number):
    for i in range(2, object_number):
        prime_number_plag = 0

        for j in range(2, i):
            if i % j == 0:
                prime_number_plag = 1

        if prime_number_plag == 0:
            prime_number.append(i)

def calculate_def(prime_number_list, object_number):
    break_plag = 0
    for i in range(0, len(prime_number_list)):
        first_prime_number = prime_number_list[i]

        for j in range(0, len(prime_number_list)):
            second_prime_number = prime_number_list[j]

            if first_prime_number + second_prime_number == object_number:
                print("{0} = {1} + {2}".format(object_number, first_prime_number, second_prime_number))
                break_plag =+ 1

    if break_plag == 0:
        stop_def()

def main():
    print("Goldbach_Conjecture\n")

    original_object_number = 2

    while True:
        object_number = original_object_number * 2

        prime_number_list = []
        prime_number_def(prime_number_list, object_number)

        calculate_def(prime_number_list, object_number)

        original_object_number += 1
        print()

if __name__ == "__main__":
    main()