# at least 8 char long
# contain any sort letters, numbers $%#@

import re
def run(string):
    #regex = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$")
    regex = re.compile(r"[A-Za-z0-9@#%$]{8,}")
    if (regex.search(string)==None):
    
        print("enter atleast 8 char and a specail key")
    else:
        print('correct password')

if __name__ =='__main__':
    string = "Malcolm1ibrahim@#"

    run(string)


regex = (r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")   

def check(email):
       if (re.fullmatch(regex, email)):
        print("correct email")
       else:
        print('incorrect email')

if __name__ == '__main__':
   email = 'malcolm123@gmail.com'
   check(email)
   email = 'mal.com'
   check(email)

