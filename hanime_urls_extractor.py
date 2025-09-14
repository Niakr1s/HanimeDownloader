# First, select year in https://hanime.tv/browse/seasons
# Then, download web page (Ctrl+S in Firefox, select complete web page)

# then, run this script:
# python hanime_urls_extractor.py path/to/html/file.htm

# output file will be located in path/to/html/file.txt
# note: all urls will be reversed, for more easier concantenation if needed

import re
import sys

from pathlib import Path


html_file_path = Path(sys.argv[1])
urls_file_path = html_file_path.with_suffix(".txt")

html_file_contents = html_file_path.read_text(encoding="utf8")


RE = re.compile(r"(https:\/\/hanime\.tv\/videos\/hentai\/.*?)\"")
urls = RE.findall(html_file_contents)

urls_file_path.write_text("\n".join(reversed(urls)))

print(f"Saved {len(urls)} urls into {urls_file_path}")