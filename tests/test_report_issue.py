import pytest
from page_objects.report_issues_page import ReportIssuePage
from test_data.maintenance_form_submission_data import FormSubmissionData
from utilities.base_test import BaseClass


class TestReportIssue(BaseClass):

    @pytest.fixture(scope="class", params=FormSubmissionData.maintenance_request_form_data)
    def get_data(self, request):
        """
        Fixture to provide test data for the test methods.

        Args:
            request: The Pytest request object.

        Returns:
            dict: The test data.
        """
        return request.param

    def test_log_residential_maintenance_request(self, get_data):
        """
        Test logging a residential maintenance request.

        Args:
            get_data (dict): Test data for the method.
        """
        report_issue = ReportIssuePage(self.driver)
        assert "RedRabbit Staging" in self.driver.title
        print("Successfully landed on home page")
        self.click_button_by_text(get_data["property_types"][1])
        self.click_button_by_text(get_data["fault_types"][0])
        self.click_button_by_text(get_data["fault_types"][1])
        report_issue.fill_in_form(get_data)
        assert get_data["validation_messages"][0] in report_issue.get_request_confirmed_message().text
        print("Request confirmed message present and correct")
        ref_number = self.get_text_of_element(report_issue.ref_number_element)
        report_issue.save_ref_number_to_file(ref_number)
        self.take_screenshot("Reference number.png")

    def test_log_commercial_maintenance_request(self, get_data):
        """
        Test logging a commercial maintenance request.

        Args:
            get_data (dict): Test data for the method.
        """
        report_issue = ReportIssuePage(self.driver)
        assert "RedRabbit Staging" in self.driver.title
        print("Successfully landed on home page")
        self.click_button_by_text(get_data["property_types"][0])
        self.click_button_by_text(get_data["fault_types"][2])
        report_issue.fill_in_form(get_data, issue_description_field="issue_descriptions_over_200")
        assert get_data["validation_messages"][1] in report_issue.get_description_too_long_message().text
        self.hover_on_element(report_issue.description_too_long_message)
        self.take_screenshot("Description too long error message.png")
        print("Description too long message correctly prevents user from submitting description longer than 200 "
              "characters")

    def test_log_body_corporate_maintenance_request(self, get_data):
        """
        Test logging a body corporate maintenance request.

        Args:
            get_data (dict): Test data for the method.
        """
        report_issue = ReportIssuePage(self.driver)
        assert "RedRabbit Staging" in self.driver.title
        print("Successfully landed on home page")
        self.click_button_by_text(get_data["property_types"][2])
        self.click_button_by_text(get_data["fault_types"][3])
        report_issue.fill_in_form(get_data, email_address_field="invalid_email_address")
        assert get_data["validation_messages"][2] in report_issue.get_invalid_email_error_message().text
        self.hover_on_element(report_issue.invalid_email_error_message)
        self.take_screenshot("Invalid email error message.png")
        print("Invalid email error message correctly prevents the user from submitting a request with an invalid "
              "email address")

    def test_residential_maintenance_max_request(self, get_data):
        """
        Test logging a maximum number of residential maintenance requests.

        Args:
            get_data (dict): Test data for the method.
        """
        report_issue = ReportIssuePage(self.driver)
        assert "RedRabbit Staging" in self.driver.title
        print("Successfully landed on home page")
        self.click_button_by_text(get_data["property_types"][1])
        self.click_button_by_text(get_data["fault_types"][4])
        self.click_button_by_text(get_data["fault_types"][5])
        self.click_button_by_text(get_data["fault_types"][6])
        assert get_data["validation_messages"][3] in report_issue.get_max_issues_alert().text
        self.hover_on_element(report_issue.max_issues_reached_message)
        self.take_screenshot("Maximum Issues Reached Warning.png")
        print("Maximum Issues Reached warning message appears when 3 maintenance request items have been selected")
        self.click_button_by_text(get_data["fault_types"][0])
        max_exceed_popup = report_issue.get_max_issues_popup()
        assert max_exceed_popup.is_displayed(), "Max issues exceeded pop up is not visible to the user"
        self.hover_on_element(report_issue.max_issues_reached_popup)
        self.take_screenshot("Maximum Issues Exceeded Popup.png")
        print("Maximum Issues reached pop up is generated when user tries to add more than 3 maintenance requests")

