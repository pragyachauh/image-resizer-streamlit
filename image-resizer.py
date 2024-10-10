import streamlit as st
import io
from PIL import Image

st.title("Image Resizer")

# User Uploads File
img_file_buffer = st.file_uploader('Upload a PNG image', type='png')

# CSS for custom text area size
css_text_area = '''
<style>
    .element-container:has(>.stTextArea), .stTextArea {
        width: 200px !important;
    }
    .stTextArea textarea {
        height: 10px;
    }
</style>
'''

# Uploaded image handling
if img_file_buffer is not None:
    infile = Image.open(img_file_buffer)

    width = infile.width
    height = infile.height

    # Display Current Width and Height
    current_dimensions = f'Current dimensions: {width} X {height}'
    st.text(current_dimensions)

    # Use Custom CSS
    st.markdown(css_text_area, unsafe_allow_html=True)

    # User width and height input
    user_width = st.text_area("Enter desired width")
    user_height = st.text_area("Enter desired height", height=25)

    width_convert = None
    height_convert = None

    # Convert user input from text area into int - handling
    try:
        width_convert = int(float(user_width))
    except ValueError:
        if user_width:  # Only show an error if a value was actually entered
            st.error("Please enter a valid width value")  # Show an error if conversion fails

    try:
        height_convert = int(float(user_height))
    except ValueError:
        if user_height:  # Only show an error if a value was actually entered
            st.error("Please enter a valid height value")  # Show an error if conversion fails

    if width_convert is not None and height_convert is not None:
        # Resize image
        new_image = infile.resize((width_convert, height_convert))

        # Show resized image
        st.image(new_image, caption="Resized Image")

        # Convert PIL Image to bytes
        img_byte_arr = io.BytesIO()
        new_image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        # Set a file name for the resized image
        file_name = "resized_image.png"

        # Create download button
        btn = st.download_button(
            label="Download New Image",
            data=img_byte_arr,
            file_name=file_name,
            mime="image/png",
        )


    

