import random
import os
import nextcord
import time
import datetime
from nextcord import ButtonStyle
from nextcord.ui import Button, View
from time import sleep
from nextcord import Embed
from nextcord.ext import commands, menus


my_secret = "TOKEN"
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("{0.user} Operativo".format(bot))


@bot.listen()
async def on_message(message):
    if message.content.startswith("!bet") or message.content.startswith("!Bet"):
        x = message.content.split(" ")
        tag1 = message.author.mention
        player1 = message.author.id
        bet = int(x[1])

        # se il file non esiste lo crea
        try:
            with open("Players/" + str(player1), "x") as f:
                money1 = 1000
                # sleep(0.1)
            with open("Players/" + str(player1), "w") as f:
                luck = 0
                f.write("1000\n0\n0\n3\n0\n0")
        # altrimenti lo legge
        except:
            with open("Players/" + str(player1), "r") as f:
                stats = f.readlines()
                money1 = int(stats[0])
                luck = int(stats[4])
        # poi esegue il resto
        try:
            if bet <= money1 and bet > 0:
                max = 100
                max -= luck
                r = random.randint(1, max)
                if r <= 50:
                    # Vincita player1
                    money1 += bet
                    with open("Players/" + str(player1), "r") as f:
                        stats = f.readlines()
                    with open("Players/" + str(player1), "w") as f:
                        f.write(
                            str(money1)
                            + "\n"
                            + stats[1]
                            + stats[2]
                            + stats[3]
                            + stats[4]
                            + stats[5]
                        )
                    await message.channel.send(
                        message.author.mention
                        + " won "
                        + str(bet)
                        + " ($"
                        + str(money1)
                        + ")."
                    )
                    print(str(message.author) + " won " + str(money1))
                else:
                    # Vincita PC
                    money1 -= bet
                    with open("Players/" + str(player1), "r") as f:
                        stats = f.readlines()
                    with open("Players/" + str(player1), "w") as f:
                        f.write(
                            str(money1)
                            + "\n"
                            + stats[1]
                            + stats[2]
                            + stats[3]
                            + stats[4]
                            + stats[5]
                        )
                    await message.channel.send(
                        message.author.mention
                        + " lost "
                        + str(bet)
                        + " ($"
                        + str(money1)
                        + ")."
                    )
                    print(str(message.author) + " lost " + str(money1))

            else:
                await message.channel.send(
                    message.author.mention
                    + " you don't have enough money. You only have ($"
                    + str(money1)
                    + ")."
                )
        except Exception as e:
            print("il problema del dio gane è qui sotto")
            print(e)
            await message.channel.send("Wrong value !")


@bot.command(
    aliases=[
        "Give",
        "Gift",
        "Send",
        "GIVE",
        "SEND",
        "GIFT",
        "send",
        "gift",
        "gifT",
        "GiVe",
    ]
)
async def give(ctx, member: nextcord.Member, gift: int):
    try:
        with open("Players/" + str(ctx.author.id), "x") as f:
            money1 = 1000
        with open("Players/" + str(ctx.author.id), "w") as f:
            f.write("1000\n0\n0\n3\n0\n0")

    except:
        with open("Players/" + str(ctx.author.id), "r") as f:
            stats = f.readlines()
            money1 = int(stats[0])

    playerid = member.id

    try:
        f = open("Players/" + str(playerid))
    except:
        await ctx.send(ctx.author.mention + " the player doesn't exist")
        return
    finally:
        f.close()

    try:
        if gift <= money1 and gift > 0:
            money1 = money1 - gift
            with open("Players/" + str(ctx.author.id), "w") as f:
                f.write(
                    str(money1)
                    + "\n"
                    + stats[1]
                    + stats[2]
                    + stats[3]
                    + stats[4]
                    + stats[5]
                )
            await ctx.send(
                ctx.author.mention
                + " donated "
                + str(gift)
                + " to "
                + str(member.mention)
            )
            with open("Players/" + str(playerid), "r") as f:
                stats = f.readlines()
                money2 = int(stats[0])
            with open("Players/" + str(playerid), "w") as f:
                money2 = money2 + gift
                f.write(
                    str(money2)
                    + "\n"
                    + stats[1]
                    + stats[2]
                    + stats[3]
                    + stats[4]
                    + stats[5]
                )

            print(ctx.author + " donated " + str(money1) + " to " + str(member))
        else:
            await ctx.send(
                ctx.author.mention
                + " you don't have enough money. You only have ($"
                + str(money1)
                + ")."
            )
    except ValueError:
        await ctx.send(ctx.author.mention + " wrong value.")


