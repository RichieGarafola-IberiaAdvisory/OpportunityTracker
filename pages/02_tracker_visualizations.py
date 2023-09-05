# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from wordcloud import WordCloud

# # Initialize the 'data' session state as an empty list if it doesn't exist
# if "data" not in st.session_state:
#     st.session_state.data = []

# # Initialize the 'df' session state as an empty DataFrame if it doesn't exist
# if "df" not in st.session_state:
#     st.session_state.df = pd.DataFrame()
    
# # Create two columns for saving the data
# col1, col2 = st.columns(2)

# with col1:
#     # Input field for Excel file name
#     excel_filename = st.text_input("Enter Excel File Name (without extension)", "opportunity_tracker")
    
#     # Save button to Excel
#     if st.button('Save Data to Excel'):
#         @st.cache_data
#         def save_to_excel(df, file_path):
#             with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
#                 df.to_excel(writer, index=False)
        
#         opportunity_df = pd.DataFrame(st.session_state.data)  # Convert opportunity data to a DataFrame

#         # Get the path to the user's downloads folder
#         downloads_folder = os.path.expanduser("~/Downloads")
#         excel_file_path = os.path.join(downloads_folder, f"{excel_filename}.xlsx")

#         save_to_excel(opportunity_df, excel_file_path)
#         st.success(f"DataFrame saved to '{excel_file_path}'")

# with col2:
#     # Input field for CSV file name
#     csv_filename = st.text_input("Enter CSV File Name (without extension)", "opportunity_tracker")
    
#     # Save button to CSV
#     if st.button('Save Data to CSV'):
#         @st.cache_data
#         def save_to_csv(df, file_path):
#             df.to_csv(file_path, index=False)
        
#         opportunity_df = pd.DataFrame(st.session_state.data)  # Convert opportunity data to a DataFrame

#         # Get the path to the user's downloads folder
#         downloads_folder = os.path.expanduser("~/Downloads")
#         csv_file_path = os.path.join(downloads_folder, f"{csv_filename}.csv")

#         save_to_csv(opportunity_df, csv_file_path)
#         st.success(f"DataFrame saved to '{csv_file_path}'")

# # Upload data file
# uploaded_file = st.sidebar.file_uploader("Upload Excel File to Append Data", type=["xlsx"])

# if uploaded_file is not None:
#     try:
#         new_data = pd.read_excel(uploaded_file)
        
#         # Define the expected columns that should match with the uploaded data
#         expected_columns = [
#             "Buying Organization",
#             "Name of Solicitation",
#             "Solicitation Number",
#             "Link to Solicitation",
#             "Release Date",
#             "Due Date",
#             "Vehicle",
#             "Type",
#             "Solicitation Value",
#             "Solicitation Duration",
#             "Set Aside",
#             "Iberia Role",
#             "Teaming Partners (Confirmed)",
#             "Teaming Partners (Potential)",
#             "Response Status",
#             "Date Submitted",
#             "Submitted to",
#         ]

#         # Check if the uploaded data has the expected columns
#         if set(new_data.columns) == set(expected_columns):
#             # Append the uploaded data to the existing 'data' list of dictionaries
#             if not st.session_state.data:
#                 st.session_state.data = new_data.to_dict("records")
#             else:
#                 st.session_state.data.extend(new_data.to_dict("records"))
#             st.success("Data appended successfully.")
#         else:
#             st.error("Uploaded data has different columns. Please check the file and try again.")
#     except Exception as e:
#         st.error(f"An error occurred while uploading and appending data: {e}")

# # Display the opportunities table
# if st.session_state.data:
#     df = pd.DataFrame(st.session_state.data)
# # else:
# #     df = pd.DataFrame()
    
# # Display table
#     st.dataframe(df)

#     sns.set_palette("Blues")

#     # Create columns for layout
#     col1, col2 = st.columns(2)

#     with col1:
#     ####################################
#     # Bar Chart for Vehicle Distribution:
#     ####################################
#         try:
#             # Count opportunities per vehicle
#             vehicle_counts = df["Vehicle"].value_counts()

