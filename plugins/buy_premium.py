from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram import Client, filters

@Client.on_message(filters.command('buy_premium'))
async def buy_premium(_, message):
    text = """🎖️ PREMIUM MEMBERSHIP 🎖️

⚡ WE ARE HAPPY TO ANNOUNCE OUR BOT'S PREMIUM MEMBERSHIP FOR PREMIUM USERS IN CHEAP RATES ⚜️

🥶 BENEFITS OF IT:
👉 FREE MOVIES / SERIES
👉 NEW RELEASES ON SAME DAY
👉 WITHOUT ANY ADS
👉 EVERY LANGUAGE AVAILABLE

🥶 PRICE:
💸 ONLY 50₹ / Month

🚨 Contact @Simplifytuber2 to buy.
"""
    keyboard = InlineKeyboardMarkup([[  
        InlineKeyboardButton("🫰 Buy Premium 💸", url="https://t.me/Simplifytuber2")],  
        [InlineKeyboardButton("Cancel Premium", callback_data="close_data")]])
    await message.reply_text(text=text, reply_markup=keyboard)