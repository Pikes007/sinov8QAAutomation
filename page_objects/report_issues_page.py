import time
from selenium.webdriver.common.by import By
from utilities.base_test import BaseClass
from test_data.reference_numbers import ReferenceNumbers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


class ReportIssuePage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.ref_num_list = []

    problem_location = (By.XPATH, "//input[@id='location']")
    number_of_issues = (By.XPATH, '//div[@class = "text-center mt-8 text-2xl"]')
    property_ref = (By.XPATH, "// input[ @ id = 'property_reference']")
    select_photo = (By.XPATH, "//span[contains(text(),'Select Photo')]")
    problem_item = (By.XPATH, "//input[@id='item']")
    problem_description = (By.XPATH, "//textarea[@id='description']")
    address = (By.XPATH, "//input[@id='address']")
    client_name = (By.XPATH, "//input[@id='name']")
    client_email = (By.XPATH, "//input[@id='reporter_email']")
    client_mobile = (By.XPATH, "//input[@id='mobile']")
    comments = (By.XPATH, "//textarea[@id='comments']")
    ref_number_element = (By.XPATH, "//span[@class = 'text-indigo-600 text-lg']")
    max_issues_reached_message = (By.XPATH, "//button[normalize-space()='Maximum issues reached']")
    max_issues_reached_popup = (By.XPATH, "//p[normalize-space()='Maximum issues reached']")
    request_confirmed_message = (By.XPATH, "//h1[contains(text(),'Thank you for logging your request.')]")
    description_too_long_message = (By.XPATH, "//div[normalize-space()='The description must not be greater than 200 "
                                              "characters.']")
    invalid_email_error_message = (By.XPATH, "//div[normalize-space()='The email must be a valid email address.']")

    def return_number_of_issues_selected(self):
        """Return the number of selected issues."""
        return len(self.driver.find_elements(*ReportIssuePage.number_of_issues))

    def fill_in_form(self, data, email_address_field="email_address", issue_description_field="issue_descriptions",
                     issue_location_field="issue_locations"):
        """
        Fill in the maintenance request form with the provided data.

        Args:
            data (dict): The data to be filled in the form.
            email_address_field (str, optional): The field name for email address. Defaults to "email_address".
            issue_description_field (str, optional): The field name for issue descriptions. Defaults to "issue_descriptions".
            issue_location_field (str, optional): The field name for issue locations. Defaults to "issue_locations".
        """
        num_of_issues = self.return_number_of_issues_selected()
        issue_locations = self.driver.find_elements(*ReportIssuePage.problem_location)
        issue_items = self.driver.find_elements(*ReportIssuePage.problem_item)
        issue_descriptions = self.driver.find_elements(*ReportIssuePage.problem_description)

        for i in range(num_of_issues):
            issue_location = issue_locations[i]
            issue_location.clear()
            issue_location.send_keys(data[issue_location_field][i])
            issue_item = issue_items[i]
            issue_item.clear()
            issue_item.send_keys(data["issue_items"][i])
            issue_description = issue_descriptions[i]
            issue_description.clear()
            issue_description.send_keys(data[issue_description_field][i])
            self.upload_pic(self.select_photo, str(data["upload_pic_filenames"][i]))
            self.driver.find_element(*ReportIssuePage.property_ref).send_keys(data["contact_detail_references"][i])

        self.driver.find_element(*ReportIssuePage.address).send_keys(data["physical_address"])
        self.driver.find_element(*ReportIssuePage.client_name).send_keys(data["form_name"])
        self.driver.find_element(*ReportIssuePage.client_email).send_keys(data[email_address_field])
        self.driver.find_element(*ReportIssuePage.client_mobile).send_keys(data["form_mobile"])

        if num_of_issues == 1:
            self.driver.find_element(*ReportIssuePage.comments).send_keys(data["comments"][0])
        elif num_of_issues > 1:
            self.driver.find_element(*ReportIssuePage.comments).send_keys(data["comments"][1])
        else:
            print("Did not find the list of issues logged")

        self.click_button_by_text("Submit")

    def get_max_issues_alert(self):
        """Get the maximum issues reached alert element."""
        return self.driver.find_element(*ReportIssuePage.max_issues_reached_message)

    def get_max_issues_popup(self):
        """Get the maximum issues reached popup element."""
        return self.wait.until(EC.visibility_of_element_located(self.max_issues_reached_popup))

    def get_request_confirmed_message(self):
        """Get the request confirmed message element."""
        return self.wait.until(EC.visibility_of_element_located(self.request_confirmed_message))

    def get_description_too_long_message(self):
        """Get the description too long error message element."""
        return self.wait.until(EC.visibility_of_element_located(self.description_too_long_message))

    def get_invalid_email_error_message(self):
        """Get the invalid email error message element."""
        return self.wait.until(EC.visibility_of_element_located(self.invalid_email_error_message))

    def save_ref_number_to_file(self, entry):
        """
        Save the reference number to a file.

        Args:
            entry (str): The reference number to be saved.
        """
        ReferenceNumbers.ref_num_list.append(entry)
        filepath = r"C:\Users\Hello\PycharmProjects\sinov8Part2\test_data\reference_numbers.py"

        with open(filepath, "r") as file:
            lines = file.readlines()

        if "    ]\n" in lines:
            ref_num_list_end = lines.index("    ]\n")
            lines.insert(ref_num_list_end, f"        '{entry}',\n")
        else:
            lines.append(f"        '{entry}',\n")

        with open(filepath, "w") as file:
            file.writelines(lines)

    def upload_pic(self, element, filepath):
        """
        Upload a picture by interacting with the file input element.

        Args:
            element: The file input element for uploading pictures.
            filepath (str): The path to the picture file.
        """
        select_photo_container = self.driver.find_element(*element)
        select_photo_container.click()
        time.sleep(2)
        pyautogui.write(filepath)
        pyautogui.press('enter')