#             # Create a bar chart
#             fig, ax = plt.subplots(figsize=(8, 6))
#             ax.bar(vehicle_counts.index, vehicle_counts.values)
#             ax.set_title("Opportunity Distribution by Vehicle", fontsize=16)
#             ax.set_xlabel("Vehicle", fontsize=12)
#             ax.tick_params(axis="x", rotation=45, labelsize=12)
#             ax.set_ylabel("Count", fontsize=12)
#             ax.tick_params(axis="y", labelsize=12)
#             st.pyplot(fig)
#         except Exception as e:
#             st.error(f"Error occurred while creating the Vehicle Distribution bar chart: {e}")



#     # Interactivity for the barchart

#     #     # Get unique vehicle options
#     #     unique_vehicles = df["Vehicle"].unique()

#     #     # Create a dropdown to select the vehicle
#     #     selected_vehicle = st.selectbox("Select Vehicle", unique_vehicles)

#     #     # Filter the data based on the selected vehicle
#     #     filtered_df = df[df["Vehicle"] == selected_vehicle]

#     #     # Count opportunities per vehicle
#     #     vehicle_counts = filtered_df["Vehicle"].value_counts()

#     #     # Create a bar chart
#     #     fig, ax = plt.subplots(figsize=(8, 6))
#     #     ax.bar(vehicle_counts.index, vehicle_counts.values)
#     #     ax.set_xlabel("Vehicle")
#     #     ax.set_ylabel("Count")
#     #     ax.set_title(f"Opportunity Distribution for {selected_vehicle} Vehicle")
#     #     ax.tick_params(axis="x", rotation=45)
#     #     st.pyplot(fig)

#     with col2:
#     ######################################
#     # Pie Chart for Set Aside Distribution:
#     ######################################

#         try:
#             # Count opportunities per set aside
#             set_aside_counts = df["Set Aside"].explode().value_counts()

#             # Create a pie chart
#             fig, ax = plt.subplots(figsize=(8, 8))
#             ax.pie(set_aside_counts.values, labels=set_aside_counts.index, autopct="%1.1f%%", startangle=140)
#             ax.axis("equal")
#             ax.set_title("Opportunity Distribution by Set Aside", fontsize=16)
#             ax.tick_params(axis="x", labelsize=12)
#             ax.tick_params(axis="y", labelsize=12)
#             st.pyplot(fig)
#         except Exception as e:
#             st.error(f"Error occurred while creating the Pie Chart for Set Aside Distribution: {e}")

#     # Create columns for layout
#     col1, col2 = st.columns(2)

#     with col1:
#     #################################
#     # Count Plot for Response Status:
#     #################################
#         try:
#             # Create a count plot
#             fig, ax = plt.subplots(figsize=(8, 6))
#             sns.countplot(data=df, x="Response Status", ax=ax)
#             ax.set_title("Opportunity Response Status", fontsize=16)
#             ax.set_xlabel("Response Status", fontsize=12)
#             ax.tick_params(axis="x", labelsize=12)
#             ax.set_ylabel("Count", fontsize=12)
#             ax.tick_params(axis="y", labelsize=12)       
#             st.pyplot(fig)
#         except Exception as e:
#             st.error(f"Error occurred while creating the Count Plot for Response Status: {e}")

#     with col2:
#     ######################################
#     # Line Chart for Opportunities Over Time 
#     ######################################

#         try:
#             # Convert the "Release Date" column to datetime
#             df["Release Date"] = pd.to_datetime(df["Release Date"])

#             # Group opportunities by release date and count
#             opportunities_over_time = df.groupby("Release Date").size()

#             # Create a line chart
#             fig, ax = plt.subplots(figsize=(10, 6))
#             ax.plot(opportunities_over_time.index, opportunities_over_time.values)
#             ax.set_title("Opportunities Over Time", fontsize=16)
#             ax.set_xlabel("Release Date", fontsize=12)
#             ax.tick_params(axis="x", rotation=45, labelsize=12)
#             ax.set_ylabel("Number of Opportunities", fontsize=12)
#             ax.tick_params(axis="y", labelsize=12)        
#             st.pyplot(fig)
#         except Exception as e:
#             st.error(f"Error occurred while creating the Line Chart for Opportunities Over Time: {e}")

