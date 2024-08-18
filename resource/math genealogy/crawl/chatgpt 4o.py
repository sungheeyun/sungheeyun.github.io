""" chatgpt 4o spit out this code
for paring math genealogy website
"""

import json
from logging import getLogger, Logger
import re
from typing import Any

import requests
from bs4 import BeautifulSoup

from freq_used.logging_utils import set_logging_basic_config

logger: Logger = getLogger()

class StopCrawlingException(Exception):
    pass


def crawl(data: dict[str, Any], id: str, depth: int, /) -> None:
    if depth < 0 or id in data:
        return

    url = f"https://genealogy.math.ndsu.nodak.edu/id.php?id={id}"
    response = requests.get(url)

    if response.status_code != 200:
        logger.warning(
            f"For id={id}, request received status code {response.status_code}"
        )
        return

    soup = BeautifulSoup(response.content, "html.parser")

    # Extracting the mathematician's name
    name: str = soup.find("h2").get_text().strip()

    # Extracting advisor(s)
    advisors = []
    advisor_elements = soup.find_all(string=re.compile("Advisor(\s+\d)?:.*"))
    for advisor_element in advisor_elements:
        try:
            advisor_name: str = advisor_element.find_next_sibling("a").get_text()
        except AttributeError as e:
            logger.warning(f"AttributeError: {e}, {advisor_element}")
            return

        advisor_id: str = re.match(
            "id\.php\?id=(\d+)$", advisor_element.next_element.attrs["href"]
        ).group(1)
        advisors.append(dict(name=advisor_name, id=advisor_id))

    data[id] = dict(id=id, name=name, advisors=advisors, height=depth)
    print(depth, id, name)

    if name.startswith("Carl Friedrich"):
        raise StopCrawlingException()

    for advisor in advisors:
        crawl(data, advisor["id"], depth - 1)


if __name__ == "__main__":
    set_logging_basic_config(__file__)

    my_id: str = "283283"
    depth: int = 10
    my_math_gen_data: dict[str, dict[str, Any]] = dict()
    try:
        crawl(my_math_gen_data, my_id, depth)
    except StopCrawlingException:
        pass

    print(json.dumps(my_math_gen_data, indent=2))
    with open("my_math_gen.json", "w") as fid:
        json.dump(my_math_gen_data, fid, indent=2)
