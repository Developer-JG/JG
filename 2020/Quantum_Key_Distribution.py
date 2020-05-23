from random import randint

print("Quantum Key Distribution project / 양자 키 분배 프로젝트\n")

bit = 72


Alice_random_bit = []
Alice_random_sending_basis = []
Photon_polarization_Alice_sends = []

def Alice (bit, Alice_random_bit, Alice_random_sending_basis, Photon_polarization_Alice_sends):
    print("\n\n\n[Alice / 통신 과정의 첫 번째 당사자]\n")
    print("Alice's random bit / 앨리스가 생성한 비트 :")
    for i in range(bit):
        random_bit = randint(0, 1)
        Alice_random_bit.append(random_bit)
    print(Alice_random_bit)

    print("\nAlice's random sending basis / 앨리스가 사용하는 전송용 편광필터 :")
    for i in range(bit):
        basis = randint(0,1)
        if basis == 0:
            basis = '+'
        elif basis == 1:
            basis = 'x'
        Alice_random_sending_basis.append(basis)
    print(Alice_random_sending_basis)

    print("\nPhoton polarization Alice sends / 앨리스가 전송하는 광자 편광신호 :")
    for i in range(bit):
        if Alice_random_bit[i] == 0:
            if Alice_random_sending_basis[i] == '+':
                Photon_polarization_Alice_sends.append('Top')
            elif Alice_random_sending_basis[i] == 'x':
                Photon_polarization_Alice_sends.append('Top_right')
        elif Alice_random_bit[i] == 1:
            if Alice_random_sending_basis[i] == '+':
                Photon_polarization_Alice_sends.append('Right')
            elif Alice_random_sending_basis[i] == 'x':
                Photon_polarization_Alice_sends.append('Bottom_Right')
    print(Photon_polarization_Alice_sends)


Eve_random_measuring_basis = []
Polarization_Eve_measures_and_sends = []

def Eve(Eve_random_measuring_basis, Polarization_Eve_measures_and_sends):
    print("\n\n[Eve / 엿듣는 사람, 소극적 공격자를 뜻한다]\n")
    print("Eve's random measuring basis / 이브가 임의로 선택한 측정필터 :")
    for i in range(bit):
        basis = randint(0, 1)
        if basis == 0:
            basis = '+'
        elif basis == 1:
            basis = 'x'
        Eve_random_measuring_basis.append(basis)
    print(Eve_random_measuring_basis)

    print("\nPolarization Eve measures and sends / 이브가 측정하고 재전송하는 편광신호 :")
    for i in range(bit):
        if Eve_random_measuring_basis[i] == '+':
            random_bit = randint(0, 1)
            if random_bit == 0:
                Polarization_Eve_measures_and_sends.append('Top')
            elif random_bit == 1:
                Polarization_Eve_measures_and_sends.append('Top_right')
        elif Eve_random_measuring_basis[i] == 'x':
            random_bit = randint(0, 1)
            if random_bit == 0:
                Polarization_Eve_measures_and_sends.append('Right')
            elif random_bit == 1:
                Polarization_Eve_measures_and_sends.append('Bottom_Right')
    print(Polarization_Eve_measures_and_sends)

    Photon_polarization_Alice_sends = Polarization_Eve_measures_and_sends


Bobs_random_measuring_basis = []
Photon_polarization_Bob_measures = []

def Bob (bit, Bobs_random_measuring_basis, Photon_polarization_Bob_measures):
    print("\n\n[Bob / 통신 과정의 두 번째 당사자]\n")
    print("Bob's random measuring basis / 밥이 임의로 선택한 측정필터 :")
    for i in range(bit):
        basis = randint(0, 1)
        if basis == 0:
            basis = '+'
        elif basis == 1:
            basis = 'x'
        Bobs_random_measuring_basis.append(basis)
    print(Bobs_random_measuring_basis)

    print("\nPhoton polarization Bob measures / 밥이 측정한 편광 상태 :")
    for i in range(bit):
        if Bobs_random_measuring_basis[i] == '+':
            random_bit = randint(0, 1)
            if random_bit == 0:
                Photon_polarization_Bob_measures.append('Top')
            elif random_bit == 1:
                Photon_polarization_Bob_measures.append('Top_right')
        elif Bobs_random_measuring_basis[i] == 'x':
            random_bit  = randint(0, 1)
            if random_bit == 0:
                Photon_polarization_Bob_measures.append('Right')
            elif random_bit == 1:
                Photon_polarization_Bob_measures.append('Bottom_Right')
    print(Photon_polarization_Bob_measures)


Photon_polarization = []
Shared_secret_key = []
Shared_secret_key_num = []

def Public_discussion_of_basis(Photon_polarization_Alice_sends, Photon_polarization_Bob_measures):
    print("\n\n[PUBLIC DISCUSSION OF BASIS / 전송 패드와 측정패드가 일치하는지 여부 검증]\n\n")
    for i in range(bit):
        if Photon_polarization_Alice_sends[i] == Photon_polarization_Bob_measures[i]:
            Photon_polarization.append(Photon_polarization_Alice_sends[i])
            Shared_secret_key_num.append(i)

    for i in range(len(Photon_polarization)):
        if Photon_polarization[i] == 'Top' or Photon_polarization[i] == 'Top_right':
            Shared_secret_key.append('0')
        elif Photon_polarization[i] == 'Right' or Photon_polarization[i] == 'Bottom_Right':
            Shared_secret_key.append('1')


def main():
    input("Enter to start quantum key distribution / 양자 키 분배를 시작하려면 엔터")
    eavesdropper = input("\neavesdropper / 도청자 ([yes](0), no(1)) : ")

    Alice (bit, Alice_random_bit, Alice_random_sending_basis, Photon_polarization_Alice_sends)

    if eavesdropper != '1':
        Eve (Eve_random_measuring_basis, Polarization_Eve_measures_and_sends)

    Bob (bit, Bobs_random_measuring_basis, Photon_polarization_Bob_measures)
    Public_discussion_of_basis (Photon_polarization_Alice_sends, Photon_polarization_Bob_measures)

    print("Shared secret key / 최종적으로 생성되는 비밀키\n")
    key_02 = (''.join(Shared_secret_key))
    print("binary number / 2진수 : {0}".format(key_02))
    key_02 = '0b' + key_02
    key_10 = int(key_02, 2)
    print("decimal number / 10진수 : {0}".format(key_10))

    print("\n\nErrors in key / 생성된 비밀키에 대한 무결성 검증\n")
    num, eavesdropper = 0, 0
    for i in Shared_secret_key_num:
        print("{0}th Alice's random bit / {0}번째로 앨리스가 생성한 비트 : {1}".format(i, Alice_random_bit[i]))
        print("{0}th Shared secret key / {0}번째 최종적으로 생성되는 비밀키 : {1}\n".format(num + 1, Shared_secret_key[num]))
        if int(Alice_random_bit[i]) != int(Shared_secret_key[num]):
            eavesdropper = eavesdropper + 1
        num = num + 1

    if eavesdropper != 0:
        print("\nEavesdropper has been found / 도청자가 발견됨")
    else:
        print("\nEavesdropper has been not found / 도청자가 발견되지 않음")


if __name__ == "__main__":
    main()
