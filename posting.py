from instabot import Bot
import os
bot = Bot()
import resize as re

user = 'deadshort2020'
pas = 'pass@777'
text = 'first post!!!!'

bot.login(username=user, password=pas)


def posting(src):
    try:
        bot.upload_photo(src, caption='form src')
        dl = src + '.REMOVE_ME'
        os.remove(dl)
    except:
        print("PHOTO NOT UPLOADED... MAY BE BECAUSE OF NOT COMPATIBLE ASPECT RATIO OF IMAGE...")
    print("done posting....")