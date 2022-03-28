import instaloader
import os
import platform
import time
import shutil

l = instaloader.Instaloader()
il = instaloader
run = False

def byHashtag():
    clearScreen()
    print('Informe a hashtag abaixo')
    hashtagName = input('#')
    x = input('Deseja salvar quantos posts? ')
    x = int(x)
    y = 0
    hashtag = il.Hashtag.from_name(l.context, hashtagName)
    for post in hashtag.get_posts():
        if y < x:
            l.download_post(post, "#"+hashtag.name)
            y += 1
        else:
            delExtras('#'+hashtagName)
            print('Posts salvos com sucesso!')
            time.sleep(2)
            break
    main()

def byProfile():
    clearScreen()
    print('Informe o perfil abaixo')
    userName = input('@')
    x = input('Deseja salvar quantos posts? ')
    x = int(x)
    y = 0
    profile = il.Profile.from_username(l.context, userName).get_posts()
    for post in profile:
        if y < x:
            l.download_post(post, '@'+userName)
            y += 1
        else:
            delExtras('@'+userName)
            print('Posts salvos com sucesso!')
            time.sleep(2)
            break
    main()

def delExtras(folderName):
    folder = folderName
    if platform.system() == 'Windows':
        os.system('del /f /q "'+folder+'\*.xz"')
        os.system('del /f /q "'+folder+'\*.txt"')
    else:
        return

def clearScreen():
    if platform.system() == 'Windows':
        os.system('cls')
        banner()
    else:
        os.system('Clear')
        banner()

def banner():
    print('######################################################################################')
    print('#   ________      ___.         .__       .__    ____   ____.__                       #')
    print('#  /  _____/_____ \_ |_________|__| ____ |  |   \   \ /   /|__|____    ____ _____    #')
    print('# /   \  ___\__  \ | __ \_  __ \  |/ __ \|  |    \   Y   / |  \__  \  /    \\__  \    #')
    print('# \    \_\  \/ __ \| \_\ \  | \/  \  ___/|  |__   \     /  |  |/ __ \|   |  \/ __ \_ #')
    print('#  \______  (____  /___  /__|  |__|\___  >____/    \___/   |__(____  /___|  (____  / #')
    print('#         \/     \/    \/              \/                          \/     \/     \/  #')
    print('######################################################################################')
    print('#                                                                                    #')
    print('#                    INSTASAVER - AUTOMATIC INSTAGRAM POSTS SAVER                    #')
    print('#                                                                                    #')
    print('######################################################################################')
    print('\n')

def opcao():
    clearScreen()
    print('Baixar posts por:')
    print('1 - Perfil')
    print('2 - Hashtag')
    print('3 - Sair')
    global op
    op = input('\nDigite o número referente a opcao desejada: ')

def main():
    opcao()
    
    while op != '1' and op != '2' and op != '3':
        print('Opcao invalida!')
        print('Reiniciando em 3...')
        time.sleep(1)
        print('Reiniciando em 2...')
        time.sleep(1)
        print('Reiniciando em 1...')
        time.sleep(1)
        opcao()

    if op == '1':
        byProfile()
    elif op == '2':
        byHashtag()

login = input('Login: ')
passw = input('Password: ')
l.login(login,passw)
main()