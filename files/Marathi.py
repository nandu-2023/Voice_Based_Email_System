from Function import texttospeech,listen_mr,sendmail_mr,readmail_mr
import os
file = "new"
i = "5"
while(1):

    str ="तुम्हाला काय करायचं आहे?"
    texttospeech(str,file+i) 
    

    str = "ईमेल पाठवण्यासाठी पाठवा बोला इनबॉक्स वाचण्यासाठी वाचा बोला बाहेर पडण्यासाठी बाहेर पडा म्हणा"
    texttospeech(str,file+i) 
    

    ch = listen_mr()
     
    if (ch == 'send' or ch =='pathwa' or ch== 'पाठवा') :
        str = "तुम्ही ईमेल पाठवणे निवडले आहे"
        texttospeech(str,file+i) 
        
        sendmail_mr()
    
    elif ( ch == 'read' or ch=='Vacha' or ch=='Read' or ch=='wachya') :
        str = "तुम्ही मेल वाचण्यासाठी निवडले आहे"
        texttospeech(str,file+i) 
        
        readmail_mr()
    
    elif ( ch == 'exit' or ch=='बाहेर पडा' or ch=='baher Pada' or ch=='Bahare Pada' ) :
        str = "तुम्ही निवड रद्द केली आहे, बाय"
        texttospeech(str,file+i) 
        
        exit(1)

    else:
        str = "अवैध पर्याय, तुम्ही म्हणालात:"
        texttospeech(str,file+i)
        texttospeech(ch,file+i) 