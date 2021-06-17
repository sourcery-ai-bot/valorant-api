"""A asynchronous api client for https://valorant-api.com"""
import aiohttp


class AsyncClient:
    """A asynchronous api client for https://valorant-api.com"""

    def __init__(self) -> None:
        """A asynchronous api client for https://valorant-api.com"""
        self.session = aiohttp.ClientSession()

    async def get_agents(self) -> dict:
        """Get the response from https://valorant-api.com/v1/agents

        Returns:
            dict: The response from https://valorant-api.com/v1/agents
        """
        async with self.session.get("https://valorant-api.com/v1/agents") as response:
            return await response.json()

    async def get_buddies(self) -> dict:
        """Get the response from https://valorant-api.com/v1/buddies

        Returns:
            dict: The response from https://valorant-api.com/v1/buddies
        """
        async with self.session.get("https://valorant-api.com/v1/buddies") as response:
            return await response.json()

    async def get_bundles(self) -> dict:
        """Get the response from https://valorant-api.com/v1/bundles

        Returns:
            dict: The response from https://valorant-api.com/v1/bundles
        """
        async with self.session.get("https://valorant-api.com/v1/bundles") as response:
            return await response.json()

    async def get_contenttiers(self) -> dict:
        """Get the response from https://valorant-api.com/v1/contenttiers

        Returns:
            dict: The response from https://valorant-api.com/v1/contenttiers
        """
        async with self.session.get(
            "https://valorant-api.com/v1/contenttiers"
        ) as response:
            return await response.json()

    async def get_currencies(self) -> dict:
        """Get the response from https://valorant-api.com/v1/currencies

        Returns:
            dict: The response from https://valorant-api.com/v1/currencies
        """
        async with self.session.get(
            "https://valorant-api.com/v1/currencies"
        ) as response:
            return await response.json()

    async def get_gamemodes(self) -> dict:
        """Get the response from https://valorant-api.com/v1/gamemodes

        Returns:
            dict: The response from https://valorant-api.com/v1/gamemodes
        """
        async with self.session.get(
            "https://valorant-api.com/v1/gamemodes"
        ) as response:
            return await response.json()

    async def get_maps(self) -> dict:
        """Get the response from https://valorant-api.com/v1/maps

        Returns:
            dict: The response from https://valorant-api.com/v1/maps
        """
        async with self.session.get("https://valorant-api.com/v1/maps") as response:
            return await response.json()

    async def get_playercards(self) -> dict:
        """Get the response from https://valorant-api.com/v1/playercards

        Returns:
            dict: The response from https://valorant-api.com/v1/playercards
        """
        async with self.session.get(
            "https://valorant-api.com/v1/playercards"
        ) as response:
            return await response.json()

    async def get_playertitles(self) -> dict:
        """Get the response from https://valorant-api.com/v1/playertitles

        Returns:
            dict: The response from https://valorant-api.com/v1/playertitles
        """
        async with self.session.get(
            "https://valorant-api.com/v1/playertitles"
        ) as response:
            return await response.json()

    async def get_seasons(self) -> dict:
        """Get the response from https://valorant-api.com/v1/seasons

        Returns:
            dict: The response from https://valorant-api.com/v1/seasons
        """
        async with self.session.get("https://valorant-api.com/v1/seasons") as response:
            return await response.json()

    async def get_sprays(self) -> dict:
        """Get the response from https://valorant-api.com/v1/sprays

        Returns:
            dict: The response from https://valorant-api.com/v1/sprays
        """
        async with self.session.get("https://valorant-api.com/v1/sprays") as response:
            return await response.json()

    async def get_themes(self) -> dict:
        """Get the response from https://valorant-api.com/v1/themes

        Returns:
            dict: The response from https://valorant-api.com/v1/themes
        """
        async with self.session.get("https://valorant-api.com/v1/themes") as response:
            return await response.json()

    async def get_weapons(self) -> dict:
        """Get the response from https://valorant-api.com/v1/weapons

        Returns:
            dict: The response from https://valorant-api.com/v1/weapons
        """
        async with self.session.get("https://valorant-api.com/v1/weapons") as response:
            return await response.json()

    async def get_version(self) -> dict:
        """Get the response from https://valorant-api.com/v1/version

        Returns:
            dict: The response from https://valorant-api.com/v1/version
        """
        async with self.session.get("https://valorant-api.com/v1/version") as response:
            return await response.json()

    async def close(self) -> None:
        """Closes the aiohttp.ClientSession"""
        await self.session.close()
