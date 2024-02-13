import imaplib,email
import os

import re
from playsound import playsound
from gtts import gTTS

password = "elzpxssdtvxyboea"
usr = "vcontrolproject@gmail.com"
file = "new"
i = "5"
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
imap_url = 'imap.gmail.com'
conn = imaplib.IMAP4_SSL(imap_url)

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)

def texttospeech(text, filename):
    filename = filename + '.mp3'
    flag = True
    while flag:
        try:
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(filename)
            flag = False
        except:
            print('Trying again')
    playsound(filename)
    os.remove(filename)
    return

def readmail():
    global s, i
    conn.login(usr,password)
    conn.select("INBOX")
    result, data = conn.uid('search',None,"ALL")
    inbox_item_list = data[0].split()
    inbox_item_list.reverse()
    mail_count = 0
    to_read_list = list()
    for item in inbox_item_list:
        result, email_data = conn.uid('fetch',item, '(RFC822)')
        
        raw_email = email_data[0][1].decode()
        message = email.message_from_string(raw_email)
        To = message['To']
        From = message['From']
        Subject = message['Subject']
        Msg_id = message['Message-ID']
        texttospeech("Email number " + str(mail_count + 1) + "    .The mail is from " + From + " to " + To + "  . The subject of the mail is " + Subject, file + i)
        i = i + str(1)
        print('message id= ', Msg_id)
        print('From :', From)
        print('To :', To)
        print('Subject :', Subject)
        print("\n")
        to_read_list.append(Msg_id)
        mail_count = mail_count + 1

    flag = True
    while flag :
        n = 0
        flag1 = True
        while flag1:
            texttospeech("Enter the email number of mail you want to read.",file + i)
            i = i + str(1)
            n = input()
            print(n)
            texttospeech("You meant " + str(n) + ". Say yes or no.", file + i)
            i = i + str(1)
            say = input()
            say = say.lower()
            if say == 'yes':
                flag1 = False
        n = int(n)
        msgid = to_read_list[n - 1]
        print("message id is =", msgid)
        typ, data = conn.search(None, '(HEADER Message-ID "%s")' % msgid)
        data = data[0]
        result, email_data = conn.fetch(data, '(RFC822)')
        raw_email = email_data[0][1].decode()
        message = email.message_from_string(raw_email)
        To = message['To']
        From = message['From']
        Subject = message['Subject']
        Msg_id = message['Message-ID']
        print('From :', From)
        print('To :', To)
        print('Subject :', Subject)
        texttospeech("The mail is from " + From + " to " + To + "  . The subject of the mail is " + Subject, file + i)
        i = i + str(1)
        Body = get_body(message)
        Body = Body.decode()
        Body = re.sub('<.*?>', '', Body)
        Body = os.linesep.join([s for s in Body.splitlines() if s])
        if Body != '':
            texttospeech(Body, file + i)
            i = i + str(1)
        else:
            texttospeech("Body is empty.", file + i)
            i = i + str(1)
        print("attach")


