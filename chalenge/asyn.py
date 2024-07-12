import asyncio

async def tes():
 print('a') 
#setTime out   
 await asyncio.sleep(2)
  print('b') 

asyncio.run(tes())