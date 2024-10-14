def login():
    gmail = input('Gmail pochtangizni kiriting: ')
    with open('tekshiruv.txt') as f:
        for i in f.read().split('\n'):
            if len(i) != 0:
                i = i.split(',')
                if gmail == i[2]:
                    parol = input('Parolingizni kiriting: ')
                    if parol == i[0]:
                        post_menyu(i[1])
                        return 
                    else:
                        print("Parol notog'ri!")
                        return
        print("Bunday gmail pochta mavjud emas!")

def kirish():
    ism = input('Ismingizni kiriting: ')
    sana = input('Tugilgan sanangizni kiriting: ')
    tekshiruv = False
    while tekshiruv == False:
        gmail = input("O'zingiz uchun gmail poctha yarating (valikarimov@gmail.com): ")
        if '@' not in gmail or '.com' not in gmail:
                print('Bu gmail pochta emas! Qayta urining!')
        else:
            with open('tekshiruv.txt') as f:
                if gmail in f.read():
                    print('Bu gmailni boshqa user ishlatyapti, qayta urining!')
                else:
                    break
    parol = input("O'zingiz uchun parol yarating: ")
    with open('tekshiruv.txt', 'a') as f:
        f.write(f"{parol},{ism},{gmail},{sana}\n")
    with open('post.txt', 'a') as f:
        f.write(f"{ism}:\n")

def post_menyu(name):
    while True:
        choice = input("1. Post yozish\n2. Postlarimni ko\'rish\n3. Boshqaning postlarini ko'rish.\n4. Chiqish\n")
        if choice == '1':
            post_yozish(name)
        elif choice == '2':
            postlarimni_korish(name)
        elif choice == '3':
            postlarni_korish(name)
        elif choice == '4':
            main()
        else:
            print("Notog'ri tanlov, qayta urinib ko'ring!")

def postlarni_korish(name):
    tekshiruv = False
    with open ('post.txt') as f:
        for i in f.read().split('\n'):
            if len(i) > 0:
                i = i.split(':')
                if len(i[1]) != 0:
                    if i[0] != name:
                        print(f'{i[0]} ning yozgan habarlari: {i[1]}\n')
                        tekshiruv = True
        if tekshiruv == False:
            print('Hali hech kim post yozmagan!')
def postlarimni_korish(name):
    with open('post.txt') as f:
        for i in f.read().split('\n'):
            x = i.split(':')
            if x[0] == name:
                if len(x[1]) == 0:
                    print('Hali hechqanday post yozilmagan')
                    return
                else:
                    print(f"Yozilgan habarlar:{x[1]}")
                    return
        print(f"{name} nomli hech qanday post topilmadi")

def post_yozish(name):
    text = ""
    post = ""
    with open('post.txt') as f:
        for i in f.read().split('\n'):
            x = i.split(':')
            if x[0] == name:
                post = input('Postni kiriting: ')
                post += ','
                text += f"{i} {post}\n" 
            else:
                text += i + '\n'
    if len(post) == 0:
        text += f"{name}: {post}\n"
    with open('post.txt', 'w') as f:
        f.write(f"{text}")

    print("Post muvaffaqiyatli qo'shildi!")
def main():
    while True:
        tanlov = input('1. Login\n2. Kirish\n3. Chiqish\n')
        if tanlov == '1':
            login()
        elif tanlov == '2':
            kirish()
        elif tanlov == '3':
                print('Dastur tugadi!')
                exit()
        else:
            print("Notog'ri tanlov, qayta urining!")
main()