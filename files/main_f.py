import os
import subprocess
from Function import listen,texttospeech
file = "new"
i = "2"





str = "Welcome to voice controlled email service how can i help you"
str_mr = "व्हॉईस नियंत्रित ईमेल सेवेमध्ये आपले स्वागत आहे मी आपल्याला कशी मदत करू शकतो "
str_hi=  "वॉयस कंट्रोल्ड ईमेल सर्विस में आपका स्वागत है मैं आपकी कैसे मदद कर सकता हूं"
texttospeech(str,file+i)

texttospeech(str_mr,file+i)

texttospeech(str_hi,file+i)
flag = True


while(1):

    str ="Please select the Language to use this application"
    str_hi = "कृपया इस एप्लिकेशन का उपयोग करने के लिए भाषा का चयन करें"
    str_mr = "कृपया हा अनुप्रयोग वापरण्यासाठी भाषा निवडा"
    texttospeech(str,file+i)
    
    texttospeech(str_hi,file+i)
    
    texttospeech(str_mr,file+i)
    

    str1 = ("Say English for selecting English")
    str1_hi=("हिंदी को भाषा के रूप में चुनने के लिए हिंदी बोलें")  
    str1_mr=("भाषा म्हणून मराठी निवडण्यासाठी मराठी म्हणा")
     
    
    str2 =  ("say exit to exit the application")  
    str2_hi=("एप्लिकेशन से बाहर निकलने के लिए बाहर निकलें कहें")  
    str2_mr=("अनुप्रयोगातून बाहेर पडण्यासाठी बाहेर पडा म्हणा")
        
    texttospeech(str1,file+i)
        
    texttospeech(str1_hi,file+i)
        
    texttospeech(str1_mr,file+i)
        
    
    while flag is True:
        texttospeech(str2,file+i)
        
        texttospeech(str2_hi,file+i)
        
        texttospeech(str2_mr,file+i)
        flag = False
    

    ch = listen()
     
    if (ch == 'English'or ch == 'english' ) :
        str = "You have chosen English as a langauge"
        texttospeech(str,file+i)
        
        
        p1=subprocess.Popen('python sub_eng.py', shell=True)
        

        exit(1)
           
    
    elif ( ch == 'hindi'or ch == 'हिंदी' or ch == "Hindi") :
        str = "आपने हिंदी को एक भाषा के रूप में चुना है"
        texttospeech(str,file+i)
        
        p1=subprocess.Popen('python sub_hindi.py', shell=True)
        exit(1)
        
     
    elif ( ch == 'Marathi'or ch == "मराठी" or ch == "marathi" ) :
        str = "तुम्ही भाषा म्हणून मराठी निवडली आहे"
        texttospeech(str,file+i)
        
        p1=subprocess.Popen('python sub_marathi.py', shell=True)
        exit(1)
    
    elif ( ch == 'Exit'or ch == "exit" or ch == "बाहर निकलें" or ch =="बाहेर पडा" or ch == "Get out") :
        str = "You have exited the application,Good Bye"
        str_mr = "तुम्ही अॅप्लिकेशनमधून बाहेर पडा "
        str1_mr = "अलविदा"
        str_hi = "आप एप्लिकेशन से बाहर निकल गए हैं अलविदा" 
        texttospeech(str,file+i)
        
        texttospeech(str,file+i)
        
        texttospeech(str,file+i)
        
        texttospeech(str1_mr,file+i)
        
        exit(1)

    else:
        str = "Please Select the language again"
        str_hi = "कृपया भाषा फिर से चुनें"
        str1_mr = "कृपया भाषा पुन्हा निवडा"
        texttospeech(str,file+i)
        
        texttospeech(str_hi,file+i)
        
        texttospeech(str1_mr,file+i)
        
          
