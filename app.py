import streamlit as st
import pandas as pd
import io

st.title("📊 Finance Report AI Generator")
st.write("Upload your financial statements to get instant summary and downloadable report.")

uploaded_file = st.file_uploader("Upload your file (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.subheader("🧾 Data Preview")
        st.dataframe(df.head())

        st.subheader("📈 Summary Report")
        st.write(df.describe())

        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df.describe().to_excel(writer, sheet_name='Summary')
        st.download_button(
            label="Download Excel Report",
            data=buffer.getvalue(),
            file_name="Finance_Report.xlsx",
            mime="application/vnd.ms-excel"
        )

    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.info("Please upload a file to generate your report.")
