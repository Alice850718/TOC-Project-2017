# TOC-Project-2017
Telegram Bot
##機器人ID：@Lucky12Bot

##機器人名稱：星座每日運勢

##基本功能：
1.How to interact with your chatbot?
	使用者可隨便輸入，機器人會隨機回答普通文字(包含笑話和鬼故事)、圖片或音檔。正常指令包含：
	*	help：幫助使用者了解其他指令
	*	setup：設定自己的星座以便查詢，若尚未設定，則強制設定
	*	search：查詢自己星座或其他星座運勢，使用者可以按鈕，打字或數字回答
			

2.How to run you code?
*	需安裝python-telegram-bot
		pip install python-telegram-bot
*	需安裝BeautifulSoup
		pip install beautifulsoup4
*	需安裝ngork並架設server，到官方網站下載ngrok並直接執行
		./ngrok http 5000
	將Forwarding中獲取到的URL放入app.py中的WEBHOOK_URL = 'URL/hook'與pygraphviz = 'URL/show-fsm'參數中
*	執行程式
		python3 app.py

##進階功能：
*	使用BeautifulSoup抓取網頁內容
*	使用reply_photo, reply_audio以及telegram.ReplyKeyboardMarkup()等function
*	使用random回覆使用者不正確的輸出，並加入顏文字、特殊符號、鬼故事、笑話以及有趣的圖片為元素，增添樂趣
*	以全域變數記錄使用者設定的星座，以及flag判斷是否已設定星座，若無則強迫設定星座，亦可查詢他人星座
