from supabase import create_client, Client

url = "https://spuorfzpecagkepiidwt.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNwdW9yZnpwZWNhZ2tlcGlpZHd0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM4NDUwOTcsImV4cCI6MjA4OTQyMTA5N30.MSSSPLwcekuhoEB2dp64a67BQyQpHTufzbM0UBVRHfI"

supabase: Client = create_client(url, key)
from androguard.misc import AnalyzeAPK

class ApkAnalysisPipeline:

    def process_item(self, item, spider):
        apk_path = item.get("apk_path")

        try:
            a, d, dx = AnalyzeAPK(apk_path)

            permissions = a.get_permissions()
            item["permissions"] = permissions

            # 🔥 SAVE TO DATABASE
            data = {
                "app_name": item["app_name"],
                "app_hash": item["app_hash"],
                "permissions": permissions
            }

            supabase.table("apps").insert(data).execute()

            print(f"✅ Saved to DB: {item['app_name']}")

        except Exception as e:
            print(f"❌ Error: {e}")
            item["permissions"] = []

        return item