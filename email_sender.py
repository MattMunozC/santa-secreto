from email.message import EmailMessage
import smtplib
import random
import json
from pprint import pprint
EMAIL_ADDRESS="la.posada.libreria@gmail.com"
EMAIL_PASSWORD="wawduionfpuycrxs"
TEST_RECIEVER="soulxstar720@gmail.com"
def send_email(EMAIL_ADDRESS,EMAIL_PASSWORD,msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    server.send_message(msg)
    server.close()    
def set_msg(EMAIL_ADDRESS,EMAIL_RECIEVER,CONTENT, CONTENT_TYPE="standard"):
    msg=EmailMessage()
    msg['Subject']='¡Feliz Navidad! Descubre quien te ha tocado de amigo secreto'
    msg['From']=EMAIL_ADDRESS
    msg['To']=EMAIL_RECIEVER
    msg.set_content('')
    switch={"standard":msg.set_content(CONTENT),"html_body":msg.add_alternative(CONTENT,subtype='html')}
    switch[CONTENT_TYPE]
    return msg
def shuffle(values_list):
    shuffled_values=dict()
    for CURRENT_VALUE in values_list:
        while True:
            SELECTED_PAIR=random.randint(0,len(values_list)-1)
            if values_list[SELECTED_PAIR] not in [*shuffled_values.values()] and values_list[SELECTED_PAIR]!=CURRENT_VALUE:
                shuffled_values[CURRENT_VALUE]=values_list[SELECTED_PAIR]
                break
    return shuffled_values

with open("contact_info.json","r",encoding='utf-8') as info:
    json_info=json.loads(info.read())

with open("msg_view.html","r",encoding='utf-8') as msg_file:
    content=msg_file.read()

secret_santa=shuffle(json_info["participantes"])
for i in secret_santa:
    email=content.format(i,json_info["direcciones"][i])
    msg=set_msg(EMAIL_ADDRESS,json_info["correos"][secret_santa[i]],email,"html_body")
    send_email(EMAIL_ADDRESS,EMAIL_PASSWORD,msg)
    print(f"participantes: {secret_santa[i]} le toco: {i}")


##msg.add_alternative(",subtype='html')
#msg=set_msg(EMAIL_ADDRESS,TEST_RECIEVER,"test message")
#send_email(EMAIL_ADDRESS,EMAIL_PASSWORD,msg)

