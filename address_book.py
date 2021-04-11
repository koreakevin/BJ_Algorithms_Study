class contact:
    def __init__(self, name, phone_number, sex):
        self.name = name
        self.phone_number = phone_number
        self.sex = sex

result = []
while True:
    name = input("이름을 입력하시오 : ")
    if name == "그만":
        for a in result:
            print("이름은" + a.name + "," + "전화번호는" + a.phone_number + "," + "성별은" + a.sex)

        break
    phone_number = input("전화번호를 입력하세요 : ")
    sex = input("성별을 입력하세요(male이나 female로 작성해주세요) : ")

    # if sex == "male" or sex == "female" :

    if sex != "male" and  sex != "female" :
        sex = "unknown"

    # print("이름은" + name + ","+ "전화번호는" + phone_number + "," + "성별은" + sex)

    addressbook = contact(name, phone_number, sex)
    result.append(addressbook)
    for a in result:
        print("이름은" + a.name + "," + "전화번호는" + a.phone_number + "," + "성별은" + a.sex)
