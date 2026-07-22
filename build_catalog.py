import csv,json
from pathlib import Path

rows=[]
def add(family,ref,dmin,dmax,**kw):
    r={'family':family,'reference':ref,'diameter_min_mm':dmin,'diameter_max_mm':dmax}
    r.update(kw); rows.append(r)

# Separador SP-2: reference SP-2/<diameter-range>/<length>
sp2={
 '17-20':[(250,1.15),(300,1.25),(330,1.30),(400,1.43),(450,1.53)],
 '20-23':[(250,1.13),(300,1.23),(330,1.28),(400,1.41),(450,1.51)],
 '23-26':[(250,1.11),(300,1.20),(330,1.26),(400,1.39),(450,1.49)],
 '26-29':[(250,1.10),(300,1.20),(330,1.25),(400,1.39),(450,1.50)],
 '29-32':[(300,1.29),(400,1.48),(450,1.57)],
 '32-35':[(300,1.25),(400,1.44),(450,1.54)]}
for dr,items in sp2.items():
    a,b=map(int,dr.split('-'))
    for L,m in items: add('separador_SP2',f'SP-2/{dr}/{L}',a,b,length_mm=L,torque_Nm=30,mass_kg=m)

# Separador SP-3, straight.
for dr,items in {'13-16':[(330,.94),(400,1.00),(450,1.03)],'16-20':[(330,.93),(400,1.00),(450,1.02)],'20-24':[(330,.93),(400,.98),(450,1.00)],'24-28':[(330,.92),(400,.97),(450,1.00)],'28-32':[(330,.90),(400,.95),(450,1.00)]}.items():
    a,b=map(int,dr.split('-'))
    for L,m in items: add('separador_SP3',f'SP-3/{dr}/{L}',a,b,length_mm=L,torque_Nm=25,mass_kg=m)

# Separador SP-3/3, triple.
for dr,items in {'13-16':[(400,1.73),(450,1.90)],'16-20':[(400,1.72),(450,1.90)],'20-24':[(400,1.70),(450,1.88)],'24-28':[(400,1.70),(450,1.87)],'28-32':[(400,1.67),(450,1.85)]}.items():
    a,b=map(int,dr.split('-'))
    for L,m in items: add('separador_SP3_3',f'SP-3/3/{dr}/{L}',a,b,length_mm=L,torque_Nm=25,mass_kg=m)

# SAPREM separator-damper families. Values are dmin,dmax,A,B,mass for B=400/450.
spa={
 'SPA400DA':[(17.3,19.5,80,2.45),(19.3,21.5,80,2.42),(21.3,23.5,80,2.40),(23.4,25.4,80,2.57),(25.2,27.8,80,2.55),(27.6,30.6,80,2.50),(30.4,33.0,80,2.46),(32.8,35.0,86,2.86),(34.8,37.0,86,2.81),(36.8,39.0,86,2.77)],
 'SPA400TA':[(17.3,19.5,80,3.94),(19.3,21.5,80,3.89),(21.3,23.5,80,3.86),(23.4,25.4,80,4.12),(25.2,27.8,80,4.08),(27.6,30.6,80,4.05),(30.4,33.0,80,3.95),(32.8,35.0,86,4.54),(34.8,37.0,86,4.48),(36.8,39.0,86,4.41)],
 'SPA400CA':[(17.3,19.5,80,5.23),(19.3,21.5,80,5.18),(21.3,23.5,80,5.13),(23.4,25.4,80,5.48),(25.2,27.8,80,5.43),(27.6,30.6,80,5.33),(30.4,33.0,80,5.26),(32.8,35.0,86,6.05),(34.8,37.0,86,5.96),(36.8,39.0,86,5.87)]}
for fam,vals in spa.items():
    suffixes=[19,21,23,25,27,30,33,35,37,39]
    for suffix,(dmin,dmax,A,m400) in zip(suffixes,vals):
        code=fam+str(suffix)
        add(fam,code,dmin,dmax,dimension_A_mm=A,dimension_B_mm=400,torque_Nm=45,mass_kg=m400)
        # 450 mm variant masses transcribed from the companion sheet.
        m450={'SPA400DA':{17.3:2.53,19.3:2.50,21.3:2.48,23.4:2.65,25.2:2.63,27.6:2.57,30.4:2.54,32.8:2.93,34.8:2.89,36.8:2.85},'SPA400TA':{17.3:4.05,19.3:4.01,21.3:3.97,23.4:4.24,25.2:4.20,27.6:4.12,30.4:4.07,32.8:4.66,34.8:4.59,36.8:4.53},'SPA400CA':{17.3:5.51,19.3:5.46,21.3:5.41,23.4:5.76,25.2:5.71,27.6:5.61,30.4:5.54,32.8:6.33,34.8:6.24,36.8:6.15}}[fam][dmin]
        add(fam.replace('400','450'),code.replace('400','450'),dmin,dmax,dimension_A_mm=A,dimension_B_mm=450,torque_Nm=45,mass_kg=m450)

# Stockbridge SD dampers from the previous sheet.
for ref,code,cl,cs,a,b,m in [('SD-0302-D13','10899','SD-D13','DMP-3',7,13,1.83),('SD-0302-D20','10898','SD-D20','DMP-2',13,20,1.89),('SD-0302-D27','10897','SD-D27','DMP-2',20,37,1.93),('SD-0403-D20','10561','SD-D20','DMP-3',13,20,3.03),('SD-0403-D27','10562','SD-D27','DMP-3',20,37,3.07),('SD-0403-D34','10563','SD-D34','DMP-3',27,34,3.13),('SD-0403-D44','10896','SD-D44','DMP-3',34,44,3.21),('SD-0504-D20','10558','SD-D20','DMP-4',13,20,4.23),('SD-0504-D27','10559','SD-D27','DMP-4',20,27,4.27),('SD-0504-D34','10560','SD-D34','DMP-4',27,34,4.33),('SD-0504-D44','10895','SD-D44','DMP-4',34,44,4.41),('SD-0605-D34','10557','SD-D34','DMP-5',27,34,6.39),('SD-0605-D44','10894','SD-D44','DMP-5',34,44,6.42)]:
    add('amortiguador_SD',ref,a,b,code=code,mass_large_clamp=cl,mass_small_clamp=cs,mass_kg=m)

