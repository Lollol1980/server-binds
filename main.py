import subprocess, os, pyautogui
from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import emoji
import keyboard
import sqlite3
import threading
import urllib.request

class funanul():
	def _db(self):
		data = [
		(1,"minecraft", "open_main()"),
		(2,"telegram", "open_telega()"),
		(3,"baiDPI", "open_bbDPI()"),
		(4,"rave", "open_Rave()"),
		(5,"sublime", "open_sublime()"),
		(6,"pause", "keyboard.send('Play/Pause')"),
		(7,"vol-", "keyboard.send('volume down')"),
		(8,"vol+", "keyboard.send('volume up')"),
		(9, "pass", "pass_()"),
		(10, "altUt", "open_bbDPIalt()"),
		(11, "splitLf", "keyboard.send('shift+left windows+left')"),
		(12, "splitRt", "keyboard.send('shift+left windows+right')"),
		(13, "left", "keyboard.send('left')"),
		(14, "right", "keyboard.send('right')"),
		]
		self.data = data
		data2 = [
		('but1', 1),
		('but2', 2),
		('but3', 3),
		('but4', 4),
		('but5', 5),
		('but6', 6),
		('but7', 7),
		('but8', 8),
		('but9', 9),
		('but10', 9),
		('but11', 9),
		('but12', 9),
		('but13', 9),
		('but14', 9)
		]
		
		promt = """ CREATE TABLE IF NOT EXISTS projects (
			id INTEGER PRIMARY KEY, 
			name text NOT NULL,
			def text NOT NULL
		);
		"""
		promt2 = """ CREATE TABLE IF NOT EXISTS sopost (
			name text NOT NULL,
			id INTEGER NOT NULL			
		);
		"""
		try:
			with sqlite3.connect(r"C:\pytonProgekt\server_bind\my12.db") as conn:
				cursor = conn.cursor()
				cursor.execute(promt)
				cursor.executemany("INSERT INTO projects VALUES(?, ?, ?)", data)
				conn.commit()
		except:
			print("база данных уже создана")
		try:
			with sqlite3.connect(r"C:\pytonProgekt\server_bind\my12.db") as conn:
				cursor = conn.cursor()
				cursor.execute(promt2)
				cursor.executemany("INSERT INTO sopost VALUES(?, ?)", data2)
				conn.commit()
		except:
			print("база данных уже создана")
			
	def get_name(self):
		with sqlite3.connect(r"C:\pytonProgekt\server_bind\my12.db") as conn:
			cursor = conn.cursor()
			cursor.execute("select name from projects")
			a = cursor.fetchall()
			ret = ''
			g = a[0][0]
			n = 1
			for i in a:
				ret=ret+str(n)+"."+i[0]+" "
				n +=1
			
			return(ret)
			# cursor.executemany("INSERT INTO projects VALUES(?, ?, ?)", data)
	def get_komand(self, com):
		with sqlite3.connect(r"C:\pytonProgekt\server_bind\my12.db") as conn:
			cursor = conn.cursor()
			cursor.execute("select def from projects where id = (?)", (com,))
			a = cursor.fetchall()
		ret = a[0][0]
		print(ret)
		return(ret)
	def ind(self, nam):
		with sqlite3.connect(r"C:\pytonProgekt\server_bind\my12.db") as conn:
			cursor = conn.cursor()
			cursor.execute("select id from sopost where name = (?)", (nam,))
			a = cursor.fetchall()
		ret = a[0][0]
		return(ret)
	def repost(self, _id, name):
		name = "but"+str(name)
		with sqlite3.connect(r"C:\pytonProgekt\server_bind\my12.db") as conn:
			cursor = conn.cursor()
			print(__file__)
			cursor.execute("update sopost set id = ? where name = ?", (_id, name))
	def name_com(self, name):
		return self.get_komand(self.ind(name))
	def get_name_where(self, name):
		name="but" + str(name)
		
		with sqlite3.connect(r"C:\pytonProgekt\server_bind\my12.db") as conn:
			cursor = conn.cursor()
			cursor.execute("select name from projects where id=?", (self.ind(name),))
			a = cursor.fetchall()
		return a[0][0]

	def dobavlen_komand(self,_id, name, komand):
		
		print(_id, name, komand)
		with sqlite3.connect(r"C:\pytonProgekt\server_bind\my12.db") as conn:
			cursor = conn.cursor()
			cursor.execute("insert into projects (id, name, def) values (?,?,?)", (_id, name, komand))
	def delete_komand(self, _id):
		with sqlite3.connect(r"C:\pytonProgekt\server_bind\my12.db") as conn:
			cursor = conn.cursor()
			cursor.execute("delete from projects where id=?", (_id,))
			

