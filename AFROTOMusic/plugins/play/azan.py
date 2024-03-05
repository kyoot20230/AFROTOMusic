import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types
from AFROTOMusic import app
import random
from datetime import datetime
import requests
import pytz
from AFROTOMusic.core.call import Zelzaly
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AFROTOMusic.core.call import Zelzaly
from AFROTOMusic.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)
from pyrogram.errors import (
    ChatAdminRequired,
    UserAlreadyParticipant,
    UserNotParticipant,
)

tz = pytz.timezone('Africa/Cairo')

chat = []

@app.on_message(filters.text & ~filters.private, group = 20)
async def azaan(c, msg):
  if msg.text == "تفعيل الاذان":
    if msg.chat.id in chat:
      return await msg.reply_text("- الاذان متفعل هنا من قبل 🥰♥️")
    else:
      chat.append(msg.chat.id)
      return await msg.reply_text("تم تفعيل الاذان ♥️🌿")
  elif msg.text == "تعطيل الاذان":
    if msg.chat.id in chat:
      chat.remove(msg.chat.id)
      return await msg.reply_text("تم تعطيل الاذان ♥️🌿")
    else:
      return await msg.reply_text("- الاذان متعطل هنا من قبل 🥰♥️")
      
async def kill():
  for i in chat:
    await Zelzaly.force_stop_stream(i)


async def play(i):
  assistant = await group_assistant(Zelzaly,i)
  file_path = "AFROTOMusic/assets/azan.m4a"
  stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
  try:
      await assistant.join_group_call(
           i,
           stream,
           stream_type=StreamType().pulse_stream,
      )
  except NoActiveGroupCall:
    try:
        await Zelzaly.join_assistant(i,i)
    except Exception as e:
       await app.send_message(i,f"{e}")
  except TelegramServerError:
    await app.send_message(i,"في خطا ف سيرفرات التليجرام")
  except AlreadyJoinedError:
    await kill()
    try:
        await assistant.join_group_call(
           i,
           stream,
           stream_type=StreamType().pulse_stream,
        )
    except Exception as e:
        await app.send_message(i,f"{e}")
    
           
       
def get_prayer_times(city):
    prayer_times = {}
    try:
        response = requests.get(f"http://api.aladhan.com/timingsByAddress?address={city}&method=4&school=0")
        data = response.json()
        prayer_times = data['data']['timings']
    except Exception as e:
        print(e)
    return prayer_times

def check_current_prayer(prayer_times):
    current_time = datetime.now(pytz.timezone('Africa/Cairo')).strftime('%I:%M %p')
    for prayer, time in prayer_times.items():
        prayer_time = datetime.strptime(time, '%H:%M').strftime('%I:%M %p')
        if current_time == prayer_time:
            return prayer
    return None

def main():
    try:
        city = "Cairo"
        prayer_times = get_prayer_times(city)
        current_prayer = check_current_prayer(prayer_times)
        if current_prayer:
            print("حان الآن وقت صلاة:", current_prayer)
        else:
            print("لا يوجد صلاة في هذا الوقت.")
    except Exception as e:
        print(e)
#لالالالا
# جتة مواعيد الصلاة الي تحت دي سارقها من هلال علشان م بعرف استخدم مكتبة ال time ف انضموا لقناته @SOURCEFR3ON

async def azkar():
  while not await asyncio.sleep(2):
    if prayer_time():
     prayer = prayer_time()
     await kill()
     for i in chat:
       await app.send_message(i, f"حان الان وقت اذان {prayer} بتوقيت القاهرة 🥰♥️")
       await play(i)
     await asyncio.sleep(174)
     await kill()
#مواعيد الصلاه بس الي سارقها بقيت الكود كتابتي هي اكيد كتابه معاقه بس عادي م مهم رايك انا مبسوط بيها يوزري للاعمال الخاصه @z0hary

        
