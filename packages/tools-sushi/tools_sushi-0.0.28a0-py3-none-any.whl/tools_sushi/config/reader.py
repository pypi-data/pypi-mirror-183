import json
import os
from typing import Optional

from exceptions.ConfigNotFound import ConfigNotFound


class config_reader():
    def get_config_data(path: Optional[str] = 'sushi.json') -> any:
        # check if json exists
        if not os.path.exists(path):
            raise ConfigNotFound("config not found")

        data = json.load(open(path))
        return data
