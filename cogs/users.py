import discord
from discord.ext import commands
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

cluster = MongoClient(os.getenv("MONGODB_URL"))

ucer = cluster["discord"]["taco"]


class users(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        stats = ucer.find_one({"id": message.author.id})
        imgp = str(message.author.avatar_url)

        if not message.author.bot:
            if stats is None:
                newuser = {"id": message.author.id, "taco_count": 0, "xp": 0, "username": message.author.name,
                           "discrim": message.author.discriminator, "messagecount": 0, "image_url": imgp}
                ucer.insert_one(newuser)

            else:
                xp = stats["xp"] + 5
                kung = stats["messagecount"] + 1
                babang_taco = stats["taco_count"]
                img = str(message.author.avatar_url)
                ucer.update_one({"id": message.author.id}, {
                    "$set": {"taco_count": babang_taco, "xp": xp, "username": message.author.name, "discrim": message.author.discriminator, "messagecount": kung, "image_url": img}})
                lvl = 0
                while True:
                    if xp < ((50*(lvl**2))+(50*lvl)):
                        break
                    lvl += 1
                xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                if xp == 0:
                    osas = stats["xp"]
                    osis = stats["messagecount"]
                    nambah_taco = stats["taco_count"] + 1
                    ucer.update_one({"id": message.author.id}, {
                        "$set": {"taco_count": nambah_taco, "xp": osas, "username": message.author.name, "discrim": message.author.discriminator, "messagecount": osis, "image_url": img}})


def setup(client):
    client.add_cog(users(client))
