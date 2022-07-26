from discord.ext import commands, vbu


class FarmyardCommands(vbu.Cog):
    """
    Commands that handle a user's properties.
    """

    @commands.group(
        application_command_meta=commands.ApplicationCommandMeta(),
    )
    async def farmyard(self, _: commands.SlashContext):
        ...

    @farmyard.command(
        name="create",
        application_command_meta=commands.ApplicationCommandMeta(),
    )
    async def farmyard_create(self, ctx: commands.SlashContext):
        """
        """

        ...

    @farmyard.command(
        name="clear",
        application_command_meta=commands.ApplicationCommandMeta(),
    )
    async def farmyard_clear(self, ctx: commands.SlashContext):
        """
        """

        ...

    @farmyard.command(
        name="list",
        application_command_meta=commands.ApplicationCommandMeta(),
    )
    async def farmyard_list(self, ctx: commands.SlashContext):
        """
        """

        ...


def setup(bot: vbu.Bot):
    x = FarmyardCommands(bot)
    bot.add_cog(x)
