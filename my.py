import streamlit as st

# ----------------------------------------------------------------wide page---------------------
st.set_page_config(layout="wide")
from streamlit_option_menu import option_menu
import time
from streamlit_lottie import st_lottie
import requests

# ----------------------------------------------dark mode-----------------------------------------------
# Set background color to dark gray
st.markdown(
    """
    <style>
    .css-17eq0hr {
        color: white;
        background-color: #1E1E1E;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# --------------------------------------------------sidebar----------------------------------------


# ----------------------------------------------------option menu-----------------------------------------
selected = option_menu(
    menu_title=None,
    options=["Home", "Projects", "About Me"],
    icons=["house", "bi bi-stack", "bi bi-person-circle"],
    menu_icon="cast",
    orientation="horizontal",
    styles={
        "container": {"padding": "10"},
        # "selected_option": {"color": "#CE4BC2"},  # Set color for the selected option
        "nav-link-selected": {"background-color": "#CE4BC2"},
    },
)


# ----------------------------------------------------Home------------------------------------------------


if selected == "Home":
    w1, w2 = st.columns([6, 2])
    with w1:
        styled_text = """
            <style>

                h2 {
                    # color: #f8f8f8;
                }
                h1 {
                    color: #f8f8f8;
                    padding-left: 10px;
                    # padding-bottom: 100px;
                    text-shadow: 2px 2px 8px #CE4BC2;
                }

            </style>

            ## Hello, It's Me
            # Shubham Pal
            
            """
        st.markdown(styled_text, unsafe_allow_html=True)
        text = "I'm a passionate coder, front-end developer, and machine learning enthusiast. I turn ideas into captivating digital solutions, blending elegant front-end interfaces with the magic of machine learning. Let's innovate together through technology!"
        t = st.empty()
        for i in range(len(text) + 1):
            t.markdown(text[0:i])
            time.sleep(0.015)

        with st.expander("Read More..."):
            url = requests.get(
                "https://lottie.host/1551fd2a-a56d-4fe1-a2c4-4dbe9e94078f/99ChdRr6TC.json"
            )
            url_json = dict()
            if url.status_code == 200:
                url_json = url.json()
            else:
                st.write("Error in URL")
            st_lottie(
                url_json,
                # change the direction of our animation
                reverse=True,
                # height and width of animation
                height=200,
                width=400,
                # speed of animation
                speed=1,
                # means the animation will run forever like a gif, and not as a still image
                loop=True,
                # quality of elements used in the animation, other values are "low" and "medium"
                quality="high",
                # THis is just to uniquely identify the animation
                key="Hello",
            )
            st.write(
                "As a passionate Information Technology student at IIIT Lucknow, I thrive on transforming innovative ideas into technological solutions. Explore more about me by clicking the 'About Me' option above."
            )

        # ---------------------------------------------------Download Resume----------------------------------

        with open("ShubhamPal_resume.pdf", "rb") as file:
            # Use the custom CSS class (css-hi6a2p) to apply the styling
            btn = st.download_button(
                label="Download Resume",
                data=file,
                file_name="ShubhamPal_resume.pdf",
                mime="application/octet-stream",
                key="custom_download_button",
            )
        # ------------------------------------------------------------contact me----------------------------------------------------------------

        s1, s2 = st.columns([1, 1])
        with s1:
            # ----------------------------------------------------------contact form------------------------------------------------------------
            form_text = """
                        <style>

                            h3 {
                                color: #f8f8f8;
                                padding-left: 10px;
                                padding-top: 100px;
                                text-shadow: 2px 2px 8px #CE4BC2;
                            }

                        </style>

                        ### Contact Form
                        
                        """
            st.markdown(form_text, unsafe_allow_html=True)

            st.header(":mailbox: Get In Touch With Me!")
            contact_form = """
                <form action="https://formsubmit.co/shubhampaliitr@email.com" method="POST">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="text" name="name" placeholder="Your name" required>
                    <input type="email" name="email" placeholder="Your email" required>
                    <textarea name="message" placeholder="Details of your problem"></textarea>
                    <button type="submit">Send</button>
                </form>
                """
            st.markdown(contact_form, unsafe_allow_html=True)

            # Use Local CSS File
            def local_css(file_name):
                with open(file_name) as f:
                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

            local_css("pages/style.css")
        with s2:
            url = requests.get(
                "https://lottie.host/f4d597d4-dcb2-4192-a6ac-4eed6d41b422/YKnPIo8ExR.json"
            )
            url_json = dict()
            if url.status_code == 200:
                url_json = url.json()
            else:
                st.write("Error in URL")
            st_lottie(
                url_json,
                # change the direction of our animation
                reverse=True,
                # height and width of animation
                height=400,
                width=400,
                # speed of animation
                speed=1,
                # means the animation will run forever like a gif, and not as a still image
                loop=True,
                # quality of elements used in the animation, other values are "low" and "medium"
                quality="high",
                # THis is just to uniquely identify the animation
                key="contact",
            )

    with w2:
        st.image("dp.jpeg", width=200)
# ---------------------------------------------------About me-------------------------------------------------------------------------

if selected == "About Me":
    with open("pages/1_about.py", "r") as file:
        code = file.read()
        exec(code)

# ---------------------------------------------------Projects-------------------------------------------------------------------------

if selected == "Projects":
    c1, c2 = st.columns([6, 2])
    with open("pages/2_project.py", "r") as file:
        code = file.read()
        exec(code)
    # with c1:
    # styled_text = """

    # """
    # st.markdown(styled_text, unsafe_allow_html=True)

# -------------------------------------------------------------------------footer------------------------------------------------------------

media_text = """
        <style>
            h3 {
                color: #f8f8f8;
                padding-left: 10px;
                text-shadow: 2px 2px 8px #CE4BC2;
            }
        </style>

        ### Social Media Links
        """


def social_media_icons():
    icons = {
        "LinkedIn": "https://www.linkedin.com/in/your-linkedin-profile",
        "Twitter": "https://twitter.com/your-twitter-profile",
        "GitHub": "https://github.com/your-github-profile",
        "Instagram": "https://instagram.com/your-instagram-profile",
        "Facebook": "https://facebook.com/your-facebook-profile",
        "Discord": "https://discord.com/your-discord-id",
        # Add more social media icons and links as needed
    }

    icons_html = []
    for platform, link in icons.items():
        icon_html = f"""
            <a href="{link}" target="_blank" class="social-icon">
                <i class="fab fa-{platform.lower()}"></i>
            </a>
        """
        icons_html.append(icon_html)

    return " ".join(icons_html)


# Additional Contact Information
contact_info = """
        <style>
            .contact-info {
                font-size: 18px;
                color: #f8f8f8;
                text-shadow: 2px 2px 8px #CE4BC2;
                margin-top: 20px;
            }
        </style>

        ### Contact Information
        - **Name:** Shubham Pal
        - **Email:** shubhampaliitr@gmail.com
        - **Phone:** +91- 7988192771
        """
# st.markdown(contact_info, unsafe_allow_html=True)

# Copyright Section
copyright_text = """
        <style>
            .copyright {
                font-size: 16px;
                color: #f8f8f8;
                text-shadow: 2px 2px 8px #CE4BC2;
                # margin-top: 20px;
            }
        </style>

        ### Copyright © 2023 Shubham Pal. All Rights Reserved.
        """
# st.markdown(copyright_text, unsafe_allow_html=True)

# Styled footer with social media links, contact information, and copyright
st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">',
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
        .social-icon {
            font-size: 30px;
            color: #3498db; /* Icon color */
            margin: 0 10px; /* Adjust spacing between icons */
            transition: color 0.3s; /* Add smooth transition effect on hover */
            text-decoration: none;
        }

        .social-icon:hover {
            color: #e74c3c; /* Change color on hover */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display social media icons and contact information in columns
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown(media_text, unsafe_allow_html=True)
    st.markdown(social_media_icons(), unsafe_allow_html=True)

with col2:
    st.markdown(contact_info, unsafe_allow_html=True)
st.markdown(copyright_text, unsafe_allow_html=True)
