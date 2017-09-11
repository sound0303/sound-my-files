#! /usr/bin/python3
import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)                                                                  
s.starttls() 
s.login("www.soundaryapowndurai@gmail.com","hi hello")
message ="Message_you_need_send"
s.sendmail("www.soundaryapowndurai@gamil.com","www.soundaryapowndurai@gmail.com")
s.quit()









