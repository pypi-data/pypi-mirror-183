# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiohere']

package_data = \
{'': ['*']}

modules = \
['py']
install_requires = \
['aiohttp>=3.8.3,<4.0.0']

setup_kwargs = {
    'name': 'aiohere',
    'version': '2.1.0',
    'description': 'Asynchronous Python client for the HERE API',
    'long_description': '# aiohere\n\nAsynchronous Python client for the HERE API\n\nBased on [herepy](https://github.com/abdullahselek/HerePy)\n\n[![GitHub Actions](https://github.com/eifinger/aiohere/workflows/CI/badge.svg)](https://github.com/eifinger/aiohere/actions?workflow=CI)\n[![PyPi](https://img.shields.io/pypi/v/aiohere.svg)](https://pypi.python.org/pypi/aiohere)\n[![PyPi](https://img.shields.io/pypi/l/aiohere.svg)](https://github.com/eifinger/aiohere/blob/master/LICENSE)\n[![codecov](https://codecov.io/gh/eifinger/aiohere/branch/master/graph/badge.svg)](https://codecov.io/gh/eifinger/aiohere)\n[![Downloads](https://pepy.tech/badge/aiohere)](https://pepy.tech/project/aiohere)\n\n## Installation\n\n```bash\npip install aiohere\n```\n\n## Usage\n\n```python\nfrom aiohere import AioHere, WeatherProductType\n\nimport asyncio\n\nAPI_KEY = ""\n\n\nasync def main():\n    """Show example how to get weather forecast for your location."""\n    async with AioHere(api_key=API_KEY) as aiohere:\n        response = await aiohere.weather_for_coordinates(\n            latitude=49.9836187,\n            longitude=8.2329145,\n            products=[WeatherProductType.FORECAST_7DAYS_SIMPLE],\n        )\n        lowTemperature = response["dailyForecasts"][0]["forecasts"][0]["lowTemperature"]\n        highTemperature = response["dailyForecasts"][0]["forecasts"][0][\n            "highTemperature"\n        ]\n        weekday = response["dailyForecasts"][0]["forecasts"][0]["weekday"]\n\n        print(\n            f"Temperature on {weekday} will be between {lowTemperature}°C and {highTemperature}°C"\n        )\n\n\nif __name__ == "__main__":\n    loop = asyncio.new_event_loop()\n    loop.run_until_complete(main())\n```\n\n<a href="https://www.buymeacoffee.com/eifinger" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/black_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a><br>\n',
    'author': 'Kevin Stillhammer',
    'author_email': 'kevin.stillhammer@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'http://github.com/eifinger/aiohere',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
