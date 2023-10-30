import os, time
os.system("clear")
print("")

print("                       SCRIPT FOR WTS CHAT BACKUP")
print("_____________________________________________________________")
print("|                                                           ")
print("| 1) a5tarnin 1 time                           ")
print("|                                            ")
print("| 2) a5tarni ba3d backup men el WTS e7zefy el WTS 3ady.   ")
print("|                                      ")
print("| 3) a5tarni ba3d ma tnzel el wts we t5tary el lo8a.            ")
print("|                                                  ")
print("| 0) a5tarini ba3d ma el wts yeft7 we el chat el adem mawgood  ")
print("|")
print("| C) EXIT                                       ")
print("_____________________________________________________________")
print(" by seveN")
print ("")
answer = input("Enter your answer (1, 2, 3, or 0):  ")

if answer.upper() == "1":
    os.system("mkdir /sdcard/Android/media/wbp")
    print("")
    os.system("clear")
    print(" kolo tmam now use 2")
    time.sleep(4)
    os.system("python /sdcard/Download/Whatsapp_Backup.py")
    
elif answer.upper() == "2":
    os.system("cp -r /sdcard/Android/media/com.aero/. /sdcard/Android/media/wbp")
    print("")
    print("KOLO TMAM A7ZEFY EL WTS")
    time.sleep(4)
    os.system("python /sdcard/Download/Whatsapp_Backup.py")
                             
elif answer.upper() == "3":
    os.system("cp -r /sdcard/Android/media/wbp/. /sdcard/Android/media/com.aero/")
    print("")
    os.system("clear")
    print("KOLO TMAM SABTY EL WTS")
    time.sleep(4)
    os.system("python /sdcard/Download/Whatsapp_Backup.py")
    
elif answer.upper() == "0":
    os.system("rm -rif /sdcard/Android/media/wbp/")
    os.system("clear")
    print("tmam el backup et7asf")
    time.sleep(4)
    os.system("python /sdcard/Download/Whatsapp_Backup.py")
    
elif answer.upper() == "C":
    print("")
    print("bye bye <3")
    os.system("am startservice -a com.termux.service_stop com.termux/.app.TermuxService")