# ZTT Stockbridge damper used in study 109475. Mass and dynamic response are
# not specified in the drawing and are therefore intentionally left null.
add('amortiguador_4D','4D-20',0,15,manufacturer='ZTT',drawing='JSF-109475-4 Rev A',design_conductor_diameter_mm=11.8,rts_kN=48.3,overall_length_mm=319,clamp_width_mm=53,clamp_height_mm=73,messenger_diameter_mm=7.5,messenger_cable='19/1.5 galvanized steel',large_weight='4D-20L cast iron',small_weight='4D-20S cast iron',temperature_min_C=-20,temperature_max_C=90,mass_kg=None,dynamic_curve_available=False)
add('amortiguador_FR','FR-2',11,22,manufacturer='ZTT',drawing='JSH-110007 Rev A',design_conductor='AAAC Cairo',design_conductor_diameter_mm=19.88,overall_length_mm=430,clamp_width_mm=50,clamp_height_mm=80,messenger_diameter_mm=11,large_weight='cast iron',small_weight='cast iron',temperature_min_C=-20,temperature_max_C=90,mass_kg=None,dynamic_curve_available=False)
add('amortiguador_FR3','FR-3',18,28,manufacturer='ZTT',drawing='JSH-125025 Rev A',design_conductor='AAAC FLINT 37/3.59',design_conductor_diameter_mm=25.13,overall_length_mm=510,clamp_width_mm=60,clamp_height_mm=90,messenger_diameter_mm=13,mass_kg=None,dynamic_curve_available=False)

# SAPREM AMG four-resonance asymmetric Stockbridge dampers, drawing
# AMG-XXYYZZ Rev.18 supplied by the user. Weight is converted g -> kg.
saprem_amg = [
 ('AMG-030513','G-13',7,13,'S-03','S-05',7.8,19,'M10',101,119,1225,30,55),
 ('AMG-030520','G-20',13,20,'S-03','S-05',7.8,19,'M10',101,119,1260,30,55),
 ('AMG-050913','G-13',7,13,'S-05','S-09',7.8,19,'M10',88,110,1770,30,55),
 ('AMG-050920','G-20',13,20,'S-05','S-09',7.8,19,'M10',88,110,1805,30,55),
 ('AMG-050926','G-26',18,26,'S-05','S-09',7.8,19,'M12',88,110,2015,35,58),
 ('AMG-050929','G-29',21.5,29.5,'S-05','S-09',7.8,19,'M12',88,110,2015,35,58),
 ('AMG-051126','G-26',18,26,'S-05','S-11',7.8,19,'M12',88,110,2240,35,58),
 ('AMG-091520','G-20',13,20,'S-09','S-15',9.3,19,'M10',111,140,2910,30,55),
 ('AMG-091526','G-26',18,26,'S-09','S-15',9.3,19,'M12',111,140,3125,35,58),
 ('AMG-091529','G-29',21.5,29.5,'S-09','S-15',9.3,19,'M12',111,140,3125,35,58),
 ('AMG-091534','G-34',28,34,'S-09','S-15',9.3,19,'M12',111,140,3155,35,63),
 ('AMG-091540','G-40',34,40,'S-09','S-15',9.3,19,'M14',111,140,3360,35,68),
 ('AMG-091826','G-26',18,26,'S-09','S-18',9.3,19,'M12',123,160,3410,35,58),
 ('AMG-152426','G-26',18,26,'S-15','S-23',11.9,19,'M12',147,185,4565,35,58),
 ('AMG-152429','G-29',21.5,29.5,'S-15','S-23',11.9,19,'M12',147,185,4565,35,58),
 ('AMG-152434','G-34',28,34,'S-15','S-23',11.9,19,'M12',147,185,4595,35,63),
 ('AMG-152440','G-40',34,40,'S-15','S-23',11.9,19,'M14',147,185,4800,35,68),
 ('AMG-152445','G-45',40,45,'S-15','S-23',11.9,19,'M14',147,185,4810,35,68),
 ('AMG-243534','G-34',28,34,'S-23','S-35',11.9,19,'M12',147,185,6710,35,63),
 ('AMG-243540','G-40',34,40,'S-23','S-35',11.9,19,'M14',147,185,6915,35,68),
 ('AMG-243545','G-45',40,45,'S-23','S-35',11.9,19,'M14',147,185,6920,35,68),
]
for ref,clamp,dmin,dmax,large,small,cable_d,wires,bolt,l1,l2,weight_g,torque,a_dim in saprem_amg:
    add('amortiguador_SAPREM_AMG',ref,dmin,dmax,manufacturer='SAPREM',clamp=clamp,
        large_weight=large,small_weight=small,messenger_diameter_mm=cable_d,
        messenger_wires=wires,bolt=bolt,L1_mm=l1,L2_mm=l2,mass_kg=weight_g/1000,
        torque_Nm=torque,dimension_A_mm=a_dim,resonances=4,dynamic_curve_available=False)

for r in rows: r['source']='fichas tecnicas suministradas por el usuario'
fields=sorted({k for r in rows for k in r})
with open('catalogo_amortiguadores.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
Path('catalogo_amortiguadores.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'{len(rows)} registros escritos')
