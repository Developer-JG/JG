def calculate_def(object_number, n):
    print(object_number)
    for i in range(1,object_number):

        for j in range(1,object_number):

            if i ** n + j ** n == object_number ** n:
                print("{0} ** {1} + {2} ** {1} = {3} ** {1}".format(i, n, j, object_number))
                input("program is stopped ({0})".format(object_number))

def main():
    print("Fermat's Last Theorem\n")

    n = 3

    object_number = 3

    while True:
        calculate_def(object_number, n)

        object_number += 1

if __name__ == "__main__":
    main()