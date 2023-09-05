################
# Version with sidebar
################

# Import necessary libraries
import streamlit as st
import pandas as pd
import os
# import pyautogui

# Define the data structure as a list of dictionaries
# Initialize the 'data' session state as an empty list
st.session_state.data = st.session_state.get("data", [])

# Add title to the streamlit app
st.title("Opportunity Tracker")

# Create the Opportunity Form using Streamlit's 'with form' context manager
with st.form("Opportunity Form", clear_on_submit=True):
    
    # Divide the form into three columns for better layout
    col1, col2, col3 = st.columns(3)

    # Input fields for Buying Organization, Name of Solicitation, and Solicitation Number
    with col1:
        buying_org = st.text_input("Buying Organization")

    with col2:
        solicitation_name = st.text_input("Name of Solicitation")

    with col3:
        solicitation_number = st.text_input("Solicitation Number")

    # Input fields for Link to Solicitation, Release Date, and Due Date
    link_to_solicitation = st.text_input("Link to Solicitation")
    release_date = st.date_input("Release Date")
    due_date = st.date_input("Due Date")

    # Select boxes for Vehicle and Type
    vehicle = st.selectbox("Vehicle", ["GSA MAS", "OASIS", "PACTS III", "Other"])
    rfp_type = st.selectbox("Type", ["RFP", "RFI", "Sources Sought"])

    # Multiselect box for Set Aside, and a text input for Solicitation Value
    solicitation_value = st.number_input("Solicitation Value ($)", step=100000.0)
    solicitation_duration = st.number_input("Solicitation Duration (Months)", step=1)
    set_aside = st.multiselect("Set Aside", ["SDVOSB", "HUBZone", "8(a)", "WOSB", "VOSB"])

    # Select box for Iberia Role (Prime or Sub)
    iberia_role = st.selectbox("Iberia Role", ["Sub", "Prime"], index=0)

    # If Iberia Role is 'Sub', provide additional fields for confirmed partners and potential partners
    if iberia_role == "Sub":
        confirmed_partners = st.text_area("Confirmed Partners")#, [])
        potential_partners = st.text_area("Potential Partners")
    else:
        confirmed_partners = st.text_area("Confirmed Partners", value="NA")
        potential_partners = st.text_area("Potential Partners", value="NA")

    # Select box for Response Status (In progress or Submitted)
    response_status = st.selectbox("Response Status", ["Submitted", "In progress", ], index=0)

    # If Response Status is 'Submitted', provide additional fields for date submitted and submitted to details
    if response_status == "Submitted":
        date_submitted = st.date_input("Date Submitted")
        submitted_to = st.text_area("Submitted to")
    else:
        date_submitted = "NA"
        submitted_to = "NA"        

    # Define the required columns and their data types
    required_columns = {
        "Buying Organization": str,
        "Name of Solicitation": str,
        "Solicitation Number": str,
        "Link to Solicitation": str,
        "Release Date": str,  # You can change this to datetime if needed
        "Due Date": str,      # You can change this to datetime if needed
        "Vehicle": str,
        "Type": str,
        "Solicitation Value": float,
        "Solicitation Duration": int,
        "Set Aside": list,
        "Iberia Role": str,
        "Teaming Partners (Confirmed)": list,
        "Teaming Partners (Potential)": str,
        "Response Status": str,
        "Date Submitted": str,  # You can change this to datetime if needed
        "Submitted to": str,
    }
        

    # When the 'Add Opportunity' button is clicked, store the entered data in 'opportunity_data' dictionary
    if st.form_submit_button("Add Opportunity"):
        try:
            opportunity_data = {
                "Buying Organization": buying_org,
                "Name of Solicitation": solicitation_name,
                "Solicitation Number": solicitation_number,
                "Link to Solicitation": link_to_solicitation,
                "Release Date": str(release_date),
                "Due Date": str(due_date),
                "Vehicle": vehicle,
                "Type": rfp_type,
                "Solicitation Value": solicitation_value,
                "Solicitation Duration": solicitation_duration,
                "Set Aside": list(set_aside),
                "Iberia Role": iberia_role,
                "Teaming Partners (Confirmed)": confirmed_partners,
                "Teaming Partners (Potential)": potential_partners,
                "Response Status": response_status,
                "Date Submitted": str(date_submitted) if response_status == "Submitted" else "N/A",
                "Submitted to": submitted_to if response_status == "Submitted" else "N/A",
            }

            # Validate the input data against the required columns and data types
            for col, data_type in required_columns.items():
                if col not in opportunity_data:
                    
                    # Check if the data type should be a list
                    if data_type == list:  
                        
                        # Initialize as an empty list
                        opportunity_data[col] = []  
                    else:
                        st.error(f"Invalid data for column '{col}'. Please check the data type.")
                        raise ValueError("Invalid data")

            # Append the 'opportunity_data' dictionary to the 'data' list
            st.session_state.data.append(opportunity_data)
            
        except Exception as e:
            st.error(f"An error occurred while adding the opportunity: {e}")

    
# # Add a custom "Refresh" button outside the form context
# if st.button("Refresh"):
#     pyautogui.press('r') 
    
    
# Create two columns for saving the data
col1, col2 = st.columns(2)

