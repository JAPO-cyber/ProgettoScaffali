from typing import Tuple
import pandas as pd

def pack_boxes_2d(df_shelves: pd.DataFrame, df_boxes: pd.DataFrame) -> pd.DataFrame:
    """
    Packing 2D (left-to-right, bottom-to-top) per ciascuno scaffale:
    Aggiunge colonne `px`, `py` a df_boxes.
    """
    df = df_boxes.copy()
    df['px'], df['py'] = 0, 0
    for _, s in df_shelves.iterrows():
        sub = df[df.id_scaffale == s.id_scaffale]
        cursor_x, cursor_y, max_h = s.x0, s.y0, 0
        for idx in sub.index:
            L, W = df.at[idx, 'Lunghezza'], df.at[idx, 'Larghezza']
            if cursor_x + L > s.x0 + s.lung_s:
                cursor_x = s.x0
                cursor_y += max_h
                max_h = 0
            df.at[idx, 'px'] = cursor_x
            df.at[idx, 'py'] = cursor_y
            cursor_x += L
            max_h = max(max_h, W)
    return df

# TODO: implement pack_boxes_3d usando algoritmo bin-packing 3D (es. py3dbp)
