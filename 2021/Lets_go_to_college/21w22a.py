print("\n[프로젝트] 대학가자\n\n")

with open('data_package.csv') as file:
    csv_data = []
    for line in file.readlines():
        csv_data.append(line.split(','))

class select:
    def __init__(self, value_1, value_2, value_3):
        self.value_1 = value_1
        self.value_2 = value_2
        self.value_3 = value_3

def main():
    while True:
        print("검색어를 입력하세요.")
        system_input = input(" : ")
        system_input_result = system_input.split()

        input_log = select(0, 0, 0)

        plag = 0
        while plag < 3:
            i = 0
            if plag == 0 or plag == 1 or plag == 2:
                while True:
                    i += 1
                    try:
                        for j in range(len(system_input_result)):
                            if system_input_result[j] == csv_data[i][plag]:
                                if plag == 0:
                                    input_log.value_1 = i
                                elif plag == 1 and input_log.value_1 != 0:
                                    input_log.value_2 = i
                                elif plag == 2:
                                    input_log.value_3 = i
                    except:
                        break
                    plag += 1


if __name__ == "__main__":
    main()