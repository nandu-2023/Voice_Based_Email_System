from Function import listen,sendmail,readmail,texttospeech
import os
file = "new"
i = "2"

while(1):
 
    str ="What do you want to do?"
    texttospeech(str,file+i)

    str = "Speak SEND to Send email    Speak READ to Read Inbox    Speak EXIT to Exit"
    texttospeech(str,file+i)

    ch = listen()
     
    if (ch == 'send') :
        str = "You have chosen to send an email"
        texttospeech(str,file+i)
        sendmail()
    
    elif ( ch == 'read') :
        str = "you have chosen to read mail"
        texttospeech(str,file+i)
        readmail()
    
    elif ( ch == 'exit') :
        str = "you have chosen to exit, bye bye"
        texttospeech(str,file+i)
        exit(1)

    else:
        str = "Invalid choice, you said:"
        texttospeech(str,file+i)
        texttospeech(str,file+i)    