#     # Create columns for layout
#     col1, col2 = st.columns(2)

#     with col1:
#     #######################################################
#     # Stacked Bar Chart for Iberia Role vs. Response Status:
#     #######################################################
#         try:
#             # Create a crosstab of Iberia Role vs. Response Status
#             cross_tab = pd.crosstab(df["Iberia Role"], df["Response Status"])

#             # Create a stacked bar chart
#             fig, ax = plt.subplots(figsize=(8, 6))
#             cross_tab.plot(kind="bar", stacked=True, ax=ax)
#             ax.set_title("Response Status by Iberia Role", fontsize=16)
#             ax.set_xlabel("Iberia Role", fontsize=12)
#             ax.tick_params(axis="x", labelsize=12)
#             ax.set_ylabel("Count", fontsize=12)
#             ax.tick_params(axis="y", labelsize=12)
#             st.pyplot(fig)
#         except Exception as e:
#             st.error(f"Error occurred while creating the Stacked Bar Chart for Iberia Role vs. Response Status: {e}")

#     with col2:
#     ###################################
#     # Word Cloud for Potential Partners: 
#     ###################################
#         try:
#             st.write("word cloud goes here")
#             # # Concatenate potential partners' names into a single string
#             # potential_partners_text = " ".join(df[df["Iberia Role"] == "Sub"]["Potential Partners"])

#             # # Create a word cloud
#             # wordcloud = WordCloud(width=800, height=400, background_color="white").generate(potential_partners_text)

#             # # Display the word cloud
#             # fig, ax = plt.subplots(figsize=(10, 6))
#             # ax.imshow(wordcloud, interpolation="bilinear")
#             # ax.axis("off")
#             # ax.set_title("Potential Partners Word Cloud")
#             # st.pyplot(fig)
#         except Exception as e:
#             st.error(f"Error occurred while creating the Word Cloud for Potential Partners:  {e}")

#     # Create columns for layout
#     col1, col2 = st.columns(2)

#     with col1:
#     ##########################
#     # Count Plot for RFP Types:
#     ##########################
#         try:
#             # Create a count plot
#             fig, ax = plt.subplots(figsize=(8, 6))
#             sns.countplot(data=df, x="Type", ax=ax)
#             ax.set_title("Opportunity RFP Types", fontsize=16)
#             ax.set_xlabel("RFP Type", fontsize=12)
#             ax.tick_params(axis="x", rotation=45, labelsize=12)
#             ax.set_ylabel("Count", fontsize=12)
#             ax.tick_params(axis="y", labelsize=12)
#             st.pyplot(fig)
#         except Exception as e:
#             st.error(f"Error occurred while creating the Count Plot for RFP Types: {e}")
#     # Interactivity
#     #     # Create a checkbox to select plot orientation
#     #     horizontal_plot = st.checkbox("Horizontal Plot", value=True)

#     #     # Create a count plot
#     #     fig, ax = plt.subplots(figsize=(8, 6))

#     #     if horizontal_plot:
#     #         sns.countplot(data=df, y="Type", ax=ax)
#     #         ax.set_xlabel("Count")
#     #         ax.set_ylabel("RFP Type")
#     #     else:
#     #         sns.countplot(data=df, x="Type", ax=ax)
#     #         ax.set_xlabel("RFP Type")
#     #         ax.set_ylabel("Count")

#     #     ax.set_title("Opportunity RFP Types")
#     #     ax.tick_params(axis="x", rotation=45)
#     #     st.pyplot(fig)


#     with col2:
#     ################################
#     # Histogram for Opportunity Size:
#     ################################
#         try:
#             # Convert the "Size" column to numeric
#             df["Solicitation Value"] = pd.to_numeric(df["Solicitation Value"], errors="coerce")

