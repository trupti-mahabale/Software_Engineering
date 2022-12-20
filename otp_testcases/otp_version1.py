import random  #random mmdule to get random integers to create OTp
import senders_data #email and password of sender from another file
import smtplib  #simple message transfer protocol#library to send email to users email_address

n=(int(input("Enter your range of otp ")))  #getting the input for length of otp

#function to generate otp 
def generate_otp(n):
    OTP=""
    for i in range(n):
        OTP+=str(random.randint(0,9))#OTP will append any random digits[index] 
    return (OTP)


#create gmails server
server =smtplib.SMTP('smtp.gmail.com',587)

#get senders email from another file
Senders_email = senders_data.email
Senders_password= senders_data.password

#function to login and add tls to the server
def login_into_sendersemail():
    server.starttls()   #transfered layer security
    server.login(Senders_email,password=Senders_password)  #Login into sender mail

receivers_name=input("Enter receivers name ") 
receivers_email=input("Enter receivers email ")



#function to send email
def send_email(): 

    login_into_sendersemail()
    #generate_otp function called
    otp_var=generate_otp(n)
    msg=("Hello "+ receivers_name +"\n"+ str(otp_var)+" is your OTP ")
    print(msg)
    server.sendmail(Senders_email,receivers_email,msg)
    server.quit() #to quit the server
    print("email has been sent!")

#send emailfunction called
send_email()