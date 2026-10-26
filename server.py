import socket
import json
import sys
import main
import customtkinter as ctk
import threading
import sys
import time

print("Starting")
HOST = '0.0.0.0'
PORT = 12340
DISCOVERY_PORT = 50001 
DISCOVERY_MESSAGE = "DISCOVER_PYTHON_SERVER"
RESPONSE_MESSAGE_KEY = "server_info"
global phone
global name
global nout
global app
global flag_app
flag_app = [1]
global funs
funs = main.funanul()
name = [1, "ggg", "j"]
phone = ["j", "j"]
nout = ["j", "j"]

import threading

def start_discovery_beacon():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80)) 
        current_ip = s.getsockname()[0]
        s.close()
    except Exception as e:
        print(e)
        current_ip = '0.0.0.0' 
    print(f"IP: {current_ip}\n")
    print(f"Port: {DISCOVERY_PORT}\n")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", DISCOVERY_PORT)) 

    
    while True:
        try:
            data, addr = sock.recvfrom(1024) # Буфер
            received_message = data.decode('utf-8').strip()
            print(f"Получени из широковещателя: '{received_message}' адрес: {addr}")

            if received_message == DISCOVERY_MESSAGE:
                # Отправляем информацию о сервере обратно клиенту
                server_info = {
                    "ip": current_ip,
                    "port": PORT,
                    "message": "Hello from Python!"
                }
            response = json.dumps({RESPONSE_MESSAGE_KEY: server_info}).encode('utf-8')
            sock.sendto(response, addr)

        except Exception as e:
            print(e)


def handle_client(conn, addr):
    print(f"Новое соединение от {addr[0]}:{addr[1]}")
    print(f"[АКТИВНЫЕ ПОДКЛЮЧЕНИЯ] {threading.active_count() - 3}")

    
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                print(f"Клиент {addr} отключился.") 
                break

            message = data.decode('utf-8')
            message = message[:-1]
            print(f"[{addr[0]}:{addr[1]}] Получено: '{message}'")
            if message == "Привет от Android!":
                phone[0] = conn
                phone[0].sendall((f'say\n').encode('utf-8'))
            elif message == "Hello from nout":
                nout[0] = conn
            elif message == "Привет от master-Android!":
                print("master")
            elif message.split(" ")[0] == "setlight":
                phone[1] = float(message.split(" ")[1])
            global flag_app
            if message == "but15":

                if flag_app[0] == 1:
                    app.withdraw()
                    flag_app = [0]

                    
                else:   
                    app.deiconify()
                    flag_app = [1]
                    app.state("zoomed")
            elif "but" in message:
                main.but(funs.name_com(message))
                app.update()
            elif "exet" == message:
                print(phone[0])
                if phone[0] != "j":
                    phone[0].sendall((f"exet of master say it\n").encode('utf-8'))
                main.ext()
            if message.lower() == 'quit':
                print(f"Клиент {addr} отправил 'quit'. Отключаю...")
                break

    except Exception as e:
        print(f"Ошибка при работе с клиентом {addr}: {e}")
    finally:
        if conn == phone[0]:
            phone[1] = "j"
            phone[0] = "j"
        if conn == nout[0]:
            nout[1] = "j"
            nout[0] = "j"
        conn.close()
        print(f"Соединение с {addr} закрыто.")
        print(f"[АКТИВНЫЕ ПОДКЛЮЧЕНИЯ] {threading.active_count() - 4}")
    
    
def main_serv(HOST, PORT):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((HOST, PORT))
        print(f"Сервер успешно привязан к {HOST}:{PORT}\n")
        server_socket.listen(5)
        
        print("Ожидание подключений...\n")

        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()


    except OSError as e:
        print(f"Ошибка сокета: {e}")
        print("Возможно, порт уже занят или возникла проблема с сетью.")
    except KeyboardInterrupt:
        print("\nСервер остановлен пользователем (Ctrl+C).")
    finally:
        server_socket.close()
        print("Серверный сокет закрыт.")









