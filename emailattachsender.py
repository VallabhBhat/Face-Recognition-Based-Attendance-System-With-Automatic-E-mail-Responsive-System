import smtplib
Sender_email = "pythondammy123@gmail.com"
Password = input(str("Please enter your password : "))
message = "Hey you were present for the class today"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(Sender_email,Password)
print("Login Successful")
server.sendmail(Sender_email,Rec_email, message)
print("Email has been sent to", Rec_email)