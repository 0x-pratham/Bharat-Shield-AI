from androguard.misc import AnalyzeAPK

def analyze_apk(apk_path):
    """
    Analyze APK and extract important features
    """

    a, d, dx = AnalyzeAPK(apk_path)

    permissions = a.get_permissions()
    services = a.get_services()

    features = {
        "permission_count": len(permissions),

        "sms_permission": int(
            "android.permission.READ_SMS" in permissions or
            "android.permission.SEND_SMS" in permissions
        ),

        "internet_access": int(
            "android.permission.INTERNET" in permissions
        ),

        "background_services": len(services),

        "hidden_code": int(len(d) > 1),  # simple logic for now

        "libraries": len(a.get_libraries())
    }

    return features