class ConsoleOutput:
    def __init__(self, text_widget):
        self.text_widget = text_widget
 
    def write(self, message):
        try:
            self.text_widget.insert(text=message, index='end')
            self.text_widget.see("end")
        except:
            app.after(5, self.write)
 
    def flush(self):
        pass  

app = ctk.CTk()
app.title("my app")
app.geometry("1000x700")
ctk.set_appearance_mode("dark")
app.state("zoomed")


app.grid_columnconfigure((0,1,2), weight=1)
app.grid_rowconfigure((0,1,2), weight=1)


frame00 = ctk.CTkFrame(master=app, width=250, height=200,)
frame10 = ctk.CTkFrame(master=app, width=250, height=200,)
frame20 = ctk.CTkFrame(master=app, width=250, height=200,)
frame20_0 = ctk.CTkFrame(master=app, width=250, height=200,)
frame01 = ctk.CTkFrame(master=app)
frame02 = ctk.CTkFrame(master=app, width=250, height=200,)
frame11 = ctk.CTkFrame(master=app, width=250, height=200,)
frame12 = ctk.CTkFrame(master=app, fg_color="transparent", width=250, height=200,)
frame21 = ctk.CTkFrame(master=app, width=250, height=200,)
frame22 = ctk.CTkFrame(master=app, width=250, height=200,)
frame00.grid(row=0, column=0)
frame10.grid(row=1, column=0, sticky="nwse")
frame20.grid(row=2,column=0)
frame01.grid(row=0, column=1)
frame02.grid(row=0, column=2, sticky="nwse")
frame11.grid(row=1,column=1, sticky="nwse")
frame12.grid(row=1, column=2)
frame21.grid(row=2, column=1)
frame22.grid(row=2, column=2)

#01

wensd = {
    0: "Понедельник",
    1: "Вторник",
    2: "Среда",
    3: "Четверг",
    4: "Пятница",
    5: "Суббота",
    6: "Воскресенье"
}
temir = ctk.CTkLabel(frame01, text="",
                        font=("Helvetica", 50))
dater = ctk.CTkLabel(frame01, text=f"{wensd[time.localtime().tm_wday]}, {time.localtime().tm_mday}.{time.localtime().tm_mon}",
                        font=("Helvetica", 30))
temir.pack(fill="both", expand=1)
dater.pack(side="bottom")
def apdate_time():
    sek = str(time.localtime().tm_sec)
    mine = str(time.localtime().tm_min)
    chas = str(time.localtime().tm_hour)
    if int(mine)==0:
        apdate_mas()
    if len(sek)==1:
        sek = "0"+sek
    if len(chas)==1:
        chas = "0"+chas
    if len(mine)==1:
        mine = "0"+mine

    temir.configure(text=f"{chas}:{mine}:{sek}")
    app.after(300, apdate_time)
def apdate_mas():
    day = str(time.localtime().tm_mday)
    man = str(time.localtime().tm_mon)
    if len(day)==1:
        day = "0"+day
    if len(man)==1:
        man = "0"+man
    dater.configure(text=f"{wensd[time.localtime().tm_wday]}, {day}.{man}")
apdate_time()
apdate_mas()


#02
frame02.grid_columnconfigure((0), weight=1)
frame02.grid_rowconfigure((0), weight=1)
textbox02 = ctk.CTkTextbox(frame02, activate_scrollbars=0, text_color=('lime'), width=250, height=200,)
textbox02.grid(sticky="nwse")


#10

fr1 = ctk.CTkFrame(frame10, width=10, height=50)
fr2 = ctk.CTkFrame(frame10, width=10, height=50)
fr3 = ctk.CTkFrame(frame10, width=10, height=50)
fr4 = ctk.CTkFrame(frame10, width=10, height=50)
fr5 = ctk.CTkFrame(frame10, width=10, height=50)
fr6 = ctk.CTkFrame(frame10, width=10, height=50)
fr7 = ctk.CTkFrame(frame10, width=10, height=50)
fr8 = ctk.CTkFrame(frame10, width=10, height=50)
fr9 = ctk.CTkFrame(frame10, width=10, height=50)
fr10= ctk.CTkFrame(frame10, width=10, height=50)
fr11 = ctk.CTkFrame(frame10, width=10, height=50)
fr12 = ctk.CTkFrame(frame10, width=10, height=50)
fr13 = ctk.CTkFrame(frame10, width=10, height=50)
fr14 = ctk.CTkFrame(frame10, width=10, height=50)
fr15 = ctk.CTkFrame(frame10, width=10, height=50)
r = 0
c = 0
frame10.grid_columnconfigure((0, 1,  2, 3, 4), weight=1)
frame10.grid_rowconfigure((0, 1, 2), weight=1)
for g in range(1, 16):
    eval(f'fr{g}.grid(row={r}, column={c},sticky="nwse")')
    c = c+1
    if c == 5:
        r = r+1
        c = 0


