# Opportunity Tracker App

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

The Opportunity Tracker is a Streamlit web application designed to help users manage and track business opportunities. It allows users to input and organize details about various solicitations and opportunities, making it convenient to monitor potential business ventures and collaboration opportunities.

With the Opportunity Tracker, you can efficiently organize and monitor a wide range of opportunities, including Requests for Proposals (RFPs), Requests for Information (RFIs), and Sources Sought notices. The app streamlines the process of data entry, persistence, and visualization, making it a valuable tool for business development, teaming, and decision-making.

![Opportunity Tracker Screenshot](screenshot.png)

## Key Features

- **User-Friendly Interface:** The app provides a simple and intuitive user interface, making it easy for users of all levels of expertise to add, manage, and analyze opportunities.

- **Efficient Data Entry:** With a structured data entry form, users can swiftly input essential details for each opportunity, such as the buying organization, solicitation name, solicitation number, link to the solicitation, release date, due date, vehicle, RFP type, set-aside, size, and Iberia role. For opportunities where your role is "Sub," you can conveniently add confirmed and potential teaming partners.

- **Persistent Data Storage:** The app leverages Streamlit's session state to ensure that the entered data remains accessible even when the page is refreshed or the application is revisited.

- **Data Export and Import:** Seamlessly export your opportunity data to an Excel file with just a click, allowing you to perform in-depth analysis or share information with stakeholders. Additionally, you can easily import data from an Excel file, enabling quick data updates and consolidation.

- **Interactive Opportunities Table:** The app presents opportunities in a dynamic and interactive tabular format. Users can apply filters based on buying organization, release date, and due date, and sort opportunities based on specific columns for better data exploration.

## Parameter Summary

### Summary of Each Parameter:

- **Buying Organization:** Information about the organization or agency responsible for the solicitation. Includes options for "Agency," "Office/Organization," and "Existing Relationship" (if any).

- **Name of Solicitation:** A free-text field to enter the name/title of the solicitation.

- **Solicitation Number:** A free-text field to enter the unique identifier for the solicitation.

- **Link to Solicitation:** A URL field to provide a link to the online location of the solicitation.

- **Release Date (Confirmed or Projected):** The date when the solicitation is released. It can be either confirmed or projected.

- **Date Due:** The deadline for submitting responses to the solicitation.

- **Vehicle:** The procurement vehicle associated with the solicitation. Includes options like "GSA MAS," "OASIS," "PACTS III," or "Other" (with a free-text field for additional information).

- **Type:** The type of solicitation, such as "RFP" (Request for Proposal), "RFI" (Request for Information), or "Sources Sought."

- **Set Aside:** Information about any set-aside requirements for the solicitation, like "SDVOSB," "HUBZone," "8(a)," "WOSB," or "VOSB."

- **Size:** A free-text field to provide information about the size of the solicitation.

- **Iberia Role:** Indicates the role in the solicitation process, either "Prime" or "Sub." If "Prime," there's a free-text field to input the name of the Prime.

- **Response Status:** The status of the response to the solicitation, which can be "In progress" or "Submitted." If "Submitted," there are additional fields for "Date Submitted" and "Submitted to" (a free-text field to specify who/where it was submitted).

- **Teaming Partners:** Information about the teaming partners involved in the solicitation, including "Confirmed Partners" (linked to separate pages for more details) and a free-text field for "Potential Partners."

- **Teaming Partner Page:** Detailed information about each teaming partner, including:
    - **POCs (Points of Contact):** Names of individuals from the partner organization, with details about their relationship type (Capture, Technical, Leadership), and their email addresses & phone numbers.
    - **Worked with Before?:** A checkbox or field to indicate if the teaming partner has been worked with before.
    - **NDA Status:** Status of the Non-Disclosure Agreement (NDA) with options for "Issued," "Partially Executed," or "Fully Executed." If "Issued," there are additional fields for "Date Issued" and "Sent to." If "Partially Executed" or "Fully Executed," there are fields for "Date PE/FE" and "Received from/Sent to."
    - **Teaming Agreement Status:** Status of the Teaming Agreement with options for "Issued," "Partially Executed," or "Fully Executed." If "Issued," there are additional fields for "Date Issued" and "Sent to." If "Partially Executed" or "Fully Executed," there are fields for "Date PE/FE" and "Received from/Sent to."

---

*These parameters are designed to capture essential information about solicitation opportunities and the teaming partners involved, facilitating efficient management and tracking of the process.*

## Installation

1. Clone the repository to your local machine:

git clone https://github.com/RichieGarafola-IberiaAdvisory/OpportunityTracker

2. Install the required libraries mentioned in the 'requirements.txt' file:

pip install -r requirements.txt

## Usage

1. Run the app locally using the following command:

streamlit run OpportunityTracker.py

2. The app will launch in your default web browser, where you can start entering and managing opportunities.

3. Fill out the details of each opportunity using the provided data entry form.

4. To add an opportunity, fill out the details in the form and click on the "Add Opportunity" button to store the entered information. The data will be displayed in the opportunities table below the form.

4. To save the opportunity data to an Excel file, click on the "Save to Excel" button. The data will be exported and saved as "opportunity_tracker.xlsx" in the root directory.

5. If you have additional data in an Excel file that you want to include, use the "Upload Excel File to Append Data" section. The uploaded data will be appended to the existing dataset.

6. The opportunities table can be filtered and sorted based on various columns. Use the dropdowns for "Filter By" and "Sort By" to interactively explore your opportunities.

## Data Export

To export the opportunity data, click on the "Save to Excel" button. The data will be saved to an Excel file named "opportunity_tracker.xlsx" in the root directory.

## Data Import

To append data from an Excel file, use the "Upload Excel File to Append Data" section. The uploaded file should be in .xlsx format, and the data will be appended to the existing dataset.

## Contributing

If you find any issues or have suggestions for improvements, feel free to raise an issue or submit a pull request. We welcome contributions from the community to enhance the functionality and usability of the Opportunity Tracker app.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code following the terms of the license.

## Credits

The Opportunity Tracker app was developed by https://github.com/RichieGarafola-IberiaAdvisory.
