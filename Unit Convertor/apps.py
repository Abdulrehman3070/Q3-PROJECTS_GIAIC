import streamlit as st

def convertor(value,from_unit):

    if from_unit == "Inch to cm":
        return value*2.54
    elif from_unit == "Cm to inch":
        return value /2.54
    
st.title("📏Inch to Centimeter converter")

value = st.number_input("Enter Value : ",min_value=0.0 , format="%.2f")
from_unit = st.selectbox("Convert From :" , ["Inch to cm", "Cm to inch"])
to_unit = "Cm to inch" if from_unit == "Inch to cm" else "Inch"

if st.button("Convert"):
    result = convertor(value,from_unit)
    st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")