w = 60
for i in range(1, 16):
    eval(f"fr{i}.grid_columnconfigure((0), weight=1)")
l1 = ctk.CTkEntry(fr1, width=w) #, font=("algerian", 10)
l2 = ctk.CTkEntry(fr2, width=w)
l3 = ctk.CTkEntry(fr3, width=w)
l4 = ctk.CTkEntry(fr4, width=w)
l5 = ctk.CTkEntry(fr5, width=w)
l6 = ctk.CTkEntry(fr6, width=w)
l7 = ctk.CTkEntry(fr7, width=w)
l8 = ctk.CTkEntry(fr8, width=w)
l9 = ctk.CTkEntry(fr9, width=w)
l10 = ctk.CTkEntry(fr10, width=w)
l11 = ctk.CTkEntry(fr11, width=w)
l12 = ctk.CTkEntry(fr12, width=w)
l13 = ctk.CTkEntry(fr13, width=w)
l14 = ctk.CTkEntry(fr14, width=w)
l15 = ctk.CTkEntry(fr15, width=w)
def optionmenu_callback(choice, f):
    print()
    strok = str(f).split('.!')[2][8:]
    print(strok, choice[2:], choice.split(".")[0])
    funs.repost(int(choice.split(".")[0]),strok)

try:
    ret = funs.get_name()
except:
    funs._db()
    ret = funs.get_name()
valu=ret.split(" ")
valu.remove("")
widt=10
op1 = ctk.CTkOptionMenu(master=fr1,values=valu, command=optionmenu_callback,width=widt, variable=ctk.StringVar(value=funs.get_name_where(1)), fg_color="#434343", text_color="#c3c3c3")
op2 = ctk.CTkOptionMenu(master=fr2,values=valu, command=optionmenu_callback,width=widt, variable=ctk.StringVar(value=funs.get_name_where(2)), fg_color="#434343", text_color="#c3c3c3")
op3 = ctk.CTkOptionMenu(master=fr3,values=valu, command=optionmenu_callback,width=widt, variable=ctk.StringVar(value=funs.get_name_where(3)), fg_color="#434343", text_color="#c3c3c3")
op4 = ctk.CTkOptionMenu(master=fr4,values=valu, command=optionmenu_callback,width=widt, variable=ctk.StringVar(value=funs.get_name_where(4)), fg_color="#434343", text_color="#c3c3c3")
op5 = ctk.CTkOptionMenu(master=fr5,values=valu, command=optionmenu_callback,width=widt, variable=ctk.StringVar(value=funs.get_name_where(5)), fg_color="#434343", text_color="#c3c3c3")
op6 = ctk.CTkOptionMenu(master=fr6,values=valu, command=optionmenu_callback,width=widt, variable=ctk.StringVar(value=funs.get_name_where(6)), fg_color="#434343", text_color="#c3c3c3")
op7 = ctk.CTkOptionMenu(master=fr7,values=valu, command=optionmenu_callback,width=widt, variable=ctk.StringVar(value=funs.get_name_where(7)), fg_color="#434343", text_color="#c3c3c3")
op8 = ctk.CTkOptionMenu(master=fr8,values=valu, command=optionmenu_callback,width=widt, variable=ctk.StringVar(value=funs.get_name_where(8)), fg_color="#434343", text_color="#c3c3c3")
op9 = ctk.CTkOptionMenu(master=fr9,values=valu, command=optionmenu_callback,width=widt, variable=ctk.StringVar(value=funs.get_name_where(9)), fg_color="#434343", text_color="#c3c3c3")
op10 = ctk.CTkOptionMenu(master=fr10,values=valu, command=optionmenu_callback,width=widt, variable=ctk.StringVar(value=funs.get_name_where(10)), fg_color="#434343", text_color="#c3c3c3")
op11 = ctk.CTkOptionMenu(master=fr11,values=valu, command=optionmenu_callback,width=widt, variable=ctk.StringVar(value=funs.get_name_where(11)), fg_color="#434343", text_color="#c3c3c3")
op12 = ctk.CTkOptionMenu(master=fr12,values=valu, command=optionmenu_callback,width=widt, variable=ctk.StringVar(value=funs.get_name_where(12)), fg_color="#434343", text_color="#c3c3c3")
op13 = ctk.CTkOptionMenu(master=fr13,values=valu, command=optionmenu_callback,width=widt, variable=ctk.StringVar(value=funs.get_name_where(13)), fg_color="#434343", text_color="#c3c3c3")
op14 = ctk.CTkOptionMenu(master=fr14,values=valu, command=optionmenu_callback,width=widt, variable=ctk.StringVar(value=funs.get_name_where(14)), fg_color="#434343", text_color="#c3c3c3")


