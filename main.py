from PIL import Image
import pytesseract
import numpy as np
def imageRecognize():
    pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    import pyautogui

    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'Path to save screenshot\file name.png')
    fileName = r"tempImg.png"
    img1 = np.array(Image.open(fileName))
    text = pytesseract.image_to_string(img1)


    tempFile = open("tempValues.txt", "w")
    tempFile.write(text)
    tempFile.close()
    tempFile = open("tempValues.txt", "r")

    tempText = tempFile.readlines()
    num_lines = len(tempText)
    for x in range(num_lines):
        tempLine = tempText[x]
        tempLine = tempLine.lower()
        if "guests:" in tempLine:
            print(tempLine)
    tempFile.close()

    for x in range(num_lines):
        tempLine2 = tempText[x]
        tempLine2 = tempLine2.lower()
        if "cookies:" in tempLine:
            print(tempLine2)
    tempFile.close()
    return (tempLine+"\n"+tempLine2)

import  discord
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
from discord_slash import SlashCommand # Importing the newly installed library.
guild_ids = ["992013192140181574"]
client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)
@slash.slash(name="House")
async def _ping(ctx): # Defines a new "context" (ctx) command called "house."
    await ctx.send(imageRecognize())


client.run('MTExODQ1OTQ4ODk1ODE2MDk3Ng.GtF0tz.lvplwAGkq733laPeSfR2FRRb1pN7izbK0eKrCU')
