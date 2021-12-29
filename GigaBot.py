import discord
import random
from config_for_GigaBot import settings


s = 0
common_case = [0, 0, 1, 1, 2, 2, 5]
all_case = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 10]
chip_case = [0, 0, 1, 1, 2] 
big_case = [0, 0, 0, 0, 1, 1, 2, 2, 2, 5, 5, 10] 
gold_case = [0, 0, 0, 0, 1, 1, 1, 2, 2, 5, 10]


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on ass', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
######################################################

        if message.content == '*Help':
            await message.channel.send('Привет! Мой разраб ленивый и потом добавит эту функцию! А пока можешь пооткрывать кейсы.')

################################Кейсы######################################################        
        if message.content == '>Обычный кейс':
            s = random.choice(common_case)
            if s == 0:
                await message.channel.send('Ты ничего не выиграл. Повезёт в следущий раз!')
            elif s == 1:
                await message.channel.send('Поздравляю! Ты выйграл 500 сыра!')
            elif s == 2:
                await message.channel.send('Поздравляю! Ты выйграл 750 сыра!')
            elif s  == 5:
                await message.channel.send('Поздравляю! Ты выйграл 1500 сыра!')

        if message.content == '>Всё или ничего':
            s = random.choice(all_case)
            if s == 0:
                await message.channel.send('Ты ничего не выиграл. Повезёт в следущий раз!')
            elif s == 1:
                await message.channel.send('Поздравляю! Ты выйграл 750 сыра!')
            elif s == 2:
                await message.channel.send('Поздравляю! Ты выйграл 1500 сыра!')
            elif s == 10:
                await message.channel.send('Поздравляю! Ты выйграл 10000 сыра!')
        
        if message.content == '>Дешевый кейс':
            s = random.choice(chip_case)
            if s == 0:
                await message.channel.send('Ты ничего не выиграл. Повезёт в следущий раз!')
            elif s == 1:
                await message.channel.send('Поздравляю! Ты выйграл 300 сыра!')
            elif s == 2:
                await message.channel.send('Поздравляю! Ты выйграл 500 сыра!') 
       
        if message.content == '>Большой кейс':
            s = random.choice(big_case)
            if s == 0:
                await message.channel.send('Ты ничего не выиграл. Повезёт в следущий раз!')
            elif s == 1:
                await message.channel.send('Поздравляю! Ты выйграл 750 сыра!')
            elif s == 2:
                await message.channel.send('Поздравляю! Ты выйграл 1500 сыра!')
            elif s == 5:
                await message.channel.send('Поздравляю! Ты выйграл 3000 сыра!')
            elif s == 10:
                await message.channel.send('Поздравляю! Ты выйграл 5000 сыра!')
        
        if message.content == '>Золотой кейс':
            s = random.choice(gold_case)
            if s == 0:
                await message.channel.send('Ты ничего не выиграл. Повезёт в следущий раз!')
            elif s == 1:
                await message.channel.send('Поздравляю! Ты выйграл 1000 сыра!')
            elif s == 2:
                await message.channel.send('Поздравляю! Ты выйграл 5000 сыра!')
            elif s == 5:
                await message.channel.send('Поздравляю! Ты выйграл 15000 сыра!')
            elif s == 10:
                await message.channel.send('Поздравляю! Ты выйграл 50000 сыра!')
         
              
####################Рофлеки##################################        
#        if message.content == 'F*ck you':
#            await message.channel.send('Oh, fuck you leather man')

#        if message.content == 'Чё':
#            await message.channel.send('https://c.tenor.com/wE8ie6blvPYAAAAM/white-guy.gif')
#        if message.content == 'чё':
#            await message.channel.send('https://c.tenor.com/wE8ie6blvPYAAAAM/white-guy.gif')
#        if message.content == 'че':
#            await message.channel.send('https://c.tenor.com/wE8ie6blvPYAAAAM/white-guy.gif')
        if message.content == 'Че':
            await message.channel.send('https://c.tenor.com/wE8ie6blvPYAAAAM/white-guy.gif')
        if message.content == 'Каво':
            await message.channel.send('https://c.tenor.com/wE8ie6blvPYAAAAM/white-guy.gif')
#        if message.content == 'каво':
#            await message.channel.send('https://c.tenor.com/wE8ie6blvPYAAAAM/white-guy.gif')
        
        if message.content == 'Mmm':
            await message.channel.send('https://c.tenor.com/Qjj6UpIi2AYAAAAM/gachi-oh-shit-a-am-sorry.gif')
#        if message.content == 'mmm':
#            await message.channel.send('https://c.tenor.com/Qjj6UpIi2AYAAAAM/gachi-oh-shit-a-am-sorry.gif')
        
        
#        if message.content == "Let's celebrate":
#            await message.channel.send('https://tenor.com/view/celebrate-gachi-gif-21919560')

#        if message.content == 'f*ck you':
#            await message.channel.send('https://tenor.com/view/slave-gachimuchi-van-triggered-billy-gif-21373549')

#        if message.content == 'come on college boy':
#           await message.channel.send('https://tenor.com/view/gachi-%D1%8F%D0%BC%D0%B0%D1%82%D0%BE-gif-18078141')
#        if message.content == 'Come on college boy':
#            await message.channel.send('https://tenor.com/view/gachi-%D1%8F%D0%BC%D0%B0%D1%82%D0%BE-gif-18078141')
        if message.content == 'Shut up and take my money':
            await message.channel.send(' https://tenor.com/view/money-dollars-cash-rich-shut-up-and-take-my-money-gif-3555042')

##        if message.content == 'диз':
##            await message.channel.send("""
##🟥🟥🟥🟥🟥🟥
##🟥⬜⬜🟥⬜🟥 
##🟥⬜⬜🟥⬜🟥
##🟥🟥⬜🟥🟥🟥
##🟥🟥🟥🟥🟥🟥 
##""")
##        if message.content == 'Диз':
##            await message.channel.send("""
##🟥🟥🟥🟥🟥🟥
##🟥⬜⬜🟥⬜🟥 
##🟥⬜⬜🟥⬜🟥
##🟥🟥⬜🟥🟥🟥
##🟥🟥🟥🟥🟥🟥 
##""")

##        if message.content == 'лайк':
##            await message.channel.send('''
##🟩🟩🟩🟩🟩🟩 
##🟩🟩⬜🟩🟩🟩 
##🟩⬜⬜🟩⬜🟩 
##🟩⬜⬜🟩⬜🟩 
##🟩🟩🟩🟩🟩🟩
##''')
##        if message.content == 'Лайк':
##            await message.channel.send('''
## 🟩🟩🟩🟩🟩🟩 
## 🟩🟩⬜🟩🟩🟩 
## 🟩⬜⬜🟩⬜🟩 
## 🟩⬜⬜🟩⬜🟩 
## 🟩🟩🟩🟩🟩🟩
## ''')
##        if message.content == '':
##            await message.channel.send('')



bot = MyClient()
bot.run(settings['token'])
