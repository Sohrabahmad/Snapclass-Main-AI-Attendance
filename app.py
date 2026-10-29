import streamlit as st
from pathlib import Path

from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen


def main():
    
    src_folder = Path(__file__).resolve().parent / "src"
    icon_path = src_folder / "images" / "logo1.png"

   
    st.set_page_config(
        page_title='SnapClass - Making Attendance faster using AI',
        page_icon=str(icon_path),
        layout="wide"
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()

        case None:
            home_screen()

    

main()