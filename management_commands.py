from bot import client, ADMINS, HOME_GUILDS
import data
from nextcord import Interaction, Permissions, SlashOption, Embed
import webcolors


@client.slash_command(
    name="add_server",
    description="Grant permission to a new discord server.",
    default_member_permissions=Permissions(administrator=True),
    guild_ids=HOME_GUILDS,
    dm_permission=False,
)
async def add_server(interaction: Interaction, id: str = SlashOption(required=True)):
    if interaction.user.id not in ADMINS:
        await interaction.send(
            "You don't have enough permissions to use this command.", ephemeral=True
        )
        return

    interaction_response = await interaction.send("Please wait...", ephemeral=True)

    server_id = int(id)
    target_guild = client.get_guild(server_id)
    if target_guild is None:
        await interaction_response.edit("Server with this id does not exists.")
        return

    result = data.add_server(str(target_guild), server_id)
    if result == server_id:
        await interaction_response.edit(
            f"Server **{target_guild}** has been registered and activated.",
        )
    else:
        await interaction_response.edit(str(result))


@client.slash_command(
    name="edit_server",
    description="Edit permissions of a discord server.",
    default_member_permissions=Permissions(administrator=True),
    guild_ids=HOME_GUILDS,
    dm_permission=False,
)
async def edit_server(
    interaction: Interaction,
    id: str = SlashOption(required=True),
    active: bool = SlashOption(required=True),
):
    if interaction.user.id not in ADMINS:
        await interaction.send(
            "You don't have enough permissions to use this command.", ephemeral=True
        )
        return

    interaction_response = await interaction.send("Please wait...", ephemeral=True)

    server_id = int(id)
    target_guild = client.get_guild(server_id)
    if target_guild is None:
        await interaction_response.edit("Server with this id does not exists.")
        return

    result = data.edit_server(server_id, active)
    if result == server_id:
        active_status = "activated" if active else "deactivated"
        await interaction_response.edit(
            f"Server **{target_guild}** has been **{active_status}**.",
        )
    else:
        await interaction_response.edit(str(result))


@client.slash_command(
    name="remove_server",
    description="Remove permission from a discord server.",
    default_member_permissions=Permissions(administrator=True),
    guild_ids=HOME_GUILDS,
    dm_permission=False,
)
async def remove_server(interaction: Interaction, id: str = SlashOption(required=True)):
    if interaction.user.id not in ADMINS:
        await interaction.send(
            "You don't have enough permissions to use this command.", ephemeral=True
        )
        return

    interaction_response = await interaction.send("Please wait...", ephemeral=True)

    server_id = int(id)
    target_guild = client.get_guild(server_id)
    if target_guild is None:
        await interaction_response.edit("Server with this id does not exists.")
        return

    result = data.remove_server(server_id)
    if result == server_id:
        await interaction_response.edit(
            f"Server **{target_guild}** has been removed.",
        )
    else:
        await interaction_response.edit(str(result))


