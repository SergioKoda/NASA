import streamlit as st
import math

st.title("🌠 Simulador de Impacto de Meteoritos")

diametro = st.number_input("Diámetro del meteoro (m)", 1.0, 10000.0, 50.0)
densidad = st.number_input("Densidad (kg/m³)", 500.0, 8000.0, 3000.0)
velocidad = st.number_input("Velocidad (km/s)", 1.0, 70.0, 20.0)

r = diametro / 2
m = (4/3) * math.pi * (r**3) * densidad
v = velocidad * 1000
E = 0.5 * m * v**2
E_TNT = E / 4.184e9

st.write(f"**Energía liberada:** {E_TNT:,.2f} toneladas de TNT")

if E_TNT < 0.001:
    st.info("Impacto imperceptible 🌌")
elif E_TNT < 1:
    st.warning("Bola de fuego local 🔥")
elif E_TNT < 1000:
    st.error("Destrucción regional 💥")
else:
    st.error("Evento global 🌍")

