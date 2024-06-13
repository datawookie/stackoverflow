import re
from collections import defaultdict

import pandas as pd


class ParquetPipeline:
    def open_spider(self, spider):
        self.items = defaultdict(lambda: [])

    def close_spider(self, spider):
        # Iterate over pages, writing data for each to a parquet file.
        #
        for page, data in self.items.items():
            df = pd.DataFrame(data)
            df.to_parquet(f"page-{page}.parquet", index=False)

    def process_item(self, item, spider):
        # Extract page number from URL.
        page = int(re.search(r"/page/(\d+)/", item["file_urls"]).group(1))

        self.items[page].append(dict(item))
        return item
