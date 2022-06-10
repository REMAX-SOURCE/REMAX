import asyncio
from pytgcalls import idle
from driver.saroot import call_py, bot

async def mulai_bot():
    print("[saroot]: بـدء جلسـة البـوت")
    await bot.start()
    print("[saroot]: بـدء جلسـة مكتبـة الاغـاني")
    await call_py.start()
    await idle()
    await pidle()
    print("[saroot]: توقـف البـوت & الحسـاب المسـاعد")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(mulai_bot())