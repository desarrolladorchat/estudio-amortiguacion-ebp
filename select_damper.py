"""Consulta el catalogo mecanico digitizado desde las fichas.
Example: python select_damper.py 16 --family amortiguador_SD
"""
import argparse,csv,json

ap=argparse.ArgumentParser(); ap.add_argument('diameter_mm',type=float); ap.add_argument('--family'); ap.add_argument('--catalog',default='catalogo_amortiguadores.json'); args=ap.parse_args()
rows=json.load(open(args.catalog,encoding='utf-8'))
found=[r for r in rows if r['diameter_min_mm'] <= args.diameter_mm <= r['diameter_max_mm'] and (not args.family or r['family']==args.family)]
for r in found:
    print(f"{r['family']:20} {r['reference']:24} {r['diameter_min_mm']:5g}-{r['diameter_max_mm']:5g} mm  {r.get('length_mm',r.get('dimension_B_mm',''))!s:>5}  {r['mass_kg']:.2f} kg")
print(f"{len(found)} compatibles")
