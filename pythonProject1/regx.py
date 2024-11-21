import re
def validate_register_number(Register_num):
    pattern=r'^FUT\d{5}$'
    if re.match(pattern,Register_num):
        return True
    else:
       return False
Register_num = input ("enter")

if validate_register_number(Register_num):
     print("valid register number")
else:
     print("invalid register")

