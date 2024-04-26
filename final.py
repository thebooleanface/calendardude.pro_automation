from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from instagrapi import Client
import pyotp

#Generating image first
font = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf', 50)
now = datetime.now()

img = Image.new('RGB', (400,300), color='black')
draw = ImageDraw.Draw(img)

date_str = now.strftime('%B %d, %Y')
day_str = now.strftime('%A')

draw.text((50, 100), date_str, font=font, fill='white')
draw.text((50, 150), day_str, font=font, fill='white')

img.save(f'{date_str}.png')

#Uploading to Instagram
username = 'calendardude.pro' #your username
password = 'my password'
secret_key = ''

totp = pyotp.TOTP(secret_key)
current_otp = totp.now()

cl = Client()
cl.delay_range = [1, 10]
cl.load_settings("session.json")
cl.login(username, password, False, current_otp)
# cl.dump_settings("session.json")
cl.photo_upload(f"{date_str}.png", f"Today is {date_str} and it is a {day_str}. \n#calendar #calendargirl #calendarguy #calendar2024")