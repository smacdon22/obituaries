# Casket Obituaries

## Processing

1. Run `processing_obits_for_import.py` with your data and desired parameters.
   - This will generate a new folder containing XML files of your data.

2. Run `create_zips.py` with your preferred settings.
   - This will create ZIP files based on the generated XML files.

## Uploading

1. Upload the ZIP files using the batch ingest feature in your Islandora collection.

## Checking

1. In your collection, navigate to **Manage** ➜ **Collection** ➜ **Generate CSV file of metadata used in this collection**.
   - Select the fields you require; at minimum, you need `dc.identifier`, but I recommend choosing `mods_*` (although it may not be the best choice).
   
2. Run `data-check.py`, and if you only exported the identifiers, comment out most of the script.
   - This step will process the metadata and extract the necessary information if you exported more fields.

3. Ensure that no lists are printed, and there is a zero displayed at the end.
   - Any inconsistencies with names may be due to data problems in the spreadsheet, but it is useful to identify any missing titles.