#             # Create a histogram
#             fig, ax = plt.subplots(figsize=(8, 6))
#             ax.hist(df["Solicitation Value"].dropna(), bins=20, edgecolor="black")
#             ax.set_title("Opportunity Size Distribution", fontsize=16)
#             ax.set_xlabel("Opportunity Size", fontsize=12)
#             ax.tick_params(axis="x", labelsize=12)
#             ax.set_ylabel("Count", fontsize=12)
#             ax.tick_params(axis="y", labelsize=12)
#             st.pyplot(fig)
#         except Exception as e:
#             st.error(f"Error occurred while creating the Histogram for Opportunity Size: {e}")

#     # Create columns for layout
#     col1, col2 = st.columns(2)

#     with col1:
#     ###################################
#     # Count Plot for Buying Organization:
#     ###################################
#         try:
#             # Count opportunities per buying organization
#             buying_org_counts = df["Buying Organization"].value_counts()

#             # Create a count plot
#             fig, ax = plt.subplots(figsize=(12, 6))
#             sns.barplot(x=buying_org_counts.index, y=buying_org_counts.values, ax=ax)
#             ax.set_title("Opportunity Distribution by Buying Organization", fontsize=16)
#             ax.set_xlabel("Buying Organization", fontsize=12)
#             ax.tick_params(axis="x", rotation=90, labelsize=12)
#             ax.set_ylabel("Count", fontsize=12)
#             ax.tick_params(axis="y", labelsize=12)
#             st.pyplot(fig)
#         except Exception as e:
#             st.error(f"Error occurred while creating the Count Plot for Buying Organization: {e}")

#     with col2:
#     #######################################################
#     # Count Plot for Response Status by Buying Organization:
#     #######################################################
#         try:
#             # Create a crosstab of Buying Organization vs. Response Status
#             cross_tab_buying_org = pd.crosstab(df["Buying Organization"], df["Response Status"])

#             # Create a stacked bar chart
#             fig, ax = plt.subplots(figsize=(12, 6))
#             cross_tab_buying_org.plot(kind="bar", stacked=True, ax=ax)
#             ax.set_title("Response Status by Buying Organization", fontsize=16)
#             ax.set_xlabel("Buying Organization", fontsize=12)
#             ax.tick_params(axis="x", rotation=90, labelsize=12)
#             ax.set_ylabel("Count", fontsize=12)
#             ax.tick_params(axis="y", labelsize=12)
#             st.pyplot(fig)
#         except Exception as e:
#             st.error(f"Error occurred while creating the Count Plot for Response Status by Buying Organization: {e}")
            
# else:
#     st.info("Please import data using the sidebar to display the opportunities table.")






import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import plotly.express as px

# Initialize the 'data' session state as an empty list if it doesn't exist
if "data" not in st.session_state:
    st.session_state.data = []

# Create two columns for saving the data
col1, col2 = st.columns(2)

with col1:
    # Input field for Excel file name
    excel_filename = st.text_input("Enter Excel File Name (without extension)", "opportunity_tracker")

    # Save button to Excel
    if st.button('Save Data to Excel'):
        @st.cache
        def save_to_excel(df, file_path):
            with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False)

        opportunity_df = pd.DataFrame(st.session_state.data)  # Convert opportunity data to a DataFrame

        # Get the path to the user's downloads folder
        excel_file_path = st.download_button(
            label=f"Download Excel ({excel_filename}.xlsx)",
            data=opportunity_df.to_excel,
            args=(excel_filename + '.xlsx',),
            key="download_excel"
        )

        st.success(f"DataFrame saved to '{excel_file_path}'")

with col2:
    # Input field for CSV file name
    csv_filename = st.text_input("Enter CSV File Name (without extension)", "opportunity_tracker")

    # Save button to CSV
    if st.button('Save Data to CSV'):
        @st.cache
        def save_to_csv(df, file_path):
            df.to_csv(file_path, index=False)

        opportunity_df = pd.DataFrame(st.session_state.data)  # Convert opportunity data to a DataFrame

        # Get the path to the user's downloads folder
        csv_file_path = st.download_button(
            label=f"Download CSV ({csv_filename}.csv)",
            data=opportunity_df.to_csv,
            args=(csv_filename + '.csv',),
            key="download_csv"
        )
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
            st.session_state.data.extend(new_data.to_dict("records"))
            st.success("Data appended successfully.")
        else:
            st.error("Uploaded data has different columns. Please check the file and try again.")
    except Exception as e:
        st.error(f"An error occurred while uploading and appending data: {e}")

