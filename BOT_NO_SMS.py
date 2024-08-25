import discord
from requests import post
from datetime import datetime
from discord.ext import commands
import youtube_dl
import nextcord
from nextcord.ext import commands
import asyncio
import json
import requests
import logging
import nextcord


logging.basicConfig(filename='bot.log', level=logging.INFO)

# from keepAlive import keep_alive

PREFIX = '!'
TOKEN = 'ใส่โทเค่น'  # โทเค่น
bot = commands.Bot(command_prefix=PREFIX,
                   help_command=None,
                   intents=discord.Intents.all())
@bot.event
async def on_connect():
    print(f"Login Bot Name : {bot.user.name}#{bot.user.discriminator}")
    logging.info(f"Login Bot Name : {bot.user.name}#{bot.user.discriminator}")

@bot.event
async def on_ready():
    activity = discord.Game(name="KOKO SHOP", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
print("""

██╗  ██╗ ██████╗ ██╗  ██╗ ██████╗     ███████╗██╗  ██╗ ██████╗ ██████╗ 
██║ ██╔╝██╔═══██╗██║ ██╔╝██╔═══██╗    ██╔════╝██║  ██║██╔═══██╗██╔══██╗
█████╔╝ ██║   ██║█████╔╝ ██║   ██║    ███████╗███████║██║   ██║██████╔╝
██╔═██╗ ██║   ██║██╔═██╗ ██║   ██║    ╚════██║██╔══██║██║   ██║██╔═══╝ 
██║  ██╗╚██████╔╝██║  ██╗╚██████╔╝    ███████║██║  ██║╚██████╔╝██║     
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                                                                    
        """)

logging.info("Bot is online.")

@bot.event
async def on_command_error(ctx, error):
    print(str(error))
    logging.error(str(error))


@bot.command()
async def help(ctx):
    embed = discord.Embed(
    title=f"KOKO SHOP", # ไม่ใส่ก็ได้
    description=
    f" \nสถานะบอท\n```สามารถใช้งานได้ตอนที่เจ้าของบอทเปิดเท่านั้น```\nคำสั่งข้อความ\n```!messages @ชื่อผู้ใช้ จำนวน``````!set_message @ชื่อผู้ใช้ จำนวน ข้อความที่ต้องการ```\nเช็คราคาคริปโต\n```!price เหรียญที่ต้องการ```\nเช็คกำไรคริปโต\n```!currentprice จำนวนเหรียญ ราคาซื้อ เหรียญอะไร```\nโปรโหมด\n```!create ชื่อช่อง ข้อความ```\nยิงNGL\n```!ngl ชื่อผู้ใช้  ข้อความ จำนวน```",
    color=0x0eff00,
    timestamp=datetime.utcnow())
    embed.set_thumbnail(url='https://cdn3.emoji.gg/emojis/5171-verify-green.gif')  #ไม่ใส่ก็ได้
    embed.set_author(name='')  # ไม่ใส่ก็ได้
    ima = "https://cdn.discordapp.com/attachments/1059034383266349158/1080874429682302976/how_to_use_bot_free.gif"
    embed.set_image(url=ima)
    await ctx.reply(embed=embed)
    # embed = discord.Embed(description=f"❌ | กรุณาใส่ข้อมูลให

      #ส่งข้อความ
@bot.command()
async def set_message(ctx, target: discord.Member, count: int, *, messages: str):
    """
    ฟังก์ชันนี้ใช้สำหรับส่งข้อความไปยังสมาชิก Discord ที่ระบุ

    Parameters:
    - ctx (commands.Context): ข้อมูล context ของคำสั่ง
    - target (discord.Member): สมาชิก Discord ที่ต้องการส่งข้อความ
    - count (int): จำนวนข้อความที่ต้องการส่ง
    - messages (str): ข้อความที่ต้องการส่ง

    Returns:
    - None
    """
    try:
        # ตรวจสอบว่ามีสมาชิก Discord ที่ระบุหรือไม่
        if not target:
            await ctx.send("❌ ไม่พบผู้ใช้งานนี้")
            return

        # ตรวจสอบว่าจำนวนข้อความมีค่ามากกว่า 0 หรือไม่
        if count < 1:
            await ctx.send("❌ โปรดระบุจำนวนข้อความที่มากกว่า 0")
            return

        # ส่งข้อความไปยังสมาชิกที่ระบุตามจำนวนที่ระบุ
        for _ in range(count):
            await target.send(messages)

        # ส่งข้อความยืนยันการส่งเสร็จสมบูรณ์
        await ctx.send(f"✅ ส่งข้อความถึง {target.mention} สำเร็จทั้งหมด {count} ข้อความ")

    except discord.Forbidden:
        # ถ้าบอทไม่มีสิทธิ์ส่งข้อความ
        await ctx.send("❌ บอทไม่มีสิทธิ์ส่งข้อความถึงสมาชิกนี้")

    except Exception as e:
        # หรือจะประมวลผล exception อื่นๆ ตามที่คุณต้องการ
        await ctx.send(f"❌ เกิดข้อผิดพลาด: {e}")




@bot.command()
async def messages(ctx, target: discord.Member, count: int):
    embed = discord.Embed(
        title="KOKO SHOP",
        description="ประกาศจาก KOKO SHOP",
        color=discord.Color.purple(),
    )
    embed.add_field(name="[+] เเจกเว็ปไชต์", value="ผมจะมีแจก src เว็ปไซต์เรื่อยๆติดตามไว้เลย")
    embed.add_field(name="[+] เเจกออนเม็ดม่วง", value="ตัวนี้ผมจะลงให้เรื่อยๆนะครับเนื่องจากมีหลายรูปแบบ")
    embed.add_field(name="[+] แจกบอทยิงเบอร์", value="ตัวนี้เป็นบอทยิงเบอร์แต่ผมจะแจกยก SRC")
    embed.add_field(name="[+] แจกบอทสเปมข้อความ", value="บอทสเปมคือบอทตัวนี้เลยครับ")
    embed.add_field(name="[+] แจกโปรแกรม ต่าง", value="แจกทุกโปรแกรมที่ผมหามาได้")
    embed.add_field(name="[+] พูดคุย", value="ห้องนี้สำหรับคนขี้เหงา")
    embed.add_field(name="[+] หาเพือน", value="ห้องนี้ใช้สำหรับหาเพื่อนหาแฟนนะครับ")
    embed.add_field(name="[+] เช็คไวรัส", value="เว็ปไชต์เช็คไวรัส")
    embed.add_field(name="[+] เว็ปต่าง", value="เช็คที่จะทำให้ชีวิตคุณสบายมากยิ่งขึ้น")
    embed.add_field(name="[+] ปั้มผู้ติดตาม", value="บอทปั้มผู้ติดตาม,เว็ปปั้มต่างๆ")
    embed.add_field(name="[+] ยิงNGL", value="ยิงNGL")
    embed.add_field(name="Discord: https://discord.gg/ft4bg4ZySV", value="ยินดีต้อนรับทุกคนนะค้าบ")

    # Add more fields as needed

    if count < 1:
        await ctx.send("❌ โปรดระบุจำนวนข้อความที่มากกว่า 0")
        return

    for _ in range(count):
        await target.send(embed=embed)

    await ctx.send(f"✅ ส่งข้อความถึง {target.mention} สำเร็จทั้งหมด {count} ข้อความ")

   
@bot.command()
async def play(ctx, url):
    voice_channel = ctx.author.voice.channel
    if voice_channel:
        vc = await voice_channel.connect()

        # Download audio from YouTube using youtube_dl
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        # Create YoutubeDL object
        ydl = youtube_dl.YoutubeDL(ydl_opts)

        # Extract information
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']

        # Play audio in the voice channel
        vc.play(nextcord.FFmpegPCMAudio(url2), after=lambda e: print('done', e))
    else:
        await ctx.send("You are not in a voice channel.")

@bot.command()
async def stop(ctx):
    voice_channel = ctx.voice_client
    if voice_channel:
        await voice_channel.disconnect()

#เช็คราคาคริปโต
@bot.command(name='price')
async def crypto_price(ctx, symbol):
    price = get_crypto_price(symbol)
    
    if price is not None:
        embed = Embed(
            title=f"ราคา {symbol.upper()}",
            description=f"ราคา {symbol.upper()} ณ ตอนนี้คือ ${price}",
            color=0x00ff00,
            timestamp=datetime.utcnow(),
        )
        embed.add_field(name="ตลาด", value="Crypto Market", inline=False)
        embed.add_field(name="สถานะ", value="ปกติ", inline=False)
        embed.set_author(name="Crypto Price Bot", icon_url="https://cdn.discordapp.com/attachments/1033470702659043399/1178198325338570762/png-clipart-nem-litecoin-blockchain-virtual-currency-coin-nem-coin-removebg-preview.png?ex=657545b2&is=6562d0b2&hm=18929031a52b07982f2bca8029650cbe7991f9c5b497c3f5de43f050349b078c&")  # แทนที่ URL ด้วยลิงก์รูปภาพไอคอนบอท
        embed.set_image(url=f"https://cdn.discordapp.com/attachments/1033470702659043399/1178203474828210176/standard.gif?ex=65754a7e&is=6562d57e&hm=82020679bc90d5a6e21c0dc401aa8c59b8b838f1d0cc669f0ca760935e34f5a0&")  # Set image URL here
        await ctx.reply(embed=embed)
    else:
        embed = Embed(
            title="เกิดข้อผิดพลาด",
            description=f"ไม่สามารถดึงข้อมูลราคา {symbol.upper()} ได้",
            color=0xff0000,
            timestamp=datetime.utcnow(),
        )
        await ctx.reply(embed=embed)

def get_crypto_price(symbol):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=thb'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        return data.get(symbol, {}).get('thb')  # ปรับค่าเงินที่ต้องการ
    else:
        return None

@bot.command(name='currentprice')
async def calculate_current_price(ctx, amount: float, buy_price_thb: float, coin_symbol: str):
    # Get current price of the cryptocurrency
    current_price = get_crypto_price(coin_symbol)

    if current_price is not None:
        # Calculate current value and profit/loss
        current_value = current_price * amount
        profit_loss = calculate_profit_loss(current_value, buy_price_thb)
        profit_loss_percentage = (profit_loss / buy_price_thb) * 100

        # Determine if it's profit or loss
        profit_text = "กำไร" if profit_loss >= 0 else "ขาดทุน"
        profit_amount_text = f"{profit_text}: ฿{abs(profit_loss):,.2f}"

        # Create an Embed to display the result
        embed = Embed(
            title=f"การคำนวณราคาปัจจุบัน {coin_symbol.upper()}",
            description=f"จำนวน: {amount:.4f}\nราคาซื้อ: ฿{buy_price_thb:.2f}\nราคาปัจจุบัน: ฿{current_value:.2f}\n{profit_amount_text} ({profit_loss_percentage:.2f}%)",
            color=0x00ff00 if profit_loss >= 0 else 0xff0000,
            timestamp=datetime.utcnow(),
        )

        # Additional details
        embed.set_thumbnail(url=f"https://www.coingecko.com/coins/{coin_symbol.lower()}/icon/large.png")
        embed.set_footer(text=f"For more information, visit [CoinGecko](https://www.coingecko.com/en/coins/{coin_symbol.lower()})")

        await ctx.reply(embed=embed)
    else:
        # If unable to fetch cryptocurrency data
        embed = Embed(
            title="เกิดข้อผิดพลาด",
            description=f"ไม่สามารถดึงข้อมูลราคา {coin_symbol.upper()} ได้",
            color=0xff0000,
            timestamp=datetime.utcnow(),
        )
        await ctx.reply(embed=embed)

def get_crypto_price(identifier):
    url_symbol = f'https://api.coingecko.com/api/v3/simple/price?ids={identifier}&vs_currencies=thb'
    url_name = f'https://api.coingecko.com/api/v3/simple/price?vs_currencies=thb&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&ids={identifier}'

    response_symbol = requests.get(url_symbol)
    response_name = requests.get(url_name)

    if response_symbol.status_code == 200 and response_name.status_code == 200:
        data_symbol = json.loads(response_symbol.text)
        data_name = json.loads(response_name.text)

        # Use Symbol if available, otherwise use Name
        if identifier in data_symbol:
            return data_symbol[identifier].get('thb')
        elif identifier in data_name:
            return data_name[identifier].get('usd')

    return None

def calculate_profit_loss(current_value, buy_price_thb):
    return current_value - buy_price_thb

#ส่งข้อความทั้งหมด
@bot.command()
async def dmall(ctx, *, msg):
    successful_sends = 0
    unsuccessful_sends = 0

    for m in ctx.guild.members:
        try:
            await asyncio.sleep(1)
            await m.send(msg)
            print(f"ข้อความที่ส่งถึง {m}")
            successful_sends += 1
        except Exception as e:
            print(f"ไม่สามารถส่งข้อความถึง {m} โดยเนื่องจาก: {str(e)}")
            unsuccessful_sends += 1

    # เว้นบรรทัดใหม่
    result_embed = discord.Embed(
        title="ส่งข้อความทั้งหมด",
        description=f"ส่งข้อความสำเร็จไปที่ {successful_sends} คน ✅ \nไม่สำเร็จที่ {unsuccessful_sends} คน ❌",
        color=0x00ff00 if successful_sends > 0 else 0xff0000
    )

    # เพิ่มรูปภาพใน Embed
    result_embed.set_image(url="https://cdn.discordapp.com/attachments/1160805861975937121/1166388821923999784/standard.gif?ex=65b90d3d&is=65a6983d&hm=4f8933f2bfa8a6874599cc7551c7ddba30453b30d13b4eb283b7ae281696bb4b&")

    # ส่ง Embed
    await ctx.send(embed=result_embed)

GUILD_ID = 1160805859467730964  # Replace with your actual guild ID
CATEGORY_ID = 1252138863368081420  # Replace with your actual category ID
ROLE_ID = 1252138982607683605  # Replace with your actual role ID

created_channels = {}  # ประกาศตัวแปรนี้เพื่อให้สามารถใช้งานในทุกๆ ฟังก์ชันได้

@bot.command(name="create", description="Create a new channel with a message")
async def create(ctx, channel_name: str, message: str):
    guild = ctx.guild
    member = ctx.author

    role = nextcord.utils.get(guild.roles, id=ROLE_ID)
    if role not in member.roles:
        await ctx.send("ต้องมียศถึงจะใช้คำสั่งนี้ได้.")
        return

    # Check if the member has already created a channel
    if member.id in created_channels:
        await ctx.send("สร้างได้เพียงช่องเดียวเท่านั้น.")
        return

    category = nextcord.utils.get(guild.categories, id=CATEGORY_ID)
    if category is None:
        await ctx.send(f"ไม่พบหมวดหมู่ที่มีไอดี '{CATEGORY_ID}'.")
        return

    new_channel = await guild.create_text_channel(channel_name, category=category)
    await new_channel.send(message)

    created_channels[member.id] = new_channel.id

    await ctx.send(f"สร้างช่องเรียบร้อยแล้ว: '{channel_name}' ข้อความในช่อง: {message}")


#NGL
@bot.command()
async def ngl(ctx, nglusername: str = None, message: str = None, count: int = None):
    # ตรวจสอบว่ามีข้อมูลครบถ้วนหรือไม่
    if nglusername is None or message is None or count is None or count <= 0:
        missing_info = []
        if nglusername is None:
            missing_info.append("ชื่อผู้ใช้")
        if message is None:
            missing_info.append("ข้อความ")
        if count is None or count <= 0:
            missing_info.append("จำนวนครั้ง (ต้องมากกว่า 0)")
        
        await ctx.send(f"กรุณาระบุ {'และ'.join(missing_info)} ให้ครบถ้วน.")
        return

    headers = {
        'Host': 'ngl.link',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://ngl.link',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': f'https://ngl.link/{nglusername}',
        'accept-language': 'en-US,en;q=0.9',
    }

    data = {
        'username': nglusername,
        'question': message,
        'deviceId': '0',
        'gameSlug': '',
        'referrer': '',
    }

    value = 0
    notsend = 0
    while value < count:
        response = requests.post('https://ngl.link/api/submit', headers=headers, data=data)
        if response.status_code == 200:
            value += 1
        else:
            notsend += 1
            await ctx.send("ส่งข้อความไม่สำเร็จ ❌ ")

        if notsend == 10:
            await ctx.send("ไม่สามารถส่งข้อความได้ติดต่อกัน 10 ครั้ง กำลังรอ 5 วินาที...")
            time.sleep(5)
            notsend = 0

    if value == count:
        await ctx.send(f"ส่งข้อความ '{message}' ไปยัง '{nglusername}' จำนวน {count} ครั้ง สำเร็จ ✅ ") 

# keep_alive()
bot.run(TOKEN, reconnect=True)