import os
import requests
from datetime import datetime
from sequoia.core.config import config


class NotifySlack:
    """Send notifikasi ke slack channel"""

    async def send_slack(self, text: str):
        text = f"{text} - {datetime.now()} - {os.getenv('PROJECT_SERVER')}"
        requests.post(config.SLACK, json={"text": text})
