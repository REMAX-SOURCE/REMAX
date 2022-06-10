import asyncio
from pytgcalls import idle
from driver.amort import call_py, bot

async def mulai_bot():
    print("[amort]: بـدء جلسـة البـوت")
    await bot.start()
    print("[amort]: بـدء جلسـة مكتبـة الاغـاني")
    await call_py.start()
    await idle()
    await pidle()
    print("[amort]: توقـف البـوت & الحسـاب المسـاعد")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(mulai_bot())