from pyadtpulsedotcom import AdtPulsedotcom
import aiohttp
import asyncio
import logging

async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as session:
       alarm = AdtPulsedotcom(username="email", password="password", websession=session, loop=loop)
       await alarm.async_update()



if __name__ == '__main__':
    logging.basicConfig(filename='adtpulse.log', level=logging.DEBUG,filemode="w")
    logging.info('Started')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    logging.info('Finished')
