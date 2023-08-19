#########################
# Version with tab - needs work
#########################

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


# Initialize the 'data' session state as an empty list if it doesn't exist
if "data" not in st.session_state:
    st.session_state.data = []

# # Initialize the 'df' session state as an empty DataFrame if it doesn't exist
# if "df" not in st.session_state:
#     st.session_state.df = pd.DataFrame()
    
# Save the DataFrame to Excel
def save_to_excel():
    if st.button("Save to Excel"):
        df = pd.DataFrame(st.session_state.data)
        df.to_excel("opportunity_tracker.xlsx", index=False)
        st.success("DataFrame saved to 'opportunity_tracker.xlsx'")

# Upload and append data from Excel
def upload_and_append_data():
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
def display_opportunities_table():
    if st.session_state.data:
        df = pd.DataFrame(st.session_state.data)
    else:
        df = pd.DataFrame()

    # Display table
    st.dataframe(df)

sns.set_palette("Blues")

# Define a function for creating bar charts
def create_bar_chart(data, x_label, y_label, title):
    try:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(data.index, data.values)
        ax.set_title(title, fontsize=16)
        ax.set_xlabel(x_label, fontsize=12)
        ax.tick_params(axis="x", rotation=45, labelsize=12)
        ax.set_ylabel(y_label, fontsize=12)
        ax.tick_params(axis="y", labelsize=12)
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error occurred while creating the bar chart: {e}")

# Define a function for creating count plots
def create_count_plot(data, x_label, y_label, title, rotation=45):
    try:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.countplot(data=data, x=x_label, ax=ax)
        ax.set_title(title, fontsize=16)
        ax.set_xlabel(x_label, fontsize=12)
        ax.tick_params(axis="x", labelsize=12)
        ax.set_ylabel(y_label, fontsize=12)
        ax.tick_params(axis="y", labelsize=12)
        # st.pyplot(fig)
        return fig, ax
    except Exception as e:
        st.error(f"Error occurred while creating the count plot: {e}")
        return None, None

# Define a function for creating histograms
def create_histogram(data, x_label, y_label, title):
    try:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(data.dropna(), bins=20, edgecolor="black")
        ax.set_title(title, fontsize=16)
        ax.set_xlabel(x_label, fontsize=12)
        ax.tick_params(axis="x", labelsize=12)
        ax.set_ylabel(y_label, fontsize=12)
        ax.tick_params(axis="y", labelsize=12)
        st.pyplot(fig)
        return fig, ax
    except Exception as e:
        st.error(f"Error occurred while creating the histogram: {e}")
        return None, None
    
# Define a function for creating a line chart
def create_linechart(data, x_label, y_label, title):
    try:
        # Convert the "Release Date" column to datetime
        data["Release Date"] = pd.to_datetime(data["Release Date"])

        # Group opportunities by release date and count
        opportunities_over_time = data.groupby("Release Date").size()

        # Create a line chart
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(opportunities_over_time.index, opportunities_over_time.values)
        ax.set_title(title, fontsize=16)
        ax.set_xlabel(x_label, fontsize=12)
        ax.tick_params(axis="x", rotation=45, labelsize=12)
        ax.set_ylabel(y_label, fontsize=12)
        ax.tick_params(axis="y", labelsize=12)
        return fig, ax
    except Exception as e:
        st.error(f"Error occurred while creating the Line Chart for Opportunities Over Time: {e}")

# Define a function for creating a stacked bar chart
def create_stacked_bar_chart(data, x_column, y_column, title, x_label, y_label):
    try:
        # Create a crosstab of x_column vs. y_column
        cross_tab = pd.crosstab(data[x_column], data[y_column])

        # Create a stacked bar chart
        fig, ax = plt.subplots(figsize=(8, 6))
        cross_tab.plot(kind="bar", stacked=True, ax=ax)
        ax.set_title(title, fontsize=16)
        ax.set_xlabel(x_label, fontsize=12)
        ax.tick_params(axis="x", labelsize=12)
        ax.set_ylabel(y_label, fontsize=12)
        ax.tick_params(axis="y", labelsize=12)
        return fig, ax
    except Exception as e:
        st.error(f"Error occurred while creating the Stacked Bar Chart: {e}")
        return None, None

        
