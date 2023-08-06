from nonebot import on_command
from nonebot.params import CommandArg

from .converter import msg_convert,msg_deconvert

convert = on_command('兽音加密',aliases={'animalvoice','convert'}, priority=5, block=True)
deconvert = on_command('兽音解密',aliases={'deanimalvoice','deconvert'}, priority=5, block=True)

@convert.handle()
async def _handle(msg_input: CommandArg()):
    try:
        msg = msg_convert(msg_input)
    except Exception as e:
        await convert.finish("寄，加密失败了，报错为{}".format(e), reply_message=True) 
    await convert.finish("加密结果\n {}".format(msg), reply_message=True)


@deconvert.handle()
async def _handle(msg_input: CommandArg()):
    try:
        msg = msg_deconvert(msg_input)
    except Exception as e:
        await convert.finish("寄，加密失败了，报错为{}".format(e), reply_message=True) 
    await deconvert.finish("加密结果\n {}".format(msg), reply_message=True)
