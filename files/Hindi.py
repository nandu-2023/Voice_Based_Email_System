from Function import sendmail_hi,texttospeech,listen_hi,readmail_hi
import os
file = "new"
i = "3"
while(1):

    str ="aap kya karna chahate hain?"
    texttospeech(str,file+i)

    str = "ईमेल लिखने के लिए लिखना कहें इनबॉक्स पढ़ने के लिए पढ़ें बोलें बाहर निकलने के लिए बाहर बोलें"
    texttospeech(str,file+i)

    ch = listen_hi()
     
    if (ch == 'send' or ch =='लिखना' or ch== 'likana' or ch == 'Likhna') :
        str = "आपने एक ईमेल भेजने के लिए चुना है"
        texttospeech(str,file+i)
        sendmail_hi()
    
    elif ( ch == 'read' or ch=='padhe' or ch=='Read' or ch=='पढ़ें') :
        str = "आपने मेल पढ़ना चुना है"
        texttospeech(str,file+i)
        readmail_hi()
    
    elif ( ch == 'exit' or ch=='Bahar' or ch=='बाहर' or ch=='Bahar nikale' ) :
        str = "आपने बाहर निकलने का विकल्प चुना है, अलविदा"
        texttospeech(str,file+i)
        exit(1)

    else:
        str = "अमान्य विकल्प, आपने कहा:"
        texttospeech(str,file+i)
        texttospeech(ch,file+i)    
