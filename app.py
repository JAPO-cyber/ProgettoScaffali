import streamlit as st
from progettoscaffali.data import load_data
from progettoscaffali.packing import pack_boxes_2d
from progettoscaffali.usd_generator import generate_usdz

st.title("ProgettoScaffali: Warehouse USD Viewer")

box_csv = st.sidebar.text_input("Percorso CSV casse", "boxes.csv")
shelf_csv = st.sidebar.text_input("Percorso CSV scaffali", "shelves.csv")

if st.sidebar.button("Genera USDZ"):
    df_boxes, df_shelves = load_data(box_csv, shelf_csv)
    df_packed = pack_boxes_2d(df_shelves, df_boxes)
    output = "magazzino.usdz"
    usdz_path = generate_usdz(df_shelves, df_packed, output)

    html = f"""
    <model-viewer src="{usdz_path}" alt="Magazzino 3D"
                  autoplay camera-controls auto-rotate
                  style="width:100%; height:600px;">
    </model-viewer>
    <script type="module"
      src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js">
    </script>
    """
    st.components.v1.html(html, height=650)
