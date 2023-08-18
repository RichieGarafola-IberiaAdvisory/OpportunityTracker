import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import psycopg2

# Define the database connection parameters
db_params = {
    'dbname': 'TeamingPartners',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

# Establish a connection to the database
conn = psycopg2.connect(**db_params)

# Create a cursor
cur = conn.cursor()

def visualize_data():
    st.title("Teaming Partners Data Visualization")
    try:
        # Read data from the database tables
        partners_df = pd.read_sql_query("SELECT * FROM TeamingPartners", conn)
        poc_df = pd.read_sql_query("SELECT * FROM POCs", conn)
        nda_status_df = pd.read_sql_query("SELECT * FROM NDAStatus", conn)
        teaming_status_df = pd.read_sql_query("SELECT * FROM TeamingAgreementStatus", conn)
        worked_with_before_df = pd.read_sql_query("SELECT * FROM WorkedWithBefore", conn)
    except Exception as e:
        st.error(f"An error occured: {e}")

     # Data Quality Check: Check for missing values in partners_df
    if partners_df.isnull().any().any():
        st.warning("There are missing values in the 'TeamingPartners' table.")
    
    # Data Cleaning: Replace missing values with 'N/A'
    partners_df.fillna({'PartnerName': 'N/A'}, inplace=True)
    
    sns.set_palette("Blues")    
    col1, col2 = st.columns(2)
    with col1:
        # Partner Type Distribution
        st.subheader("Partner Type Distribution")
        partner_type_counts = partners_df['partnertype'].value_counts()
        st.bar_chart(partner_type_counts)
        
    with col2:    
        # Relationship Type Distribution among POCs
        st.subheader("Relationship Type Distribution among POCs")
        relationship_type_counts = poc_df['relationshiptype'].value_counts()

        # Create a pie chart using Matplotlib
        fig, ax = plt.subplots()
        ax.pie(relationship_type_counts, labels=relationship_type_counts.index, autopct='%1.1f%%')
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.axis('equal')  
        st.pyplot(fig)
    
    col1, col2 = st.columns(2)
    with col1:
        # Worked with Before Percentage
        st.subheader("Worked with Before Percentage")
        worked_with_before_counts = worked_with_before_df['workedbefore'].value_counts()
        # Create a pie chart using Matplotlib
        fig, ax = plt.subplots()
        ax.pie(worked_with_before_counts, labels=worked_with_before_counts.index, autopct='%1.1f%%')
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.axis('equal')  
        st.pyplot(fig)
        
    with col2: 
        # NDA Status Summary
        st.subheader("NDA Status Summary")
        nda_status_counts = nda_status_df['status'].value_counts()
        st.bar_chart(nda_status_counts)
        
    col1, col2 = st.columns(2)
    with col1:
        # Teaming Agreement Status Summary
        st.subheader("Teaming Agreement Status Summary")
        teaming_status_counts = teaming_status_df['status'].value_counts()
        st.bar_chart(teaming_status_counts)
    
#     # Heatmap of NDA and Teaming Agreement Dates
#     st.subheader("Heatmap of NDA and Teaming Agreement Dates")
#     heatmap_data = pd.concat([nda_status_df[['dateissued', 'partialexecuteddate', 'fullyexecuteddate']],
#                               teaming_status_df[['dateissued', 'partialexecuteddate', 'fullyexecuteddate']]])
#     heatmap_data = heatmap_data.dropna()
#     # Reshape the data for the pivot table
#     heatmap_data = heatmap_data.melt(value_vars=['dateissued', 'partialexecuteddate', 'fullyexecuteddate'],
#                                      value_name='AgreementDate')
#     # Convert the AgreementDate column to datetime
#     heatmap_data['AgreementDate'] = pd.to_datetime(heatmap_data['AgreementDate'])
    
#     heatmap_data['partialexecuteddate'] = pd.to_datetime(heatmap_data['partialexecuteddate'])
#     heatmap_data['fullyexecuteddate'] = pd.to_datetime(heatmap_data['fullyexecuteddate'])
#     heatmap = heatmap_data.pivot_table(index=heatmap_data.index.date, columns=heatmap_data.columns,
#                                        aggfunc='size', fill_value=0)
#     plt.figure(figsize=(10, 6))
#     sns.heatmap(heatmap, cmap='YlGnBu', annot=True, fmt='d', cbar_kws={'label': 'Number of Agreements'})
#     st.pyplot()

# Close the database connection at the end
if __name__ == "__main__":
    visualize_data()
    conn.close()