# Define a function for creating a histogram
def create_histogram(data, column, bins=20, title="", x_label="", y_label="Count"):
    try:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(data[column].dropna(), bins=bins, edgecolor="black")
        ax.set_title(title, fontsize=16)
        ax.set_xlabel(x_label, fontsize=12)
        ax.tick_params(axis="x", labelsize=12, rotation=45)
        ax.set_ylabel(y_label, fontsize=12)
        ax.tick_params(axis="y", labelsize=12)
        return fig, ax
    except Exception as e:
        st.error(f"Error occurred while creating the Histogram: {e}")

########################
# Visualization functions
#########################  

def visualize_vehicle_distribution(df):
    st.subheader("Opportunity Distribution by Vehicle")
    create_bar_chart(
        df["Vehicle"].value_counts(), 
        "Vehicle", 
        "Count", 
        "Opportunity Distribution by Vehicle")

def visualize_set_aside_distribution(df):
    st.subheader("Opportunity Distribution by Set Aside")
    create_bar_chart(
        df["Set Aside"].explode().value_counts(), 
        "Set Aside", 
        "Count", 
        "Opportunity Distribution by Set Aside")
    
def visualize_set_aside_distribution_pie_chart(df):
    st.subheader("Opportunity Distribution by Set Aside")
    set_aside_counts = df["Set Aside"].explode().value_counts()

    # Create a pie chart
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(set_aside_counts.values, labels=set_aside_counts.index, autopct="%1.1f%%", startangle=140)
    ax.axis("equal")
    ax.set_title("Opportunity Distribution by Set Aside", fontsize=16)
    ax.tick_params(axis="x", labelsize=12)
    ax.tick_params(axis="y", labelsize=12)
    st.pyplot(fig)

def visualize_response_status(df):
    st.subheader("Opportunity Response Status")
    create_count_plot(
        df, 
        "Response Status", 
        "Count", 
        "Opportunity Response Status")

# Visualization function for opportunities over time
def visualize_opportunities_over_time(df):
    st.subheader("Opportunities Over Time")
    fig, ax = create_linechart(
        df, 
        "Release Date", 
        "Number of Opportunities", 
        "Opportunities Over Time")
    st.pyplot(fig)

# Visualization function for response status by Iberia Role
def visualize_response_by_iberia_role(df):
    st.subheader("Response Status by Iberia Role")
    create_stacked_bar_chart(
        df, 
        x_column="Iberia Role", 
        y_column="Response Status", 
        title="Response Status by Iberia Role", 
        x_label="Iberia Role", 
        y_label="Count")

# Visualization function for RFP types
def visualize_rfp_types(df):
    st.subheader("RFP Type Distribution")
    create_count_plot(
        df, 
        "Type", 
        "Count", 
        "RFP Type Distribution")

# Visualization function for opportunity size distribution
def visualize_opportunity_size(df):
    st.subheader("Opportunity Size Distribution")
    fig, ax = create_histogram(
        df, 
        "Solicitation Value", 
        bins=20, 
        title="Opportunity Size Distribution", 
        x_label="Opportunity Size")
    st.pyplot(fig)

# # Visualization function for buying organization distribution
# def visualize_buying_organization(df):
#     st.subheader("Opportunity Distribution by Buying Organization")
#     fig, ax = create_count_plot(
#         df["Buying Organization"].value_counts(), 
#         title="Opportunity Distribution by Buying Organization", 
#         x_label="Buying Organization", 
#         y_label="Count", 
#         rotation=90)
#     st.pyplot(fig)

# Visualization function for response status by buying organization
def visualize_response_by_buying_organization(df):
    st.subheader("Response Status by Buying Organization")
    fig, ax = create_stacked_bar_chart(
        df, 
        x_column="Buying Organization", 
        y_column="Response Status",
        title="Response Status by Buying Organization", 
        x_label="Buying Organization", 
        y_label="Count")
    st.pyplot(fig)
        
