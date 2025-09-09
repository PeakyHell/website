from bitwarden_sdk import BitwardenClient, DeviceType, client_settings_from_dict

client = BitwardenClient(
    client_settings_from_dict(
        {
            "apiUrl": "",
            "deviceType": DeviceType.SDK,
            "identityUrl": "",
            "userAgent": "Python"
        }
    )
)