@bot.command(aliases=["Satu", "SaTu", "shop", "Shop", "SATU"])
async def satu(ctx):
    embed = nextcord.Embed(
        title="Home page", description="All commands and more", color=0xF9E655
    )
    embed.set_author(name="Satu Bot")
    embed.set_footer(
        text="Type !satu to display the homepage.\nType '!profile' to check your stats.\nType '!bet VALUE' to bet your money.\nType '!money' to check your money.\nType '!drop' to receive random free money.\nType '!attack @player' to mug someone\nType '!give' to give money to another player.\nType '!leaderboard' to check the leaderboard\n\n💪🏼 Strenght is needed to defend you or !attack other players, the player with the most strenght wins the !attack.\n\n💸 The drops increase the money from the !drop.\n\n🥷 Stealing power increases stolen money from another player you attacked or stealing money from a weaker player who tried to !attack you.\n\nSatu 1.18"
    )
    home = Button(label="Home", style=nextcord.ButtonStyle.gray)
    shop = Button(label="🛒 Market", style=nextcord.ButtonStyle.green)
    shopvip = Button(label="💎 Vip Market", style=nextcord.ButtonStyle.blurple)
    help = Button(label="Help", style=nextcord.ButtonStyle.gray)
    strenght = Button(label="💪🏼", style=nextcord.ButtonStyle.blurple)
    drop = Button(label="💸", style=nextcord.ButtonStyle.blurple)
    stmoney = Button(label="🥷", style=nextcord.ButtonStyle.blurple)
    mouse = Button(label="🐹", style=nextcord.ButtonStyle.blurple)
    bee = Button(label="🐝", style=nextcord.ButtonStyle.blurple)
    dolphin = Button(label="🐬", style=nextcord.ButtonStyle.blurple)
    butterfly = Button(label="🦋", style=nextcord.ButtonStyle.blurple)

    async def home_callback(interaction):
        embed = nextcord.Embed(
            title="Home page", description="All commands and more", color=0xF9E655
        )
        embed.set_author(name="Satu Bot")
        embed.set_footer(
            text="Type !satu toType !satu to display the homepage.\nType '!profile' to check your stats.\nType '!bet VALUE' to bet your money.\nType '!money' to check your money.\nType '!drop' to receive random free money.\nType '!attack @player' to mug someone\nType '!give' to give money to another player.\nType '!leaderboard' to check the leaderboard\n\n💪🏼 Strenght is needed to defend you or !attack other players, the player with the most strenght wins the !attack.\n\n💸 The drops increase the money from the !drop.\n\n🥷 Stealing power increases stolen money from another player you attacked or stealing money from a weaker player who tried to !attack you.\n\nSatu 1.18"
        )
        return await interaction.message.edit(embed=embed, view=view)

    async def shopvip_callback(interaction):
        embed = Embed(title="💎 Satu Vip", description="", color=0xF9E655)
        embed.set_footer(
            text="Money Packs\n\n€0.99 for 100'000.\n€4.99 for 750'000.\n€9.99 for 1'500'000.\n\nStats Packs\n\nFREE for 5 drops 💸.\n€0.99 for 5  💸  5 💪🏼  5 🥷.\n\nDM Galoka#6482 for the purchase"
        )
        return await interaction.message.edit(embed=embed, view=view)


    
    async def help_callback(interaction):
        embed = nextcord.Embed(title="Contact me on DM for issues and suggestions Galoka#6482", color=0xf9e655)
        embed.set_author(name="Satu Bot")
        return await interaction.message.edit(embed=embed, view=view)

    async def shop_callback(interaction):
        # await interaction.response.edit_message(content="EPIC")
        embed = Embed(title="🛒 Satu Market", description="", color=0xF9E655)
        embed.set_footer(
            text="Statistics\n\n💪🏼 Gives you +1 Strenght ($10'000)\n💸 Gives you better drops ($10'000)\n🥷 Gives you +0.1% stealing money ($10'000)\n\nLuck\n\n🐹 Gives you 1% luck ($50'000)\n🐝 Gives you 2% luck ($250'000)\n🐬 Gives you 3% luck ($1'000'000)\n🦋 Gives you 5% luck ($15'000'000)\n\n❌ (luck isn't cumulable)\n\nOne use items\n\n🎲 Double or divide the strength ($50'000)\n🎁 Random perk ($1'000'000)"
        )
        return await interaction.message.edit(embed=embed, view=market)

    async def strenght_callback(interaction):
        try:
            with open("Players/" + str(interaction.user.id), "x") as f:
                money1 = 1000
            with open("Players/" + str(interaction.user.id), "w") as f:
                f.write("1000\n0\n0\n3\n0\n0")
        except:
            with open("Players/" + str(interaction.user.id), "r") as f:
                stats = f.readlines()
                money1 = int(stats[0])
                strenght = int(stats[1])
        if money1 > 9999:
            money1 -= 10000
            strenght += 1
            with open("Players/" + str(interaction.user.id), "w") as f:
                f.write(
                    str(money1)
                    + "\n"
                    + str(strenght)
                    + "\n"
                    + stats[2]
                    + stats[3]
                    + stats[4]
                    + stats[5]
                )
            await interaction.response.send_message(
                interaction.user.mention + " bought +1 strenght for ($10'000)."
            )
        else:
            await interaction.response.send_message(
                interaction.user.mention
                + " you don't have enough money. You only have ($"
                + str(money1)
                + ")."
            )

    async def drop_callback(interaction):
        try:
            with open("Players/" + str(interaction.user.id), "x") as f:
                money1 = 1000
            with open("Players/" + str(interaction.user.id), "w") as f:
                f.write("1000\n0\n0\n3\n0\n0")
        except:
            with open("Players/" + str(interaction.user.id), "r") as f:
                stats = f.readlines()
                money1 = int(stats[0])
                drop = int(stats[2])
        if money1 > 9999:
            money1 -= 10000
            drop += 1
            with open("Players/" + str(interaction.user.id), "w") as f:
                f.write(
                    str(money1)
                    + "\n"
                    + stats[1]
                    + str(drop)
                    + "\n"
                    + stats[3]
                    + stats[4]
                    + stats[5]
                )
            await interaction.response.send_message(
                interaction.user.mention + " bought +1 drop for ($10'000)."
            )
        else:
            await interaction.response.send_message(
                interaction.user.mention
                + " you don't have enough money. You only have ($"
                + str(money1)
                + ")."
            )

    async def stmoney_callback(interaction):
        try:
            with open("Players/" + str(interaction.user.id), "x") as f:
                money1 = 1000
            with open("Players/" + str(interaction.user.id), "w") as f:
                f.write("1000\n0\n0\n3\n0\n0")
        except:
            with open("Players/" + str(interaction.user.id), "r") as f:
                stats = f.readlines()
                money1 = int(stats[0])
                stmoney = float(stats[3])
        if money1 > 9999 and stmoney<100:
            money1 -= 10000
            stmoney += 0.1
            with open("Players/" + str(interaction.user.id), "w") as f:
                f.write(
                    str(money1)
                    + "\n"
                    + stats[1]
                    + stats[2]
                    + str(stmoney)
                    + "\n"
                    + stats[4]
                    + stats[5]
                )
            await interaction.response.send_message(
                interaction.user.mention + " bought +0.1% stealing power for ($10'000)."
            )
        else:
            if stmoney==100:
                await interaction.response.send_message(interaction.user.mention+' purchase failed, you have reached the maximum stealing power.')
            else:
                await interaction.response.send_message(
                    interaction.user.mention
                    + " you don't have enough money. You only have ($"
                    + str(money1)
                    + ")."
                )

    async def mouse_callback(interaction):
        try:
            with open("Players/" + str(interaction.user.id), "x") as f:
                money1 = 1000
            with open("Players/" + str(interaction.user.id), "w") as f:
                f.write("1000\n0\n0\n3\n0\n0")
        except:
            with open("Players/" + str(interaction.user.id), "r") as f:
                stats = f.readlines()
                money1 = int(stats[0])
                luck = int(stats[4])
        if money1 > 49999:
            money1 -= 50000
            luck = 1
            with open("Players/" + str(interaction.user.id), "w") as f:
                f.write(
                    str(money1)
                    + "\n"
                    + stats[1]
                    + stats[2]
                    + stats[3]
                    + str(luck)
                    + "\n"
                    + stats[5]
                )
            await interaction.response.send_message(
                interaction.user.mention + " bought 1% luck for ($50'000)."
            )
        else:
            await interaction.response.send_message(
                interaction.user.mention
                + " you don't have enough money. You only have ($"
                + str(money1)
                + ")."
            )

    async def bee_callback(interaction):
        try:
            with open("Players/" + str(interaction.user.id), "x") as f:
                money1 = 1000
            with open("Players/" + str(interaction.user.id), "w") as f:
                f.write("1000\n0\n0\n3\n0\n0")
        except:
            with open("Players/" + str(interaction.user.id), "r") as f:
                stats = f.readlines()
                money1 = int(stats[0])
                luck = int(stats[4])
        if money1 > 249999:
            money1 -= 250000
            luck = 2
            with open("Players/" + str(interaction.user.id), "w") as f:
                f.write(
                    str(money1)
                    + "\n"
                    + stats[1]
                    + stats[2]
                    + stats[3]
                    + str(luck)
                    + "\n"
                    + stats[5]
                )
            await interaction.response.send_message(
                interaction.user.mention + " bought 2% luck for ($250'000)."
            )
        else:
            await interaction.response.send_message(
                interaction.user.mention
                + " you don't have enough money. You only have ($"
                + str(money1)
                + ")."
            )

    async def dolphin_callback(interaction):
        try:
            with open("Players/" + str(interaction.user.id), "x") as f:
                money1 = 1000
            with open("Players/" + str(interaction.user.id), "w") as f:
                f.write("1000\n0\n0\n3\n0\n0")
        except:
            with open("Players/" + str(interaction.user.id), "r") as f:
                stats = f.readlines()
                money1 = int(stats[0])
                luck = int(stats[4])
        if money1 > 999999:
            money1 -= 1000000
            luck = 3
            with open("Players/" + str(interaction.user.id), "w") as f:
                f.write(
                    str(money1)
                    + "\n"
                    + stats[1]
                    + stats[2]
                    + stats[3]
                    + str(luck)
                    + "\n"
                    + stats[5]
                )
            await interaction.response.send_message(
                interaction.user.mention + " bought 3% luck for ($1'000'000)."
            )
        else:
            await interaction.response.send_message(
                interaction.user.mention
                + " you don't have enough money. You only have ($"
                + str(money1)
                + ")."
            )

    async def butterfly_callback(interaction):
        try:
            with open("Players/" + str(interaction.user.id), "x") as f:
                money1 = 1000
            with open("Players/" + str(interaction.user.id), "w") as f:
                f.write("1000\n0\n0\n3\n0\n0")
        except:
            with open("Players/" + str(interaction.user.id), "r") as f:
                stats = f.readlines()
                money1 = int(stats[0])
                luck = int(stats[4])
        if money1 > 14999999:
            money1 -= 15000000
            luck = 5
            with open("Players/" + str(interaction.user.id), "w") as f:
                f.write(
                    str(money1)
                    + "\n"
                    + stats[1]
                    + stats[2]
                    + stats[3]
                    + str(luck)
                    + "\n"
                    + stats[5]
                )
            await interaction.response.send_message(
                interaction.user.mention + " bought 5% luck for ($15'000'000)."
            )
        else:
            await interaction.response.send_message(
                interaction.user.mention
                + " you don't have enough money. You only have ($"
                + str(money1)
                + ")."
            )

    home.callback = home_callback
    shop.callback = shop_callback
    shopvip.callback = shopvip_callback
    help.callback = help_callback
    strenght.callback = strenght_callback
    drop.callback = drop_callback
    stmoney.callback = stmoney_callback
    mouse.callback = mouse_callback
    bee.callback = bee_callback
    dolphin.callback = dolphin_callback
    butterfly.callback = butterfly_callback

    view = View()
    view.add_item(home)
    view.add_item(shop)
    view.add_item(shopvip)
    view.add_item(help)
    

    market = View()
    market.add_item(home)
    market.add_item(strenght)
    market.add_item(drop)
    market.add_item(stmoney)
    market.add_item(mouse)
    market.add_item(bee)
    market.add_item(dolphin)
    market.add_item(butterfly)
    await ctx.send(embed=embed, view=view)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = ctx.author.mention + " This command is on cooldown ({:.0f}s)".format(
            error.retry_after
        )
        await ctx.send(msg)
    else:
        pass