@client.slash_command(
    name="settings",
    description="Change bot settings.",
    default_member_permissions=Permissions(administrator=True),
    dm_permission=False,
)
async def settings(
    interaction: Interaction,
    setting: str = SlashOption(
        name="setting",
        required=True,
        choices=[
            "Set welcome channel id",
            "Set role message id",
            "Set free game channel id",
            "Set free game role id",
            "Set DST role id",
            "Set member count channel id",
        ],
    ),
    id: str = SlashOption(required=True),
):
    interaction_response = await interaction.send("Please wait...", ephemeral=True)
    if setting == "Set welcome channel id":
        try:
            if id.lower() in ["none", "null", "0", "-"]:
                result = data.set_welcome_channel_id(interaction.guild_id, None)
                if result == None:
                    await interaction_response.edit(
                        "Welcome channel has been unset.",
                    )
                else:
                    await interaction_response.edit(str(result))
                return

            message_id = int(id)
            result = data.set_welcome_channel_id(interaction.guild_id, message_id)
            if result == message_id:
                await interaction_response.edit(
                    "Welcome channel has been set.",
                )
            else:
                await interaction_response.edit(str(result))
        except Exception as e:
            print(e)
            await interaction_response.edit(str(e))

    if setting == "Set free game channel id":
        try:
            if id.lower() in ["none", "null", "0", "-"]:
                result = data.set_free_games_channel_id(interaction.guild_id, None)
                if result == None:
                    await interaction_response.edit(
                        "free game channel has been unset.",
                    )
                else:
                    await interaction_response.edit(str(result))
                return

            message_id = int(id)
            result = data.set_free_games_channel_id(interaction.guild_id, message_id)
            if result == message_id:
                await interaction_response.edit(
                    "free game channel has been set.",
                )
            else:
                await interaction_response.edit(str(result))
        except Exception as e:
            print(e)
            await interaction_response.edit(str(e))

    if setting == "Set free game role id":
        try:
            if id.lower() in ["none", "null", "0", "-"]:
                result = data.set_free_games_role_id(interaction.guild_id, None)
                if result == None:
                    await interaction_response.edit(
                        "Free game role has been unset.",
                    )
                else:
                    await interaction_response.edit(str(result))
                return

            role_id = int(id)
            result = data.set_free_games_role_id(interaction.guild_id, role_id)
            if result == role_id:
                await interaction_response.edit(
                    "Free game role has been set.",
                )
            else:
                await interaction_response.edit(str(result))
        except Exception as e:
            print(e)
            await interaction_response.edit(str(e))

    if setting == "Set DST role id":
        try:
            if id.lower() in ["none", "null", "0", "-"]:
                result = data.set_dst_role_id(interaction.guild_id, None)
                if result == None:
                    await interaction_response.edit(
                        "DST role has been unset.",
                    )
                else:
                    await interaction_response.edit(str(result))
                return

            role_id = int(id)
            result = data.set_dst_role_id(interaction.guild_id, role_id)
            if result == role_id:
                await interaction_response.edit(
                    "DST role has been set.",
                )
            else:
                await interaction_response.edit(str(result))
        except Exception as e:
            print(e)
            await interaction_response.edit(str(e))

    if setting == "Set member count channel id":
        try:
            if id.lower() in ["none", "null", "0", "-"]:
                result = data.set_member_count_channel_id(interaction.guild_id, None)
                if result == None:
                    await interaction_response.edit(
                        "member count channel has been unset.",
                    )
                else:
                    await interaction_response.edit(str(result))
                return

            message_id = int(id)
            result = data.set_member_count_channel_id(interaction.guild_id, message_id)
            if result == message_id:
                await interaction_response.edit(
                    "member count channel has been set.",
                )
            else:
                await interaction_response.edit(str(result))
        except Exception as e:
            print(e)
            await interaction_response.edit(str(e))

    if setting == "Set role message id":
        try:
            if id.lower() in ["none", "null", "0", "-"]:
                result = data.set_role_message_id(interaction.guild_id, None)
                if result == None:
                    await interaction_response.edit("Role message has been unset."),
                else:
                    await interaction_response.edit(str(result))
                return

            message_id = int(id)
            result = data.set_role_message_id(interaction.guild_id, message_id)
            if result == message_id:
                await interaction_response.edit(
                    "Role message has been set.",
                )
            else:
                await interaction_response.edit(str(result))
        except Exception as e:
            print(e)
            await interaction_response.edit(str(e))


# set roles by emojis
@client.slash_command(
    name="set_role_emoji",
    description="Choose an emoji to assign a roll",
    default_member_permissions=Permissions(administrator=True),
    dm_permission=False,
)
async def set_role_emoji(
    interaction: Interaction,
    emoji_name: str = SlashOption(
        name="emoji_name",
        description="CaSe sEnSiTiVe!",
        required=True,
    ),
    role_name: str = SlashOption(
        name="role_name", description="CaSe sEnSiTiVe!", required=True
    ),
):
    interaction_response = await interaction.send(f"Please wait ...", ephemeral=True)

    get_roles = data.get_role_emoji(interaction.guild_id)
    if get_roles == None:
        get_roles = {}
    if role_name.lower() in ["none", "null", "0", "-"]:
        get_roles.pop(emoji_name)
        await interaction_response.edit("Emoji and roll removed!")
    else:
        get_roles[emoji_name] = role_name
        await interaction_response.edit("Emoji and roll paired!")
    data.set_role_emoji(interaction.guild_id, get_roles)


@client.slash_command(
    name="embed",
    description=" Send an embed message",
    default_member_permissions=Permissions(administrator=True),
    dm_permission=False,
)
async def embed(
    interaction: Interaction,
    text: str = SlashOption(required=True, description="Write a text in embed"),
    color: str = SlashOption(
        required=False,
        description="Color name or HEX e.g: red/ff0000, default color is cyan.",
    ),
):
    try:
        default_color = "cyan"
        if color is None:
            color = default_color
        try:
            rgb = webcolors.name_to_rgb(color)
            hex_value = webcolors.rgb_to_hex(rgb)
            embed_color = hex_value.replace("#", "0x")
            embed_color = int(embed_color, base=16)
        except Exception:
            await interaction.send("Your color or HEX not found.", ephemeral=True)
            return
        if hex_value is None:
            try:
                embed_color = int(f"0x{color}", base=16)
            except Exception:
                await interaction.send("Your color or HEX not found.", ephemeral=True)
                return

        embed = Embed(title=text, color=embed_color)
        await interaction.send(embed=embed)
    except Exception:
        await interaction.send("Unknown error.", ephemeral=True)
