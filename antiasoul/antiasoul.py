import os
import random
import aiohttp
from hoshino import R, Service, util
from hoshino.config import RES_DIR

sv = Service('antiasoul', help_='嘉心糖滚出去')

antiasoul = os.path.join(os.path.expanduser(RES_DIR), 'img', 'asoul')

@sv.on_keyword(('然然','嘉然','的捏'))
async def qks_keyword(bot, ev):
    asoulimg = random.choice(os.listdir(antiasoul))
    msg = f'嘉❤糖滚出去\n'
    try:
        jiaranimg = R.img(f'asoul/{asoulimg}').cqcode
        msg += str(jiaranimg)
    except Exception as e:
        hoshino.logger.error(f'读取反嘉然的图片时发生错误{type(e)}')
    await bot.send(ev, msg, at_sender=True)
    await util.silence(ev, 60)