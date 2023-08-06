import pyFipper

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from typing import Union

class EndClient:
    async def endclient(
        self: "pyFipper.Client",
        end_time: Union[int, str],
    ):
        """Disconnect the client from Telegram servers.

        Raises:
            ConnectionError: In case you try to disconnect an already disconnected client or in case you try to
                disconnect a client that needs to be terminated first.
        """
        while True:
            dt_now = datetime.now()
            months = dt_now + timedelta(minutes=end_time)
            if dt_now == months:
                if self.is_connected:
                    await self.stop()
            else:
                pass
