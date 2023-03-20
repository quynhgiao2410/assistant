from selenium.webdriver.common.by import By
from tkinter import *
import textwrap
import os
import json
import datetime
import wikipedia
from googlesearch import search
from wikipedia.exceptions import WikipediaException
from bs4 import BeautifulSoup
from youtubesearchpython import VideosSearch
import requests
import threading
import speech_recognition as sr
import playsound
import time
import ctypes
import speech_recognition
import datetime
import re
import webbrowser
import smtplib
import requests
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
from datetime import date
import datetime

root = Tk()
root.config(bg="light grey")
root.geometry('300x500+500+10')
root.title('Trợ lý ảo')


# Main window
canvas = Canvas(root, width=200, height=200, bg="snow")
canvas.grid(row=0, column=0, columnspan=2)
canvas.place(x=10, y=10, width=280, height=430)

wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()
robot_ear = speech_recognition.Recognizer()

def stop():
    
    put_answer("Hẹn gặp lại bạn sau!")

class Me:
    def __init__(self, master, message=""):
        self.master = master
        self.frame = Frame(master, bg="pink")
        
        self.i = self.master.create_window(
            270, 390, window=self.frame, anchor="ne")
        Label(self.frame, text=textwrap.fill(message, 20), font=(
            "Sogue", 10), bg="pink").grid(row=1, column=0, sticky="w", padx=1, pady=3)
        root.update_idletasks()
        ask.delete(0, END)

        # Apply commands
        put_answer("Xin chào, bạn tên là gì nhỉ?")
        time.sleep(2)
        name = get_text()
        canvas.move(ALL, 0, -50)
    
        me = question(canvas, question= name)
        
        if name:
          put_answer("Chào bạn {}".format(name))
          time.sleep(2)
          put_answer("Bạn cần Trợ Lý ảo  giúp gì ạ?")
          time.sleep(3)
          while True:
            
            text = get_text()
            canvas.move(ALL, 0, -50)
            
            me = question(canvas, question= text)
            if not text:
                break
            if "dừng" in text or "tạm biệt" in text or "chào robot" in text or "ngủ thôi" in text:
                stop()
                break
            elif "giới thiệu bản thân" in text:
                introduce()
            elif "có thể làm gì" in text:
                help_me()
            elif "chào trợ lý ảo" in text:
                hello(name)
            elif "giờ" in text:
                get_time(text)
            elif "mở" in text:
                if 'mở google và tìm kiếm' in text:
                    open_google_and_search(text)
                elif "." in text:
                    open_website(text)
                else:
                    open_application(text)
            elif "email" in text or "mail" in text or "gmail" in text:
                send_email(text)
            elif "thời tiết" in text:
                current_weather()
            elif "nghe nhạc" in text:
                play_song()
            elif "hình nền" in text:
                change_wallpaper()
            elif "đọc báo" in text:
                read_news()
            elif "định nghĩa" in text:
                tell_me_about()
            elif "kể chuyện"in text:
                ke_chuyen()            
            else:
                put_answer("Bạn cần Bot giúp gì ạ?")
get_text = []            



answers = []




class Assistant:
    def __init__(self, master, answer=""):
        self.master = master
        self.frame = Frame(master, bg="dodger blue")
        
        self.i = self.master.create_window(
            10, 390 + 40, window=self.frame, anchor="nw")
        
        Label(self.frame, text=textwrap.fill(answer, 40), font=("Sogue", 10),
              bg="dodger blue").grid(row=1, column=0, sticky="w", padx=1, pady=3)
        root.update_idletasks()
class question:
    def __init__(self, master, question=""):
        self.master = master
        self.frame = Frame(master, bg="pink")
        
        self.i = self.master.create_window(
            270, 390, window=self.frame, anchor="ne")
        Label(self.frame, text=textwrap.fill(question, 20), font=(
            "Sogue", 10), bg="pink").grid(row=1, column=0, sticky="w", padx=1, pady=3)
        root.update_idletasks()
        ask.delete(0, END)
# Functions

def write_message():
    put_answer("xin chào")
    #message = get_text
    canvas.move(ALL, 0, -50)
    
    me = Me(canvas, message=get_text())
    #text = get_text.append(me)
    
def ke_chuyen():
    put_answer("Máy vi tính hỏi virus ") 
    time.sleep(3)
    put_answer("Cậu từ đâu đến đây thế")   
    time.sleep(2)
    
    put_answer("Thế cậu ở đâu ra")
    time.sleep(2)
    put_answer("Tớ đến từ USA.")
    time.sleep(2)
    put_answer("Vậy tớ là hàng xóm của cậu rồi")
    time.sleep(2)
    put_answer("Tớ đến từ… USB.kkk")
    time.sleep(3)
    put_answer("Bạn cần gì thêm khong ạ")
    time.sleep(3)


