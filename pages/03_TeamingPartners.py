# import streamlit as st
# import pandas as pd
# import psycopg2

# # Define the database connection parameters
# db_params = {
#     'dbname': 'TeamingPartners',
#     'user': 'postgres',
#     'password': 'postgres',
#     'host': 'localhost',
#     'port': '5432'
# }

# # Establish a connection to the database
# conn = psycopg2.connect(**db_params)

# # Create a cursor
# cur = conn.cursor()

# def main():
#     st.title("Teaming Partners Form")
    
#     confirmed_partners = st.text_area("Confirmed Partners (one per line)", height=100)
#     potential_partners = st.text_area("Potential Partners (free text)", height=100)
    
#     st.header("Teaming Partner Page")
    
#     num_pocs = st.number_input("Number of Points of Contact (POCs)", min_value=1, max_value=10, step=1)
#     poc_data = []
#     for i in range(num_pocs):
#         poc_name = st.text_input(f"POC {i + 1} Name")
#         relationship = st.selectbox(f"Type of Relationship for {poc_name}",
#                                     ["Capture", "Technical", "Leadership"])
#         email = st.text_input(f"{poc_name} Email Address")
#         phone = st.text_input(f"{poc_name} Phone Number")
#         poc_data.append({"Name": poc_name, "Relationship": relationship, "Email": email, "Phone": phone})
    
#     worked_before = st.checkbox("Worked with Before?")
    
#     nda_statuses = ["Issued", "Partially Executed", "Fully Executed"]
#     nda_data = []

#     for status in nda_statuses:
#         st.subheader(f"{status} NDA Status")
#         nda_status_data = {"Status": status}

#         if status == "Issued":
#             issued_date = st.date_input(f"{status} Date Issued", key=f"{status.lower()}_date_issued")
#             sent_to_issued = st.text_input(f"{status} Sent to - Issued", key=f"{status.lower()}_sent_to_issued")
#             nda_status_data["Date Issued"] = issued_date
#             nda_status_data["Sent to - Issued"] = sent_to_issued

#         elif status == "Partially Executed":
#             pe_date = st.date_input(f"{status} Date PE", key=f"{status.lower()}_date_pe")
#             received_from_pe = st.text_input(f"{status} Received from - Partially Executed", key=f"{status.lower()}_received_from_pe")
#             nda_status_data["Date PE"] = pe_date
#             nda_status_data["Received from - Partially Executed"] = received_from_pe

#         elif status == "Fully Executed":
#             fe_date = st.date_input(f"{status} Date FE", key=f"{status.lower()}_date_fe")
#             sent_to_fe = st.text_input(f"{status} Sent to - Fully Executed", key=f"{status.lower()}_sent_to_fe")
#             nda_status_data["Date FE"] = fe_date
#             nda_status_data["Sent to - Fully Executed"] = sent_to_fe

#         nda_data.append(nda_status_data)
    
#     teaming_data = []
#     for status in nda_statuses:
#         st.subheader(f"{status} Teaming Agreement Status")
#         teaming_status_data = {"Status": status}
#         if status == "Issued":
#             issued_date = st.date_input(f"{status} Date Issued", key=f"teaming_{status.lower()}_date_issued")
#             sent_to = st.text_input(f"{status} Sent to - Issued", key=f"teaming_{status.lower()}_sent_to_issued")
#             teaming_status_data["Date Issued"] = issued_date
#             teaming_status_data["Sent to - Issued"] = sent_to
#         elif status == "Partially Executed":
#             pe_date = st.date_input(f"{status} Date PE", key=f"teaming_{status.lower()}_date_pe")
#             received_from = st.text_input(f"{status} Received from - Partially Executed", key=f"teaming_{status.lower()}_received_from_pe")
#             teaming_status_data["Date PE"] = pe_date
#             teaming_status_data["Received from - Partially Executed"] = received_from
#         elif status == "Fully Executed":
#             fe_date = st.date_input(f"{status} Date FE", key=f"teaming_{status.lower()}_date_fe")
#             sent_to = st.text_input(f"{status} Sent to - Fully Executed", key=f"teaming_{status.lower()}_sent_to_fe")
#             teaming_status_data["Date FE"] = fe_date
#             teaming_status_data["Sent to - Fully Executed"] = sent_to
#         teaming_data.append(teaming_status_data)
    
