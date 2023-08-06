import os
import sys

SCRIPT_DIR = "."
if __name__ == "__main__":
    SCRIPT_DIR = os.path.dirname(
        os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__)))
    )
    SCRIPT_DIR = os.path.join(SCRIPT_DIR, "..")
    sys.path.insert(0, os.path.normpath(SCRIPT_DIR))

from buffy.buffypyclient import (
    BuffyPyClient,
    ReCachingStrategy,
    RequestCacheConfiguration,
)
from requests.auth import HTTPBasicAuth

owl_url = "http://purl.obolibrary.org/obo/bfo.owl"

# connect to Buffy-server
c = BuffyPyClient(
    host="localhost",
    port=8008,
    ssl=False,
    local_download_fallback=False,
    http_auth=HTTPBasicAuth(username="username", password="mySuperPasswort"),
)

# this will redownload the owl file every 24h
strategy = ReCachingStrategy.age(seconds=60 * 60 * 24)
# Lets pack the strategy in our cache config and define that the want to keep the last 3 versions
config = RequestCacheConfiguration(
    recaching_strategy=strategy, max_cached_unpinned_versions=3
)

# create a request
req = c.create_request(
    url=owl_url,
    http_header_fields={
        "user-agent": "MyTestClient",
        "Accept": "text/plain",
    },
    cache_configuration=config,
)
# save requested file
owl_file = ""
for chunk in req.download_response_content():
    owl_file += chunk.decode("utf-8")
print(owl_file)
