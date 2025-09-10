import os
from bitwarden_sdk import BitwardenClient, DeviceType, client_settings_from_dict

with open(os.getenv("BW_API_URL")) as f: BW_API_URL=f.read().strip()
with open(os.getenv("BW_IDENTITY_URL")) as f: BW_IDENTITY_URL=f.read().strip()
with open(os.getenv("BW_ACCESS_TOKEN")) as f: BW_ACCESS_TOKEN=f.read().strip()

client = BitwardenClient(
    client_settings_from_dict(
        {
            "apiUrl": BW_API_URL,
            "deviceType": DeviceType.SDK,
            "identityUrl": BW_IDENTITY_URL,
            "userAgent": "Python"
        }
    )
)

client.auth().login_access_token(BW_ACCESS_TOKEN)
