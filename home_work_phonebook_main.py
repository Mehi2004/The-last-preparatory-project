from home_work_phonebook import Phone
name_true1 = False
char = []
print("Hello ! Welcom to Mehrshad's phonebook . please enter the following information.")
contact = Phone(name=input(f"enter your name : "), family=input("enter your family : "), telphon=input("enter your telphon number :"), mobile_1=input("entre your 1st mobile number : "), mobile_2=input(
    "enter your 2nd mobile number : "), mobile_3=input("enter your 3th mobile number : "), address=input("enter your address : "), postal_code=input("enter your postal code : "), gender=input("entre your gender : "))

# check name
while contact.name() == False:
    contact.Name = input(f"enter your name (just a,z or A,Z or " "): ")

# check family
while contact.family() == False:
    contact.Family = input(f"enter your family (just a,z or A,Z or " "): ")

# check telphon just number
while contact.telphon_just_num() == False:
    contact.Telphon = input(
        f"{contact.Name},enter your telphon (just number): ")

# check telphon len number
if contact.telphon_len() == 1:
    contact.Telphon = "021"+(contact.Telphon)
elif contact.telphon_len() == 2:
    contact.Telphon = "0"+(contact.Telphon)
elif contact.telphon_len() == 3:
    while contact.telphon_len() == 3:
        contact.Telphon = input(
            f"{contact.Name},enter your telphon (8 or 10 or 11 numbers): ")

# check mobile 1 just number
while contact.mobile_just_num() == False:
    contact.Mobile_1 = input(
        f"{contact.Name},enter your 1st mobile (just number, you must enter  at least one number ): ")

# check len mobile 1 number
if contact.mobile_1_need() == 1:
    char = list(contact.Mobile_1)
    char[0] = '0'
    del char[1]
    contact.Mobile_1 = ''.join(char)
elif contact.mobile_1_need() == 2:
    char = list(contact.Mobile_1)
    char[0] = '0'
    char[1] = '9'
    contact.Mobile_1 = ''.join(char)
else:
    while contact.mobile_1_need() == 3:
        contact.Mobile_1 = input(
            f"{contact.Name},enter your mobile (with 98 or 0 exampel : 98911111111 or 09111111111): ")

# check mobile 2 just number
while contact.mobile_2_just_num_or_not() == False:
    contact.Mobile_2 = input(
        f"{contact.Name},enter your 2nd mobile (just number, or not thing ): ")
# check len mobile 2 number
if contact.mobile_2_need() == 0:
    contact.Mobile_2 = ""
elif contact.mobile_2_need() == 2:
    char = list(contact.Mobile_2)
    char[0] = '0'
    char[1] = '9'
    contact.Mobile_2 = ''.join(char)
elif contact.mobile_2_need() == 1:
    char = list(contact.Mobile_2)
    char[0] = '0'
    del char[1]
    contact.Mobile_2 = ''.join(char)
else:
    while contact.mobile_2_need() == 3:
        contact.Mobile_2 = input(
            f"{contact.Name},enter your 2en mobile (with 98 or 0): ")

# check len mobile 3 number
while contact.mobile_3_just_num_or_not() == False:
    contact.Mobile_3 = input(
        f"{contact.Name},enter your 3th mobile (just number, or not thing ): ")

# check len mobile 3 number
if contact.mobile_3_need() == 0:
    contact.Mobile_3 = ""
elif contact.mobile_3_need() == 2:
    char = list(contact.Mobile_3)
    char[0] = '0'
    char[1] = '9'
    contact.Mobile_3 = ''.join(char)
elif contact.mobile_3_need() == 1:
    char = list(contact.Mobile_3)
    char[0] = '0'
    del char[1]
    contact.Mobile_3 = ''.join(char)
else:
    while contact.mobile_3_need() == 3:
        contact.Mobile_3 = input(
            f"{contact.Name},enter your 3th mobile (with 98 or 0): ")

# check adderss
while contact.addres_check() == False:
    contact.Address = input(
        f"{contact.Name},enter your address (just a,z or A,Z or " " or ',' or numbers): ")

# check postal code just number
while contact.postal_code_number_check() == False:
    contact.postal_code = input(
        f"{contact.Name},enter your post code just number : ")

# check len postal code
while contact.postal_code_digit() == False:
    contact.postal_code = input(
        f"{contact.Name},enter your post code (its must have 10 digit) : ")

# check gender
if contact.gender_check() == 1:
    contact.gender = 'm'
elif contact.gender_check() == 2:
    contact.gender = 'f'
else:
    while contact.gender_check() == 3:
        contact.gender = input(
            f"{contact.Name}, enter your gender (m or f) : ")


file_1 = open("phonebook1.csv", mode='a')
print({contact.Name}, {contact.Family}, {contact.Telphon}, {contact.Mobile_1}, {contact.Mobile_2}, {
      contact.Mobile_3}, {contact.Address}, {contact.postal_code}, {contact.gender}, file=file_1)
file_1.close()