def put_answer(answer):
    assistant = Assistant(canvas, answer=answer)
    answers.append(assistant)
    canvas.move(ALL, 0, -35)
    canvas.update()
    q = threading.Thread(target=speak(answer))
    q.start()
def write_answer(answer):
    assistant = Assistant(canvas, answer=answer)
    answers.append(assistant)
    canvas.move(ALL, 0, -35)
    canvas.update()
    
    
    

def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            put_answer("Máy không nghe rõ. Bạn nói lại được không!")
            time.sleep(3)
    time.sleep(2)
    stop()
    return 0

def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        put_answer("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        put_answer("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        put_answer("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))
    time.sleep(5)
    put_answer("Bạn cần trợ lý ảo giúp gì")


def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        put_answer('Bây giờ là %d giờ %d phút %d giây' % (now.hour, now.minute, now.second))
        time.sleep(3)
        put_answer("bạn cần bot giúp gì nữa không ạ")
        
    elif "ngày" in text:
        put_answer("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
        time.sleep(3)
        put_answer("bạn cần bot giúp gì nữa không ạ")
        
    else:
        put_answer("Bot chưa hiểu ý của bạn. Bạn nói lại được không?")
    time.sleep(4)

def open_application(text):
    if "google" in text:
        put_answer("Mở Google Chrome")
        time.sleep(2)
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
    elif "word" in text:
        put_answer("Mở Microsoft Word") 
        time.sleep(2)
        os.startfile('C:\Program Files\Microsoft Office\Office15\WINWORD.EXE') 
    elif "excel" in text:
        put_answer("Mở Microsoft Excel")
        time.sleep(2)
        os.startfile('C:\Program Files\Microsoft Office\Office15\EXCEL.EXE') 
    elif "Sublime Text" in text:
        put_answer("Sublime Text đang được mở, bạn chờ xíu nha Ihihi")
        time.sleep(2)
        os.startfile('C:\Program Files\Sublime Text 3\sublime_text.exe')
    else:
        put_answer("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
        time.sleep(3)


# Alex mở web cho bạn được luôn nè
def open_website(text):
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        webbrowser.open(url)
        put_answer("Trang web bạn yêu cầu đã được mở.")
        return True
    else:
        return False



def open_google_and_search(text):
    search_for = text.split("kiếm", 1)[1]
    put_answer('Okay!')
    driver = webdriver.Chrome(path)
    driver.get("https://www.google.com")
    que = driver.find_element(By.XPATH, "//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)
    time.sleep(10)
    put_answer("Bạn cần bot giúp thêm gì không ạ")


def send_email(text):
    put_answer('Bạn gửi email cho ai nhỉ')
    
    
    recipient = get_text()
    canvas.move(ALL, 0, -50)
            
    me = question(canvas, question= recipient)
    if 'phương' in recipient: 
        put_answer('Nội dung bạn muốn gửi là gì')
        content = get_text()
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('diachiEmail', 'password') 
        mail.sendmail('Diachiemailnguoigui', 
                      'diachiemailnguoinhan', content.encode('utf-8')) 
        mail.close()
        put_answer('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')
        put_answer("Bạn cần bot giúp thêm gì không ạ")
    else:
        put_answer('Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không')



def current_weather():
    put_answer("Bạn muốn xem thời tiết ở đâu ạ.")
    time.sleep(3)
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    city = get_text()
    canvas.move(ALL, 0, -50)
            
    me = question(canvas, question= city)
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content1 = """Hôm nay là ngày {day} tháng {month} năm {year}""".format(day = now.day,month = now.month, year= now.year)
        content2 = """Mặt trời mọc vào {hourrise} giờ {minrise} phút""".format(hourrise = sunrise.hour, minrise = sunrise.minute)
        content3 = """Mặt trời lặn vào {hourset} giờ {minset} phút""".format(hourset = sunset.hour, minset = sunset.minute)
        content4 = """Nhiệt độ trung bình là {temp} độ C""".format(temp = current_temperature)
        content5 = """Áp suất không khí là {pressure} héc tơ Pascal""".format(pressure = current_pressure)
        content6 = """Độ ẩm là {humidity}%""".format(humidity = current_humidity)
                                                                      
        put_answer(content1)
        time.sleep(4)
        put_answer(content2)
        time.sleep(3)
        put_answer(content3)
        time.sleep(3)
        put_answer(content4)
        time.sleep(3)
        put_answer(content5)
        time.sleep(3)
        put_answer(content6)
        time.sleep(3)
        
        put_answer("Bạn cần giúp gì thêm không ạ")
        time.sleep(3)
        
    else:
        put_answer("Không tìm thấy địa chỉ của bạn")
        time.sleep(3)
        put_answer("Bạn cần bot giúp thêm gì không ạ")
        time.sleep(3)


def play_song():
    put_answer('Xin mời bạn chọn tên bài hát')
    time.sleep(2)
    mysong = get_text()
    canvas.move(ALL, 0, -50)
            
    me = question(canvas, question= mysong)
    
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    put_answer("Bài hát bạn yêu cầu đã được mở.")
    time.sleep(3)
    put_answer("Bạn cần bot giúp thêm gì không ạ")


def read_news():
    put_answer("Bạn muốn đọc báo về gì")
    time.sleep(3)
    queue = get_text()
    canvas.move(ALL, 0, -50)
            
    me = question(canvas, question= queue)
    params = {
        'apiKey': '30d02d187f7140faacf9ccd27a1441ad',
        "q": queue,
    }
    api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
    api_response = api_result.json()
    put_answer("Tin tức")

    for number, result in enumerate(api_response['articles'], start=1):
        if number <= 3:
            write_answer(f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}
    """)
            time.sleep(3)
        
            webbrowser.open(result['url'])
            
    time.sleep(10)
    put_answer("bạn cần bot giúp gì nữa không ạ")


def change_wallpaper():
    api_key = 'RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw'
    url = 'https://api.unsplash.com/photos/random?client_id=' + \
        api_key  
    f = urllib2.urlopen(url)
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']

    urllib2.urlretrieve(photo, "C:\\Users\\Admin\\OneDrive\\Documents\\Documents\\a.png")
    image=os.path.join("C:\\Users\\Admin\\OneDrive\\Documents\\Documents\\a.png")
    ctypes.windll.user32.SystemParametersInfoW(20,0,image,3)
    put_answer('Hình nền máy tính vừa được thay đổi')
    time.sleep(3)
    put_answer("Bạn cần bot giúp thêm gì không ạ")


def tell_me_about():
    try:
        put_answer("Bạn muốn nghe về gì ạ")
        time.sleep(4)

        text = get_text()
        canvas.move(ALL, 0, -50)

        me = question(canvas, question= text)
        contents = wikipedia.summary(text).split('\n')
        put_answer(contents[0].split(".")[0])
        time.sleep(10)
        for content in contents[1:]:
            put_answer("Bạn muốn nghe thêm không")
            time.sleep(2)
            ans = get_text()
            if "có" not in ans:
                break    
            put_answer(content)
            time.sleep(30)

        put_answer('Cảm ơn bạn đã lắng nghe!!!')
        time.sleep(3)
        put_answer("Bạn cần bot giúp thêm gì không ạ")
    except:
        put_answer("Bot không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")
        time.sleep(5)

def introduce():
    put_answer("Xin chào bạn.")
    time.sleep(2)
    put_answer("Rất hân hạnh được phục vụ bạn")
    time.sleep(2)
    put_answer("Tôi là Trợ Lý ảo.")
    time.sleep(2)
    put_answer("Tôi được tạo ra dựa trên ngôn ngữ lập trình Python kết hợp với AI.")
    
    time.sleep(5)
    put_answer("Bạn cần bot giúp gì không ạ")
    time.sleep(3)
def help_me():
    put_answer("Chức năng của tôi là")
    time.sleep(2)
    put_answer("0. Giới thiệu bản thân")
    time.sleep(2)
    put_answer("1. Chào hỏi")
    time.sleep(2)
    put_answer("2. Hiển thị giờ")
    time.sleep(2)
    put_answer("3. Mở website, application")
    time.sleep(2)
    put_answer("4. Tìm kiếm trên Google")
    time.sleep(2)
    put_answer("5. Gửi email")
    time.sleep(2)
    put_answer("6. Dự báo thời tiết")
    time.sleep(2)
    put_answer("7. Mở video nhạc")
    time.sleep(2)
    put_answer("8. Thay đổi hình nền máy tính")
    time.sleep(2)
    put_answer("9. Đọc báo hôm nay")
    time.sleep(2)
    put_answer("10. Tra cứu wikimedia")
    time.sleep(2)
    put_answer("11.kể chuyện cười")
   
    time.sleep(2)
    put_answer("Bạn cần bot giúp gì nào")




def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove("sound.mp3")


def get_audio():
    print("Bot: Đang nghe ")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=8)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text.lower()
        except:
            canvas.move(ALL, 0, -50)
            
            me = question(canvas, question= "...")
            
            return 0

ask = Entry(root, bd=0, width=26, font=("Sogue", 12))
ask.place(x=10, y=450, width=230, height=35)
ask.focus()
ask.insert(0, "")


button = Button(root, justify=LEFT)
photo = PhotoImage(file="img/f.gif")
button.config(image=photo, width="32", height="30", relief=FLAT)
button.pack(side=LEFT)
button.place(x=250, y=450)


root.resizable(width=False, height=False)
root.lift()
root.call('wm', 'attributes', '.', '-topmost', True)
root.update()

write_message()
root.mainloop()
threading.Thread._keep_alive = False
