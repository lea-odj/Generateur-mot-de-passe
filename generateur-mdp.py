import secrets
import string 
import random 

def password():
    passwd = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits), 
        secrets.choice(string.punctuation)]

    for i in range (10):
        random_choice = secrets.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
        passwd.append(random_choice)

    random.SystemRandom().shuffle(passwd)
    final_password = ''.join(passwd)
    return final_password

print(password())