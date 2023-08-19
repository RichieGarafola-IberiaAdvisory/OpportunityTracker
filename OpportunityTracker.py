################
# Version with sidebar
################

# Import necessary libraries
import streamlit as st
import pandas as pd

# Define the data structure as a list of dictionaries
# Initialize the 'data' session state as an empty list
st.session_state.data = st.session_state.get("data", [])

# Add title to the streamlit app
st.title("Opportunity Tracker")

# Create the Opportunity Form using Streamlit's 'with form' context manager
with st.form("Opportunity Form"):
    
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
    iberia_role = st.selectbox("Iberia Role", ["Prime", "Sub"])

    # If Iberia Role is 'Sub', provide additional fields for confirmed partners and potential partners
    if iberia_role == "Sub":
        confirmed_partners = st.multiselect("Confirmed Partners", [])
        potential_partners = st.text_area("Potential Partners")
    else:
        confirmed_partners = []
        potential_partners = ""

    # Select box for Response Status (In progress or Submitted)
    response_status = st.selectbox("Response Status", ["In progress", "Submitted"])

    # If Response Status is 'Submitted', provide additional fields for date submitted and submitted to details
    if response_status == "Submitted":
        date_submitted = st.date_input("Date Submitted")
        submitted_to = st.text_area("Submitted to")

    # When the 'Add Opportunity' button is clicked, store the entered data in 'opportunity_data' dictionary
    if st.form_submit_button("Add Opportunity"):
        try:
            opportunity_data = {
                "Buying Organization": buying_org,
                "Name of Solicitation": solicitation_name,
                "Solicitation Number": solicitation_number,
                "Link to Solicitation": link_to_solicitation,
                "Release Date": release_date,
                "Due Date": due_date,
                "Vehicle": vehicle,
                "Type": rfp_type,
                "Solicitation Value": solicitation_value,
                "Solicitation Duration": solicitation_duration,
                "Set Aside": list(set_aside),
                "Iberia Role": iberia_role,
                "Teaming Partners (Confirmed)": confirmed_partners,
                "Teaming Partners (Potential)": potential_partners,
                "Response Status": response_status,
                "Date Submitted": date_submitted if response_status == "Submitted" else None,
                "Submitted to": submitted_to if response_status == "Submitted" else "",
            }

            # Append the 'opportunity_data' dictionary to the 'data' list
            st.session_state.data.append(opportunity_data)
        except Exception as e:
            st.error(f"An error occurred while adding the opportunity: {e}")
        
        
    # Clear the form fields after submission
    buying_org = ""
    solicitation_name = ""
    solicitation_number = ""
    link_to_solicitation = ""
    release_date = None
    due_date = None
    vehicle = "GSA MAS"
    rfp_type = "RFP"
    set_aside = []
    solicitation_value = 0
    solicitation_duration = 0
    iberia_role = "Prime"
    confirmed_partners = []
    potential_partners = ""
    response_status = "In progress"
    date_submitted = None
    submitted_to = ""

# Save the DataFrame to Excel
if st.button("Save to Excel"):
    df = pd.DataFrame(st.session_state.data)
    st.cache(df.to_excel)("opportunity_tracker.xlsx", index=False)
    df.to_excel("opportunity_tracker.xlsx", index=False)
    st.success("DataFrame saved to 'opportunity_tracker.xlsx'")

# Upload and append data from Excel
uploaded_file = st.sidebar.file_uploader("Upload Excel File to Append Data", type=["xlsx"])

if uploaded_file is not None:
    try:
        new_data = pd.read_excel(uploaded_file)
        if not st.session_state.data:
            st.session_state.data = new_data.to_dict("records")
        else:
            st.session_state.data.extend(new_data.to_dict("records"))
        st.success("Data appended successfully.")
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