from androguard.misc import AnalyzeAPK
import os

apk_folder = "crawler/crawler/apk_files"

for apk_file in os.listdir(apk_folder):
    if apk_file.endswith(".apk"):
        apk_path = os.path.join(apk_folder, apk_file)

        print("\n========================")
        print("Analyzing:", apk_file)

        try:
            a, d, dx = AnalyzeAPK(apk_path)

            print("Package Name:", a.get_package())
            print("Permissions:", a.get_permissions()[:5])  # first 5 only

        except Exception as e:
            print("Error:", e)