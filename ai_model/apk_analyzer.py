from androguard.core.apk import APK

def analyze_apk(apk_path):
    """
    Optimized APK analysis (fast + smart)
    """

    a = APK(apk_path)

    permissions = a.get_permissions()
    services = a.get_services()
    activities = a.get_activities()

    # --- Feature Extraction ---
    permission_count = len(permissions)
    service_count = len(services)
    activity_count = len(activities)

    sms_permission = int(
        "android.permission.READ_SMS" in permissions or
        "android.permission.SEND_SMS" in permissions
    )

    internet_access = int(
        "android.permission.INTERNET" in permissions
    )

    # --- Smart Hidden Code Approximation ---
    # Instead of heavy DEX analysis, we estimate suspicious behavior
    hidden_code = 0

    if permission_count > 25 and service_count > 10:
        hidden_code = 1  # suspicious pattern

    if activity_count > 20:
        hidden_code = 1

    # --- Libraries ---
    libraries = len(a.get_libraries())

    # --- Final Feature Dictionary ---
    features = {
        "permission_count": permission_count,
        "sms_permission": sms_permission,
        "internet_access": internet_access,
        "background_services": service_count,
        "hidden_code": hidden_code,
        "libraries": libraries
    }

    return features