from pxr import Usd, UsdGeom, Gf, UsdUtils
import os

def generate_usdz(df_shelves, df_boxes_packed, output_usdz: str):
    """
    Crea uno stage USD e lo esporta in USDZ.

    - df_shelves: colonne [id_scaffale, x0, y0, lung_s, lar_s, alt_s]
    - df_boxes_packed: colonne [id_scaffale, Lunghezza, Larghezza, Altezza, px, py]
    """
    usda_path = output_usdz.replace('.usdz', '.usda')
    stage = Usd.Stage.CreateNew(usda_path)
    root = UsdGeom.Xform.Define(stage, '/Magazzino')

    # Scaffali
    for _, s in df_shelves.iterrows():
        path = f"/Magazzino/{s.id_scaffale}"
        cube = UsdGeom.Cube.Define(stage, path)
        cube.AddTranslateOp().Set(
            Gf.Vec3d(s.x0 + s.lung_s/2,
                      s.y0 + s.lar_s/2,
                      s.alt_s/2)
        )
        cube.GetSizeAttr().Set((s.lung_s, s.lar_s, s.alt_s))

    # Casse
    for idx, b in df_boxes_packed.iterrows():
        path = f"/Magazzino/{b.id_scaffale}/Box_{idx}"
        cube = UsdGeom.Cube.Define(stage, path)
        cube.AddTranslateOp().Set(
            Gf.Vec3d(
                b.px + b.Lunghezza/2,
                b.py + b.Larghezza/2,
                b.Altezza/2
            )
        )
        cube.GetSizeAttr().Set((b.Lunghezza, b.Larghezza, b.Altezza))

    stage.GetRootLayer().Save()
    # Crea USDZ
    UsdUtils.CreateUsdzPackage(usda_path, output_usdz)
    os.remove(usda_path)
    return output_usdz
