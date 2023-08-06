from NEMO.decorators import customization
from NEMO.views.customization import CustomizationBase


@customization(title="User details", key="user_details")
class UserDetailsCustomization(CustomizationBase):
    variables = {
        "user_details_enable_groups": "",
        "user_details_enable_emergency_contact": "",
        "user_details_enable_phone_number": "",
        "user_details_enable_race": "",
        "user_details_enable_gender": "",
        "user_details_enable_ethnicity": "",
        "user_details_enable_rate_category": "",
        "user_details_require_groups": "",
        "user_details_require_emergency_contact": "",
        "user_details_require_phone_number": "",
        "user_details_require_race": "",
        "user_details_require_gender": "",
        "user_details_require_ethnicity": "",
        "user_details_require_rate_category": "",
    }

    @classmethod
    def disable_fields(cls):
        return [
            var.replace("user_details_enable_", "")
            for var in cls.variables
            if var.startswith("user_details_enable_") and not cls.get_bool(var)
        ]

    @classmethod
    def require_fields(cls):
        return [
            var.replace("user_details_require_", "")
            for var in cls.variables
            if var.startswith("user_details_require_") and cls.get_bool(var)
        ]