# Display the opportunities table
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    
    # Display table
    st.dataframe(df)

    # Add interactivity for visualizations here...

    # Vehicle Distribution Bar Chart
    st.subheader("Opportunity Distribution by Vehicle")
    vehicle_counts = df["Vehicle"].value_counts()
    st.bar_chart(vehicle_counts)

    # Set Aside Pie Chart
    st.subheader("Opportunity Distribution by Set Aside")
    set_aside_counts = df["Set Aside"].explode().value_counts()
    fig = px.pie(
        names=set_aside_counts.index,
        values=set_aside_counts.values,
        labels=set_aside_counts.index,
        title="Opportunity Distribution by Set Aside"
    )
    st.plotly_chart(fig)

    # Response Status Count Plot
    st.subheader("Opportunity Response Status")
    sns.set_palette("Blues")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x="Response Status", ax=ax)
    ax.set_title("Opportunity Response Status", fontsize=16)
    ax.set_xlabel("Response Status", fontsize=12)
    ax.tick_params(axis="x", labelsize=12)
    ax.set_ylabel("Count", fontsize=12)
    ax.tick_params(axis="y", labelsize=12)
    st.pyplot(fig)

    # Opportunities Over Time Line Chart
    st.subheader("Opportunities Over Time")
    df["Release Date"] = pd.to_datetime(df["Release Date"])
    opportunities_over_time = df.groupby("Release Date").size()
    st.line_chart(opportunities_over_time)

    # Iberia Role vs. Response Status Stacked Bar Chart
    st.subheader("Response Status by Iberia Role")
    cross_tab = pd.crosstab(df["Iberia Role"], df["Response Status"])
    st.bar_chart(cross_tab, use_container_width=True)

    # Word Cloud for Potential Partners
    if 'Teaming Partners (Potential)' in df.columns:
        st.subheader("Potential Partners Word Cloud")
        potential_partners_text = " ".join(df[df["Iberia Role"] == "Sub"]["Teaming Partners (Potential)"])
        if potential_partners_text:
            wordcloud = WordCloud(width=800, height=400, background_color="white").generate(potential_partners_text)
            st.image(wordcloud.to_array())
        else:
            st.info("No data available for Potential Partners Word Cloud.")
    else:
        st.info("The 'Teaming Partners (Potential)' column does not exist in the DataFrame.")


    # RFP Types Count Plot

    st.subheader("Opportunity RFP Types")
    sns.set_palette("Blues")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x="Type", ax=ax)
    ax.set_title("Opportunity RFP Types", fontsize=16)
    ax.set_xlabel("RFP Type", fontsize=12)
    ax.tick_params(axis="x", rotation=45, labelsize=12)
    ax.set_ylabel("Count", fontsize=12)
    ax.tick_params(axis="y", labelsize=12)
    st.pyplot(fig)
    
    # Opportunity Size Histogram
    st.subheader("Opportunity Size Distribution")
    df["Solicitation Value"] = pd.to_numeric(df["Solicitation Value"], errors="coerce")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df["Solicitation Value"].dropna(), bins=20, edgecolor="black", alpha=0.7)
    ax.set_title("Opportunity Size Distribution", fontsize=16)
    ax.set_xlabel("Opportunity Size", fontsize=12)
    ax.tick_params(axis="x", labelsize=12)
    ax.set_ylabel("Count", fontsize=12)
    ax.tick_params(axis="y", labelsize=12)
    st.pyplot(fig)

    # Buying Organization Count Plot
    st.subheader("Opportunity Distribution by Buying Organization")
    buying_org_counts = df["Buying Organization"].value_counts()
    st.bar_chart(buying_org_counts)

    # Response Status by Buying Organization Stacked Bar Chart
    st.subheader("Response Status by Buying Organization")
    cross_tab_buying_org = pd.crosstab(df["Buying Organization"], df["Response Status"])
    st.bar_chart(cross_tab_buying_org, use_container_width=True)
else:
    st.info("Please import data using the sidebar to display the opportunities table.")
