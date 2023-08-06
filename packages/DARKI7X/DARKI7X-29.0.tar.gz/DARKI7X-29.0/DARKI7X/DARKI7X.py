from LegendsLIB import *
from gdolib import *
from VENOMgetREST import *
def HITS(email):
	return "هذة  الاداة ملك ل ALAA7X اذا كا اي شخص اخر يقول ان الاداة خاصة به  فهو مجرد مغير حقوق وليس مبرمج     قناتي الاصلية.  @ALAA7X"
	print("هذة  الاداة ملك ل ALAA7X اذا كا اي شخص اخر يقول ان الاداة خاصة به  فهو مجرد مغير حقوق وليس مبرمج     قناتي الاصلية.  @ALAA7X")
def info(email):
				user = email.split('@')[0]
				info = A7X.info(user)
				name=info["Name"]
				user=info["User"]
				folwing=info["Followers"]
				folowers=info["Followors"]
				ID=info["ID"]
				privet=info["Privacy"]
				rest=VENOM.get_rest(user)
				date=info["Date"]
				bio=info["Bio"]
				X=f'''
"هذة  الاداة ملك ل ALAA7X اذا كا اي شخص اخر يقول ان الاداة خاصة به  فهو مجرد مغير حقوق وليس مبرمج     قناتي الاصلية.  @ALAA7X"
 '''
				return X