import json


class FormSubmissionData:
    maintenance_request_form_data = [
        {
            "property_types": [
                "Commercial",
                "Residential",
                "Body Corporate"
            ],
            "fault_types": [
                "Blocked Drain",
                "Window Broken",
                "My problem is not listed",
                "Irrigation System Faulty",
                "Garage Door Faulty",
                "Oven Faulty",
                "Tap leaking"
            ],
            "issue_locations": [
                "Kitchen",
                "Bathroom",
                "Outside"
            ],
            "issue_items": [
                "Gully",
                "Geyser"
                "Toilet"
                "Irrigation System"
            ],
            "issue_descriptions": [
                "_Test1_Faulty description",
                "_Test2_Faulty description",
                "_Test3_Faulty description",
            ],
            "issue_descriptions_over_200": [
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget felis eu libero tincidunt "
                "dignissim. Sed vehicula, enim et consequat aliquam, libero odio convallis nulla, nec tincidunt "
                "ligula turpis vel mauris. Sed eu scelerisque urna. Fusce et augue sit amet ligula hendrerit "
                "facilisis at sit amet quam. Integer ac elit id velit dignissim fringilla nec nec urna. Donec feugiat "
                "accumsan quam, a dictum tellus blandit vel. Suspendisse eu bibendum ligula. Proin non nulla auctor, "
                "laoreet ex nec, dignissim augue. Quisque non urna vel justo accumsan ultricies vel vel nulla. Duis "
                "vestibulum pharetra velit, non bibendum dolor dictum vitae. Sed ultrices consectetur sem, "
                "in fermentum elit feugiat et. Vivamus accumsan ultrices elit vel varius."
            ],
            "physical_address": [
                "16 Galway road, Klipkop",
            ],
            "form_name": [
                "test_report_issue",
            ],
            "email_address": [
                "test@gmail.com",
            ],
            "invalid_email_address": [
                "123"
            ],
            "form_mobile": [
                "0801001001",
            ],
            "comments": [
                "Test:Comments: maintenance request with single issue listed",
                "Test:Comments: maintenance request with multiple issues listed",
            ],
            "contact_detail_references": [
                "T01",
                "T02",
                "T03"
            ],
            "validation_messages": [
                "Thank you for logging your request. We will respond to your request within 24hrs",
                "The description must not be greater than 200 characters.",
                "The email must be a valid email address.",
                "Maximum issues reached"
            ],
            "upload_pic_filenames": [
                r"C:\Users\Hello\PycharmProjects\sinov8Part2\test_data\upload_pictures\sinov8.jpeg",
                r"C:\Users\Hello\PycharmProjects\sinov8Part2\test_data\upload_pictures\sinov8(1).jpeg",
                r"C:\Users\Hello\PycharmProjects\sinov8Part2\test_data\upload_pictures\sinov8(2).jpg"

            ]
        }
    ]
