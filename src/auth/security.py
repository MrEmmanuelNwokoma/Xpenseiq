import bcrypt

def hash(plain_string: str) -> str:
    """Function for hashing"""   
    hashed_password =  bcrypt.hashpw(plain_string.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    return hashed_password



def verify(plain_string: str, hashed_string: str):
    """function to verifiy plain string"""
    return bcrypt.checkpw(plain_string.encode("utf-8"), hashed_string.encode("utf-8"))