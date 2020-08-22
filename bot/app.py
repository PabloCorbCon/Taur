# TAUR
# By Pablo Corbalán
# Twitter: @pablocorbcon
# GitHub: @PabloCorbCon


# This is the main file of Taur. Our Discord bot written in discord.py
# if you need more information about Taur, you can check the GitHub repository
# https://github.com/PabloCorCon/Taur

import discord
from discord.ext import commands
import colorama
import platform


import load

colorama.init(autoreset=True)

# set the token (const token)
TOKEN = 'NzQ1NTM1NDg2Nzg0ODMxNTA5.XzzMBw.dKv3RL7_lKKDvgBZG1vlyF_sGsE'

# create the bot using the discord.Bot() class
bot = commands.Bot(command_prefix='t/')

@bot.event
async def on_ready():

    """
    This function will start once the bot is ready, using the client.event decorator
    and the on_ready() function. 
    It will display information about the bot itself, the server and the programmer
    """
    print(colorama.Fore.LIGHTYELLOW_EX + '· · · · · · · · · TAUR · · · · · · · · ·')
    print('\nBy Pablo Corbalán.')
    print('   Twitter: @pablocorbcon')
    print('   GitHub: @PabloCorbCon')

    # bot log in information
    print('\nLogged in as {}, id: {} | Servers: {} | Users: {}'.format(bot.user.name,
                                                                     bot.user.id,
                                                                     len(bot.guilds),
                                                                     len(set(bot.get_all_members()))) + ' users')

    # bot python information
    print('\nPython version: {} | Discord.py version: {}'.format(platform.python_version(),
                                                               discord.__version__))

    #liks
    invite = 'https://discord.com/oauth2/authorize?client_id=745535486784831509&scope=bot&permissions=268690782'
    print('\nUse this link to invite {}:'.format(bot.user.name))
    print(invite)

    github_repo = 'github.com/PabloCorbCon/Taur'
    print('\nGitHub repository: {}'.format(github_repo))


@bot.command()
async def info(ctx):

    """
    This function will display information about the bot using the
    t/info ccommand, to display an embed message.
    """
    # create the discord embed message
    info_embed = discord.Embed(title="Information",
        description=d,
        color=0x0a8f3f)

    # create the embed message
    info_embed=discord.Embed(title="Taur | Information",
        description=open('doc/description.txt').read(),
        color=0x087d1b)
    info_embed.set_author(name="Taur",
        url="https://github.com/PabloCorbCon/Taur")
    info_embed.set_image(url='https://github.com/PabloCorbCon/Taur/blob/master/branding/logo.png?raw=true')
    info_embed.set_footer(text="By Pablo Corbalán | Twitter: @pablocorbcon - GitHub: @PabloCorbCon")

    print('Taur has responded to a command (t/info) in {}'.format(ctx))
    await ctx.send(embed=info_embed)




@bot.command()
async def commands(ctx):

    """
    This function will display information about the bot using the
    t/commands ccommand, to display an embed message and it uses other functions
    as load_help_commadns() located in commands.py to load all the data.
    """

    # get the bot commands as a Python dic
    bot_commands = load.load_help_commands('doc/commands.json')['commands']

    # create the embed message
    commands_embed=discord.Embed(title="Taur | Commands",
        description=load.load_help_commands('doc/commands.json', True),
        color=0x087d1b)
    commands_embed.set_author(name="Taur",
        url="https://github.com/PabloCorbCon/Taur")
    commands_embed.set_footer(text="By Pablo Corbalán | Twitter: @pablocorbcon - GitHub: @PabloCorbCon")

    print('Taur has responded to a command (t/commands) in {}'.format(ctx))
    await ctx.send(embed=commands_embed)




@bot.command()
async def invite(ctx):

    """
    This function will provide a link to invite Taur
    to your own discord server. This link is not provided using
    an embed message
    """

    #create the bot link
    bot_invite_link = 'https://discord.com/oauth2/authorize?client_id=745535486784831509&scope=bot&permissions=268690782'

    print('Taur has responded to a command (t/commands) in {}'.format(ctx))
    await ctx.send("You can invite @Taur using **[this link]**({}) :point_left:".format(bot_invite_link))


bot.run(TOKEN)