import discord
from cmds_utility.data_utility import STATICS


def ex(invoke, args, message, client):

    embed = discord.Embed(title="CAPSLOCK HELP",
                                colour=discord.Colour(0x23cace),
                                url=STATICS.GIT_LINK,
                                description=("```\n{0} - dev```")
                                .format(STATICS.VERSION))

    embed.set_image(url="https://goo.gl/LJeASG")
    embed.set_author(name="Cody Beaty",
        url=STATICS.GIT_LINK,
        icon_url="https://goo.gl/py664U")
    embed.set_footer(text="Hello World!",
        icon_url="https://goo.gl/Pe7RzK")

    embed.add_field(name="Announcement",
        value="!echo [insert message]",
        inline=False)
    embed.add_field(name="Ban",
        value="!ban [@user] [days] [reason]",
        inline=False)
    embed.add_field(name="Clean",
        value="!clean [type] [amount] : type - [bot] or [user].",
        inline=False)
    embed.add_field(name="Hello",
        value="!hello",
        inline=False)
    embed.add_field(name="Help",
        value="!help",
        inline=False)
    embed.add_field(name="Highfive",
        value="!highfive",
        inline=False)
    embed.add_field(name="Info",
        value="!info",
        inline=False)
    embed.add_field(name="Invite",
        value="!invite [type] : type [server] or [bot]",
        inline=False)
    embed.add_field(name="Kick",
        value="!kick [@user]",
        inline=False)
    embed.add_field(name="Roll",
        value="!roll [amount]d[type] + [optional mod]",
        inline=False)
    embed.add_field(name="Search",
        value="!search [type] [keyword(s)] : type [python] or [msdm]",
        inline=False)
    embed.add_field(name="Ping",
        value="!ping",
        inline=False)
    embed.add_field(name="Unban",
        value="!unban [@user]",
        inline=False)

    yield from client.send_message(message.author, embed=embed)
    return