@commands.cooldown(1, 60, commands.BucketType.user)
@bot.command(aliases=["Drop", "DROP", "DRop", "DroP"])
async def drop(ctx):
    try:
        with open("Players/" + str(ctx.author.id), "x") as f:
            money1 = 1000
        with open("Players/" + str(ctx.author.id), "w") as f:
            luck = 0
            f.write("1000\n0\n0\n3\n0\n0")
    except:
        pass
    with open("Players/" + str(ctx.author.id), "r") as f:
        stats = f.readlines()
        money1 = int(stats[0])
        drop = int(stats[2])
        karma = int(stats[5])

    rlow = random.randint(1, 3)
    karma += rlow
    drop=int(drop)
    r=random.randint(round((300-drop/4)*drop+500),round((1000-drop/4)*drop+1500))
    await ctx.send(
        ctx.author.mention + " has earned $" + str(r) + " and " + str(rlow) + " Karma"
    )
    money1 += r
    with open("Players/" + str(ctx.author.id), "w") as file:
        file.write(
            str(money1) + "\n" + stats[1] + stats[2] + stats[3] + stats[4] + str(karma)
        )


@bot.command(aliases=["Attack", "ATTACK", "AttacK"])
async def attack(ctx, member: nextcord.Member):
    try:
        with open("Players/" + str(ctx.author.id), "x") as f:
            money1 = 1000
            # sleep(0.1)
        with open("Players/" + str(ctx.author.id), "w") as f:
            luck = 0
            f.write("1000\n0\n0\n3\n0\n0")
    except:
        pass

    with open("Players/" + str(ctx.author.id), "r") as f:
        stats = f.readlines()
        money1 = int(stats[0])
        strenght1 = int(stats[1])
        stmoney1 = float(stats[3])
        karma1 = int(stats[5])
    id2 = member.id

    with open("Players/" + str(id2), "r") as f:
        stats2 = f.readlines()
        money2 = int(stats2[0])
        strenght2 = int(stats2[1])
        stmoney2 = int(stats2[3])
        karma2 = int(stats2[5])

    # se attaccante vince
    if karma1 >= 0:
        if strenght1 > strenght2:
            rlow = random.randint(1, 5)
            rmax = random.randint(6, 10)
            bottino = money2 / 100 * stmoney1
            money1 += bottino

            if bottino >= 100000:
                karma1 -= rmax
            else:
                karma1 -= rlow

            money2 -= bottino

            # ROUND
            money1 = round(money1)
            money2 = round(money2)
            bottino = round(bottino)

            with open("Players/" + str(ctx.author.id), "w") as f:
                f.write(
                    str(money1)
                    + "\n"
                    + stats[1]
                    + stats[2]
                    + stats[3]
                    + stats[4]
                    + str(karma1)
                )
            with open("Players/" + str(id2), "w") as f:
                f.write(
                    str(money2)
                    + "\n"
                    + stats2[1]
                    + stats2[2]
                    + stats2[3]
                    + stats2[4]
                    + str(karma2)
                )
            await ctx.send(
                ctx.author.mention + " stole from his opponent $" + str(bottino)
            )
        # se difensore vince
        if strenght1 < strenght2:
            rlow = random.randint(1, 5)
            karma1 -= rlow
            karma2 += rlow

            bottino = money1 / 100 * stmoney2
            money1 -= bottino

            money2 += bottino

            money1 = round(money1)
            money2 = round(money2)
            bottino = round(bottino)

            with open("Players/" + str(ctx.author.id), "w") as f:
                f.write(
                    str(money1)
                    + "\n"
                    + stats[1]
                    + stats[2]
                    + stats[3]
                    + stats[4]
                    + str(karma1)
                )
            with open("Players/" + str(id2), "w") as f:
                f.write(
                    str(money2)
                    + "\n"
                    + stats2[1]
                    + stats2[2]
                    + stats2[3]
                    + stats2[4]
                    + str(karma2)
                )

            await ctx.send(
                ctx.author.mention
                + " was too weak and his opponent stole from him $"
                + str(bottino)
            )

        # se pareggiano
        if strenght1 == strenght2:
            rlow = random.randint(1, 5)
            karma1 -= rlow
            karma2 += rlow

            with open("Players/" + str(ctx.author.id), "w") as f:
                f.write(
                    stats[0] + stats[1] + stats[2] + stats[3] + stats[4] + str(karma1)
                )
            with open("Players/" + str(id2), "w") as f:
                f.write(
                    stats2[0]
                    + stats2[1]
                    + stats2[2]
                    + stats2[3]
                    + stats2[4]
                    + str(karma2)
                )
            await ctx.send(
                ctx.author.mention
                + " ran away, he and his opponents had the same strenght!"
            )

    else:
        await ctx.send(ctx.author.mention + " your karma is negative!")


