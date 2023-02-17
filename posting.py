from instabot import Bot
import os
import shutil
import Gui
import resize as re

try:
    shutil.rmtree(r'./config')
except:
    pass

bot = Bot()
user = 'deadshort2020'
pas = 'pass@777'
text = 'first post!!!!'
bot.login(username=user, password=pas)


def posting(src):
    # print(src, "from posting.......")
    temp = re.resize(src)
    capt = Gui.gui(temp)
    bot.upload_photo(temp, caption=capt)
    # os.remove(src)
    try:
        dl = temp + '.REMOVE_ME'
        os.remove(dl)
    except:
        pass
    # temp = ""


# post_folder()
# posting("./Img_file/p.jpg")
