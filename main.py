import streamlit as st
import langchain_helper

st.title("Hello Everyone!")
st.subheader("Restaurant Name Generator App!", divider="rainbow")

cuisine = st.sidebar.selectbox(
    "Pick a cuisine",
    ["Italian", "Chinese", "Mexican", "Indian", "French"]
)

# theme = st.sidebar.selectbox(
#     "Pick a theme",
#     ["Casual", "Fine Dining", "Family Friendly", "Fast Food", "Cafe"]
# )

# location = st.sidebar.selectbox(
#     "Pick a location",
#     ["Downtown", "Suburbs", "Beachfront", "Mountain", "Rural"]
# )

if cuisine:
    response = langchain_helper.generate_restaurant_name(cuisine)

    st.subheader("Restaurant Name")
    st.header(response["restaurant_name"])

    st.subheader("Menu Items")

    # Convert menu text into list
    menu_items = response["menu_items"].split("\n")

    for item in menu_items:
        if item.strip() != "":
            st.write(f"- {item}")

    