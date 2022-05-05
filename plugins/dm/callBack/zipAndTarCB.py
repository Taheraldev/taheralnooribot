# fileName : plugins/dm/callBack/asZip.py
# copyright ©️ 2021 nabilanavab

from pyrogram import filters
from pyrogram import Client as ILovePDF
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#--------------->
#--------> PDF IMAGES TO ZIP, TAR(CB/BUTTON)
#------------------->

zIp = filters.create(lambda _, __, query: query.data == "zip")
KzIp = filters.create(lambda _, __, query: query.data.startswith("Kzip|"))

# Extract pgNo as Zip(with unknown pdf page number)
@ILovePDF.on_callback_query(zIp)
async def _zip(bot, callbackQuery):
    try:
        await callbackQuery.edit_message_text(
            "__Pdf - Img » كا Zip » صفحات:           \nعدد صفحات: unknown(غير معروف)__ 😐\n__Pdf - Img » as Zip » Pages:           \nTotal pages: unknown__ 😐",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Extract All Extract All استخراج الكل 🙄", callback_data="zipA")
                    ],[
                        InlineKeyboardButton("With In RangeWith In Rangeمع  النطاق 🙂 ", callback_data="zipR")
                    ],[
                        InlineKeyboardButton("صفحة واحدة Single Page  🌝", callback_data="zipS")
                    ],[
                        InlineKeyboardButton("« Back عودة «", callback_data="BTPM")
                    ]
                ]
            )
        )
    except Exception:
        pass

# Extract pgNo as Zip(with known pdf page number)
@ILovePDF.on_callback_query(KzIp)
async def _Kzip(bot, callbackQuery):
    try:
        _, number_of_pages = callbackQuery.data.split("|")
        await callbackQuery.edit_message_text(
            f"__Pdf - Img » كا Zip» صفحات:           \nعدد صفحات: {number_of_pages}__ 🌟\n__Pdf - Img » as Zip» Pages:           \nTotal pages: {number_of_pages}__ 🌟",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Extract All استخراج الكل 🙄", callback_data=f"KzipA|{number_of_pages}")
                    ],[
                        InlineKeyboardButton("With In Rangeمع  النطاق 🙂 ", callback_data=f"KzipR|{number_of_pages}")
                    ],[
                        InlineKeyboardButton("صفحة واحدة Single Page  🌝", callback_data=f"KzipS|{number_of_pages}")
                    ],[
                        InlineKeyboardButton("« Back عودة «", callback_data=f"KBTPM|{number_of_pages}")
                    ]
                ]
            )
        )
    except Exception:
        pass

tAr = filters.create(lambda _, __, query: query.data == "tar")
KtAr = filters.create(lambda _, __, query: query.data.startswith("Ktar|"))

# Extract pgNo as Zip(with unknown pdf page number)
@ILovePDF.on_callback_query(tAr)
async def _tar(bot, callbackQuery):
    try:
        await callbackQuery.edit_message_text(
            "__Pdf - Img » كا Tar » صفحات:           \nعدد: unknown(غير معروف)__ 😐\n__Pdf - Img » as Tar » Pages:           \nTotal pages: unknown__ 😐",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Extract All استخراج الكل 🙄", callback_data="tarA")
                    ],[
                        InlineKeyboardButton("With In Rangeمع  النطاق 🙂 ", callback_data="tarR")
                    ],[
                        InlineKeyboardButton("صفحة واحدة Single Page  🌝", callback_data="tarS")
                    ],[
                        InlineKeyboardButton("« Back عودة «", callback_data="BTPM")
                    ]
                ]
            )
        )
    except Exception:
        pass

# Extract pgNo as Zip(with known pdf page number)
@ILovePDF.on_callback_query(KtAr)
async def _Ktar(bot, callbackQuery):
    try:
        _, number_of_pages = callbackQuery.data.split("|")
        await callbackQuery.edit_message_text(
            f"__Pdf - Img » كا Tar» Pages:           \nعدد صفحات: {number_of_pages}__ 🌟\n__Pdf - Img » as Tar» Pages:           \nTotal pages: {number_of_pages}__ 🌟",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Extract All استخراج الكل 🙄", callback_data=f"KtarA|{number_of_pages}")
                    ],[
                        InlineKeyboardButton("With In Rangeمع  النطاق 🙂 ", callback_data=f"KtarR|{number_of_pages}")
                    ],[
                        InlineKeyboardButton("صفحة واحدة Single Page  🌝", callback_data=f"KtarS|{number_of_pages}")
                    ],[
                        InlineKeyboardButton("« Back عودة «", callback_data=f"KBTPM|{number_of_pages}")
                    ]
                ]
            )
        )
    except Exception:
        pass

#                                                                                             Telegram: @nabilanavab
