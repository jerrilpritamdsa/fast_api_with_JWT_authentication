from passlib.context import CryptContext

# this class takes in the password as string 
# and returns a hashed value of that string 
# using the CryptContext from passlib module
# it is also used to verify the passwords and one of them can be hashed password from db 

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated = "auto") 
    

class Hash():
    
    def bcrypt(password:str):
        
        return pwd_cxt.hash(password)
    
    
    def verify(hashed_password, plain_password):
        
        boolean = pwd_cxt.verify(plain_password,hashed_password)
        print(boolean)
        return boolean