def readmail_mr():
    global s, i
    conn.login(usr,password)
    conn.select("INBOX")
    result, data = conn.uid('search',None,"ALL")
    inbox_item_list = data[0].split()
    inbox_item_list.reverse()
    mail_count = 0
    to_read_list = list()
    for item in inbox_item_list:
        result, email_data = conn.uid('fetch',item, '(RFC822)')
        
        raw_email = email_data[0][1].decode()
        message = email.message_from_string(raw_email)
        To = message['To']
        From = message['From']
        Subject = message['Subject']
        Msg_id = message['Message-ID']
        texttospeech("Email number " + str(mail_count + 1) + "    .The mail is from " + From + " to " + To + "  . The subject of the mail is " + Subject, file + i)
        i = i + str(1)
        print('message id= ', Msg_id)
        print('From :', From)
        print('To :', To)
        print('Subject :', Subject)
        print("\n")
        to_read_list.append(Msg_id)
        mail_count = mail_count + 1

    flag = True
    while flag :
        n = 0
        flag1 = True
        while flag1:
            texttospeech("Enter the email number of mail you want to read.",file + i)
            i = i + str(1)
            n = input()
            print(n)
            texttospeech("You meant " + str(n) + ". Say yes or no.", file + i)
            i = i + str(1)
            say = input()
            say = say.lower()
            if say == 'yes':
                flag1 = False
        n = int(n)
        msgid = to_read_list[n - 1]
        print("message id is =", msgid)
        typ, data = conn.search(None, '(HEADER Message-ID "%s")' % msgid)
        data = data[0]
        result, email_data = conn.fetch(data, '(RFC822)')
        raw_email = email_data[0][1].decode()
        message = email.message_from_string(raw_email)
        To = message['To']
        From = message['From']
        Subject = message['Subject']
        Msg_id = message['Message-ID']
        print('From :', From)
        print('To :', To)
        print('Subject :', Subject)
        texttospeech("The mail is from " + From + " to " + To + "  . The subject of the mail is " + Subject, file + i)
        i = i + str(1)
        Body = get_body(message)
        Body = Body.decode()
        Body = re.sub('<.*?>', '', Body)
        Body = os.linesep.join([s for s in Body.splitlines() if s])
        if Body != '':
            texttospeech(Body, file + i)
            i = i + str(1)
        else:
            texttospeech("Body is empty.", file + i)
            i = i + str(1)
        print("attach")


def readmail_hi():
    global s, i
    conn.login(usr,password)
    conn.select("INBOX")
    result, data = conn.uid('search',None,"ALL")
    inbox_item_list = data[0].split()
    inbox_item_list.reverse()
    mail_count = 0
    to_read_list = list()
    for item in inbox_item_list:
        result, email_data = conn.uid('fetch',item, '(RFC822)')
        
        raw_email = email_data[0][1].decode()
        message = email.message_from_string(raw_email)
        To = message['To']
        From = message['From']
        Subject = message['Subject']
        Msg_id = message['Message-ID']
        texttospeech("Email number " + str(mail_count + 1) + "    .The mail is from " + From + " to " + To + "  . The subject of the mail is " + Subject, file + i)
        i = i + str(1)
        print('message id= ', Msg_id)
        print('From :', From)
        print('To :', To)
        print('Subject :', Subject)
        print("\n")
        to_read_list.append(Msg_id)
        mail_count = mail_count + 1

    flag = True
    while flag :
        n = 0
        flag1 = True
        while flag1:
            texttospeech("Enter the email number of mail you want to read.",file + i)
            i = i + str(1)
            n = input()
            print(n)
            texttospeech("You meant " + str(n) + ". Say yes or no.", file + i)
            i = i + str(1)
            say = input()
            say = say.lower()
            if say == 'yes':
                flag1 = False
        n = int(n)
        msgid = to_read_list[n - 1]
        print("message id is =", msgid)
        typ, data = conn.search(None, '(HEADER Message-ID "%s")' % msgid)
        data = data[0]
        result, email_data = conn.fetch(data, '(RFC822)')
        raw_email = email_data[0][1].decode()
        message = email.message_from_string(raw_email)
        To = message['To']
        From = message['From']
        Subject = message['Subject']
        Msg_id = message['Message-ID']
        print('From :', From)
        print('To :', To)
        print('Subject :', Subject)
        texttospeech("The mail is from " + From + " to " + To + "  . The subject of the mail is " + Subject, file + i)
        i = i + str(1)
        Body = get_body(message)
        Body = Body.decode()
        Body = re.sub('<.*?>', '', Body)
        Body = os.linesep.join([s for s in Body.splitlines() if s])
        if Body != '':
            texttospeech(Body, file + i)
            i = i + str(1)
        else:
            texttospeech("Body is empty.", file + i)
            i = i + str(1)
        print("attach")



readmail()