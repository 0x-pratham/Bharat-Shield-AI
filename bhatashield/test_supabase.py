from supabase import create_client

url = "https://spuorfzpecagkepiidwt.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNwdW9yZnpwZWNhZ2tlcGlpZHd0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM4NDUwOTcsImV4cCI6MjA4OTQyMTA5N30.MSSSPLwcekuhoEB2dp64a67BQyQpHTufzbM0UBVRHfI"

supabase = create_client(url, key)

data = {
    "app_name": "Crawler Test",
    "app_hash": "abc123xyz",
    "apk_path": "/apk/test.apk"
}

response = supabase.table("apps").insert(data).execute()

print(response)