@bot.command(aliases=["Profile", "PROFILE", "proFile", "ProFile", "stats"])
async def profile(ctx):
    try:
        with open("Players/" + str(ctx.author.id), "x") as f:
            money1 = 1000
        with open("Players/" + str(ctx.author.id), "w") as f:
            luck = 0
            f.write("1000\n0\n0\n3\n0\n0")
    except:
        pass
    with open("Players/" + str(ctx.author.id), "r") as f:
        stats = f.readlines()
        money1 = stats[0]
        strenght = stats[1]
        drop = stats[2]
        stmoney = stats[3]
        luck = stats[4]
        karma = stats[5]
    embed = nextcord.Embed(
        title=ctx.author,
        description="💰ᴍᴏɴᴇʏ ($"
        + str(money1).strip("\n")
        + ")\n💪🏼Sᴛʀᴇɴɢʜᴛ ("
        + str(strenght).strip("\n")
        + ")\n💸ᴅʀᴏᴘ ("
        + str(drop).strip("\n")
        + ")\n🥷Sᴛᴇᴀʟɪɴɢ ᴘᴏᴡᴇʀ ("
        + str(stmoney).strip("\n")
        + "%)\n🍀ʟᴜᴄᴋ (+"
        + str(luck).strip("\n")
        + "%)\n💥ᴋᴀʀᴍᴀ ("
        + str(karma).strip("n")
        + ")",
        color=0xF9E655,
    )
    embed.set_author(
        name="Satu Bot"
    )  # embed.set_footer(text="💰Money ($"+str(money1).strip('\n')+")\n💪🏼Strenght ("+str(strenght).strip('\n')+")\n💸Drop ("+str(drop).strip('\n')+")\n🥷Stealing power ("+st.strip('\n')trip('\n')+")\n🍀Luck ("+str(luck).strip('\n')+")")
    return await ctx.send(embed=embed)


