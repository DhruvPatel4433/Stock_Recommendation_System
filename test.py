
# import streamlit as st

# # Custom CSS to add background image
# page_bg_img = '''
# <style>
# .stApp {
#     background-image: url("https://images.unsplash.com/photo-1517816743773-6e0fd518b4a6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDl8fGRhcmslMjBjb25zdGVsbGF0aW9ufGVufDB8fHx8MTYyNjk2Mzk2Ng&ixlib=rb-1.2.1&q=80&w=1080");
#     background-size: cover;
#     background-position: center;
#     background-repeat: no-repeat;
#     background-attachment: fixed;
# }
# </style>
# '''

# # Inject the custom CSS
# st.markdown(page_bg_img, unsafe_allow_html=True)

# # Page title and inputs for signup
# st.title("Sign Up")

# # Input fields for the signup form
# username = st.text_input("Username")
# email = st.text_input("Email")
# password = st.text_input("Password", type="password")

# # Sign up button
# if st.button("Sign Up"):
#     if username and email and password:
#         st.success(f"Welcome, {username}! Your account has been created.")
#     else:
#         st.error("Please fill in all the fields.")

# # Login link
# st.write("Already have an account? [Login](#)")


# import streamlit as st

# # Set page layout to centered (which is more mobile-friendly)
# st.set_page_config(layout="centered")

# # Custom CSS for centering the form and adding a background image
# page_style = '''
# <style>
# .stApp {
#     background-image: url("https://images.unsplash.com/photo-1517816743773-6e0fd518b4a6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDl8fGRhcmslMjBjb25zdGVsbGF0aW9ufGVufDB8fHx8MTYyNjk2Mzk2Ng&ixlib=rb-1.2.1&q=80&w=1080");
#     background-size: cover;
#     background-position: center;
#     background-repeat: no-repeat;
#     background-attachment: fixed;
#     display: flex;
#     justify-content: center;
#     align-items: center;
#     height: 100vh;
# }

# /* Style for form container */
# div.block-container {
#     background-color: rgba(255, 255, 255, 0.85);
#     padding: 3rem;
#     border-radius: 15px;
#     max-width: 400px;
#     width: 100%;
#     box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
# }

# /* Styling input boxes and button */
# input, button {
#     width: 100%;
#     height: 45px;
#     border-radius: 5px;
#     font-size: 16px;
#     margin-bottom: 10px;
#     padding: 10px;
# }

# button {
#     background-color: #6c63ff;
#     color: white;
#     border: none;
# }

# button:hover {
#     background-color: #4a47a3;
# }
# </style>
# '''

# # Apply custom CSS for layout and background image
# st.markdown(page_style, unsafe_allow_html=True)

# # Sign Up Form (Centered on the page with background)
# st.title("Sign Up")

# # Input fields for the signup form
# username = st.text_input("Username")
# email = st.text_input("Email")
# password = st.text_input("Password", type="password")

# # Sign up button
# if st.button("Sign Up"):
#     if username and email and password:
#         st.success(f"Welcome, {username}! Your account has been created.")
#     else:
#         st.error("Please fill in all the fields.")

# # Login link
# st.write("Already have an account? [Login](#)")
import streamlit as st

# Set page layout to centered (which is more mobile-friendly)
st.set_page_config(layout="centered")

# Custom CSS for centering the form, adding a background image, and adjusting the eye button
page_style = '''
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1517816743773-6e0fd518b4a6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDl8fGRhcmslMjBjb25zdGVsbGF0aW9ufGVufDB8fHx8MTYyNjk2Mzk2Ng&ixlib=rb-1.2.1&q=80&w=1080");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* Style for form container */
div.block-container {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 3rem;
    border-radius: 15px;
    max-width: 400px;
    width: 100%;
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
}

/* Styling input boxes and button */
input, button {
    width: 100%;
    height: 45px;
    border-radius: 5px;
    font-size: 16px;
    margin-bottom: 10px;
    padding: 10px;
}

button {
    background-color: #6c63ff;
    color: white;
    border: none;
}

button:hover {
    background-color: #4a47a3;
}

/* Password input with 'eye' icon */
.password-input {
    position: relative;
    width: 100%;
}

.password-input input {
    padding-right: 40px; /* Space for eye icon */
}

.password-input button {
    position: absolute;
    right: 30px;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    font-size: 14px; /* Adjust the font size (smaller icon) */
    padding: 5px; /* Adjust padding inside the button to make it smaller */
    cursor: pointer;
    color: #333;
    width: 30px;  /* Adjust width of the button */
    height: 30px; /* Adjust height of the button */
}

/* Make the eye icon smaller */
.password-input button i {
    font-size: 18px; /* Adjust icon size */
}
</style>
'''

# Apply custom CSS for layout and background image
st.markdown(page_style, unsafe_allow_html=True)

# Sign Up Form (Centered on the page with background)
st.title("Sign Up")

# Input fields for the signup form
username = st.text_input("Username")
email = st.text_input("Email")

# Password input field with placeholder for the eye button
password_container = st.empty()  # This is where the password field will be
password = password_container.text_input("Password", type="password")

# Eye button logic (toggle show/hide password) - needs manual implementation

# Sign up button
if st.button("Sign Up"):
    if username and email and password:
        st.success(f"Welcome, {username}! Your account has been created.")
    else:
        st.error("Please fill in all the fields.")

# Login link
st.write("Already have an account? [Login](#)")