def generate_visualizations(df):
    st.title("Opportunity Tracker")
    
    # Print the DataFrame for debugging purposes
    st.write(df)

    # Create tabs
    # tabs = st.tabs(["Vehicle Distribution", "Set Aside Distribution", "Response Status", "Opportunities Over Time", "Response by Iberia Role", "RFP Types", "Opportunity Size", "Buying Organization", "Response by Buying Org"])
    tabs = st.tabs(["Vehicle Distribution", "Set Aside Distribution", "Response Status", "Opportunities Over Time", "Response by Iberia Role", "RFP Types", "Opportunity Size", "Response by Buying Org"])

    # First tab: Vehicle Distribution
    with tabs[0]:
        visualize_vehicle_distribution(df)

    # Second tab: Set Aside Distribution
    with tabs[1]:
        # Create columns for layout
        col1, col2 = st.columns(2)

        with col1:
            visualize_set_aside_distribution(df)
        with col2:
            visualize_set_aside_distribution_pie_chart(df)

    # Third tab: Response Status
    with tabs[2]:
        visualize_response_status(df)

    # Fourth tab: Opportunities Over Time
    with tabs[3]:
        visualize_opportunities_over_time(df)

    # Fifth tab: Response by Iberia Role
    with tabs[4]:
        visualize_response_by_iberia_role(df)

    # Sixth tab: RFP Types
    with tabs[5]:
        visualize_rfp_types(df)

    # Seventh tab: Opportunity Size
    with tabs[6]:
        visualize_opportunity_size(df)
        
    # Eighth tab: Response by Buying Organization
    with tabs[7]:
        visualize_response_by_buying_organization(df)
        
    # # Ninth tab: Buying Organization
    # with tabs[8]:
    #     visualize_buying_organization(df)



# def generate_visualizations(df):
#     st.title("Opportunity Tracker")
    
#     # Print the DataFrame for debugging purposes
#     st.write(df)

#     # Custom CSS for tab headers
#     custom_styles = """
#     <style>
#     .custom-tabs {
#       display: flex;
#       overflow-x: scroll;
#     }

#     .tab {
#       padding: 10px 20px;
#       background-color: white;
#       border: 1px solid gray;
#       margin-right: 10px;
#       cursor: pointer;
#     }

#     .tab:hover {
#       background-color: gray;
#       color: white;
#     }

#     .tab:last-child {
#       margin-right: 0;
#     }
#     </style>
#     """

#     # Render the custom CSS
#     st.markdown(custom_styles, unsafe_allow_html=True)

#     # Custom HTML for tab headers
#     custom_tab_headers = """
#     <div class="custom-tabs">
#       <div class="tab">Vehicle Distribution</div>
#       <div class="tab">Set Aside Distribution</div>
#       <div class="tab">Response Status</div>
#       <div class="tab">Opportunities Over Time</div>
#       <div class="tab">Response by Iberia Role</div>
#       <div class="tab">RFP Types</div>
#       <div class="tab">Opportunity Size</div>
#       <div class="tab">Buying Organization</div>
#       <div class="tab">Response by Buying Org</div>
#     </div>
#     """

#     # Render the custom tab headers
#     st.markdown(custom_tab_headers, unsafe_allow_html=True)

#     # Create tabs
#     tabs = st.tabs([
#         "Vehicle Distribution",
#         "Set Aside Distribution",
#         "Response Status",
#         "Opportunities Over Time",
#         "Response by Iberia Role",
#         "RFP Types",
#         "Opportunity Size",
#         "Buying Organization",
#         "Response by Buying Org"
#     ])

#     # Add your visualization functions here for each tab
#     with tabs[0]:
#         visualize_vehicle_distribution(df)

#     with tabs[1]:
#         visualize_set_aside_distribution(df)

#     with tabs[2]:
#         visualize_response_status(df)

#     with tabs[3]:
#         visualize_opportunities_over_time(df)

#     with tabs[4]:
#         visualize_response_by_iberia_role(df)

#     with tabs[5]:
#         visualize_rfp_types(df)

#     with tabs[6]:
#         visualize_opportunity_size(df)

#     with tabs[7]:
#         visualize_buying_organization(df)

#     with tabs[8]:
#         visualize_response_by_buying_organization(df)
    

# Main code
if __name__ == "__main__":
    st.set_page_config(page_title="Opportunity Tracker", page_icon=":chart_with_upwards_trend:")

    # Initialize the 'data' session state as an empty list if it doesn't exist
    if "data" not in st.session_state:
        st.session_state.data = []

    # Display the navigation menu and selected tab's content
    with st.sidebar:
        st.sidebar.header("Navigation")
        st.sidebar.markdown(
            """
            <style>
            .sidebar .sidebar-content {
                overflow-y: scroll;
                max-height: 80vh; /* Set a maximum height for the sidebar */
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        selected_tab = st.sidebar.selectbox("Select a tab", ["Opportunity Tracker", "Add Data", "Saved Data"])


    if selected_tab == "Opportunity Tracker":
        # Display visualizations on this tab
        generate_visualizations(pd.DataFrame(st.session_state.data))
    elif selected_tab == "Add Data":
        # Upload and append data on this tab
        upload_and_append_data()
    elif selected_tab == "Saved Data":
        # Display the opportunities table on this tab
        display_opportunities_table()
        # Save data to Excel on this tab
        save_to_excel()
