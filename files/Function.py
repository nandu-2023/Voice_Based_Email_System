import speech_recognition as sr
import easyimap as e
import smtplib
import imaplib,email
import os
import re
from playsound import playsound
from gtts import gTTS
from googletrans import Translator

r = sr. Recognizer()
pwd = "rtcgckrwmuctsjox"
unm = "vcontrolproject@gmail.com"
file = "new"
i = "5"
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
imap_url = 'imap.gmail.com'
conn = imaplib.IMAP4_SSL(imap_url)


def remove(string):
    return string.replace(" ", "").lower()

def convertTeng(str):
    translator = Translator()
    translation = translator.translate(str,dest="en")
    return translation.text

def convertTmr(str):
    translator = Translator()
    translation = translator.translate(str,dest="mr")
    return translation.text

def convertThi(str):
    translator = Translator()
    translation = translator.translate(str,dest="hi")
    return translation.text


 

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str = "Speak Now:"
        texttospeech(str,file+i) 
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            str = "Sorry could not recognize what you said"
            texttospeech (str,file+i)

def listen_hi():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str = "अब बोलो:"
        texttospeech(str,file+i)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            str = "क्षमा करें आपने जो कहा उसे पहचान नहीं सका"
            texttospeech (str,file+i)

def listen_mr():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str = "बोल आता:"
        texttospeech(str,file+i) 
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            str = "सॉरी तुम्ही काय बोललात ते ओळखता आले नाही"
            texttospeech (str,file+i)

def sendmail():
    
    str = "Please Give Reciever Email"
    texttospeech(str,file+i)
    recs=listen()+"@gmail.com"
    rec =remove(recs) 
    texttospeech(rec,file+i)
    


    str = "Please speak the Subject of your email"
    texttospeech(str,file+i)
    SUBJECT = listen()
    strq1 = "Please speak the body of your email"
    texttospeech(strq1,file+i)
    TEXT = listen()
    msg  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    str = "You have spoken the message"
    texttospeech(str,file+i)
    texttospeech ("subject is : ",file+i)
    texttospeech(SUBJECT,file+i)
    texttospeech("Body is :",file+i)
    texttospeech(TEXT,file+i)
    

    
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(unm,pwd)
    server.sendmail(unm,rec,msg)
    server.quit()

    str = "The E-mail has been sent"
    texttospeech(str,file+i)

def sendmail_hi():
    ##change the prompts to hindi
    str = "कृपया प्राप्तकर्ता ईमेल दें"
    texttospeech(str,file+i)
    recs=listen_hi()+"@gmail.com"
    rec = remove(recs) 
    texttospeech(rec,file+i)
    

    

    str = "कृपया अपने ईमेल का विषय बोलें"
    texttospeech(str,file+i)
    var = listen_hi()
    SUBJECT = convertTeng(var)
    strq1 = "कृपया अपने ईमेल का मुख्य भाग बोलें"
    texttospeech(strq1,file+i)
    var1 = listen_hi()
    TEXT = convertTeng(var1)
    msg  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    str = "आपने संदेश बोला है"
    texttospeech(str,file+i)
    texttospeech("विषय hai : .",file+i)
    texttospeech(var,file+i)
    texttospeech("मुख्य भाग hai:",file+i)
    texttospeech(var1,file+i)
    
    

    
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(unm,pwd)
    server.sendmail(unm,rec,msg)
    server.quit()

    str = "ईमेल भेज दिया गया है"
    texttospeech(str,file+i)

