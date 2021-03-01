import emoji
from . import *
from google_trans_new import google_translator
from googletrans import LANGUAGES
from langdetect import detect


@asst_cmd("tr") 
async def _(event):
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await ultroid_bot.send_message(
            event.chat_id, "`/tr LanguageCode` as reply to a message"
        )
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = google_translator()
    translated = translator.translate(text, lang_tgt=lan)
    lmao = detect(text)
    after_tr_text = lmao
    source_lan = LANGUAGES[after_tr_text]
    transl_lan = LANGUAGES[lan]
    output_str = f"""**Trᴀnslᴀᴛᴇd by By CɪᴘʜᴇʀX Bᴏᴛ**
**Source ({source_lan})**:
`{text}`

**Translation ({transl_lan})**:
`{translated}`"""

    try:
        await ultroid_bot.send_message(event.chat_id, output_str)
    except Exception:
        await ultroid_bot.send_message(event.chat_id, "Something went wrong 🤔")