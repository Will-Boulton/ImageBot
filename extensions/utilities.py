from discord.ext import commands


class Util(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def reload(self, ctx, extension):
        self.client.unload_extension(f'extensions.{extension}')
        self.client.load_extension(f'extensions.{extension}')
        await ctx.send(f'Reloaded {extension}')

    @commands.command()
    async def load(self,ctx,extension):
        self.client.load_extension(f'extensions.{extension}')
        await ctx.send(f'Loaded {extension}')

def setup(client):
    client.add_cog(Util(client))
