import streamlit as st
import math 
st.title("2205A21044-PS8")
st.header("Calculate the winding resistance[R1] and reactance[X1] of a transformer based on short circuit test measurements like VSC,ISC and WSC")

def Tran_Eff(vsc,isc,wsc):
    zsc=vsc/isc
    r1=wsc/(isc**2)
    x1=math.sqrt((zsc**2)-(r1**2))
    return r1,x1

col1,col2=st.columns(2)
with col1:
    vsc=st.number_input("VSC (volt)", value=100)
    isc=st.number_input("ISC (Amps)", value=100)
    wsc=st.number_input("WSC (Watts)", value=100)
    compute=st.button("compute")

with col2:
    with st.container(border=True):
        if compute:
            r1,x1=Tran_Eff(vsc,isc,wsc)
            st.write(f"R1={r1:.2f} ohms")
            st.write(f"X1={x1:.2f} ohms")

