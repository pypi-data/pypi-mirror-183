from django.apps import apps
from django.test import TestCase

from NEMO_user_details.customizations import UserDetailsCustomization
from NEMO_user_details.forms import UserDetailsForm


class TestUserDetails(TestCase):
    def test_form_fields(self):
        test_form_field(self, "emergency_contact")
        test_form_field(self, "phone_number")
        test_form_field(self, "race")
        test_form_field(self, "gender")
        test_form_field(self, "ethnicity")

    def test_rate_category(self):
        if apps.is_installed("NEMO_billing.rates"):
            print("Testing with billing")
            test_form_field(self, "rate_category")
        else:
            print("Testing without billing")
            # No matter the options set, it should always be disabled
            # and not required if the billing plugin is not installed
            UserDetailsCustomization.set("user_details_enable_rate_category", "enabled")
            UserDetailsCustomization.set("user_details_require_rate_category", "enabled")
            form = UserDetailsForm()
            self.assertTrue(form.fields["rate_category"].disabled)
            self.assertFalse(form.fields["rate_category"].required)


def test_form_field(test_case: TestCase, field_name):
    # By default fields are not enabled
    form = UserDetailsForm()
    test_case.assertTrue(form.fields[field_name].disabled)
    test_case.assertFalse(form.fields[field_name].required)
    # Requires means enable and required
    UserDetailsCustomization.set(f"user_details_require_{field_name}", "enabled")
    form = UserDetailsForm()
    test_case.assertFalse(form.fields[field_name].disabled)
    test_case.assertTrue(form.fields[field_name].required)
    # Reset required part
    UserDetailsCustomization.set(f"user_details_require_{field_name}", "")
    # Set enabled only
    UserDetailsCustomization.set(f"user_details_enable_{field_name}", "enabled")
    form = UserDetailsForm()
    test_case.assertFalse(form.fields[field_name].disabled)
    test_case.assertFalse(form.fields[field_name].required)
