import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    # Page configuration
    st.set_page_config(
        layout="wide",
        page_title="Cold Mail Generator",
        page_icon="📧"
    )

    # --- Header ---
    st.markdown(
        """
        <div style="text-align:center; background-color:#f0f2f6; padding:25px; border-radius:12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h1 style="color:#4B0082; font-size:40px;">📧 Cold Mail Generator</h1>
            <p style="font-size:18px; color:#333">Generate personalized cold emails from job postings quickly and efficiently!</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Step 1: Enter the Job URL")

    # Create 3 columns: left, center, right
    col1, col2, col3 = st.columns([1, 2, 1])  # middle column is wider

    with col2:
        url_input = st.text_input(
            "Paste the URL of the company's career/job page here:",
            value="https://gdr-iasis.cnrs.fr/kiosque/phd-offer-scalable-indexing-and-retrieval-in-multimedia-and-geospatial-contents-paris-area-france/",
            placeholder="https://example.com/job-posting"
        )
        submit_button = st.button("Generate Cold Emails", key="submit_btn")

    # --- Output Section ---
    if submit_button:
        if not url_input:
            st.warning("⚠️ Please enter a valid URL.")
        else:
            with st.spinner("⏳ Processing your request..."):
                try:
                    # Load and clean data
                    loader = WebBaseLoader([url_input])
                    page_data = clean_text(loader.load().pop().page_content)

                    # Load portfolio
                    portfolio.load_portfolio()

                    # Extract jobs
                    jobs = llm.extract_jobs(page_data)

                    if not jobs:
                        st.warning("No jobs were extracted from the provided URL.")

                    # Display emails in cards
                    for idx, job in enumerate(jobs, start=1):
                        role = job.get('role', 'Unknown Role')
                        skills = job.get('skills', [])
                        links = portfolio.query_links(skills)
                        email_content = llm.write_mail(job, links)

                        st.markdown(
                            f"""
                            <div style="
                                border:2px solid #4B0082; 
                                border-radius:12px; 
                                padding:20px; 
                                margin-bottom:20px; 
                                background-color:#fafafa;
                                box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
                            ">
                                <h3 style="color:#4B0082;">✉️ Cold Email for Job {idx}: {role}</h3>
                                <pre style="white-space:pre-wrap; font-family: 'Courier New', Courier, monospace;">{email_content}</pre>
                            """
                            +
                            (f"<h4>🔗 Relevant Portfolio Links:</h4>" +
                             "".join([f'<p><a href="{link}" target="_blank">{link}</a></p>' for link in links])
                             if links else "") +
                            "</div>"
                            ,
                            unsafe_allow_html=True
                        )

                except Exception as e:
                    st.error(f"❌ An Error Occurred: {e}")

    # --- Footer ---
    st.markdown("---")
    st.markdown(
        "<p style='text-align:center; color:gray;'>Built with ❤️ using Streamlit and LangChain</p>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)
