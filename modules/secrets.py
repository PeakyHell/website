import os
from bitwarden_sdk import BitwardenClient, DeviceType, client_settings_from_dict

client = BitwardenClient(
    client_settings_from_dict(
        {
            "apiUrl": os.getenv("BW_API_URL"),
            "deviceType": DeviceType.SDK,
            "identityUrl": os.getenv("BW_IDENTITY_URL"),
            "userAgent": "Python"
        }
    )
)

client.auth().login_access_token(os.getenv("BW_ACCESS_TOKEN"))
