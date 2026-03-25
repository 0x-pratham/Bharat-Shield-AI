from androguard.core.apk import APK


def analyze_apk(apk_path):
    """
    Analyze APK and extract basic security features
    """

    try:
        a = APK(apk_path)
    except Exception as e:
        print(f"❌ Error loading APK: {e}")
        return None

    # --- Extract Data ---
    permissions = a.get_permissions()
    services = a.get_services()
    activities = a.get_activities()

    # --- Basic Counts ---
    permission_count = len(permissions)
    service_count = len(services)
    activity_count = len(activities)

    # --- Key Permissions ---
    sms_permission = int(
        "android.permission.READ_SMS" in permissions or
        "android.permission.SEND_SMS" in permissions
    )

    internet_access = int(
        "android.permission.INTERNET" in permissions
    )

    # --- Hidden Code Heuristic ---
    hidden_code = 0

    if permission_count > 25 and service_count > 10:
        hidden_code = 1

    if activity_count > 20:
        hidden_code = 1

    # --- Libraries ---
    try:
        libraries = len(a.get_libraries())
    except:
        libraries = 0

    # --- Final Features (ONLY NUMERIC ⚠️) ---
    features = {
        "permission_count": permission_count,
        "sms_permission": sms_permission,
        "internet_access": internet_access,
        "background_services": service_count,
        "hidden_code": hidden_code,
        "libraries": libraries
    }

    return features