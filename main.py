import asyncio

from src import Tox


async def main():
    token = input("Please input your token [>] ")
    opt = input("Please input type of report.\nMessage\nGuild\n[>] ")
    if opt.lower() == "message":
        tox = Tox(3).load("message")
        tox.show_options()
        await tox.trigger(token)
    else:
        tox = Tox(0).load("guild")
        tox.show_options()
        await tox.trigger(token)
    
if __name__ == "__main__":
    asyncio.run(main())
