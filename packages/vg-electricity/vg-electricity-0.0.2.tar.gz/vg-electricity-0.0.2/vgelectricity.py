""" Simple Python class to interact with the VG electricity API
"""

import logging
import aiohttp

from const import BASE_URL

logger = logging.getLogger('vg-electricity')

class VGElectricity:
    """VG API connection class"""

    def __init__(self):

        self.session = aiohttp.ClientSession()

    async def today(self):
        """Get Today's electricity stats"""
        return await self._get("v2/nordpool/historic/day")

    async def future(self):
        """Get estimated future electricity prices"""
        return await self._get("v1/nasdaq/future-prices")

    async def _get(self, uri):
        """Generic GET request helper function"""
        url = f'{BASE_URL}{uri}'
        async with self.session.get(url) as resp:
            return await resp.json()

    async def close_session(self):
        """Close the connection session"""
        await self.session.close()
    
 
    async def sensor_data(self):
        """Get flat json structure for Home Assistant Sensor parsing"""
        data = {}
        data['state'] = "unavailable"

        try:
            today = await self.today()
            
            if today:
                data['state'] = "available"
                data['oslo_price_this_month'] = today['soFarThisMonth']['oslo']
                data['bergen_price_this_month'] = today['soFarThisMonth']['bergen']
            
            future = await self.future()

            if future:
                data['oslo_price_future_month'] = future['regions']['oslo']['periodTypes']['m'][0]['priceNOK']
                data['bergen_price_future_month'] = future['regions']['bergen']['periodTypes']['m'][0]['priceNOK']

        except Exception as ex:
            logger.error('Exception during data parsing update: %s', ex)

        return data
