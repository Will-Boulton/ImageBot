from discord.ext import commands
import csv
import random

messages = []
messages2 = []
usermsgs = []

try:
    with open("extensions/wholesome.csv", 'r') as file:
        reader = csv.reader(file, delimiter=',')
        ind = 0
        for row in reader:
            if ind == 0:
                ind += 1
                for message in row: messages.append(message)
            elif ind == 1:
                ind += 1
                for message in row: messages2.append(message)
            else:
                for message in row: usermsgs.append(message)
except FileNotFoundError:
    print("No wholesome messages found :(")


class Wholesome(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def wholesome(self, ctx, *, arg=None):
        if not arg:
            await ctx.send(random.choice(messages))
        else:
            message = random.choice(messages2)
            m = message.split('-')
            m = ''.join([m[0], arg, m[1]])
            await ctx.send(m)


def setup(client):
    client.add_cog(Wholesome(client))
