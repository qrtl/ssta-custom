This module does the following:

* This module is used in env where have only one product record per product

* A cron task that will "Archive" products which have met certain conditions.

  - Target products to "Archive": The product has to be a stockable or consumable product and (qty_delivered > 0)