def sendmail_mr():
    ##change the prompts to marathi
    str = "कृपया प्राप्तकर्त्याचा ईमेल द्या"
    texttospeech(str,file+i)
    recs=listen_mr()+"@gmail.com"
    rec = remove(recs) 
    texttospeech(rec,file+i)
    

    

    str = "कृपया तुमच्या ईमेलचा विषय सांगा"
    texttospeech(str,file+i)
    var = listen_mr()
    SUBJECT = convertTeng(var)
    strq1 = "कृपया तुमच्या ईमेलचा मुख्य भाग सांगा"
    texttospeech(strq1,file+i)
    var1 = listen_mr()
    TEXT = convertTeng(var1)
    msg  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    str = "तुम्ही संदेश बोललात"
    texttospeech(str,file+i)
    texttospeech("विषय आहे : .",file+i)
    texttospeech(var,file+i)
    texttospeech("मुख्य भाग आहे :",file+i)
    texttospeech(var1,file+i)
    
    

    
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(unm,pwd)
    server.sendmail(unm,rec,msg)
    server.quit()

    str = "इमेल पाठवला आहे"
    texttospeech(str,file+i)

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
    conn.login(unm,pwd)
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
            n = listen()
            print(n)
            texttospeech("You meant " + str(n) + ". Say yes or no.", file + i)
            i = i + str(1)
            say = listen()
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
    conn.login(unm,pwd)
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
        Subject1 = convertTmr(Subject)
        Msg_id = message['Message-ID']
        texttospeech("Email number " + str(mail_count + 1) + "The mail is from " + From + " to " + To + "मेलचा विषय आहे" + Subject1, file + i)
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
            texttospeech("तुम्हाला वाचायचा असलेल्या मेलचा ईमेल नंबर एंटर करा.",file + i)
            i = i + str(1)
            n = listen_mr()
            print(n)
            texttospeech("तुम्हाला" + str(n)+ "म्हणायचे आहे का?" + "होय किंवा नाही म्हणा.", file + i)
            i = i + str(1)
            say = listen_mr()
            say = say.lower()
            if say == 'yes' or say=='hoya' or say=='Hoya' :
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
        texttospeech("The mail is from " + From + " to " + To + "मेलचा विषय आहे" + Subject, file + i)
        i = i + str(1)
        Body = get_body(message)
        Body = Body.decode()
        Body = re.sub('<.*?>', '', Body)
        Body = os.linesep.join([s for s in Body.splitlines() if s])
        Body1 = convertTmr(Body)
        if Body != '':
            texttospeech(Body, file + i)
            i = i + str(1)
        else:
            texttospeech("मेल रिकामा आहे", file + i)
            i = i + str(1)
        print("attach")


def readmail_hi():
    global s, i
    conn.login(unm,pwd)
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
        Subject1 = convertThi(Subject)
        Msg_id = message['Message-ID']
        texttospeech("Email number" + str(mail_count + 1),file+i) 
        i = i + str(1)
        texttospeech( "The mail is from " + From + " to " + To,file+i) 
        i = i + str(1)
        texttospeech("मेल का विषय है " + Subject1,file+i)
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
            texttospeech("उस मेल का ईमेल नंबर बोलें जिसे आप पढ़ना चाहते हैं।",file+i)
            i = i + str(1)
            n = listen_hi()
            print(n)
            texttospeech("आप का मतलब" + str(n) + "tha" + "कहो हाँ या ना।", file + i)
            i = i + str(1)
            say = listen_hi()
            say = say.lower()
            if say == 'yes' or say == 'haan' :
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
        Subject1 = convertThi(Subject)
        Msg_id = message['Message-ID']
        print('From :', From)
        print('To :', To)
        print('Subject :', Subject)
        texttospeech("The mail is from " + From + " to " + To, file + i)
        i = i + str(1)
        texttospeech("मेल का विषय है" + Subject1,file + i)
        i = i + str(1)
        Body = get_body(message)
        Body = Body.decode()
        Body = re.sub('<.*?>', '', Body)
        Body = os.linesep.join([s for s in Body.splitlines() if s])
        Body1 = convertThi(Body)
        if Body != '':
            texttospeech(Body1,file+i)
            i = i + str(1)
        else:
            texttospeech("ईमेल खाली है।",file+i)
            i = i + str(1)
        print("attach")



