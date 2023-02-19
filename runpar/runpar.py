import random
from redbot.core import commands

class Ranpar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.word_list = ["parola1", "parola2", "parola3", "parola4", "parola5", "parola6", "parola7", "parola8", "parola9", "parola10"] # lista di parole casuali

    @commands.command()
    async def ranpar(self, ctx, num: int):
        if num <= 0:
            await ctx.send("Il numero deve essere maggiore di 0.")
            return

        if num > len(self.word_list):
            await ctx.send(f"Sono disponibili solo {len(self.word_list)} parole.")
            return

        random_words = random.sample(self.word_list, num) # seleziona un numero di parole casuali dalla lista
        message = " ".join(random_words) # unisce le parole casuali in una stringa

        await ctx.send(message)

def setup(bot):
    bot.add_cog(Ranpar(bot))
