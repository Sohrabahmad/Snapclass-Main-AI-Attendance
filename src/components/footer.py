import streamlit as st
import base64
from pathlib import Path


def footer_home():
    # Locate src/images/logo1.png
    src_folder = Path(__file__).resolve().parents[1]
    logo_path = src_folder / "images" / "name-logo.png"

    if not logo_path.is_file():
        st.error(f"Logo not found: {logo_path}")
        return

    try:
        with open(logo_path, "rb") as image_file:
            logo_base64 = base64.b64encode(
                image_file.read()
            ).decode("utf-8")

        
        st.markdown(
        f"""
        <div style="
            margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center;
        ">

        <p style="font-weight:bold; color:white;"> Created with ❤️ by </p>
            <img
                src="data:image/png;base64,{logo_base64}"
                alt="SnapClass Logo"
                style="
                    max-height:35px;
                "
            />

        

        </div>
        """,
        unsafe_allow_html=True
        )

    except (OSError, ValueError) as error:
        st.error(f"Unable to load logo: {error}")
