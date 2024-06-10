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

#image for percentage of year passed 
img2 = Image.new('RGB',(400,300),color='black')
draw = ImageDraw.Draw(img2)
red = (255,0,0,1)
white = (255,255,255,1)

cur = datetime.datetime.now()
start_of_year = datetime.datetime(cur.year,1,1)
days = (cur - start_of_year).days
end = datetime.datetime(cur.year, 12,31)
total = (end-start_of_year).days

perc = (days*300)/total

#the width of the rectangle is 300 pixels with start at 50 and end at 350
red_coords = ((50,100),(perc,150))
black_coords = ((perc,100),(300,150))

draw.rectangle(red_coords,fill=red)
draw.rectangle(black_coords,fill=black)

text = f"{perc/3} year is gone..."
text_coord =  (perc,160)
text_color = 'red'
font = ImageFont.truetype("Helvetica", 10)
draw.text(text_coord,text,fill='red',font=font)

img2.save('rectangle_image.png')

cl = Client()
cl.delay_range = [1, 10]
cl.load_settings("session.json")
cl.login(username, password, False, current_otp)
# cl.dump_settings("session.json")
cl.photo_upload(f"{date_str}.png", f"Today is {date_str} and it is a {day_str}. \n#calendar #calendargirl #calendarguy #calendar2024")