#     if st.button("Submit"):
#         for partner in confirmed_partners.split('\n'):
#             cur.execute("INSERT INTO TeamingPartners (PartnerName, PartnerType) VALUES (%s, %s)", (partner, 'Confirmed'))

#         for partner in potential_partners.split('\n'):
#             cur.execute("INSERT INTO TeamingPartners (PartnerName, PartnerType) VALUES (%s, %s)", (partner, 'Potential'))

#         for poc in poc_data:
#             cur.execute("INSERT INTO POCs (POCName, RelationshipType, EmailAddress, PhoneNumber) "
#                         "VALUES (%s, %s, %s, %s)",
#                         (poc['Name'], poc['Relationship'], poc['Email'], poc['Phone']))

#         cur.execute("INSERT INTO WorkedWithBefore (WorkedBefore) VALUES (%s)", (worked_before,))

#         for nda in nda_data:
#             cur.execute("INSERT INTO NDAStatus (Status, DateIssued, SentTo, PartialExecutedDate, PartialExecutedReceivedFrom, FullyExecutedDate, FullyExecutedSentTo) "
#                         "VALUES (%s, %s, %s, %s, %s, %s, %s)",
#                         (nda['Status'], nda.get('Date Issued'), nda.get('Sent to - Issued'),
#                          nda.get('Date PE'), nda.get('Received from - Partially Executed'),
#                          nda.get('Date FE'), nda.get('Sent to - Fully Executed')))

#         for teaming in teaming_data:
#             cur.execute("INSERT INTO TeamingAgreementStatus (Status, DateIssued, SentTo, PartialExecutedDate, PartialExecutedReceivedFrom, FullyExecutedDate, FullyExecutedSentTo) "
#                         "VALUES (%s, %s, %s, %s, %s, %s, %s)",
#                         (teaming['Status'], teaming.get('Date Issued'), teaming.get('Sent to - Issued'),
#                          teaming.get('Date PE'), teaming.get('Received from - Partially Executed', None),  # Use None as default
#                          teaming.get('Date FE'), teaming.get('Sent to - Fully Executed')))

#         conn.commit()
#         st.write("Data submitted successfully.")

#         # Display the contents of the Teaming Partners table
#         cur.execute("SELECT * FROM TeamingPartners")
#         partners_data = cur.fetchall()
#         st.subheader("Teaming Partners Table")
#         st.dataframe(pd.DataFrame(partners_data, columns=["PartnerID", "PartnerName", "PartnerType", "PageLink"]))

#         # Display the contents of the POCs table
#         cur.execute("SELECT * FROM POCs")
#         poc_data = cur.fetchall()
#         st.subheader("POCs Table")
#         st.dataframe(pd.DataFrame(poc_data, columns=["POCID", "PartnerID", "POCName", "RelationshipType", "EmailAddress", "PhoneNumber"]))

#         # Display the contents of the WorkedWithBefore table
#         cur.execute("SELECT * FROM WorkedWithBefore")
#         worked_before_data = cur.fetchall()
#         st.subheader("WorkedWithBefore Table")
#         st.dataframe(pd.DataFrame(worked_before_data, columns=["WorkedWithBeforeID", "PartnerID", "WorkedBefore"]))

#         # Display the contents of the NDAStatus table
#         cur.execute("SELECT * FROM NDAStatus")
#         nda_status_data = cur.fetchall()
#         st.subheader("NDAStatus Table")
#         st.dataframe(pd.DataFrame(nda_status_data, columns=["NDAStatusID", "PartnerID", "Status", "DateIssued", "SentTo", "PartialExecutedDate", "PartialExecutedReceivedFrom", "FullyExecutedDate", "FullyExecutedSentTo"]))