def renaem(ind):
    print(phone[0])
    mes = eval(f"l{ind}.get()")
    name[0], name[1] = ind, mes
    response = f"renaem {name[0]} {name[1]}"
    phone[0].sendall((response+ '\n').encode('utf-8'))
    print(name)
    eval(f"l{ind}.delete(first_index=0, last_index='end')")
    textbox02.focus_force()
for i in range(1,16):
    eval(f'l{i}.bind("<Return>", (lambda event: renaem({i})))')
    eval(f'l{i}.grid(row=0, column=0)')
    if i == 15:
        continue
    eval(f'op{i}.grid()')
    

def svet(yrov):
    phone[0].sendall((f'light1 {yrov}\n').encode('utf-8'))
    print((f'light1 {yrov}\n'))
    slider.set(yrov)


#11
frame11.grid_columnconfigure((0), weight=1)
frame11.grid_rowconfigure((0), weight=1)
textbox11 = ctk.CTkTextbox(frame11, activate_scrollbars=0,state='disabled', text_color=('lime'))
textbox11.grid(sticky="nwse")
entry = ctk.CTkEntry(frame11,fg_color="#1D1E1E")

def zapros_v_neiro(taxt, w):
        if w:
            prom = taxt[6:]
        else: 
            prom = taxt
        def vopros(prom):
                t = main.use_gemma3_1(prom)
                
                textbox11.configure(state='normal')
                textbox11.tag_config("start", foreground="white")
                
                if "say" in t:
                    phone[0].sendall((f'say\n').encode('utf-8'))
                    textbox11.tag_config("gg", foreground="#7518f0")
                    textbox11.insert('end',str(t+'\n'), "gg")
                elif "opentg" in t:
                    main.open_telega()
                    textbox11.tag_config("gg", foreground="#7518f0")
                    textbox11.insert('end',str(t+'\n'), "gg")
                elif t == "new_fail":
                    print("создан файл")
                else:
                    print(t)
                    speak(t)
                    textbox11.insert('end',str(t+'\n'), "start")
                textbox11.see("end")
        gemm = threading.Thread(target=vopros, args=(prom,))
        gemm.start()