with col1:
    # Input field for Excel file name
    excel_filename = st.text_input("Enter Excel File Name (without extension)", "opportunity_tracker")
    
    # Save button to Excel
    if st.button('Save Data to Excel'):
        @st.cache_data
        def save_to_excel(df, file_path):
            with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False)
        
        opportunity_df = pd.DataFrame(st.session_state.data)  # Convert opportunity data to a DataFrame

        # Get the path to the user's downloads folder
        downloads_folder = os.path.expanduser("~/Downloads")
        excel_file_path = os.path.join(downloads_folder, f"{excel_filename}.xlsx")

        save_to_excel(opportunity_df, excel_file_path)
        st.success(f"DataFrame saved to '{excel_file_path}'")

with col2:
    # Input field for CSV file name
    csv_filename = st.text_input("Enter CSV File Name (without extension)", "opportunity_tracker")
    
    # Save button to CSV
    if st.button('Save Data to CSV'):
        @st.cache_data
        def save_to_csv(df, file_path):
            df.to_csv(file_path, index=False)
        
        opportunity_df = pd.DataFrame(st.session_state.data)  # Convert opportunity data to a DataFrame

        # Get the path to the user's downloads folder
        downloads_folder = os.path.expanduser("~/Downloads")
        csv_file_path = os.path.join(downloads_folder, f"{csv_filename}.csv")

        save_to_csv(opportunity_df, csv_file_path)
        st.success(f"DataFrame saved to '{csv_file_path}'")

# Upload data file
uploaded_file = st.sidebar.file_uploader("Upload Excel File to Append Data", type=["xlsx"])

if uploaded_file is not None:
    try:
        new_data = pd.read_excel(uploaded_file)
        
        # Define the expected columns that should match with the uploaded data
        expected_columns = [
            "Buying Organization",
            "Name of Solicitation",
            "Solicitation Number",
            "Link to Solicitation",
            "Release Date",
            "Due Date",
            "Vehicle",
            "Type",
            "Solicitation Value",
            "Solicitation Duration",
            "Set Aside",
            "Iberia Role",
            "Teaming Partners (Confirmed)",
            "Teaming Partners (Potential)",
            "Response Status",
            "Date Submitted",
            "Submitted to",
        ]

        # Check if the uploaded data has the expected columns
        if set(new_data.columns) == set(expected_columns):
            # Append the uploaded data to the existing 'data' list of dictionaries
            if not st.session_state.data:
                st.session_state.data = new_data.to_dict("records")
            else:
                st.session_state.data.extend(new_data.to_dict("records"))
            st.success("Data appended successfully.")
        else:
            st.error("Uploaded data has different columns. Please check the file and try again.")
    except Exception as e:
        st.error(f"An error occurred while uploading and appending data: {e}")

# Display the opportunities table
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)

    # Convert "Release Date" and "Due Date" columns to string format
    df["Release Date"] = df["Release Date"].astype(str)
    df["Due Date"] = df["Due Date"].astype(str)
    
    # Convert the "Set Aside" column to a string representation
    df["Set Aside"] = df["Set Aside"].apply(lambda x: ", ".join(x) if isinstance(x, list) else x)
    # df["Teaming Partners (Confirmed)"] = df["Teaming Partners (Confirmed)"].apply(lambda x: ", ".join(x) if isinstance(x, list) else x)
    df["Teaming Partners (Confirmed)"] = df["Teaming Partners (Confirmed)"].apply(lambda x: x if isinstance(x, list) else [x])


    # Filter and Sort options
    filter_by = st.sidebar.selectbox("Filter By", ["None", "Buying Organization", "Release Date", "Due Date"])
    sort_by = st.sidebar.selectbox("Sort By", ["None", "Buying Organization", "Release Date", "Due Date"])

    # Data Filtering
    df_filtered = df.copy()

    if filter_by == "Buying Organization":
        buying_org_filter = st.sidebar.text_input("Enter Buying Organization")
        if buying_org_filter:
            df_filtered = df_filtered[df_filtered["Buying Organization"].str.contains(buying_org_filter, case=False)]

    elif filter_by == "Release Date":
        release_date_filter = st.date_input("Select Release Date")  
        if release_date_filter:
            # df_filtered = df_filtered[df_filtered["Release Date"] == str(release_date_filter)]
            release_date_filter_str = release_date_filter.strftime("%Y-%m-%d")
            df_filtered = df_filtered[df_filtered["Release Date"] == release_date_filter_str]


    elif filter_by == "Due Date":
        due_date_filter = st.date_input("Select Due Date")
        if due_date_filter:
            df_filtered = df_filtered[df_filtered["Due Date"] == str(due_date_filter)]

    # Data Sorting
    if sort_by != "None":
        ascending = st.checkbox("Ascending", True)
        # df_filtered = df_filtered.sort_values(by=sort_by, ascending=ascending)
        df_filtered = df_filtered.sort_values(by=sort_by, ascending=ascending, key=lambda col: pd.to_datetime(col, errors='coerce'))
    # Display the filtered and sorted opportunities table
    st.dataframe(df_filtered)

