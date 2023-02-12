from rich.console import Console
from rich.panel import Panel
from time import sleep as s
import requests, sys, os, time, random
from random import choice as rc

opsi = {'batu':'batu','gunting':'gunting','kertas':'kertas'}

kalah = [['batu','kertas'],['kertas','gunting'],['gunting','batu']]
menang = [['kertas','batu'],['gunting','kertas'],['batu','gunting']]
imbang = [['batu','batu'],['gunting','gunting'],['kertas','kertas']]

def proccess():
    for i in list("\|/-"):
        print(f"\r\033[0;97m[\033[0;92m{i}\033[0;97m] sedang mengetik...",end="")
        time.sleep(0.5)
        
def game():
	os.system("clear")
	while True:
		com = rc(list(opsi.values()))
		print(f"\n")
		print("   \033[0;97mbatu - gunting - kertas - ( stop )")
		pesan = input(f'     \033[1;90mKetik pesan\r \033[1;91m>\033[1;92m ')
		print('\033[4A');Console().print(Panel('[white]'+pesan, style='green'), justify='right')
		if pesan in ["stop","Stop"]:exit()
		pilihan = [opsi[pesan],com]
		if pilihan in kalah:
			print(f"\n");proccess()
			print('\033[3A');Console().print(Panel('[white]'+"kakak memilih "+pesan+" dan simi memilih "+com+" kakak kalah\n", style='purple'), justify='left')
		elif pilihan in menang:
			print(f"\n");proccess()
			print('\033[3A');Console().print(Panel('[white]'+"kakak memilih "+pesan+" dan simi memilih "+com+" kakak menang\n", style='purple'), justify='left')
		elif pilihan in imbang:
			print(f"\n");proccess()
			print('\033[3A');Console().print(Panel('[white]'+"kakak memilih "+pesan+" dan simi memilih "+com+" imbang\n", style='purple'), justify='left')


game()
			
			
				