#         # Display the contents of the TeamingAgreementStatus table
#         cur.execute("SELECT * FROM TeamingAgreementStatus")
#         teaming_status_data = cur.fetchall()
#         st.subheader("TeamingAgreementStatus Table")
#         st.dataframe(pd.DataFrame(teaming_status_data, columns=["TeamingAgreementStatusID", "PartnerID", "Status", "DateIssued", "SentTo", "PartialExecutedDate", "PartialExecutedReceivedFrom", "FullyExecutedDate", "FullyExecutedSentTo"]))

#         conn.commit()

# if __name__ == "__main__":
#     main()
#     cur.close()
#     conn.close()




##################
# UPDATED LAYOUT!
##################


import streamlit as st
import pandas as pd
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

def main():
    st.title("Teaming Partners Form")
    
    col1, col2 = st.columns(2)
    
    with col1:
        confirmed_partners = st.text_area("Confirmed Partners (one per line)", height=100)
        potential_partners = st.text_area("Potential Partners (free text)", height=100)
    
    with col2:
        num_pocs = st.number_input("Number of Points of Contact (POCs)", min_value=1, max_value=10, step=1)
        poc_data = []
        for i in range(num_pocs):
            poc_name = st.text_input(f"POC {i + 1} Name")
            relationship = st.selectbox(f"Type of Relationship for {poc_name}",
                                        ["Capture", "Technical", "Leadership"])
            email = st.text_input(f"{poc_name} Email Address")
            phone = st.text_input(f"{poc_name} Phone Number")
            poc_data.append({"Name": poc_name, "Relationship": relationship, "Email": email, "Phone": phone})
    
    worked_before = st.checkbox("Worked with Before?")
    
    nda_statuses = ["Issued", "Partially Executed", "Fully Executed"]
    nda_data = []

    for status in nda_statuses:
        st.subheader(f"{status} NDA Status")
        nda_status_data = {"Status": status}

        if status == "Issued":
            issued_date = st.date_input(f"{status} Date Issued", key=f"{status.lower()}_date_issued")
            sent_to_issued = st.text_input(f"{status} Sent to - Issued", key=f"{status.lower()}_sent_to_issued")
            nda_status_data["Date Issued"] = issued_date
            nda_status_data["Sent to - Issued"] = sent_to_issued

        elif status == "Partially Executed":
            pe_date = st.date_input(f"{status} Date PE", key=f"{status.lower()}_date_pe")
            received_from_pe = st.text_input(f"{status} Received from - Partially Executed", key=f"{status.lower()}_received_from_pe")
            nda_status_data["Date PE"] = pe_date
            nda_status_data["Received from - Partially Executed"] = received_from_pe

        elif status == "Fully Executed":
            fe_date = st.date_input(f"{status} Date FE", key=f"{status.lower()}_date_fe")
            sent_to_fe = st.text_input(f"{status} Sent to - Fully Executed", key=f"{status.lower()}_sent_to_fe")
            nda_status_data["Date FE"] = fe_date
            nda_status_data["Sent to - Fully Executed"] = sent_to_fe

        nda_data.append(nda_status_data)
    
    teaming_data = []
    for status in nda_statuses:
        st.subheader(f"{status} Teaming Agreement Status")
        teaming_status_data = {"Status": status}
        if status == "Issued":
            issued_date = st.date_input(f"{status} Date Issued", key=f"teaming_{status.lower()}_date_issued")
            sent_to = st.text_input(f"{status} Sent to - Issued", key=f"teaming_{status.lower()}_sent_to_issued")
            teaming_status_data["Date Issued"] = issued_date
            teaming_status_data["Sent to - Issued"] = sent_to
        elif status == "Partially Executed":
            pe_date = st.date_input(f"{status} Date PE", key=f"teaming_{status.lower()}_date_pe")
            received_from = st.text_input(f"{status} Received from - Partially Executed", key=f"teaming_{status.lower()}_received_from_pe")
            teaming_status_data["Date PE"] = pe_date
            teaming_status_data["Received from - Partially Executed"] = received_from
        elif status == "Fully Executed":
            fe_date = st.date_input(f"{status} Date FE", key=f"teaming_{status.lower()}_date_fe")
            sent_to = st.text_input(f"{status} Sent to - Fully Executed", key=f"teaming_{status.lower()}_sent_to_fe")
            teaming_status_data["Date FE"] = fe_date
            teaming_status_data["Sent to - Fully Executed"] = sent_to
        teaming_data.append(teaming_status_data)
    
    if st.button("Submit"):
        for partner in confirmed_partners.split('\n'):
            cur.execute("INSERT INTO TeamingPartners (PartnerName, PartnerType) VALUES (%s, %s)", (partner, 'Confirmed'))

        for partner in potential_partners.split('\n'):
            cur.execute("INSERT INTO TeamingPartners (PartnerName, PartnerType) VALUES (%s, %s)", (partner, 'Potential'))

        for poc in poc_data:
            cur.execute("INSERT INTO POCs (POCName, RelationshipType, EmailAddress, PhoneNumber) "
                        "VALUES (%s, %s, %s, %s)",
                        (poc['Name'], poc['Relationship'], poc['Email'], poc['Phone']))

        cur.execute("INSERT INTO WorkedWithBefore (WorkedBefore) VALUES (%s)", (worked_before,))

        for nda in nda_data:
            cur.execute("INSERT INTO NDAStatus (Status, DateIssued, SentTo, PartialExecutedDate, PartialExecutedReceivedFrom, FullyExecutedDate, FullyExecutedSentTo) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (nda['Status'], nda.get('Date Issued'), nda.get('Sent to - Issued'),
                         nda.get('Date PE'), nda.get('Received from - Partially Executed'),
                         nda.get('Date FE'), nda.get('Sent to - Fully Executed')))

        for teaming in teaming_data:
            cur.execute("INSERT INTO TeamingAgreementStatus (Status, DateIssued, SentTo, PartialExecutedDate, PartialExecutedReceivedFrom, FullyExecutedDate, FullyExecutedSentTo) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (teaming['Status'], teaming.get('Date Issued'), teaming.get('Sent to - Issued'),
                         teaming.get('Date PE'), teaming.get('Received from - Partially Executed', None),  # Use None as default
                         teaming.get('Date FE'), teaming.get('Sent to - Fully Executed')))

        conn.commit()
        st.write("Data submitted successfully.")

        # Display the contents of the Teaming Partners table
        cur.execute("SELECT * FROM TeamingPartners")
        partners_data = cur.fetchall()
        st.subheader("Teaming Partners Table")
        st.dataframe(pd.DataFrame(partners_data, columns=["PartnerID", "PartnerName", "PartnerType", "PageLink"]))

        # Display the contents of the POCs table
        cur.execute("SELECT * FROM POCs")
        poc_data = cur.fetchall()
        st.subheader("POCs Table")
        st.dataframe(pd.DataFrame(poc_data, columns=["POCID", "PartnerID", "POCName", "RelationshipType", "EmailAddress", "PhoneNumber"]))

        # Display the contents of the WorkedWithBefore table
        cur.execute("SELECT * FROM WorkedWithBefore")
        worked_before_data = cur.fetchall()
        st.subheader("WorkedWithBefore Table")
        st.dataframe(pd.DataFrame(worked_before_data, columns=["WorkedWithBeforeID", "PartnerID", "WorkedBefore"]))

        # Display the contents of the NDAStatus table
        cur.execute("SELECT * FROM NDAStatus")
        nda_status_data = cur.fetchall()
        st.subheader("NDAStatus Table")
        st.dataframe(pd.DataFrame(nda_status_data, columns=["NDAStatusID", "PartnerID", "Status", "DateIssued", "SentTo", "PartialExecutedDate", "PartialExecutedReceivedFrom", "FullyExecutedDate", "FullyExecutedSentTo"]))

        # Display the contents of the TeamingAgreementStatus table
        cur.execute("SELECT * FROM TeamingAgreementStatus")
        teaming_status_data = cur.fetchall()
        st.subheader("TeamingAgreementStatus Table")
        st.dataframe(pd.DataFrame(teaming_status_data, columns=["TeamingAgreementStatusID", "PartnerID", "Status", "DateIssued", "SentTo", "PartialExecutedDate", "PartialExecutedReceivedFrom", "FullyExecutedDate", "FullyExecutedSentTo"]))

        conn.commit()

if __name__ == "__main__":
    main()
    cur.close()
    conn.close()