# import re
#
# text="my name is suhail"
# x=re.search(*"^my",*"suhail$",text)
# if x:
#     print("true")
# else:
#     print


import re
def validate_reg_number(register_num):
    pattern=r'^[FUT]\d{5}$'
    if re.match(pattern,register_num):
        return True
    else:
        return False

register_num= input("enter the register number")
if validate_reg_number(register_num):
    print("valid register number")
else:
    print("invalid register")