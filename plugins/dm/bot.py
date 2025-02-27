import os
import requests
import weasyprint
import urllib.request
from presets import Presets
from bs4 import BeautifulSoup
from fpdf import FPDF
from pdf import PROCESS
from pyrogram import filters
from Configs.dm import Config
from pyrogram import Client as ILovePDF
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



# -------------------------------- Main execution fn --------------------------------------- #
@ILovePDF.on_message(filters.private & filters.text & ~filters.command(["start"]))
async def link_extract(self, m: Message):
    if not m.text.startswith("http"):
        return
    file_name = str()
    #
    thumb_path = os.path.join(os.getcwd(), "img")
    if not os.path.isdir(thumb_path):
        os.makedirs(thumb_path)
        urllib.request.urlretrieve(Presets.THUMB_URL, os.path.join(thumb_path, "thumbnail.png"))
    else:
        pass
    #
    thumbnail = os.path.join(os.getcwd(), "img", "thumbnail.png")
    #
    await self.send_chat_action(m.chat.id, "typing")
    msg = await m.reply_text(Presets.PROCESS_TXT, reply_to_message_id=m.message_id)
    try:
        req = requests.get(m.text)
        # using the BeautifulSoup module
        soup = BeautifulSoup(req.text, 'html.parser')
        # extracting the title frm the link
        for title in soup.find_all('title'):
            file_name = str(title.get_text()) + '.pdf'
        # Creating the pdf file
        weasyprint.HTML(m.text).write_pdf(file_name)
    except Exception:
        return
    try:
        await msg.edit(Presets.UPLOAD_TXT)
    except Exception:
        pass
    await self.send_chat_action(m.chat.id, "upload_document")
    await m.reply_document(
        document=file_name,
        caption=Presets.CAPTION_TXT.format(file_name),
        thumb=thumbnail
    )
    print(
        '@' + m.from_user.username if m.from_user.username else m.from_user.first_name,
        "قام بتنزيل الملف",
        file_name
    )
    try:
        os.remove(file_name)
    except Exception:
        pass
    await msg.delete()
print(f"\n\nبدأ البوت بنجاح!\n\n")

