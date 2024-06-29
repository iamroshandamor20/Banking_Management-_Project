# Global Variable Storing Data of users
users ={
    "user1" : {
        "id" : "7414728598",
        "pass" : "181912",
        "acno" : "01975876944",
        "ifsc" : "HDRPD8000",
        "aadhar": "741472859846",
        "pan" : "HDRPD9091R",
        "name" : "Arti Damor",
        "age" : "19",
        "farthername" : "Dulesing Damor",
        "mothername" : "Baijayanti Damor",
        "address": "16, kaushlyapuri, Indore",
        "bankbalance" : "₹12244",
        "transactions" : {
            "18/10/2024" : {"c": "₹550"},
            "17/10/2023" : {"d": "₹1550"},
            "16/10/2022" : {"w": "₹2000"},
            "15/10/2024" : {"c": "₹550"},
            "14/10/2023" : {"d": "₹1550"},
            "13/10/2022" : {"w": "₹2000"},
            "12/10/2024" : {"c": "₹550"},
            "11/10/2023" : {"d": "₹1550"},
            "10/10/2022" : {"w": "₹2000"}
        },
    }
}


# Function to check whether user and its password is correct
def login(logid, logpass):
    if int(users.get("user1",{}).get("id")) == logid:
        if int(users.get("user1",{}).get("pass")) == logpass:
            return True
    return False

# Function to check Names Valdiation
def namecheck(name):
    length = len(name)
    Result = False
    for c in name:
        if not (c.isalpha() or c.isdigit() or c == ' '):
            return False
        if c.isdigit():
            return False
        if length < 2:
            return False
    Result = True
    return True

# Function to check Options Validation
def optioncheck(option):
    if option == 1 and option == 2 and option == 3:
        return True
    else:
        return False
    
 # Function to check Empty Validation 
def emptycheck(para):
    lenght = len(para)
    if lenght<1:
        return False
    return True

# Function to check DOB Validation
def dobcheck(dob):
    lenght = len(dob)
    if lenght <=10 and lenght>=8:
        return True
    return False

# Function to check Mobile No. Validation
def mobilecheck(mobile):
    lenght = len(mobile)
    if lenght == 10:
        return True
    return False

# Function to check Email Validation
def emailcheck(email):
    if '@' in email and '.' in email:
        username, domain = email.split('@')
        if domain and '.' in domain:
            return True
    return False


# Function to get all details of Existing User
def useraccount(logid):
    
    loopcondition = True
    while loopcondition:
        print()
        print("\t Type (1) to Check Bank Balance \t Type (2) for Account Statement \t Type (3) to Money Transfer ")
        print("\t Type (4) to Buy Insurance Policy \t Type (5) to Avail Loan \t Type (6) to Log Out Your Account")
        print()
        bankingoption = int(input("\t\t"))

        if bankingoption == 1:
            print("\t\t ** Your Account Balance **")
            print(users.get("user1",{}).get("bankbalance"))
            
        elif bankingoption == 2:
            print("\t\t ** Your Account Statment **")
            print(users.get("user1",{}).get("transactions"))

        elif bankingoption == 3:
                print("Transfer Your Money")

        elif bankingoption == 4:
                print("\t\t **Insurance **")

        elif bankingoption == 5:
                print("\t\t ** Avail Loan **")

        elif bankingoption == 6:
                print("Thank you For Using Online Banking Service")
                loopcondition = False
        else:
                print("Wrong Option Selected")


# Main Function To call and Input Values of user
def main():
    print()
    print("\t \t\t     *** Welcome ***")
    print("\t\t\t**** Bank Of Jhuniya ****")
    print()

    mainchoice = int(input("For login Type (1) \t For Opening New Account Type (2) \t For Exit Type Anything else\n"))

#Login Details Here
    if mainchoice == 1:
        print("\t\t\t ** Login **")
        logid = int(input("Enter Your Bank ID: \t"))
        logpass = int(input("Enter Your Pin Here: \t"))
        logresult = login(logid, logpass)
        print(logresult)
        if logresult is True:
            print("\t\t** Login Successful **")
            useraccount(logid)
        else:
            print("Invalid ID or Password")

#Account Opening Here
    elif mainchoice == 2:
        print("\t\t\t ** New Account **")
        print()
        name = input("Enter Your Name (Same As Your ID Proof): \t")
        dob = input("Enter Date of Birth (DDMMYYYY Format): \t")
        gender = int(input("Type (1) for Male \t Type (2) for Female \t Type (3) for Third Gender: \t"))
        maritalstatus = int(input("Type (1) for Married \t Type (2) for Unmarried \t Type (3) for Other: \t"))
        dependers = input("Number of Dependers: \t")
        nameof = int(input("Type (1) for Father \t Type (2) for Mother \t Type (3) for Spouse: \t"))
        if nameof == 1:
            fathername = input("Enter Your Father's Name: \t")
            mothername = ""
            spousename = ""
        elif nameof == 2:
            fathername = ""
            mothername = input("Enter Your Mother's Name: \t")
            spousename = ""
        elif nameof == 3:
            fathername = ""
            mothername = ""
            spousename = input("Enter Your Spouse's Name: \t")
        else:
            print("Wrong Option Selected")
            return

        guardianname = input("Enter Your Guardian's Name: \t")
        relation = input("Enter your Relation With Guardian: \t")
        citizenship = int(input("Type (1) for Indian \t Type (2) for Non Resident Indian \t Type (3) for Others: \t"))
        print()
        occupation = input("Enter Your Occupation: \t")
        income = input("Enter Your Annual Income: \t")
        religion = input("Enter Your Religion: \t")
        education = int(input("Type (1) for Below 12th \t Type (2) for Graduated \t Type (3) for None: \t"))
        print()
        mobile = input("Enter Your Mobile Number: \t")
        email = input("Enter Your Personal Email: \t")
#calling all Function to validate inputs
        result1 = namecheck(name)
        result2 = namecheck(fathername)
        result3 = namecheck(mothername)
        result4 = namecheck(spousename)
        result5 = namecheck(guardianname)
        result6 = optioncheck(gender)
        result7 = optioncheck(maritalstatus)
        result8 = optioncheck(education)
        result9 = optioncheck(citizenship)
        result10 = emptycheck(dependers)
        result11 = emptycheck(relation)
        result12 = emptycheck(occupation)
        result13 = emptycheck(income)
        result14 = emptycheck(religion)
        result15 = dobcheck(dob)
        result16 = mobilecheck(mobile)
        result17 = emailcheck(email)

        if (result1 and result2 and result3 and result4 and result5 and result6 and result7 and result8 and result9 and result10 and result11 and result12 and result13 and result14 and result15 and result16 and result17) is True:
            print("Account Opened successfully")
            print("Soon You will get Massege with Password and Id")
        else:
            print()
            print()
            print("You are not Eligible or Entered Wrong Details. Please Try Again!")
        
            

    else:
        print("You Are Out or Wrong Option Selected")

# Calling Main Function
main()
