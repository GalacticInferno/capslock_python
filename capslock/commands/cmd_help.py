import discord
from commands import STATICS


def ex(invoke, args, message, client):

    embed = discord.Embed(title="CAPSLOCK HELP", colour=discord.Colour(0x23cace),
                                url="https://discordapp.com", description=("```\n{0}```").format(STATICS.VERSION))

    embed.set_image(url="https://s-media-cache-ak0.pinimg.com/originals/c0/2f/c9/c02fc9d42965203bae7cc90c7152ece3.jpg")
    embed.set_author(name="Cody Beaty", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
    embed.set_footer(text="Hello World!", icon_url="https://pbs.twimg.com/profile_images/719591403592896512/iy5aMCj6_bigger.jpg")

    embed.add_field(name="Announcement", value="!echo [insert message] : will delete message call.", inline=True)
    embed.add_field(name="Ban", value="!ban [@user] [days] [reason] : will ban user for x days.", inline=True)
    embed.add_field(name="Clean", value="!clean [x] [amount of message] : x - either bot or [user].", inline=True)
    embed.add_field(name="Hello", value="!hello : CAPSLOCK will responed will random message.", inline=True)
    embed.add_field(name="Help", value="!help : this will bring this message up.", inline=True)
    embed.add_field(name="Highfive", value="!highfive : give CAPSLOCK a highfive.", inline=True)
    embed.add_field(name="Info", value="!info : display bot info.", inline=True)
    embed.add_field(name="Kick", value="!kick [@user] : kick the user mentioned.", inline=True)
    embed.add_field(name="Search", value="!search [python, pyh, c#, sharp] [x] : searches a doc for x.", inline=True)
    embed.add_field(name="Ping", value="!ping : PONG!", inline=True)
    embed.add_field(name="Unban", value="!unban [@user] : unban user mentioned.", inline=True)

    yield from client.send_message(message.author, embed=embed)
