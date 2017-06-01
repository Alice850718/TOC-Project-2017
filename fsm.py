from transitions.extensions import GraphMachine
from bs4 import BeautifulSoup
import telegram
import urllib
import random

class TocMachine(GraphMachine):
    global x
    x = '13'

    global flag
    flag = False

    global retry
    retry = False
    #記錄自身星座
    global star
    star = '-1'

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_say(self, update):
        text = update.message.text
        if text.lower() != 'search' and text.lower() != 'setup' and text.lower() != 'help':
            return True

    def is_going_to_help(self, update):
        text = update.message.text
        return text.lower() == 'help'

    def is_going_to_search(self, update):
        text = update.message.text
        return text.lower() == 'search'

    def is_going_to_search_self(self, update):
        text = update.message.text
        return text == '查詢我的星座' or text == '1'

    def is_going_to_search_error(self, update):
        global x
        global star
        if star == '-1':
            x = '12'
            return True
        return False

    def is_going_to_search_output(self, update):
        text = update.message.text
        global x
        if x != '13' and x != '12':
            return True
        return False

    def is_going_to_search_choose(self, update):
        text = update.message.text
        return text == '查詢其他星座' or text == '2'

    def is_going_to_search_set(self, update):
        global x
        x = update.message.text

        if x == '♒水瓶座' or x == '1':
            x = '10'
            update.message.reply_text('水瓶座♒')
        elif x == '♓雙魚座' or x == '2':
            x = '11'
            update.message.reply_text('雙魚座♓')
        elif x == '♈牡羊座' or x == '3':
            x = '0'
            update.message.reply_text('牡羊座♈')
        elif x == '♉金牛座' or x == '4':
            x = '1'
            update.message.reply_text('金牛座♉')
        elif x == '♊雙子座' or x == '5':
            x = '2'
            update.message.reply_text('雙子座♊')
        elif x == '♋巨蟹座' or x == '6':
            x = '3'
            update.message.reply_text('巨蟹座♋')
        elif x == '♌獅子座' or x == '7':
            x = '4'
            update.message.reply_text('獅子座♌')
        elif x == '♍處女座' or x == '8':
            x = '5'
            update.message.reply_text('處女座♍')
        elif x == '♎天秤座' or x == '9':
            x = '6'
            update.message.reply_text('天秤座♎')
        elif x == '♏天蠍座' or x == '10':
            x = '7'
            update.message.reply_text('天蠍座♏')
        elif x == '♐射手座' or x == '11':
            x = '8'
            update.message.reply_text('射手座♐')
        elif x == '♑摩羯座' or x == '12':
            x = '9'
            update.message.reply_text('摩羯座♑')
        else:
            x = '12'
            global retry
            if retry == True:
                update.message.reply_text('不對喔～請重新輸入，感謝尼(ﾟ3ﾟ)～♪')
            retry = True
            return False
        return True

    def is_going_to_setup(self, update):
        global x
        global star
        text = update.message.text
        if text.lower() == 'setup' or star == '-2':
            return True
        return False

    def is_going_to_setup_finish(self, update):
        global x
        x = update.message.text
        text = update.message.text
        if x == '♒水瓶座' or x == '1':
            x = '10'
            update.message.reply_text('水瓶座♒')
        elif x == '♓雙魚座' or x == '2':
            x = '11'
            update.message.reply_text('雙魚座♓')
        elif x == '♈牡羊座' or x == '3':
            x = '0'
            update.message.reply_text('牡羊座♈')
        elif x == '♉金牛座' or x == '4':
            x = '1'
            update.message.reply_text('金牛座♉')
        elif x == '♊雙子座' or x == '5':
            x = '2'
            update.message.reply_text('雙子座♊')
        elif x == '♋巨蟹座' or x == '6':
            x = '3'
            update.message.reply_text('巨蟹座♋')
        elif x == '♌獅子座' or x == '7':
            x = '4'
            update.message.reply_text('獅子座♌')
        elif x == '♍處女座' or x == '8':
            x = '5'
            update.message.reply_text('處女座♍')
        elif x == '♎天秤座' or x == '9':
            x = '6'
            update.message.reply_text('天秤座♎')
        elif x == '♏天蠍座' or x == '10':
            x = '7'
            update.message.reply_text('天蠍座♏')
        elif x == '♐射手座' or x == '11':
            x = '8'
            update.message.reply_text('射手座♐')
        elif x == '♑摩羯座' or x == '12':
            x = '9'
            update.message.reply_text('摩羯座♑')
        else:
            x = '12'
            global retry
            if retry == True:
                update.message.reply_text('不對喔～請重新輸入，感謝尼(ﾟ3ﾟ)～♪')
            retry = True
            return False

        global star
        star = x
        return True

    def on_enter_say(self, update):
        global flag
        if flag == False:
            number = random.randint(0,9)
            if number == 0:
                update.message.reply_text("您好(´・ω・`)\n請您對我下指令(*´艸`*)\n\n輸入help讓我來幫助您吧～♥")
            elif number == 1:
                update.message.reply_photo(photo="http://d.ifengimg.com/mw604/y0.ifengimg.com/ifengimcp/pic/20160418/5628dd6ecd9fa100f371_size30_w521_h534.jpg")
            elif number == 2:
                update.message.reply_text("◢▆▅▄▃崩╰(〒皿〒)╯潰▃▄▅▇◣")
                update.message.reply_photo(photo="https://www.wetalk.tw/data/attachment/forum/201611/18/110934pccchocqc8u8r6fo.png")
            elif number == 3:
                update.message.reply_text("你再亂說話我要嚇你囉！！！\n一位醫生在做完急診後已是午夜，正準備回家。走到電梯門口，見一女護士，便一同乘電梯下樓，可電梯到了一樓還不停，一直向下。到了B3時，門開了，電梯門開了，一個小女孩出現在他們眼前，低著頭說要搭電梯。醫生見狀急忙關上電梯門，護士奇怪地問：「為什麼不讓她上來。」醫生說：「B3是我們醫院的停屍房，醫院給每個屍體的右手都綁了一根紅絲帶，她的右手，他的右手有一根紅絲帶……」護士聽了，漸漸伸出右手，陰笑一聲說：「是不是……這樣的一根紅繩啊？ ")
            elif number == 4:
                update.message.reply_text("看在你這麼無聊的份上，講個笑話給你聽吧╮(╯_╰)╭\n交警開罰單時，小明蹲在保時捷旁看著交警說：「你除了開罰單還會幹什麼？」交警沒理他，小明繼續嗆：「看三小？有種拖走阿」然後小明就蹲著看著小華的保時捷被拖走\n哈哈很好笑吧⁽⁽٩(๑˃̶͈̀ ᗨ ˂̶͈́)۶⁾⁾")
            elif number == 5:
                update.message.reply_text("呀～您說什麼我聽不懂啦！(╯•̀ὤ•́)╯")
            elif number == 6:
                update.message.reply_text("(๑•́ ₃ •̀๑)你要聽笑話嗎？")
                update.message.reply_photo(photo="https://imgur.dcard.tw/0un2HiB.jpg")
            elif number == 7:
                update.message.reply_text("٩(ŏ﹏ŏ、)۶")
                update.message.reply_photo(photo="https://imgur.dcard.tw/2yQOw85.jpg")
            elif number == 8:
                update.message.reply_text("就叫你不要亂講話了吼！！！(╬☉д⊙)")
            else:
                update.message.reply_text("能不能給我一首歌的時間 ヾ(´︶`*)ﾉ♬")
                update.message.reply_audio(audio=open('music.mp3', 'rb'))

        else:
            flag = False
        self.go_back(update)

    def on_exit_say(self, update):
        #print(update.message.text)
        print('Leaving say')

    def on_enter_help(self, update):
        update.message.reply_text("輸入search查看星座運勢\n輸入setup設定星座\n請不要亂輸入，否則會產生意想不到的事情喔！( • ̀ω•́ )")
        self.go_back(update)

    def on_exit_help(self, update):
        print(update.message.text)
        print('Leaving help')

    def on_enter_search(self, update):
        keyboard = [['查詢我的星座'],
                    ['查詢其他星座']]
        update.message.reply_text(text="１、查詢我的星座\n２、查詢其他星座",reply_markup=telegram.ReplyKeyboardMarkup(keyboard))
        self.advance(update)

    def on_exit_search(self, update):
        print('Leaving search')

    def on_enter_search_self(self, update):
        text = update.message.text
        if text == '查詢我的星座' or text == '1':
            update.message.reply_text(text="正在查詢您的星座ლ(╹◡╹ლ)",reply_markup=telegram.ReplyKeyboardRemove())
        else:
            update.message.reply_text(text="請選擇想查詢的星座(✪ ω ✪)",reply_markup=telegram.ReplyKeyboardRemove())
        self.advance(update)

    def on_exit_search_self(self, update):
        print('Leaving search_self')

    def on_enter_search_output(self, update):
        text = update.message.text
        global x
        if text == '查詢我的星座' or text == '1':
            x = star
        url = "http://astro.click108.com.tw/daily_" + x +".php?iAstro="+ x
        page = urllib.request.urlopen(url)
        #整體運勢
        soup = BeautifulSoup(page, "lxml")
        data = soup.find('span', class_='txt_green')
        update.message.reply_text(data.text)
        data = data.find_next("p")
        update.message.reply_text(data.text)
        #愛情運勢
        data = soup.find('span', class_='txt_pink')
        update.message.reply_text(data.text)
        data = data.find_next("p")
        update.message.reply_text(data.text)
        #事業運勢
        data = soup.find('span', class_='txt_blue')
        update.message.reply_text(data.text)
        data = data.find_next("p")
        update.message.reply_text(data.text)
        #財運運勢
        data = soup.find('span', class_='txt_orange')
        update.message.reply_text(data.text)
        data = data.find_next("p")
        update.message.reply_text(data.text)
        update.message.reply_text("報告完畢(ง๑ •̀_•́)ง")
        self.advance(update)

    def on_exit_search_output(self, update):
        global flag
        flag = True
        print('Leaving search_output')

    def on_enter_search_error(self, update):

        global star
        star = '-2'
        update.message.reply_text("請您設定星座ヽ(#`Д´)ﾉ")
        self.advance(update)

    def on_exit_search_error(self, update):
        print('Leaving search_error')

    def on_enter_search_choose(self, update):
        keyboard = [['♒水瓶座','♓雙魚座','♈牡羊座'],
                    ['♉金牛座','♊雙子座','♋巨蟹座'],
                    ['♌獅子座','♍處女座','♎天秤座'],
                    ['♏天蠍座','♐射手座','♑摩羯座']]
        update.message.reply_text(text="請輸入號碼或點選您想查詢的星座\nξ( ✿＞◡❛)\n１、水瓶座 (01/20 ~ 02/19)\n２、雙魚座 (02/20 ~ 03/20)\n３、白羊座 (03/21 ~ 04/19)\n４、金牛座 (04/20 ~ 05/20)\n５、雙子座 (05/21 ~ 06/21)\n６、巨蟹座 (06/22 ~ 07/22)\n７、獅子座 (07/23 ~ 08/22)\n８、處女座 (08/23 ~ 09/22)\n９、天秤座 (09/23 ~ 10/23)\n１０、天蠍座 (10/24 ~ 11/21)\n１１、射手座 (11/22 ~ 12/20)\n１２、摩羯座 (12/21 ~ 01/20)",reply_markup=telegram.ReplyKeyboardMarkup(keyboard))
        self.advance(update)

    def on_exit_search_choose(self, update):
        global retry
        retry = False
        print('Leaving search_choose')

    def on_enter_search_set(self, update):
        update.message.reply_text(text="沒問題！交給我吧！(๑•̀ㅂ•́)و✧",reply_markup=telegram.ReplyKeyboardRemove())
        self.advance(update)

    def on_exit_search_set(self, update):
        print('Leaving search_set')

    def on_enter_setup(self, update):
        keyboard = [['♒水瓶座','♓雙魚座','♈牡羊座'],
                    ['♉金牛座','♊雙子座','♋巨蟹座'],
                    ['♌獅子座','♍處女座','♎天秤座'],
                    ['♏天蠍座','♐射手座','♑摩羯座']]
        update.message.reply_text(text="請輸入號碼或點選您的星座\nξ( ✿＞◡❛)\n１、水瓶座 (01/20 ~ 02/19)\n２、雙魚座 (02/20 ~ 03/20)\n３、白羊座 (03/21 ~ 04/19)\n４、金牛座 (04/20 ~ 05/20)\n５、雙子座 (05/21 ~ 06/21)\n６、巨蟹座 (06/22 ~ 07/22)\n７、獅子座 (07/23 ~ 08/22)\n８、處女座 (08/23 ~ 09/22)\n９、天秤座 (09/23 ~ 10/23)\n１０、天蠍座 (10/24 ~ 11/21)\n１１、射手座 (11/22 ~ 12/20)\n１２、摩羯座 (12/21 ~ 01/20)",reply_markup=telegram.ReplyKeyboardMarkup(keyboard))
        
        self.advance(update)

    def on_exit_setup(self, update):
        print('Leaving setup')

    def on_enter_setup_finish(self, update):
        update.message.reply_text(text="設定完成(๑•̀ㅂ•́)و✧",reply_markup=telegram.ReplyKeyboardRemove())
        self.advance(update)

    def on_exit_setup_finish(self, update):
        global flag
        flag = True
        global retry
        retry = False
        print('Leaving setup_finish')