@bot.command(aliases=["Money", "balance", "Balance", "MONEY", "BALANCE"])
async def money(ctx):
    try:
        with open("Players/" + str(ctx.author.id), "r") as f:
            epicz = f.readlines()
            money = int(epicz[0])
            await ctx.send(ctx.author.mention + " has ($" + str(money) + ").")
    except Exception as e:
        print("Qualcosa di strano è successo")
        print(e)
        await ctx.send(ctx.author.mention + " has ($1000).")


@bot.command(aliases=["Leaderboard", "LeaderBoard", "LEADERBOARD"])
async def leaderboard(ctx, x=10):
    leader_board = {}
    total = []
    for user in os.listdir("Players"):
        with open("Players/" + user, "r") as f:
            stats = f.readlines()
            soldoni = stats[0].strip('\n')
        name = int(user)
        total_amount = soldoni
        leader_board[total_amount] = name
        total.append(total_amount)

    #total = sorted(total, reverse=True,key=len)
    total.sort(reverse=True, key=int)

    em = nextcord.Embed(title="Leaderboard", color=0xF9E655)
    index = 1
    for amt in total:
        user_id = leader_board[amt]
        user_id = int(user_id)
        name = await bot.fetch_user(user_id)

        em.add_field(name=f"{index}. {name}", value=f"{amt}", inline=False)
        if index == x:

            break
        else:
            index += 1
    await ctx.send(embed=em)


bot.run(my_secret)
