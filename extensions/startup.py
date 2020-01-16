from discord.ext import commands


class Startup(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("aBot has arrived!")


def setup(client):
    client.add_cog(Startup(client))
