import zipfile

try:
    with zipfile.ZipFile("try.zip", 'r') as zip_ref:
        for info in zip_ref.infolist():
            try:
                zip_ref.extract(info, path="destination_folder")
            except zipfile.BadZipFile as e:
                print(f"Corrupt file: {info.filename} - {e}")
                continue
            except zipfile.BadCRC as e:
                print(f"Bad CRC for file: {info.filename} - {e}")
                pass
except zipfile.BadZipFile as e:
    print(f"Could not read zipfile: {e}")
