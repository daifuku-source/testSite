import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


# st.title('streamlit_test')

img = Image.open('top.jpg')
st.image(img, caption='star vista project', use_column_width=True)