def lo8l(l):
    taxt=entry.get()
    textbox11.configure(state='normal')
    textbox11.insert(text=taxt+"\n", index='end')
    textbox11.see("end")
    textbox11.configure(state='disabled')
    zapros = taxt.split(" ")[0]

    if zapros == "light1":
        svet(int(taxt.split(" ")[1])/100)
    elif zapros == "send1":
        if taxt.split(" ")[1] == "light1":
            svet(int(taxt.split(" ")[2])/100)
        else:
            print(taxt[6:]+"\n")
            try:
                phone[0].sendall((f'{taxt[6:]}\n').encode('utf-8'))
            except:
                print("Нет подключения")
    elif zapros == "say":
        phone[0].sendall((f'say\n').encode('utf-8'))
    elif zapros == "update":
        app.update()
        sdvig = app.winfo_x()
        # print(app.winfo_x())
        app.wm_attributes("-fullscreen",False)
        # print(app.winfo_x())
        app.geometry(f"1000x700+{1400}+100")
        
        print("update")
    elif zapros == "full":
        app.update()
        app.wm_attributes("-fullscreen",True)
    elif zapros == "gemma":
        zapros_v_neiro(taxt, True)
    elif zapros == "name":
        textbox11.configure(state='normal')
        textbox11.insert(text=str(ret+'\n'), index='end')
        textbox11.see("end")
        textbox11.configure(state='disabled')
    elif zapros == "send2":
        print(taxt[6:]+"\n")
        try:
            nout[0].sendall((f'{taxt[6:]}\n').encode('utf-8'))
        except:
            print("Нет подключения")
    else:  
        try:zapros_v_neiro(taxt, False) 
        except:print("Запрос неудался")
    entry.delete(0, "end")
entry.bind('<Return>', lo8l)

entry.grid(sticky="we")

#12

label = ctk.CTkLabel(frame12, text="tools      ",
                    fg_color="transparent",
                    font=("calibri", 17))

label.grid(row=0, column=0)
status_phone_indbkatr = ctk.CTkButton(frame12, text="",
                                    width=10, height=10,
                                    fg_color="#3c3c3c", hover=False)
status_phone_indbkatr.grid(row=0, column=1)

label = ctk.CTkLabel(frame12, text="nout      ",
                     fg_color="transparent",
                     font=("calibri", 17))
label.grid(row=1, column=0)
status_nout_indbkatr = ctk.CTkButton(frame12, text="",
                                     width=10, height=10,
                                     fg_color="#3c3c3c", hover=False)
status_nout_indbkatr.grid(row=1, column=1)

#20
def swape(val):
    print(val)
segemented_var = ctk.StringVar(value="Value 3")
segemented = ctk.CTkSegmentedButton(app, values=["tools"],
                                                     command=swape,
                                                     variable=segemented_var)

segemented.grid(row=2, sticky="n")
segemented.insert(index=1,value="bn")
def slider_event(value):
    print(value, end=" ")
    phone[0].sendall((f'light1 {value}\n').encode('utf-8'))


slider = ctk.CTkSlider(frame20, from_=0, to=1, command=slider_event,state="disabled", button_color='#cccccc', button_hover_color='#3c3c3c')

slider.grid()

#22
def ext():
    import os
    os._exit(0)
exit_but = ctk.CTkButton(frame22,text="EXET", command=ext, fg_color="#434343", hover_color="#202020")
exit_but.grid()
app.update()
def perenazn():
    sys.stdout = ConsoleOutput(textbox02)
    sys.stderr = ConsoleOutput(textbox02)
perenazn()
global standart_err
global standart_out
standart_out = sys.stdout
standart_err = sys.stderr
thread1 = threading.Thread(target=main_serv, args=(HOST, PORT))


thread0 = threading.Thread(target=start_discovery_beacon)

def zapusc_servera():
    thread0.start()
    thread1.start()
app.after(0, zapusc_servera)

def status_phone():
    if phone[1] == "j":
        status_phone_indbkatr.configure(fg_color="#3c3c3c")
        slider.configure(state="disabled")
        app.after(100, light_phone)
    else:
        app.after(100, status_phone)
def light_phone():
    if phone[1] != "j":
        slider.configure(state="normal")
        status_phone_indbkatr.configure(fg_color="#cccccc")
        slider.set(phone[1])
        print(phone)
        app.after(100, status_phone)
    else:
        app.after(100, light_phone)

app.after(100, light_phone)

def status_nout():
    if nout[0] == "j":
        status_nout_indbkatr.configure(fg_color="#3c3c3c")
        app.after(100, light_nout)
    else:
        app.after(100, status_nout)
def light_nout():
    if nout[0] != "j":
        status_nout_indbkatr.configure(fg_color="#cccccc")
        app.after(100, status_nout)
    else:
        app.after(100, light_nout)

app.after(100, light_nout)
app.mainloop()