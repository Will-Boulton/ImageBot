import discord
from PIL import Image
from PIL import ImageFilter
from discord.ext import commands

formats = ['jpeg', 'png', 'jpg']


async def get_image(ctx):
    attachments = ctx.message.attachments
    if len(attachments) == 1:
        img_file = attachments[0]
        await img_file.save('tempin.png')
        img = Image.open('tempin.png')
        return img
    else:
        return None


class ImageManipulation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def emboss(self, ctx):
        img = await get_image(ctx)
        img = img.filter(ImageFilter.EMBOSS)
        img.save('tempout.png')
        await ctx.send("heres your image:", file=discord.File('tempout.png'))

    @commands.command(pass_context=True)
    async def edges(self, ctx):
        img = await get_image(ctx)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save('tempout.png')
        await ctx.send("heres your image:", file=discord.File('tempout.png'))

    @commands.command(pass_context=True)
    async def smooth(self, ctx):
        img = await get_image(ctx)
        img = img.filter(ImageFilter.SMOOTH_MORE)
        img.save('tempout.png')
        await ctx.send("heres your image:", file=discord.File('tempout.png'))


def setup(client):
    client.add_cog(ImageManipulation(client))
