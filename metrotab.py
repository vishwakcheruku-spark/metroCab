import streamlit as st
st.title("metro + cab booking")
#metro station lists
stations=["jntuh","lbnagar","ameerpet"]
from_stations=st.selectbox("from station",stations)
to_stations=st.selectbox("to station",stations)
tickets=st.number_input("number of tickets",min_value=1,max_value=1)
need_cab=st.radio("do you need a cab ?",["yes","no"],index=None)
cab_fare=0
if(need_cab=="yes"):
    cab_destination=st.text_input("enter destination:")
    
    cab_fare=130
if st.button("book"):
    if from_station == to_station:
        st.error("from and to stations cannot be the same.")
    else:
        metro_fare=30*tickets
        total=metro_fare + cab_fare
        st.success("Booking successful!")
        st.write(f"FROM:{from_station}")
        st.write(f"TO:{to_station}")
        st.write(f"TICKETS:{tickets}")
        st.write(f"metro_fare: {metro_fare}")
        if need_cab == "yes":
            st.write(f"cab from:{to_station}")
            st.write(f"to:{cab_destination}")
            st.write(f"cab bill:{cab_fare}")
            st.write(f"---total bill---:{total}")   
   