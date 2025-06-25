import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@bot.tree.command(name="test", description="Replies with Test")
async def test_command(interaction: discord.Interaction):
    await interaction.response.send_message("Test")

# Replace this with your bot token
bot.run("YOUR_BOT_TOKEN")
