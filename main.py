from telethon import TelegramClient, events
from hrbot import check_status

api_id = 1233125
api_hash = '728048b26a9729a387177ec582ffc6e5'
username = 'maria_sharunina'

client = TelegramClient(username, api_id, api_hash)
client.start()

@client.on(events.NewMessage(pattern=r'hi .*'))
async def handler(event):
        sender = await event.get_sender()
        if not event.out:
            status = check_status(event.raw_text)
            if status in "Найден положительный результат":
                await client.send_message(sender.username, "Вас приняли!")
            elif status in "Найден отрицательный результат":
                await client.send_message(sender.username, 'Какая неудача!')

            await client.send_message(username + "Кандидат" +sender.username + "\nОтправил сообщение: " + event.raw_text + "\nСтатус:" + status)

client.add_event_handler(handler)
client.run_until_disconnected()