import re
from collections import defaultdict


class ParquetPipeline:
    def open_spider(self, spider):
        self.items = defaultdict(lambda: [])

    def close_spider(self, spider):
        # Iterate over items, writing each to Parquet.
        #
        for name, df in self.items.items():
            df.to_parquet(name, index=False)

    def process_item(self, item, spider):
        # Get CSV filename.
        csv = re.search("[^/]+$", item["url"]).group(0)
        # Create Parquet filename.
        parquet = re.sub("\.csv", ".parquet", csv)

        self.items[parquet] = item["data"]
