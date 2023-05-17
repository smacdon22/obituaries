# Casket Obituaries

## Processing

Run processing_obits_for_import.py, with your data and various parameters.
You should have a new folder with xml files of your data.
Now run create_zips.py with the settings you want.

## Uploading
Upload the zips via the batch ingest in your Islandora collection.

## Checking

In your collection, go to Manage->Collection->Generate CSV file of metadata used in this collection.
Choose which fields you want, all you need is dc.identifier but I chose mods_* (bad choice).
Run data-check, comment out most of it if you only exported the identifiers, but this will go through all the mods fields and take out what you need.



Hope that you get no lists printed and a zero at the end. Some of the name checking was more so data problems with spreadsheet, but good to know what's missing from the titles :)
