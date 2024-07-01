import datetime
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
#print["id"]
def login(logid, logpass):
    if int(users.get("user1",{}).get("id")) == logid:
        print("User Is Valid")
        if int(users.get("user1",{}).get("pass")) == logpass:
            print("pass is valid")
            return True
    print("note valid")
    return False

current_time = datetime.datetime.now()
print(current_time.day,current_time.month,current_time.year)
logresult =login(logid=7414728598, logpass=181912)
print(logresult)