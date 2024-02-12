import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time

# ----------------------------------------------------------------------------------EDUCATION--------------------------------------------------------------------------
# --------------------------------graduation-----------------------------


c1, c2 = st.columns([1, 1])
with c1:
    styled_text = """
        <style>
            h1 {
                color:#CE4BC2
            }
        </style>
        # Education
    
        
        """
    st.markdown(styled_text, unsafe_allow_html=True)
with c2:
    url = requests.get(
        "https://lottie.host/f2c747cb-25b8-44b0-bac5-9dd9fb1c7cad/StSoiKgUOJ.json"
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

    graduation_info = """
            <style>
                h2 {
                    text-shadow: 2px 2px 8px #CE4BC2;
                }
            </style>
            ## Graduation
        
            
            """
# Create an expander for graduation information
with st.expander("Graduation Details"):
    st.markdown(graduation_info, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([2, 1, 8])

    with c1:
        st.markdown(
            """
            <style>
            .big-font {
                font-size:20px ;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<p class="big-font">Institute</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">Major</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">Degree </p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font"> Batch </p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font"> CGPA </p>', unsafe_allow_html=True)

    with c2:
        st.markdown(
            """
            <style>
            .big-font {
                font-size:23px ;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<p class="big-font">:</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">:</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">:</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">:</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">:</p>', unsafe_allow_html=True)

    with c3:
        st.markdown(
            """
            <style>
            .big-font {
                font-size:20px !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">Indian Institute of Information Technology Lucknow </p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">Information Technology (IT)</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">Bachelor of Technology (B.Tech)</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">2021-2025</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">8.5/10</p>',
            unsafe_allow_html=True,
        )

    # --------------------------------HighSchool/ matriculation-----------------------------

with st.expander("HighSchool Detail..."):
    styled_text = """
            <style>
                h2 {
                    color: #f8f8f8;
                    text-shadow: 2px 2px 8px #CE4BC2;
                }
            </style>
            ## High School and Matriculation
            """

    st.markdown(styled_text, unsafe_allow_html=True)
    c1, c2, c3 = st.columns([3, 1, 8])
    with c1:
        # st.set_page_config(layout="wide")
        st.markdown(
            """
        <style>
        .big-font {
            font-size:20px ;
        }
        </style>
        """,
            unsafe_allow_html=True,
        )
        st.markdown('<p class="big-font">School</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">Stream</p>', unsafe_allow_html=True)
        st.markdown(
            '<p class="big-font">Percentage (12th) </p>', unsafe_allow_html=True
        )
        st.markdown('<p class="big-font"> CGPA(10th) </p>', unsafe_allow_html=True)
    with c2:
        st.markdown(
            """
        <style>
        .big-font {
            font-size:23px ;
        }
        </style>
        """,
            unsafe_allow_html=True,
        )
        st.markdown('<p class="big-font">:</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">:</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">:</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">:</p>', unsafe_allow_html=True)
    with c3:
        st.markdown(
            """
        <style>
        .big-font {
            font-size:20px !important;
        }
        </style>
        """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">Kendriya Vidyalaya, Military Station, Hisar</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">Science (PCM)</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">81%</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">9.8/10</p>',
            unsafe_allow_html=True,
        )


# ----------------------------------------------------------------------------------Experience--------------------------------------------------------------------------

c1, c2 = st.columns([1, 1])
with c1:
    styled_text = """
        <style>
            h1 {
                color:#CE4BC2
            }
        </style>
        # Experience
    
        
        """
    st.markdown(styled_text, unsafe_allow_html=True)
with c2:
    url = requests.get(
        "https://lottie.host/b15d82ad-8e1f-4284-a91d-3d932870f41d/BxtoA6AiPg.json"
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
        key="experience",
    )

    intern_info = """
            <style>
                h2 {
                    text-shadow: 2px 2px 8px #CE4BC2;
                }
            </style>
            ## Intern (3 month)
            
            """
# Create an expander for graduation information
with st.expander("Intern Details"):
    st.markdown(intern_info, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([2, 1, 8])

    with c1:
        st.markdown(
            """
            <style>
            .big-font {
                font-size:20px ;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<p class="big-font">Company</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">Role</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">Workflows </p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font"> </p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font"> </p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font"> </p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font"> </p>', unsafe_allow_html=True)
        st.markdown(
            '<p class="big-font"> Tech. Stack used </p>', unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <style>
            .big-font {
                font-size:23px ;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<p class="big-font">:</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">:</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">:</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font"></p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font"></p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font"></p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font"></p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">:</p>', unsafe_allow_html=True)

    with c3:
        st.markdown(
            """
            <style>
            .big-font {
                font-size:20px !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">Alphadroid </p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">Robotic Intern</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">Diverse experience in 3D avatar creation, OCR, speech recognition, speech-to-text, text-to-speech, and user interface design.</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">FlutterFlow, FireBase, JavaScript, APIs, Blender, Machine Learning etc.</p>',
            unsafe_allow_html=True,
        )

    hackathon_info = """
            <style>
                h2 {
                    text-shadow: 2px 2px 8px #CE4BC2;
                }
            </style>
            ## Hackathon
            
            """
# Create an expander for graduation information
with st.expander("Details"):
    st.markdown(hackathon_info, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([2, 1, 8])

    with c1:
        st.markdown(
            """
            <style>
            .big-font {
                font-size:20px ;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<p class="big-font">Company</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">Role</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font"> </p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font"> </p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">Certificate </p>', unsafe_allow_html=True)

    with c2:
        st.markdown(
            """
            <style>
            .big-font {
                font-size:23px ;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<p class="big-font">:</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">:</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font"> </p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font"> </p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">:</p>', unsafe_allow_html=True)
    with c3:
        st.markdown(
            """
            <style>
            .big-font {
                font-size:20px !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">Samsung</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">Completed the Samsung Innovation Campus Course and Hackathon 2023</p>',
            unsafe_allow_html=True,
        )
        st.write(
            "Check out this [link](https://drive.google.com/file/d/1YHsw_3ifl-4eAV4GqSujT4EQvUnLP7t7/view)"
        )


# ----------------------------------------------------------Programming skills--------------------------------------------------------------
c1, c2 = st.columns([1, 1])
with c1:
    styled_text = """
        <style>
            h1 {
                color:#CE4BC2
            }
        </style>
        # Programming Skills
    
        
        """
    st.markdown(styled_text, unsafe_allow_html=True)
with c2:
    url = requests.get(
        "https://lottie.host/fee48517-e1e4-4601-b10b-b446042b40f7/6dcPZBciIC.json"
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
        key="programming skill",
    )
# --------------------------------------------------Language------------------------------------------------------

language_info = """
            <style>
                h3 {
                    text-shadow: 2px 2px 8px #CE4BC2;
                }
            </style>
            ### Languages
            
            """
# Create an expander for graduation information
with st.expander("Languages Details.."):
    st.markdown(language_info, unsafe_allow_html=True)

    c1, c2, c3, c4, c5 = st.columns([1, 1, 1, 1, 1])

    with c1:
        st.image(
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANQAAADuCAMAAAB24dnhAAAA2FBMVEX///9lmtIARIIAWZxhmNFVkc9alNAAV5sASpUAQoEALHcAVZtdltBimNEAPn/k6vEAM3oATZYANHpqn9cAPH4AT5e/zuDz9voAKXYAMHl0o9a1x9tchrTY5PKeveEAR5SpxOTV4vEcY6K6z+mNstyQtN3L1eOSrMqCq9mnw+PK2u7t8vm1zOcNSYUSWZg7YpNUc56uu86pt8s5drFOfa8SU4+drcRhfaSJnLhJa5nV3OYmVIt0jK6TpL68x9dgibYrbKlzlb5FeKwAOI6CoMNCcqkxYpp6kbHIKcy1AAANZElEQVR4nNWdYX+aSBDG1QgGBDRASjTVaEysjebUNNVEU9vmmuv3/0aHokZ0gZnZXTDPm571V+Tv7izz7Mx6uVwKanSavXo+X+81O400Pk+++l8N1TDzK5n+f37tZ31H/GoqG6K1DKWZ9T1xqqMa+QMZaifr++JQo64eIi2l1j9qbHk3ChtpGVzKzYcMrZZSjGTyVVS+Zn2HaN0ZjGDaCy3jLuu7RMkPJjOJyZ+DHym0vNvoYNqTcutlfbcwDVjLeOQcVFpZ3y9Ad3kE0gorf+yhVQEFU1h+aFWyvu8YeU0FjbTCOuLQQgVTWIY6yPrumWpjg2kPK9/OmuBA/R5t5r3LVHtHljk143MimIpHZUqYBoOi4zElkQaDItU5htDq3/AGU1jHYEq+igimsLI2JQCDQVGWpgRmMCjKzJQgDAZFyk0GmVNL1DIepfRNyZ0pGWmFZaYZWhSDQVGKpsQPplSQVlgpmRIOg0FRGqYE7dYFYEn2+/1eOsEUlm9KJIaWEINBwpJmSoQZDIrkmJK2I9BgUCTelIg2GBSZili/L8FgUCTSlEgyGBQZhpjQkmcwKBJiSuLKgRmJ25S0lKOZee/iMyV3xSNEWsooUjOntAwGRURTkqbBoIhiSlI2GBRhTUkGBoMijCmpZGIwKIKbEmI5MPqT80Vjq2Je8MVBpkSowTAMVVXy9ZtmszUYDFqt5m2vbiqqKjLvSjYl4gxG0eepNzttRmLdb3eadZ9MVJIcb0r4y4GBTB/oppMw2xudnqoaYj4vxpSIMRimoTgtYNLZ+Jrf73GkKaoI2REy0Q3VaaGsXKWVV0V8lyxT4onIifxBuiUYg/atkLRZre+lGA0B35apGgOiKfBahoBZWFRD32iDf4Ew1TyXKe2Y/FimskPV5596RpHbZwsIalN9j2eHl0nQhrcAS+psrtXkvJS40oTHvRNnrJf2CucuhJEXWJ9t81bz1OCZ3+P6coRvc3Pl045y8ra8SINroIyi8DJ6g7wz4hR/lU+uuv41bnkGSu2JRlqqR8yqv5VLJyfln/4VeNJyRVKVb0CYPc63ko/k69TL3XFAqdKao9rYu3LU6wDp5OTsU65FXm2KeYmdUf08Jm9bBdNG5T/0tc+oy0Naqo74tlfBtFHpMVenMklZInbVA1I5jyc7SD7Ude5omXK5GwiVY1yXQ0y+iFBpMEGonPxOMHFCpcOUPAOdbwejRIaSvUa8K3a18HMiFhINysynxRTniljBRIcyjRTbC71IP8wKJjqUkmonKNsYbXMiQVBp98N3Dqkc5Z8YJAKUcZsuk28j9hYLp3gdPfNIUGkuEhs54VtgL+M8UEoGh9L6OxPQeYwLJhpUNme3BhsjsmMwBEKl9tQNq75a1x0zZhmnQ2Ux+ZYKJmByMFGgjMxOlrSMfYMhCsosctyW54vjn6tJyzgVSiX1znjtwW1dVVZS67eDNoGt//kcjoSDIqwSlVZdUY3iNn8zi4aq1AfI0PxzhRgmHBR+76hTZ+/4G0odkWtdllHDhIIysQMVe24HXCdp/zpFImGgkAOV2I8Basr2fl6B1zwKFGqgGpB+DNVJiq0vp7hgwkKhlr4WrHJhxrdYfjo5JwwTAgrzjPLgG/wHFfV3Nd5OaUhwKAOeyfZNxI5xscjeu/Z+I5dxCpQCfmQiK/0mc3dgckZHAkMVwRt96O4FBlX3+ow68zBQ4GWiQvg5lL3cv/JIWcYpUECm6B2tOKrQnhs2JyJDFaG7LXVSN9BOsjI+x+ZEZCjo7KN2ZGy6H7q/zviRoFDAta9NLvQryxys/5k3mFBQwBTJJBf6l8/2L/zBhIEyWiAmevnY1+8TAcGEgVJBu+cevcvEMa7FIUGhQAPF0bcF3PoSCgUKKfJAxVcwZEEZoJYqYkQlVTCkQYE2FEjdojHlwLVKZ4HYMVdevxu+BgQKtE6gG29W+pYUTKXSp0CXLKryn+DN7muICgIFevTuV5EAggRTqby+foW1/3J2uX73c+jLAU0/0OxDI4GCSRoUZPGrIGdfqEUqA6jiDQCqgxwpaAVDFhRoRUeFlPMNXMGQBgXZc6nDF3RgOVAyFOQxBQ4pcDnw7HSlqw3Uv8HrYGUvBy/+3UA9XgV/UQJDARwiPEeCBtNZoxJo8xHrl6vnVflPP3i1edisX/aDOQCAgthe4OKHKAeeRjwcu0tvfP4l4j7gUIDKQAMClZwTfTgodr/hx4Zy3r4jkD4ElPNY0LT7fz4WVPxC4RjfrYIvDJZsKMDq149Z0p38f65WCKR9h2JJhuJ8+Dpv2gZpJWBolUrllc7XH1C5Cl4HbmX95uk2ozjfeVNYmhR1zt95vLcKIUHnYCnQNk26Wv/F7rs7adLumxAoSPPODXMT3THne0jY0JKV+5mQ6sCAkaU7+TdXO2RChVamJpGxpjuvGhsJFVqyRsoEQB2sFMtgimGCzkFpI6VAoHqhoHLM/9wYIvgclAalQvqjwifm3mJH6X0OJmKVSqumOs9rsKDOL4M3KbtJoJLbO5TzWmCseUwlz8HSVSB2h9L5+t1wqgyCAjVkbnYpNjkRTLiEECgIlAnqNwjOLyyDCTTztlTw5V0oFLCUszzd6ACDKSycKREFBeqkbCj+Mk5A8ker8A+861cUFPA3HXuYYNrDur/matwhQIH2aP2o0knjtJLuVd7wLZg8UNCGl0mVymRP/H9+WRJU+AVCAVtNh8T5Zw2Df0/sxKRBwQqkuZyHW87fB2q7KUnqmaVBgfsyZxcUpovuzhUEdPJAu8ig5xDHBCr9IXwJdB86EQo6//zFQkcz/di/Bm93HLTdFNrw51Mhx+picngNzj5GcGMwvIN7fIFYLbSLMfMiXB2n4L50RK991wav7JbdjboKR28wvNkecWTZG9qgwdLsYUw3A72LGwwFTJU2X7MOGCxLZ4TTriqvtH57+FkPBfdbhKOkRNDSR8lXpJ2MgENhj2J3h3rM3ourDyOjKSRK5oQ4FIYbKl+zaY0dW5Zdm86gVyGcNkJA4aIquKGHoW67ITNsubb+/IA6lzjDngvDnEkk/WaDt3h6tvVa1fZVren289MCf9LyEl4rxkI5PwlQAdmsu/DVrZBPxaI2Z+BQjjHfyzxT1NjGbKVBoYJyYDWr/0Oti6mUQKHWFQxrmg3TNHg4QLfSQFDv5UB9kQXTYm1noNu5AKhQBcPOYALubBLAsBKh9sqB7nP6UKPdPBISWklQB+XA6oFPla2DjbfE0IqHcj4flgMvYDmbMB3u5STOwTioiHJgumHF3HVLwIqBiqpgWPM0oVg9C6s5GIMVCbVskWJfruCO0mMaRduXaKoIqPhyoP2SFtOLHX0X0XOQCbXbIsVU9Skdpqda3F1EFiFZUIByYC0Vqh/JG6PM5f0QClYO1FOgAjCx5+D+r5f5BgO2aSd/rOLnXjRW6TrXQwXTjqqSV4sXGFPhIHMqvYaOR+73G8bLlrqyj2LWvUPthlb5d+5uC3XYb5ggdy4tt/Dmia1NIe3OwfPL7YEGdr9hvGJ2wvmE2I0/xLrqr3+tP7rfMF4XUnL2H6R65Dq0Ssvf61+2fzmvkTlRgqrPwqeg94wKp10tQytol3NYBgMsyxbs8Bf4qbfVag6urnL3HReU+9JHAgfLG4FXcjaW+ym4ELX7YSOrKmw/cFLl+4IL1ma7oc/35fiy50KWwe4cVqyLUW1bxViQVptdafqI++c0Z88cvU1rXewEOL5P4ECWPuXCmo0gxccEhUuT2D4BNtaIPAm7zwKQDroXFrwRusKqzSlLhje5rwlAcqsHDxdvyj+jl/X26gtyuBZR9UbkJ+tT1pNlNq+KuLhVdV/Az+PFi10VMEh+ZjOPqreOXQFzsLCcCPpokljUnU2edZueyoQ+0GX3zQR6EhGvS1luzR4+jWfMZMObjf8OqzVX1Gcl7S0k9z+ApWmuXdO14fRp8rBYdH0txg+Tv9OhpVdtF2NH4z8G8oj0H+uCPm79oa7rLovYvvw//BeiaAJBk5kHW0xopSDXhj9D/l4Imu5yZV38xRiEioA8TLa02jM2MVvci3gkypNm31Pc6aR2xKHl1hLa6qLkvYh6aomWpr/Q3fZsWDvCOajVhuAeNKYW2rGFln9D/Fs9P44rtKyakK1GMaZEjCIMBkViTAm/tGiDQdHYOoI5GG8wKHqKa/NNQ4kGg6K+OFNCkIg9OKa6c/LxPF4J2i1l6kGQ30fKdeX2uWZgSnyDIRUpJ9Tvg6TpaINBUTdFU0I0GBSlZkrIBoOidEyJxWMwKKpINyXcBoOiRUFmaAkxGBRJNCWuGINBkSxTItBgUCTD72vVDIIprLEmeA66lmiDQZFQU+Km0R0JUV9YaGmQE6VpaSbGlFQlGgyKBJgS2QaDIk5TkoLBoIjHlEhz6/zqfqdlTr7BOK5gCovUBZaqwaAIb0pSNxgUVZ4xmZNvMI41mMKCmxLNLmRjMCgChlaGBoMiP7QSBytjg0FRkinJxK3za6HFNLe42jEYDIqeonoTpVQw0hLblPjBdDwGg6LZfD+0BJcDs9Firm9/5UWzXH3+UYMprMpkGhxz1O6nkzTyh/8BXVeuiN53p+AAAAAASUVORK5CYII=",
            width=90,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                    padding-left:10px;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> C++ / Cpp</p>',
            unsafe_allow_html=True,
        )

    with c2:
        st.image(
            "data:image/png;base64,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",
            width=90,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> C </p>',
            unsafe_allow_html=True,
        )

    with c3:
        st.image(
            "data:image/png;base64,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",
            width=100,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> Python</p>',
            unsafe_allow_html=True,
        )

    with c4:
        st.image(
            "data:image/png;base64,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",
            width=100,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> JavaScript</p>',
            unsafe_allow_html=True,
        )
    with c5:
        st.image(
            "https://logowik.com/content/uploads/images/731_java.jpg",
            width=130,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> Java</p>',
            unsafe_allow_html=True,
        )
# --------------------------------------------------Framwork------------------------------------------------------


frameworks_info = """
            <style>
                h3 {
                    text-shadow: 2px 2px 8px #CE4BC2;
                }
            </style>
            ### Frameworks and Libraries
            
            """
# Create an expander for graduation information
with st.expander("Frameworks Details.."):
    st.markdown(language_info, unsafe_allow_html=True)

    c1, c2, c3, c4, c5 = st.columns([1, 1, 1, 1, 1])

    with c1:
        st.image(
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAA8FBMVEX////kTSbxZSnr6+sAAADkSR7pdVzrWSjIyMj39/fkRBTr8PDwXRbxYiPnp5r4u6f3sZnyek/pzcfkPwbwVwDj4+NVVVXnnI3lZEn97enAwMB6enq6urqnp6flak7jRhoiIiJqamroVCcWFhYuLi7iOADxXxvuXyjqfGXytar41tDwqJr1xLv65eHmXj398vDtlIP1l3frg27S0tLmWDT0iWTmhnPr39zzvbTpx8H52dL60MPul4b5w7Lmi3norqOSkpJERESUlJRQUFA/Pz9xcXHqURTycz71lnXscEz2oojq19T4tJ/5yLrzgVXs+vx+gb60AAALT0lEQVR4nO2de1vaWBDGgxKVgLY1WHW7Ne22UG+AWqpWLXYvra697Pf/NpsQAwnMDBnynpDy8P6zNg+c5Lfn5OTNzJyDZen0eznS88GxwaHyVuIT43qR/PjbeMsvks1Yzwf//E15jdkEJSx/Hjb8PnZ4jgjLy4NG3s4p4aCRl/Gj80QYXX0lcXCuCMthE6/nmPBzcGgteWy+CPvfeTPXhH9a1l8E9BwRln9fHj1SEMLym0gjl1Z51PAB8GVwjCJ89Xz0SFEICW3FPzokfJFoQmxhQWheC8KYFoTlN2/j3331av4Iy/E3pvLakHd+CONvvc+teezD+N+VOSUcWO6XFk+4liNfnPDtVqQMhNaX8K+/LYHw79dx/ZUfIXHJesLHV99liTCp178YYdjgS2uOCQOSf/p/zC1hJfra3BJaLz+H/51fwkgLwgUhSEPCN8QlM4RfEk1whCPN/DkjwuW1SO8HxwaH1irxj24NDifAYx+3mOP9Zt6v0XpvLbTQQgsttNBCCy200EK/oHb3Voqsvd3MhJ2GXWQ1Otk70SkVWU52QKs7awhRXQDhnj1rCkH2HoBwv9CE+wDCnjdrDEFeD0B4VOSpxjkCEB4UmvAAQHjszhpDkHsMIDwsNOEhgLBVaMIWgLBTaEKAabMsLOEfqxn1R4IQAWhhn4erSxm1Gm/NgxC2oaYGSmi3IYQrBSZcgRBibVtmwvh9CDFtlnUDNTVQQmcbQoi1bZkJ441BTBvatkEJIaYNbduwhAjThrZtWEKEaQuibUUifBdvDBFp81Up1EyTIHQqky8/jZCAmQkTpg0RaQu0gzQ1SEJ7B0QItW1QQoxps6wzpG3LSpgwbWcgwu2iEoJMm2VtICfTrITxtpwNEOFlYQkvQYSCbbMdrb7WtFpnCUGmTbJt9vmGVgdPtPqwzhJiTJtl7bK2zdmoaqU//UMzBpg0bdkTwI9iCb2b6rJSep+V6MMkIQpQIDzPgfAuTrhqhpAD9E1FDoS1JY6wBCNk08B2OwfCOkcISQCH4m2bY56wkyBMmLZzGOEJS9gwT9jiCW9ghHwa2L0wTniVIEwMIEQCOBRv29xvxgl/1FhClGmT4onuR+0wVRM+YQndaxjhFUvoXBonfNpkCa9ghKJtM014zxLiTJuQBna2jRP+ZE0bJgEcigOcwrapCZ+xhDhLY1ld1tSobZuaMD5GTaRHQ/G2bcc0YYW1pUDTJlXvdZWAakLetEGq9iLxts0zTSiYthMgodK2Id/xr3hLgzNtUhqYsm3V221eR091umejNKAEcCidbav2XDbU5n1t6iRE2jAJ4FA621bdFgKs2eKlCUKcaZPiiZRtq97mQthAxRID8Wlgj7Bt1Y9CXjwToYkE8KN4wh5BuJkPIRLQYp/4pG37ZorQUKQtEJsGpqNtQm0DjBCWAA7F2zabIhQSjpkIjZk2qXrPIQCr7RwIQVV7kfgnHGXbqsJKIhghLAEcSmnbzgwRxhuCmja9beNvRBgh1LRJaWDStgkriXCEqARwKJxtwxEiTZs22lYVSlKzEBqLtPmq8C/5VLRNsG0wQg9UtReJvWJ7X2fbshAaNG3Cogsy2nZh5j40FksMxFfvkdE2j11evrquUoIwYdpQVXuRznW2bW+H07/PVFrnCMGmTbJtDV20TXdaPpYINm1iPFGXJNXNgNd8LBFr2sQ0sC5JqiP8xKdHsaZNa9tghEJ6FGvaxHiiLkmqI3zIIwEcSkgD65KkOkKhpg1r2ixltA1GyKdHsZG2QOzzkLRtKELW0pRsOCFv23S1bTrCdY4QbtrERRfmCDt8Ahht2iyLD73okqQqwl0+PYpaajHUDW9MVbVtKsKrPKr2IqFsm4pQMG2opRZDoWybipA3bcCqvUjXINumIvyeR9VeJMG23RojFEwbNtIWaBdU26YivOdr2nBVe5E67H2os20qQr5qz4HbUpRtq6oI+aUWeNMmxRN3NhVq7TKizpm4DY2sAI6LXw1suwrVOVHnzGOpxVCgvfeYeOn6HXFK3rTZeNMm2TYI4U/ilLmaNtjeewxh85Q45XUeSy2GAm3iwhE+EKfM1bTBNnFhCGvfiVPmatok2wYh/EGcMsdIW6AWZosTjpDqlHt+fSzellpWRSCkkkw6wjp1ybxpa4DTo6H4maa7Ny7OIHCElM/kTRtig+RxsVsm23v/jeeYLpjblhulVKckPmHctElbJncJ672lI1wiTthhbakR0ybaNuotgvkoTag1bdiqvUh8oZNH1bYxIWSGkDJtwlILdAI4lG7RBVe9RxM274kTCpE2E6ZNrN7bJAiZQc0QUqZNWB+LTgCHwlTv0YSkaRPWx6ITwKGENDARbeMWXTCEn4gT5mza1NV7zM5EDCFl2k5Z02YglhiIr97zTghCJkhOE5KmjU8Ag6v2BuIJz9IvumAIqUDUHU9oBlCIJyoWXTCE1Pn4SBtmg+Rx6dLAF/S7iIKQj7ThE8Ch+DSwRxBWNYSkLeVNGz4BHIq3bY1xwOWqYqbRmjbk+ti4+Hgibdtch/jCOOF6s16nLI2wqQm6ai+SzrYtVy8ue92GMzK0RwibtfrdwzX5xp67aZtiixP/Rfjb7b7txiljhOu1+tLpDzZNlrtp09q2AeXy5sae63p2gtAfmrUPT0RrkmPVXiSdbUt05fLHm3Z4W64GdLXas6cTreVpngngULq1smOUF5fnpYbz1R+aD9dpXFeeVXuP4rdMTrfFSXBbbvQ+pc1P81V7qA2Sx8UBKrY4UdR5J+bcHCJtgRDVe6n/91f4SBt2fWxcykUX2QhnYNrE6r0tOKFg2kwkgEPpbFtGwhmYNkz1XmrCGZg2TPVeakLetBlJAIdCVO+lJpyBaRNt2+1/KRFTE+ZatReJX3RR6vYuA5MNI7x+SDzwDW2QPCYpDew5jZ3tzcmUKQhb33/Wa02B0BigsKykL9txS2eXF1WRcgJh58fpUn1kk/JR02YqlhhIBIy6sr39UehKgbDjD83RzqMI0SuA40r1y7l+V9r7t1xXcoT+0KzVm2OdR1gaQwngUMJ+F6OUje4J2ZUUoT8014mhyRACN0geF7/3HgHpuc7KxrfRrhwjvHp6xwxNjtBE1V4kbfWeP2C7veOLOGSCcPfThyY/NGOKN2ooARxqml+68Fw3/hgZEFb680oKujFCc6Zt6uq9/mPkce4JCVtPPgjzikxopGovUobqvegxEjwUTpupO48iNJMADiXYthTy5x57/+hZbeK8Mqa8TBvil3Ptr7rOIwhNJYBDZa9mn2rnj9wsjbBlcn6ExtKjobL/BFt2QpOmDbHoYirCHKr2ImlsG44wuXuSqQRwqOyLLrSE75I/xG3YtCEWXagIR+n6hOZiiYGyL7pITfhulW7AWAI4VPZFF6kIx4ZmnNCkaUP8cu5kQq7zHmVkqcVQ2X85VyaUOi8iNGraJkXbshFOpusTmgXMbkwZwglDMy7DhJltG0GYYmgOZTABHGql4WVjHCV8p6Drx/DMJYAfdXjTHqvkmpZQ1Xn9iM/ekdlnxaN2L88cd1rK1Wk7zy2dHBueRhO6OgoquaYlVMwrIZ2zf2D2MUiqc3xS0nflasqHQiR/aLaPzKVEJ6p1sO9OPWAnyp9XSr1chyatw+32dANWpguSArMYmrQ6x+dOphl2FM9pdG8OjVWvTanW0YqD6Mowz2oyJppBneubUrau9NzGTj6PvOm1ezBS9qzovEbpvADzShpdHe0o5x5/XnELNK+kUee4l3rA+p3XvpnhI296tQ6CuUem9OcVr7DzShpVRKPuzys5WWmz8o06MfcECfB8rbRZ+Ua9MZx7fDp3JlbarCrHJ92gKwMrvf1Lzitp5A/Y3Ifm/8v/wOysXxQKAAAAAElFTkSuQmCC",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                    padding-left:10px;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> HTML</p>',
            unsafe_allow_html=True,
        )

    with c2:
        st.image(
            "data:image/png;base64,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",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> CSS</p>',
            unsafe_allow_html=True,
        )

    with c3:
        st.image(
            "data:image/jpeg;base64,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",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> BootStrap</p>',
            unsafe_allow_html=True,
        )

    with c4:
        st.image(
            "data:image/png;base64,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",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> Streamlit</p>',
            unsafe_allow_html=True,
        )
    with c5:
        st.image(
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAAA81BMVEX///9LOe8fEZ12br89LNUsHbZ7cNf8/Pz09PVMO+/39/jq6u1WRfDf3+RTQvB4cMCloc7T0t1mWeXGxNnp6etgUegpG6EiFKMpGrC1stE1KKcnGaC7uNiOh8qIgcexrdKHf81VRerW1d3PzdxfT+t0a9V+cup8csqemdFvZNl+ddRkVuSYkdlwZeJ3bN5pXOOLg+GUjslyY/Kcltaln9iuqte9u9NdTueDesVSR7GVkrY3J8pKOtpzba5oYadgWK6qqL1DOaGIg7g6L6GGga2hnr6PjLRkW7NGO6F+ebVhWaZPQMuZlMRpXd5OQ7JWTae4tsWyVJHEAAAEbUlEQVR4nO2ciVYaQRBFe0ZghlWRsAgaGdTEiGsWDSQqikti3P7/awIoSdygY17Ny3jqfgH3NNVV3V01xiiKoiiKoiiKoiiKoiiKoiiKosjjz85NToTA5Ov5tKBGup5xQiO3lBXzaIan0SfIC3kUw/VwnExDRKQetofjLEl45JPhiyQX8B7pxfA9HOc1XmSO4SHw32oEFJE3aA9vg+LhvEWLzHM8nCmwhx9wPDI+WISQQgYsgz0KJI8AvSDvOB7wdLjN8XBWwB5eyEXvkAy6jF/leMC3Xkax2GfNw3qk1jgeSfSpaorj4ayCPbIhntL/ZBr8xzIJjoezDfYokCIdnUJoxSL6UmuL4wFPIY0cx2MxhfXw1jkezgzWg3Ys3ABvvX7oN4s3BOhicZPj4WyBPVgp5D146/VJF0A5dLH4gePh1MEerFNI8Aoswkoh82CPBdKCJMAerAWBXwClSUXWR7AH6yariD4Wmk8cEfSx0JgZisc63IOTRXYEeh28HYII+lg44HP4HhvoN4QB2VjYHvDa5JZWyFECL3qHtMtfQtRIrgi0ONzgl9xyPIbia2IUK+diDU09dl0kMm0+VjSgIns8EbOPFClJNvaNoYMUcds8kXQJKXIAL2ztOUSKMMMduyT7PBGzhxRxxVLeeK6hIoc8EXOAFOmCHz3+hmOkiHvME/GrSBHmDnyEFGGGex4qwiy4oOFeFTnM2lFAijDD3VwiRarEHRgb7h2eSBYqsssTMWdIEeb5CrsDn/BEzClSpEXcgbFHXuIOnK4NfkG5Ev9XKmXX/cYTMd97GnHMXXCs4krexY3Br7m4K+0YM9zPkFfzP4jF/DnQA99VZo83DRVp0goudJN/geQBfxg9J4ksgT2cOY4H/skd3epnh0CTP76/wQZ8k3+GsmsJdGiK9AWMQ6DJH92dbMcy3CNJySJZfP/ZGsPDw0+E7lAergSa/DmRjm/yv6BsvQJN/pQSXqD1N8HYegWa/Bcpd0ECE6Ho7wVYkRdIIZScju8pz1FSiECkU/5Y5gLuAf8yiBX4nM4pFgUmQuGDIVbgv+cC/xCFFQLHQsqFg49vjOekEIHZb86xEH8BtMnw8PEppPlSisVZhofAx/8uGB4Sx0JKpAsMINYZHgIDiAGna6MNF0FPEVuCfffs0SQ94qKfdTjFYo8suF4U+KiqJdjr3iKvPwv6hpvkvLLdcAoU4dw33NKpoDpPisz1MCZVdeMxm/9XciRBYobYGzvAbkShS2x0t8S3mUiqSY3WIrGYSOoSR7/sWRjrUYrCehjjjRtRiMZ6mLHhXoqKh0l1X8R6mNEjCrUIeYwK9xqrke95tJ6Mj2jsV794aia0+v/n83s8Hu6XxH7wZ9J+9H8VPY/hiELU16PH1QOPbiQ9Ho6/tKLp0T9f3d2vIupxP7u3hD5RFAJ3wr0bXY8739y5iuz/qs/v7B7d+BjgDWdCq1Gqdx/lZHANMRHl+Ljl+mj3sEOc5VQURVEURVEURVEURVGUl8dP0mxzZyNiyLAAAAAASUVORK5CYII=",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> FlutterFlow</p>',
            unsafe_allow_html=True,
        )

# --------------------------------------------------Libraries------------------------------------------------------

Libraries_info = """
            <style>
                h3 {
                    text-shadow: 2px 2px 8px #CE4BC2;
                }
            </style>
            ### Frameworks and Libraries
            
            """
# Create an expander for graduation information
with st.expander("Libraries Details.."):
    st.markdown(Libraries_info, unsafe_allow_html=True)

    c1, c2, c3, c4, c5 = st.columns([1, 1, 1, 1, 1])

    with c1:
        st.image(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgWpP1RPGLLVlsxRPUBy3qqiyeAVoay_Ezag&usqp=CAU",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                    padding-left:10px;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> NumPy</p>',
            unsafe_allow_html=True,
        )

    with c2:
        st.image(
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMIAAAEDCAMAAABQ/CumAAAAeFBMVEX///8TB1QAAEb/ygDnBIgPAFLNzNYTAFnQ0NgMAFcAAETb2eP39/oUBlfV1N7/xwDmAID/9tfLydcjG17/4Yz//vbCwM3ykcL61OfoBIwyKmgAADYAAE0AAErx8PTIxdT/+un/34T85/Lyir/lAHv50eX+9fkpH2Ma8J+4AAACEklEQVR4nO3dzVIaQRSAUYNCEIGoiYmJivnP+79hFrmLVHELZ6pnmG483xqaPruh5lb32ZkkSZIkSZIkvb52z7dZU2+rT4uH2X6rx6m31afF7M1+87dTb6tPCDWEUEMINYRQQ5MS1tu0nqtMSrhKn26e1v1WmZawyn58g4DQL4QIoSyECKEshAihLIQIoSyECKEshAihLIQIoSyECKEshAihLIQIoSyECOFA6cvM5a4nYb29yjoO4WmVvM58WPQkbF8e+RqPcDlPVp4t+xLS/W0QEBCqI8yTLpsizN8n/WmJ0CEEBAQEBAQEBIT2CF+/fci6a4hw8y7rvC3CeRYCAgICAgICAgICAgICwlCEtJYIdzdp/3+kdkKHToFQ+RjJMCEcCKF7CAdC6B7CgRC6Nylh9zGtJUJ6uNCsnsOFhhkvPAHC9x+fsloi/Pp5nXTREuH++iLpMwICAgICAgICAgICAgKC/87R7/u0lggdQkBAQEBAQEB4dYQON67UTqh9KuwkDlRBQED4R8gOF5o3Rdh8yepLGO0ez6MNPO+WQ9w3NilhvBAihLIQIoSyECKEshAihLIQIoSyECKEshAihLIQIoSyECKEshAihLIQIoSyEKJt+lL0SNeADUR4TG9cGWXHew10AkPP4aRBO9ohEuOFUEMINYRQQwg1dAKEDvd41t5t2u7lL0qSJEmSJEnSyfUXeomSFq0EzbkAAAAASUVORK5CYII=",
            width=90,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> Pandas</p>',
            unsafe_allow_html=True,
        )

    with c3:
        st.image(
            "data:image/jpeg;base64,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",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> MatplotLib</p>',
            unsafe_allow_html=True,
        )

    with c4:
        st.image(
            "data:image/png;base64,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",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> Seaborn</p>',
            unsafe_allow_html=True,
        )
    with c5:
        st.image(
            "data:image/png;base64,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",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> SciKit-Learn</p>',
            unsafe_allow_html=True,
        )
# --------------------------------------------------Tools------------------------------------------------------

tools_info = """
            <style>
                h3 {
                    text-shadow: 2px 2px 8px #CE4BC2;
                }
            </style>
            ### Dev Tools
            
            """
# Create an expander for graduation information
with st.expander("Dev Tools Details.."):
    st.markdown(tools_info, unsafe_allow_html=True)

    c1, c2, c3, c4, c5 = st.columns([1, 1, 1, 1, 1])

    with c1:
        st.image(
            "data:image/png;base64,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",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                    padding-left:10px;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">Git / Github</p>',
            unsafe_allow_html=True,
        )

    with c2:
        st.image(
            "data:image/jpeg;base64,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",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> Vs Code</p>',
            unsafe_allow_html=True,
        )

    with c3:
        st.image(
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANAAAADyCAMAAAALHrt7AAAAw1BMVEX////zdyZOTk6enp52dndhYmJCQkI8PDzybABFRUXyagBKSkq7u7vo6OjzdiNBQUHx8fGampqUlJTm5uY5OTm0tLTzcxvzcRTJycn39/fW1tbycA7v7+/FxcVaWlppaWr+9O+mpqb849f97eX2oXX1lmL70r/R0dF8fHz0gTr1kFj6x6/5v6T71sV5eXn4tZT0iUyIiIj3pXv839H96d/5vJ/3rIf0hEL1lF/71cMrKyv2oXb4sY7zfC/2m2vyYQAlJSWYM4IVAAAQiElEQVR4nO1dCXequhZuqWVUPFUElapYp1q1dajae271vv//q14GVIYAAQJoV7+1zlmtDSEfe8jOjuzc3f3iF78goTVp9B8eGs3nogfCBu1ar1eC6PVeO0UPJj0qK8wGo1dqFz2glGg66SBK/aKHlAplLx/A6KHoQaVAx8/npmVUIfEBjG7WjlZEPgBFDywh2mQBARHdqPeuBQmo9F700BKhFSQgIKJK0YNLgkkIoZvUuUYgn1LpJj13P4RQrejBJcHDL6Erx4+zIV+gfcFternnEEL1ogeXCIGhXCHB3GAznn/s/h29LSHeRsPdx3y8GcTpIlDneuWsRk1C62W2+1JlUTRNQwdQIeAPhmmKomy+7WYbi66r9AJqVep/ktHAGMzWU8DE0NX7QOi6KcqH4ewzuruAcLs3oWTTKHFcl+vWklmcNRvqshlGxQEVsDKOsygN7BNXrJRr8AbXfUTocqtWXDaf2z01mYusTPnw8RLa7xMhp7CiG9LKpoModWOF54PtQTZikjlJyhDV7zDl88mo9xSfD6REb0qzZVI2J07ydG4Fdj/puSjRTqll7tFNiNKRDHaimYaNzckUh8Gq1yidKPV6DVpjcMsHMqJ5Eps3WU/NBkOXl+PA+7Qbtdf311qDPttT9hF67EVeNJ6KrOhAqOL9jHrAUXj18XnkIvwCoJNe1zKjxPkJdZthF2z2zOlgSodgxYuBPyRCjeD2gy85CzqY0jJ8ZsqC0I6ZKyBSkodWakYkQkFubqwbGdKB0MXUptQjOAVyRGeNMtM2B8RlrHWGH32/234kNhwz9dTB0OV5KkIVn86RTego50IHQnyz0jCq+UREaPSi5yMeDN38Jw0jrwURooxtHtbjgCrvUhB67jplxBFc3EjMlQ6EuYy9MLug9X5m1O365WMdsnbWJOg6xUI9EM0S1wXgHgn+YJNJpBMNVU4VCj03G40Oaf6Z5Ww+DsjbNIwCsM3PW/shpnENZOzydwcuRkfGfNbF8gHO7ospn2F8PqquGyhPiiDLsv2TaRqGHjfZBWC8seRjxiFioGzv/mv9vZ2NF5uXz4GFMfh82SzGs/n3erQ35KjsaoaMKPUNUIFEhh8zqnz8YDPb/rs3ZZE2OWmMGPH5juYDs7riYThfxI/4rcUc5cIpWJlDJnzmEf4aktGP802KCAVM2vOjHk2Kifceh/KBZNaR+XY6DMZrVTZDg/mUKySIl2A+qi6KXzQ7IjEwmH2JYoig5FTLCQArMMkLNGSdtncyFmsjeE0sptSGPblnIJv1hs3widiszQBOqpqq4yFpvaCa8nHBaOTBWBxlonboaaajGcGAdHE6s1iNOhStGTFxLn4k7nHg46Ma8jBLVfPiZUjYd5ITj+Dg6Us1zQ+L4XBpYH2YXs1T9YR97QwPHTX9LJAEs3vPUllPFgNtZDcdhjs3cTE7uCklSxOrzj5MvTg6EDPVpXiiFb8Lp8IZYhaL+niYm44BJVA6R8ijyutUgScrOHdw4ieCpicJq+KSbbiWHIO3synF9nTz0xpIN4s1HjfGxklIxne8K098xJGVycgSY3jKDsqxolTbI+gik+1bpljYKyY9ThrIjnlSbs9kBXvHIE4EdNSRcyveV5MxR2qnLqkv+JSRN2CwtZ4RPlX4xEXqNcwINDf2VoYjSo03E4hoT9kYCkhkkzHKDjuZXkTAguTki6i8ABaflFYEXJx8TZNpEP6RVZnKzHdG6lxRPngR6WJUUc4+A8IGLyJNuDD7L8+kQTp8yhQRnXEb+obx8l9kk0UxeYOk+CfSfd2OvmHc2nh/8Ytf/OIXV4wfUoQIo90vaZTvOd0EOEFSpJt8GToAXY7jfgldM34JXTuulVAr6dYYA0J/6p6bP9cgLt8/b3WaAJ5vPHceIC6/t0GTDp4QK/0er2mCUmo4X4Ct9xsAvlfrK+UOALpZs1wudyAhZdXsdM4fO+7Rf+8qSrfU9303vgyBfmq+89pfz/vhFU2SJO1y6z9/q9Wq5vlGek0AjQTH7xpoA18qeH7VJIWDUHjNWS5E4yWJ/+t9yfdJ43n+LxphSQA/4iurCJrrxehOV8AdK5LgfSlQqvK8Bof+KIAmVQ/higCu4h2E0O9eQhLUjcvvfQlfU9YwGwxJuvT9hK7wflMftla66Md355XoasfzeH4UEBkFc3JzvXsEn1WBCAX0V3aEGnd9DY2Er/L26LSz+CvoT113N21H3yXJHi4aNwC/crSDf+GF3moFBAVv4Xq3tgflcvcs4KuZEGpI8PE3waAVofvUaTZW6L6A0dn44F05oe7vRsBG/FR6f39FjLqlHsLZRusaUjX8svRzDf7GO2WECcH/FV4QfDaUiBAPjRmy6trdtdB9OYU7NelUPWoEAHtRXj0f+LxcC37KX8qUtasu2QPhAioSlLbQ61R8HjYRoTKPBs9VHQ+uiRjx5+eMRMY7e5nArgXnA+VJhKB1SU6JIIl13Q24V6ClxPoXyQmBZi4BdJBSa6cn9gCvqTa9vSjOS0iE2lCR3e/N9UE74dIT0lTwj1woIQUhxfMa/EpxXorcgkvBkBK6qnCQCEHb0DzzoOTqCZuetw0DQt4u/yAK54eL3IJ2UfEJsgXXm/MEQlC/FG9NB3j/qpuQFFQkK4UN+UpJIBFpJ01oVt09wb96hEogdJriXID3E87uGcYXXgfKgpDvtpjCxWwkl8CQxlXd1xAIQbkK3gIIsOPL7RSfu2FDyP+M0LWXASK3cG6F2AruCwiEYBfVeqXuRAXNe+d2JPtlQsgfY/Mu5UZuQTrlQKDGeRXfT6iOXGVVcENy9cuFmRBbQo/QTC5TSElxXIYE5AlT/ISQ5yDi0i/n85aZEYIMHP4V29Tk8rMntiMQ6lwXoZ5bQji6xgSRxnmjbz8hPCEIBGjnB5UjIbQCdRCCPtieigSnRw8m1EAfVZ79qJwvTkDI+yhpCVU9A3zWTk8HqpIrbAgjVPW2cyMeoZbgu0kQIV8s9ezpyzYq6GHh7F71laMJsCEhPN2dgJDiqRO2UkiEfPMQHo3zY+QKNDA+zd1BICG0BqyGF3+KRwjdxBPtoi6cc3NApICjU9dHdrwKiRHGEDCx+nUzDaFHxWcf6LH5YznvZI2DU7dwoVsAQR/UWc1f0QnZnHv3AUWehKbJCSF7cT99NEE6pWY7V88Ca4VCHffcidyCcOePSxEI6o1WgcGBTQJC9tTmaNJAn/gJcZxLjhON8ysrXn/CqI5kGJz3VgBdpKVhFXRjEmrhVM7lufVxeoVASOk6GGG91LxpQfzEiS7BNjqPTNvo/kIIo5iEsOZwkl3ztd2rAi5EQgqnSOfHjlNavL+MIpYCeQRlrA1u/19DH0quaiLtlcN3hhOq+wghtUcJqtfVqwJTZApi7QjE7AUeVKRuv9lud2oSfgqEGjp9O8FFnFswIWHV7z89nqVdkuz7w67bk3K/xAuCY4RxCd01NPup4lSgAmYWwa3rdqTwiObbqlDl8aBJfLDv4xRy9fw+ZqTAdPSFccmOUCWUI+Ylz8KDgpBnLng4MUKXwgJ6yBB8hO56ztjYm7E9D08heMQTutLpcueE3HelmLF60xJqe+MviI5UtVPwEk7BoyS7n9BdQ+DPDR8DCinCNLfP+Z3xao9dcbmTeum0CYD+xmtdxwgFmNoP3DufeFIZpyGXJE3Qqr0+Nli4geFocwlOWw3UUOo9BFaxhUMKCWbaK7haUEp9t2uo9x/tZUO1u2q4Op8AeDd8PGMj3q/1HFjy1B1tt0I3vNC8poQ0CAbMLFTiljDuuzIZlAhaPpCABBRSJZE1UOwUsQDxIQahB1/+N2Og+1FWFT6DnhCKh4QcC83jbFloIVACqAmhSSHYxWUA7BfjXkVLqI7mqaC0egaooNA2vkZQEiqjCbqa2xcRKk9oLzN88UEEFaFKCa8LczoIYNLjBDsIjF+snoJQe4VDAMWbXMwKbTte46NqHZNAQcheRRHj1UyAEwCSkOhsOQpCOOsuhKc7mAJ+GaTbT/YtncZfEGT9L/xaKH0pz5NOGuVJ4pMeWig3G96mpnE5Bjw5oH6zh/BdI6yiBxATVlQDxsW7soYV/b56kvolxcGwIpvs9Og2V4MpRbXQgXywMh8IIyypaip8GfdWxgNhhL0xpWm2EXWdTY3CbGFNaQv171VVvN7iECcMVJ22eN5YTFsROgfAWtkm7UvEsAwbzVvWBQLWylYN2tZjWJbFZFmblzVQbVyTvggMqiOlq9dqSNYelh2iF9Dd3UK8v+I6OPZBGrFqXC1xdSNxaWU1quSwD9JQD3Eu+rSLsTE4koUxFqeDNOir+iD8e6oSlvpIFqZoHU+1vuKWO7XOJan1KyqJM7vUPY1XvAxde662Z95fR1WPF8cRW2b8aXJ5qR/I5giqlLCOjnMn1Pv4HbjK0OrysVhTstxHbCUqRrt1Vd7X5WFxlKxv0VVE1lgn6sZTmhpQKibf4KWTSOFQR97i+7r8lX+RlsFa9tbIpiuJRYC/XD2sTc10uFFYEE6qTFFFllA/XDXNXV7GZG3vCQW3U1UQnxJqkquGvMxDTOMR8YxXVU9TFtdnRicxycdsl7SbtRhQtD6xAWEsgk5J0E3xOM6ohPAm5FiB1LX85sHnjABOb3PW9mTNjmbIwQ9m+rM51mEn2+imfL8eW+l5YCy+p+FHcxgsTiH6Cj9aTYUHYa9T5/gH4++9LEac9KzTFgINxzLybEJ0uM3b9zgZq8FiOzJEM/rYaj3WIjUEU6rTFtFBStPhx/jFouzX+hxv10sTCIbqBCJVpe04Cq0D9fmR6HwoWZyO1h+zfzafFmEI1mCzmG13x70uxzojSqXYOqGFRc/oxEtH53fBo7v0w3S/hNhPD8De0GFeJjzGK945XqrJ0qHGZuQciRPJezEYTxB0dpQZdGb2c8ayiIMxz3ymzPnc3R2LO9vPpK8VHgffRZ0mmVmt7ILO+8wwMfhi5O8a1Jg533iwljEOYWQC45Dx+vg7X7WTsy81v8nxHO2cDtI45iWk3LanxuHnIzJCrntTw8yFpIpfVn58gCUdsnV3hp77FyXmYnbBXTGbbK2dP0vLiM7QKoAPgDXMgJIufxX4pcoBa0qATsGbhYMdMQOdCPCkyiv4ymtrqwafBxsDupj/SZVBWIzIZ6fGEs5bLo660p5MJu3ot1as+T656qmGeNjmsek0aTzZqPUnkTsNg21EYpoMmEn+yMNyWp3a08MFT7Vy9OaJNRuJlGlQTMYQxS/mGxhktJ+cdDClgLfS3XiZj3Q5MiOKMqzm2za3TeiGlw6iRPvSzGD8MVJF0UQJUjcRwATmwPXEqf1k6JP4AEZx3nJsfY7n38e3gwlzv6L93+HtuJvTp/NZIYAPQLL3Ni0MtoOMAaK+xdS6a0I7mA9gROUZrgthfACjqzg9Nw46EYTyfN2RCcL5AEZFDzAmQi0IEbqxdx4bEXweHm7M0UUJ6NZ07pmCUOLXkotAnYJQfmUrGCDSJ9yaV5j8NEI/TkI/zoZ+nJf7cfPQz4sUflwsd1f7WRoXvR6KWw6seEQQKnp48RGeU7g1C4L4aVmfkLxcrEzjNYFF5vS6kC63fY2Y1Hy7DzfpDy5old37Q0+dm8swetGa9E87eE8UO3i3gUp70qTZY/1FZvg/XddyAWqutWgAAAAASUVORK5CYII=",
            width=100,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">Jupiter Lab</p>',
            unsafe_allow_html=True,
        )

    with c4:
        st.image(
            "data:image/jpeg;base64,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",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> IntelliJ Idea</p>',
            unsafe_allow_html=True,
        )
    with c5:
        st.image(
            "data:image/jpeg;base64,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",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> Canva</p>',
            unsafe_allow_html=True,
        )

# --------------------------------------------------Platform------------------------------------------------------

platform_info = """
            <style>
                h3 {
                    text-shadow: 2px 2px 8px #CE4BC2;
                }
            </style>
            ### Coding PlatForms
            
            """
# Create an expander for graduation information
with st.expander("Coding PlatForm Details.."):
    st.markdown(platform_info, unsafe_allow_html=True)

    c1, c2, c3, c4, c5 = st.columns([1, 1, 1, 1, 1])

    with c1:
        st.image(
            "data:image/png;base64,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",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                    padding-left:10px;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">Leetcode</p>',
            unsafe_allow_html=True,
        )
        st.link_button("  Link", "https://leetcode.com/lit2021046_iiitl/")

    with c2:
        st.image(
            "data:image/png;base64,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",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">gfg</p>',
            unsafe_allow_html=True,
        )
        st.link_button(
            "  Link",
            "https://auth.geeksforgeeks.org/user/shubhampaliitr/?utm_source=geeksforgeeks&utm_medium=my_profile&utm_campaign=auth_user",
        )

    with c3:
        st.image(
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAsVBMVEX///9PgcH/1ACuDwpHfL+ctNj/0QD/9typAADv3NxhjMatBAD/4XTTl5f/1zC0NDI9d72Co9Fpksm6y+Tc5fGnvd08dr3T3u5WhsPo7vawxOGhudv/9tP/7rH/1hP//vfZoJ+wFxP/54v/7az/6JT//fL/9Mr/3VL/31z/4Wz/5ID/8Lv/2z/57u3lwcDqzMveray/U1G6RkTJc3HQiIfNgYD/++nEZmX25+a5QT7CXVtLKWyXAAADgElEQVR4nO3daVPaQBjA8RhjDAQxAcJlBe8DgXJVab//B2s4qu10Zo+nQ5Nt///XZmd/86zgG7OeR0RERERERERERERE9F/UytJGVVUjzVpFb/IPanaTIDhSFwRJt1n0RoW1qjrdu7Lq5BybbUPfpraDY8xsgDkxK3rDtjUTK+DRUeLYFHu2wJzYK3rTVjVMP2Q+ChpFb9qmjv0I8yF2it62Ran9CPMhpkVv2yLJCPMhFr1t80SH1Klj2pcc0vyY9oveuHEXQuFF0Rs37kQoPCl648YhRFj+ECIsfwgRlj+ECMsfQoTlDyHC8ocQYflDiLD8IUR4qE4vb2rKRrefzFYqp/CyHoahry4MB3f3jgoffJ3uHXnrpPDG0Lc1Pg7dEz5ZAPMGOmLphDU7oO/XHRNe2gL98Nkp4b01MCc+uCQcCYSac1ou4VDg0w2xXMIXyQh9v+aOcCQC+r47wrEMGKr+eiuXcCAUnjojlAERIkSIECFChAgRIkSI0HnhZHp1pmz22Wnh7DyKolhZ/gPzqavC6XUUHxsUR4uKk8KlmW9nvHJQuIhMfZuipXPCufEA98SVY8KV1QS3xKlTwoo18DiOnRIuLM/odogrh4SCEe6G6Izwi2CE299EZ4TXImG8ckY4kRzSXLhwRij6Ncy7/ueFxwgRIkSIECFChAgRIkSIECFChAgRIkSIECFChAgRIkSIECFChAgRIkSIECFChAgRIkSIECFChAgRIkSIECFChAgRIkSI8ADCQ7xH+BB3q8v/H78uFL4qdtMXCvuKNdfCdyqcezWZUPk+704iEiYd1aKxiBgvBTcjbHtSbcYTCpVrvsnebTITXY2QH9IX5W5SyTENUuWaU9EMo4nnPYlmqNyM7JiqD6ns9S3xW/7gq+R+C911Og37IQYNzZozwRCj9eZJm2t09o01m/F69kNMerpFv1oPcfc6M8nlAfpLn5q2xKSpXXMSWxLj+f7Joe13ourb/kdZ2wrYzgzWrNgR8+/C9x5t7nsaqL7sP2raENv6CW5a23zaRPOfH70zJobP2gut9rWqpic1qbYM1/TeTF8NGUdnvz75WtPeurbhhY+Gl8tta3aTQPehGgRJ12yAuypz3dtLd28wXU5+e3T4MhrXlY1rt2YH9KNWljaqqhppZjy/fevZcnGu7Ntqql+GiIiIiIiIiIiIiIjob/cdbx3Q0gt9Dn0AAAAASUVORK5CYII=",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font">Codeforces</p>',
            unsafe_allow_html=True,
        )
        st.link_button("  Link", "https://codeforces.com/profile/kucchupal")

    with c4:
        st.image(
            "data:image/jpeg;base64,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",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> CodeChef</p>',
            unsafe_allow_html=True,
        )
        st.link_button("  Link", "https://www.codechef.com/users/kucchupal")

    with c5:
        st.image(
            "data:image/png;base64,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",
            width=120,
        )
        st.markdown(
            """
                <style>
                .big-font {
                    font-size:20px ;
                }
                </style>
                """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="big-font"> AtCoder</p>',
            unsafe_allow_html=True,
        )
        st.link_button("  Link", "https://atcoder.jp/users/ifs")
