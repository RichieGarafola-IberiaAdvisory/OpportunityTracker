import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Initialize the 'data' session state as an empty list if it doesn't exist
if "data" not in st.session_state:
    st.session_state.data = []
# Save the DataFrame to Excel
if st.button("Save to Excel"):
    df = pd.DataFrame(st.session_state.data)
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

# Display table
st.dataframe(df)
    
# Create columns for layout
col1, col2 = st.columns(2)

with col1:
####################################
# Bar Chart for Vehicle Distribution:
####################################

    # Count opportunities per vehicle
    vehicle_counts = df["Vehicle"].value_counts()

    # Create a bar chart
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(vehicle_counts.index, vehicle_counts.values)
    ax.set_xlabel("Vehicle")
    ax.set_ylabel("Count")
    ax.set_title("Opportunity Distribution by Vehicle")
    ax.tick_params(axis="x", rotation=45)
    st.pyplot(fig)

with col2:
######################################
# Pie Chart for Set Aside Distribution:
######################################

    # Count opportunities per set aside
    set_aside_counts = df["Set Aside"].explode().value_counts()

    # Create a pie chart
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(set_aside_counts.values, labels=set_aside_counts.index, autopct="%1.1f%%", startangle=140)
    ax.axis("equal")
    ax.set_title("Opportunity Distribution by Set Aside")
    st.pyplot(fig)

# Create columns for layout
col1, col2 = st.columns(2)

with col1:
#################################
# Count Plot for Response Status:
#################################

    # Create a count plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x="Response Status", ax=ax)
    ax.set_xlabel("Response Status")
    ax.set_ylabel("Count")
    ax.set_title("Opportunity Response Status")
    st.pyplot(fig)

with col2:
######################################
# Line Chart for Opportunities Over Time 
######################################

    # Convert the "Release Date" column to datetime
    df["Release Date"] = pd.to_datetime(df["Release Date"])

    # Group opportunities by release date and count
    opportunities_over_time = df.groupby("Release Date").size()

    # Create a line chart
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(opportunities_over_time.index, opportunities_over_time.values)
    ax.set_xlabel("Release Date")
    ax.set_ylabel("Number of Opportunities")
    ax.set_title("Opportunities Over Time")
    ax.tick_params(axis="x", rotation=45)
    st.pyplot(fig)

# Create columns for layout
col1, col2 = st.columns(2)

with col1:
#######################################################
# Stacked Bar Chart for Iberia Role vs. Response Status:
#######################################################

    # Create a crosstab of Iberia Role vs. Response Status
    cross_tab = pd.crosstab(df["Iberia Role"], df["Response Status"])

    # Create a stacked bar chart
    fig, ax = plt.subplots(figsize=(8, 6))
    cross_tab.plot(kind="bar", stacked=True, ax=ax)
    ax.set_xlabel("Iberia Role")
    ax.set_ylabel("Count")
    ax.set_title("Response Status by Iberia Role")
    ax.tick_params(axis="x", rotation=0)
    st.pyplot(fig)

with col2:
###################################
# Word Cloud for Potential Partners: 
###################################
    st.write("word cloud goes here")
    # # Concatenate potential partners' names into a single string
    # potential_partners_text = " ".join(df[df["Iberia Role"] == "Sub"]["Potential Partners"])

    # # Create a word cloud
    # wordcloud = WordCloud(width=800, height=400, background_color="white").generate(potential_partners_text)

    # # Display the word cloud
    # fig, ax = plt.subplots(figsize=(10, 6))
    # ax.imshow(wordcloud, interpolation="bilinear")
    # ax.axis("off")
    # ax.set_title("Potential Partners Word Cloud")
    # st.pyplot(fig)

# Create columns for layout
col1, col2 = st.columns(2)

with col1:
##########################
# Count Plot for RFP Types:
##########################

    # Create a count plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x="Type", ax=ax)
    ax.set_xlabel("RFP Type")
    ax.set_ylabel("Count")
    ax.set_title("Opportunity RFP Types")
    ax.tick_params(axis="x", rotation=45)
    st.pyplot(fig)


with col2:
################################
# Histogram for Opportunity Size:
################################

    # Convert the "Size" column to numeric
    df["Solicitation Value"] = pd.to_numeric(df["Solicitation Value"], errors="coerce")

    # Create a histogram
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df["Solicitation Value"].dropna(), bins=20, edgecolor="black")
    ax.set_xlabel("Opportunity Size")
    ax.set_ylabel("Count")
    ax.set_title("Opportunity Size Distribution")
    st.pyplot(fig)

# Create columns for layout
col1, col2 = st.columns(2)

with col1:
###################################
# Count Plot for Buying Organization:
###################################

    # Count opportunities per buying organization
    buying_org_counts = df["Buying Organization"].value_counts()

    # Create a count plot
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=buying_org_counts.index, y=buying_org_counts.values, ax=ax)
    ax.set_xlabel("Buying Organization")
    ax.set_ylabel("Count")
    ax.set_title("Opportunity Distribution by Buying Organization")
    ax.tick_params(axis="x", rotation=90)
    st.pyplot(fig)

with col2:
#######################################################
# Count Plot for Response Status by Buying Organization:
#######################################################

    # Create a crosstab of Buying Organization vs. Response Status
    cross_tab_buying_org = pd.crosstab(df["Buying Organization"], df["Response Status"])

    # Create a stacked bar chart
    fig, ax = plt.subplots(figsize=(12, 6))
    cross_tab_buying_org.plot(kind="bar", stacked=True, ax=ax)
    ax.set_xlabel("Buying Organization")
    ax.set_ylabel("Count")
    ax.set_title("Response Status by Buying Organization")
    ax.tick_params(axis="x", rotation=90)
    st.pyplot(fig)
