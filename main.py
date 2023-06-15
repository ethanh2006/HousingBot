from PIL import Image
import pytesseract
import numpy as np
def imageRecognize():
    pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    import pyscreenshot as ImageGrab


    # part of the screen
    im=ImageGrab.grab(bbox=(1600,300,1900,780))
    im.save("tempImg.png")

 
    img1 = np.array(Image.open("tempImg.png"))
    text = pytesseract.image_to_string(img1)


    tempFile = open("tempValues.txt", "w")
    tempFile.write(text)
    tempFile.close()
    tempFile = open("tempValues.txt", "r")
    printLine = ""
    tempText = tempFile.readlines()
    num_lines = len(tempText)
    for x in range(num_lines):
        tempLine = tempText[x]
        tempLine = tempLine.lower()
        if "guests:" in tempLine:
            printLine = tempLine

    printLine2 = ""
    for x in range(num_lines):
        tempLine2 = tempText[x]
        tempLine2 = tempLine2.lower()
        if "cookies:" in tempLine2:
            printLine2 = tempLine2
    tempFile.close()
    return (printLine+printLine2)

import  discord
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
from discord import app_commands # Importing the newly installed library.
guild_ids = ["992013192140181574"]
client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)
@tree.command(name = "house", description = "Pull the currently tracked house stats") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    tempMessage = imageRecognize()
    await interaction.response.send_message(tempMessage)

client.run('MTExODQ1OTQ4ODk1ODE2MDk3Ng.GtF0tz.lvplwAGkq733laPeSfR2FRRb1pN7izbK0eKrCU')
