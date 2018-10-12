import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("krishgokul034@gmail.com", "gokul9448536973") 

# message to be sent 
message = "hi bhargav"
  
# sending the mail 
s.sendmail("krishgokul034@gmail.com", "bhargavsp11@gmail.com", message) 
  
# terminating the session 
s.quit() 