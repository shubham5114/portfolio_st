import streamlit as st

# --------------------------------------------movie Recommend----------------------------
project = """
            <style>
                h1 {
                    color: #CE4BC2;
                    # text-shadow: 2px 2px 8px white;
                }
            </style>
            # My Projects
            
            """
st.markdown(project, unsafe_allow_html=True)
movie = """
            <style>
                h2 {
                    text-shadow: 2px 2px 8px #CE4BC2;
                }
            </style>
            ## CineGenius:   AI Assistance
            
            """

st.markdown(movie, unsafe_allow_html=True)


col1, col2 = st.columns([1, 1])
with col1:
    st.image(
        "movie_photo.jpg",
        caption="CineGenius",
        use_column_width=True,
        output_format="auto",
    )

with col2:
    with st.expander("Description"):
        st.write(
            "**About:**  ",
            """
                CineGenius is your AI movie assistant, always ready to engage in conversation. Whether you're looking for a movie recommendation or simply want to chat about your favorite films, CineGenius is here to listen and respond. With its speech recognition capabilities, you can talk to CineGenius just like you would with a friend.
                Not only does CineGenius listen to your queries, but it also speaks back to you, providing personalized movie recommendations based on your preferences. Its extensive database of films ensures that you'll always find something new and exciting to watch.
            """,
        )
        st.write(
            "**Tech Stack:**  ",
            """

                Frontend: Streamlit, HTML, CSS, LottieFiles""",
            """

    Recommendation: Machine Learning, Data Mining, Cosine Similarity""",
            """

    Live Chat: Speech Recognition, Text-to-Speech, Speech-to-Text""",
        )
    st.link_button(
        "Project Link",
        "https://shbhmpal.streamlit.app/",
    )


# -------------------------------------------------uber price---------------------------------------
uber = """
            <style>
                h2 {
                    text-shadow: 2px 2px 8px #CE4BC2;
                    margin-top:50px
                }
            </style>
            ## FareCast
            
            """

st.markdown(uber, unsafe_allow_html=True)


col1, col2 = st.columns([1, 1])
with col1:
    st.image(
        "taxi_fare.jpg",
        caption="FareCast",
        use_column_width=True,
        output_format="auto",
    )


with col2:
    with st.expander("Description"):
        st.write(
            "**About:**  ",
            """
                FareCast is a go-to solution for predicting Uber prices between any two pickup and dropoff locations worldwide. This advanced system harnesses the power of machine learning and data analysis techniques to accurately forecast the fare for your Uber ride.
                With FareCast, you can simply input the pickup and dropoff locations, and the system will leverage sophisticated algorithms to analyze historical Uber ride data, considering factors such as distance, time of day, traffic conditions, and more. By processing this vast amount of information, FareCast generates precise predictions, giving you an estimate of the fare before you even book your ride.
            """,
        )
        st.write(
            "**Tech Stack:**  ",
            """

                Frontend: Streamlit, HTML, CSS, LottieFiles\n""",
            """
    Location and Fare:  Data Mining,Machine Learning: LinearRegression, Geopy, Haversine formula
                """,
        ),

    st.link_button(
        "Project Link",
        "https://farecast.streamlit.app/",
    )


# -------------------------------------------------home price Prediction---------------------------------------
house = """
            <style>
                h2 {
                    text-shadow: 2px 2px 8px #CE4BC2;
                    margin-top:50px
                }
            </style>
            ## NestNostradamus
            
            """

st.markdown(house, unsafe_allow_html=True)


col1, col2 = st.columns([1, 1])
with col1:
    st.image(
        "house.jpg",
        caption="NestNostradamus",
        use_column_width=True,
        output_format="auto",
    )


with col2:
    with st.expander("Description"):
        st.write(
            "**About:**  ",
            """
                NestNostradamus revolutionizes property valuation with its innovative approach, leveraging state-of-the-art algorithms to provide precise predictions tailored to your unique needs. By analyzing key metrics such as area, location, and property specifications, NestNostradamus delivers accurate insights into future house prices, empowering users to make informed decisions in a dynamic real estate market.
                Stay ahead of the curve with NestNostradamus, your trusted companion for navigating the complexities of property valuation. With its intuitive interface and comprehensive data analysis, NestNostradamus simplifies the process of predicting house prices, ensuring that you have the edge needed to succeed in your real estate endeavors
            """,
        )
        st.write(
            """**Tech Stack:**  \n""",
            """

                Frontend: Streamlit, HTML, CSS\n""",
            """
    Price Prediction: Machine Learning: LinearRegression
        """,
        ),

    st.link_button(
        "Project Link",
        "https://auth.geeksforgeeks.org/user/shubhampaliitr/?utm_source=geeksforgeeks&utm_medium=my_profile&utm_campaign=auth_user",
    )
