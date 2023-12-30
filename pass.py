password=input('enter a pass:- ')
validate={'upper':False,'lower':False,'number':False,'char':False}
if len(password)>=8:
    for char in password:
        if 'A' <= char <= 'Z':
            validate['upper']=True
        elif 'a' <=  char <= 'z':
            validate['lower']=True
        elif '0' <= char <= '9':
            validate['num']=True
        elif char != ' ':
            validate['char']=True
    if {validate['upper'] and validate['lower'] and validate['char'] and validate['num']}:
        print('password is valid')
else:
    print('password is invalid')