promt = [
        {'role': 'system', 'content': 'YOU ARE A HELPFUL ASSISTANT. YOUR ANSWERS MUST BE ONLY IN RUSSIAN AND. ОТВЕЧАЙ ТОЛЬКО НА РУССКОМ ЯЗЫКЕ.'},   
        {'role': 'user', 'content':"привет, как твои дела?"},
        {'role': 'assistant', 'content': 'ПРИВЕТ! У МЕНЯ ВСЕ ОТЛИЧНО, СПАСИБО! ЧЕМ МОГУ ПОМОЧЬ?'},
        {'role': 'system', 'content':"Ты можешь управлять вибрацией задав команду 'say', как только тебя попросили как либо повибрировать ты должен ответить только одно слово 'say' это цитата отвечай ей без кавыче без точек, точно так, как написано здесь"},
        {'role': 'user', 'content':"повибрируй пожалуйста"},
        {'role': 'assistant', 'content': 'say'},
        {'role': 'system', 'content': "ты можешь создать python файл командой 'new_fail', как только тебя попросили как либо создать файл ты должен ответить только одно слово 'new_fail' это цитата отвечай ей без кавыче без точек, точно так, как написано здесь"},
        {'role': 'user', 'content':'создай файл'},
        {'role': 'assistant', 'content': 'new_fail'},
        {'role': 'system', 'content':'ты можешь открывать телеграмм, как только тебя попросили открыть телеграмм, телегу, тг ты отвечаешь одним словом "opentg" это цитата, отвечай только словом, без переноса строки, без кавычек, только фраза'},
        {'role': 'user', 'content':"открой телеграмм"},
        {'role': 'assistant', 'content': 'opentg'},
        ]



import ollama
print("import norm")
def use_gemma3_1(prom):
	global promt
	promt.append({'role': 'user', 'content':prom})


	try:
		response = ollama.chat(model="gemma3:1b", messages=promt)  # Пример: генерация от 50 токенов
		promt.append({'role': 'assistant', 'content': response['message']['content']})
		return(response['message']['content'])
	except Exception as e:
		print(f"Произошла ошибка: {e}")



def open_main():
	try:
		subprocess.Popen('C:\\Users\\Llool\\AppData\\Roaming\\.minecraft\\TLauncher.exe')
	except:
		try:
			subprocess.Popen('D:\\Users\\Llool\\AppData\\Roaming\\.minecraft\\TLauncher.exe')
		except:
			print(8888)

def open_telega():
	try:
		subprocess.Popen('C:\\все загрузки\\Telegram Desktop\\Telegram.exe')
	except:
		try:
			subprocess.Popen('D:\\все загрузки\\Telegram Desktop\\Telegram.exe')
		except:
			print(8888)
def open_bbDPI():
	try:
		subprocess.run(['schtasks.exe', '/run', '/TN', 'GoodBayDPI'])
	except:
		print(8888)
def open_bbDPIalt():
	try:
		subprocess.run(['schtasks.exe', '/run', '/TN', 'altut'])
	except:
		print(8888)
def open_Rave():
	try: 
		subprocess.Popen('C:\\Users\\Llool\\AppData\\Local\\Programs\\rave-desktop\\Rave.exe')
	except:
		try: 
			subprocess.Popen('D:\\Users\\Llool\\AppData\\Local\\Programs\\rave-desktop\\Rave.exe')
		except:
			print(8888)
def open_sublime():
	try:
		print("open_sublime")
		subprocess.Popen('C:\\все загрузки\\Sublime Text\\sublime_text.exe')
	except:
		try:
			subprocess.Popen('D:\\все загрузки\\Sublime Text\\sublime_text.exe')
		except:
			print(8888)
def pass_():
	pass
bed = [0]
def scrcpy():
	global bed
	print(bed)
	if not bed[0]:
		print(bed)
		bed = [1]
		threa = threading.Thread(target=whait)
		threa.start()
		
	else:
		bed = [0]
def ext():
	os.system('shutdown -p')
def but(gg):
	eval(gg)
def vpn():
	os.startfile(r"D:\incy\incy\incy.exe")
def switch_f():
	response = urllib.request.urlopen('http://192.168.1.54/relay_switch')
	print(response.read().decode('utf-8'))
def switch():
	ts = threading.Thread(target=switch_f)
	ts.start()
def device():
    command = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, text=True, shell=False)
    if command.returncode != 0:
        print(f'Error receiving devices: {command.stderr}')
        return None
    result = command.stdout.strip().split('\n')
    devices = result[1:]
    devices = [device.replace('\tdevice', '') for device in devices]
    return (devices)
def whait():
	global bed
	while bed[0]:
		d = device()
		if not 'EMWWIZI7WWPBOZQ8' in d:
			pass
		else:
			break
	print("436 main ")
	bed = [0]
	re = subprocess.run(['python', r'C:\pytonProgekt\server_bind\prig.py'],creationflags=subprocess.CREATE_NO_WINDOW)
	

def bind_act():
	global inp
	from pynput import mouse
	f = []
	with mouse.Events() as events:
		for event in events:
			if str(event)[0] == "C"and str(event.button) == "Button.middle":
				inp[0] += 1
			if inp[0]==4:
				command = subprocess.run(['cmdow', '/T'], stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True,creationflags=subprocess.CREATE_NO_WINDOW)
				if command.returncode != 0:
					print(f'Error receiving devices: {command.stderr}')
				for wind in command.stdout.split('\n'):
					if wind.split()[4] == "Act":
						result = wind.split()[0]
						break
				if not result in f:
					command = subprocess.run(['cmdow', result, '/TOP'], stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True,creationflags=subprocess.CREATE_NO_WINDOW)
					f.append(result)
					print("TOP")
				else:
					command = subprocess.run(['cmdow', result, '/NOT'], stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True,creationflags=subprocess.CREATE_NO_WINDOW)
					f.remove(result)
					print("NOT")
				print(f)
				if command.returncode != 0:
					print(f'Error receiving devices: {command.stderr}')
				result = command.stdout
				print(result)
				inp = [1]
def zer():
	global inp
	while 1:
		time.sleep(0.4)
		inp = [1]

import time
global inp
inp = [1]
t1 = threading.Thread(target=zer)
t1.start()

t = threading.Thread(target=bind_act)
t.start()