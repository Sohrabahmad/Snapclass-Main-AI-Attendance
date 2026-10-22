
import streamlit as st
import base64
from pathlib import Path


def header_home():
    # Locate src/images/logo1.png
    src_folder = Path(__file__).resolve().parents[1]
    logo_path = src_folder / "images" / "logo1.png"

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
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin: 30px 0;
            width: 100%;
        ">
            <img
                src="data:image/png;base64,{logo_base64}"
                alt="SnapClass Logo"
                style="
                    display: block;
                    height: 100px;
                    width: auto;
                    max-width: 100%;
                    object-fit: contain;
                    background: transparent;
                "
            />

        <h1 style="
            text-align: center;
            color: #E0E3FF;
            line-height: 1.1;
            margin-top: 10px;
        ">SNAP<br>CLASS</h1>

        </div>
        """,
        unsafe_allow_html=True
        )

    except (OSError, ValueError) as error:
        st.error(f"Unable to load logo: {error}")
