import discord
from discord.ext import commands
import random

class RunParCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def runpar(self, ctx, num: int):
        # Apriamo i file di testo contenenti le parole casuali
        with open("nouns.txt", "r") as f:
            nouns = [line.strip() for line in f.readlines()]
        with open("adjectives.txt", "r") as f:
            adjectives = [line.strip() for line in f.readlines()]

        # Prendiamo un numero di parole casuali uguale a quello richiesto
        words = []
        for i in range(num):
            noun = random.choice(nouns)
            adjective = random.choice(adjectives)
            words.append(f"{adjective} {noun}")

        # Costruiamo il messaggio di risposta
        response = " ".join(words)

        # Inviamo il messaggio di risposta
        await ctx.send(response)

def setup(bot):
    bot.add_cog(RunParCog(bot))
