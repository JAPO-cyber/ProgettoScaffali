import pandas as pd

def load_data(box_csv: str, shelf_csv: str):
    """
    Carica dati da CSV o altre fonti.
    CSV casse: colonne [id_scaffale, Lunghezza, Larghezza, Altezza, Peso]
    CSV scaffali: colonne [id_scaffale, x0, y0, lung_s, lar_s, alt_s]
    """
    df_boxes = pd.read_csv(box_csv)
    df_shelves = pd.read_csv(shelf_csv)
    return df_boxes, df_shelves
