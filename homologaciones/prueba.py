import re

descripciones = [
    'giotrif 30mg (afatinib) 30 tabletas (medicamento de uso humano)',
    'giotrif 40mg (afatinib) 30 tabletas (medicamento de uso humano)',
    'verzenio (abemaciclib) 100mg 56 tab',
    'lorviqua (lorlatinib)caja con 30 tabletas',
    'bay 2757556 larotrectinib 20 g/ml frasco 100 ml',
    'cont 1 blass bottle cont 100ml  27bay57556 (larotrectinib) labeled',
    'medicamento trazimera (trastuzumab) caja de carton con un frasco ampula con 440 mg de polvo liofilizado y un frasco ampula con 20 ml de diluyente e instructivo anexo',
    'avastin  100 mg/4 ml solucion inyectable (bevacizumab)',
    'nivolumab (bms-936558-) vial de 10 ml (100mg/vial) ',
    'prolia (denosumab) jeringa con 60 mg/ 1.0 ml (medicamento de uso humano)',
    'xgeva (denosumab) ampula con 120 mg/ 1.7 ml (medicamento de uso humano)',
    'nivolumab,  vial de 10 ml (100mg/vial)',
    'kadcyla 100mg frasco ampula (trastuzumab emtansina)',
    'mvasi (bevacizumab) ampula con 100 mg/ 4.0 ml (medicamento de uso humano)',
    'avastin  400 mg/16ml solucion inyectable  (bevacizumab)',
    'medicamentos (adcetris 50mg (brentuximab vedotin 50mg) caja con 1 ',
    'medicamentos (opdivo 40mg/4ml[nivolumab] caja con frasco).',
    'tecentriq 1200 mg/20 ml solucion inyectable (atezolizumab)',
    'medicamentos (opdivo 40mg/4ml[nivolumab] caja con frasco).',
    'perjeta 30 mg/ml  frasco ampula 14 ml  (pertuzumab)',
    'medicamentos (keytruda[pembrolizumab 100mg/4ml]en caja con frasco con solucion inyectable para infusion intravenosa).',
    'cont 1 blass bottle cont 100ml  27bay57556 (larotrectinib) labeled',
    'tafinlar 75 mg 28capsulas (dabrafenib)',
    'jakavi 15 mg 60 tabletas (ruxolitinib)',
    'votrient 400 mg 60 tabletas (pazopanib)',
    'medicamento xalkori (crizotinib) frasco de plastico con 60 capsulas de 250mg con instructivo anexo.',
    'medicamento ibrance-21 (palbociclib) frasco con 21 capsulas de 75 mg.',
    'mekinist 0.5 mg  30 comprimidos (trametinib)',
    'zelboraf 240 mg  56 tabletas (vemurafenib)',
    'alecensa 150 mg 224 capsulas (alectinib)',
    'lynparza 50 mg capsulas (olaparib)',
    'iressa 250 mg tabletas (gefitinib)',
    'caja con 1 vial con 30 tabletas de 180 mg de alunbrig (brigatinib)',
    'jakavi 10 mg  60 tabletas (ruxolitinib)',
    'tafinlar 50 mg  28 capsulas (dabrafenib)',
    'rednez (bortezomib)(f.fsolucion)',
    'alunbrig (brigatinib) tableta',
    'brigatinib ( alunbrig ) caja con 1 vial con 60 tabletas de 30 mg',
    'tarceva 100 mg comprimidos  (erlotinib)',
    'brigatinib ( alunbrig ) caja con 1 vial con 30 tabletas de 180 mg',
    'brigatinib (alunbrig) tableta',
    'afinitor 5 mg  30 comprimidos (everolimus)',
    'tykerb 250 mg tabletas (lapatinib)',
    'tasigna 200 mg capsulas (nilotinib)',
    'medicamento inlyta (axitinib) frasco con 60 tabletas de 5 mg.',
    'medicamento con alunbrig (brigatinib) caja con 1 vial con 30 tabletas de 180 mg',
    'medicamento con alunbrig (brigatinib) caja con 1 vial con 60 tabletas de 30 mg',
    'kyprolis 60mg (carfilzomib) (medicamento de uso humano)',
    'medicamento sutent 28 (sunitinib) caja de carton con 28 capsulas de 12.5 mg en frasco etiquetado  e instructivo anexo.',
    'iclusig (ponatinib)(tableta)',
    'iclusig (ponatinib)(tableta)',
    'afinitor 10 mg  30 comprimidos (everolimus)',
    'sprycel (dasatinib) frasco con  60 tabletas de 70 mg (medicamento de uso humano)',
    'sprycel (dasatinib) frasco con 60 tabletas de 50 mg (medicamento de uso humano)'
]
descripciones2 =[
    'nivolumab (bms-936558-) vial de 10 ml (100mg/vial) ',
    ''
]

UNIDAD_CONCENTRACION = ['mg','µG']
FORMA_FARMA = ['tabletas', 'capsulas','comprimidos','solucion inyectable', 'solucion oral']

#afinitor 10 mg  30 comprimidos (everolimus)
expresion_1 = '\d{1,3}\s*mg\s*\d{1,3}\s*(tabletas|capsulas|comprimidos|solucion inyectable|solucion oral)'
expresion_1 = '\d+\.?\d*\s*mg\s*\d{1,3}\s*(tabletas|tab|capsulas|comprimidos|solucion inyectable|solucion oral)'#acepta decimal en su concentracion

#giotrif 30mg (afatinib) 30 tabletas (medicamento de uso humano)
expresion_1_1 = '\d+\.?\d*\s*mg.{0,20}\d{1,4}\s*(tabletas|capsulas|comprimidos|solucion inyectable|solucion oral)' #menos exacta que la expresion_1

#prycel (dasatinib) frasco con  60 tabletas de 70mg (medicamento de uso humano)
expresion_2 = '\d{1,3}\s*(tabletas|capsulas|comprimidos|solucion inyectable|solucion oral).{0,5}\d{1,3}\s*mg'
expresion_2 = '\d{1,3}\s*(tabletas|capsulas|comprimidos|solucion inyectable|solucion oral).{0,5}\d+\.?\d*\s*mg'#acepta decimal en su concentracion

#avastin  100 mg/4 ml solucion inyectable (bevacizumab)
expresion_soluciones = '\d+\.?\d*\s*mg.{0,30}\s*(solucion inyectable|solucion oral)'

#mvasi (bevacizumab) ampula con 100 mg/ 4.0 ml (medicamento de uso humano)
expresion_4 = '(frasco ampula|vial|ampula|jeringa)\s*.{0,5}\d+\s*mg'

#kadcyla 100mg frasco ampula (trastuzumab emtansina)
expresion_6 = '\d+\s*mg\s*(frasco ampula|vial|ampula|jeringa)'

#.
expresion_7 = '\d+.?\d+\s*mg.{10,30}(frasco ampula|vial|ampula|jeringa)'

#tarceva 100 mg comprimidos  (erlotinib)
expresion_3 = '\d+\.?\d*\s*mg\s*(tabletas|capsulas|comprimidos|solucion inyectable|solucion oral)'

#kyprolis 60mg (carfilzomib) (medicamento de uso humano)
expresion_5 = '\d+\.?\d*\s*mg'

diccionario_mayor = {}
for descripcion in descripciones:
    print(descripcion)
    match = re.search(expresion_1, descripcion)
    if match:#75 mg 28capsulas 
        info = match.group()
        numeros =  re.findall("\d+\.?\d*", info)
        concentracion = numeros[0]
        unidad_concentracion = 'mg'
        presentacion = numeros[1]
        forma_farma = re.search("[a-z]{3,15}", info).group()
        forma_farma = 'tabletas' if forma_farma == 'tab' else forma_farma
        print(concentracion, unidad_concentracion, presentacion, forma_farma)
        continue

    match = re.search(expresion_1_1, descripcion)
    if match:#30mg (afatinib) 30 tabletas
        info = match.group()
        numeros =  re.findall("\d+\.?\d*", info)
        concentracion = numeros[0]
        unidad_concentracion = 'mg'
        presentacion = numeros[1]
        forma_farma = re.search("(tabletas|tab|capsulas|comprimidos|solucion inyectable|solucion oral)", info).group()
        print(concentracion, unidad_concentracion, presentacion, forma_farma)
        continue 
      
    match = re.search(expresion_2, descripcion)
    if match:#60 capsulas de 250mg
        info = match.group()
        numeros =  re.findall("\d+\.?\d*", info)
        concentracion = numeros[1]
        unidad_concentracion = 'mg'
        presentacion = numeros[0]
        forma_farma = re.search("[a-z]{3,10}", info).group()
        print(concentracion, unidad_concentracion, presentacion, forma_farma)
        continue

    match = re.search(expresion_3, descripcion)
    if match:#250 mg tabletas
        info = match.group()
        numeros =  re.findall("\d+\.?\d*", info)
        concentracion = numeros[0]
        unidad_concentracion = 'mg'
        presentacion = 'sp'
        forma_farma = re.search("[a-z]{3,10}", info).group()
        print(concentracion, unidad_concentracion, forma_farma)
        continue

    match = re.search(expresion_soluciones, descripcion)
    if match:#100 mg/4 ml solucion inyectable
        info = match.group()
        concentracion = re.search("\d+.?\d*", info).group()
        unidad_concentracion = 'mg'
        presentacion = '1'
        forma_farma = re.search("(solucion inyectable|solucion oral)", info).group()
        print(concentracion, unidad_concentracion, presentacion, forma_farma)
        continue
    
    match = re.search(expresion_4, descripcion)
    if match:#ampula con 100 mg
        info = match.group()
        concentracion = re.search("\d+.?\d+", info).group()
        unidad_concentracion = re.search("mg", info).group()
        presentacion = '1'
        forma_farma = re.search("(frasco ampula|frasco|vial|ampula|jeringa)", info).group()
        print(concentracion, unidad_concentracion, presentacion, forma_farma)
        continue

    match = re.search(expresion_6, descripcion)
    if match:#100mg frasco ampula
        info = match.group()
        concentracion = re.search("\d+.?\d+", info).group()
        unidad_concentracion = re.search("mg", info).group()
        presentacion = '1'
        forma_farma = re.search("(frasco ampula|frasco|vial|ampula|jeringa)", info).group()
        print(concentracion, unidad_concentracion,presentacion, forma_farma)
        continue
    
    #match = re.search(expresion_7, descripcion)
    #if match:#40mg/4ml[nivolumab] caja con frasco
    #    info = match.group()    
    #    concentracion = re.search("\d+.?\d+", info).group()
    #    unidad_concentracion = 'mg'
    #    presentacion = '1'
    #    forma_farma = re.search("(frasco ampula|caja con frasco|frasco|vial|ampula|jeringa)", info).group()
    #    print(concentracion, unidad_concentracion,presentacion, forma_farma)
    #    continue
    #print(descripcion)
    print("N:")
    #match = re.search(expresion_5, descripcion)
    #if match:
    #    info = match.group()
    #    concentracion =  re.search("\d+", info).group()
    #    unidad_concentracion = re.search("mg", info).group()
    #    diccionario_mayor[descripcion] = str(concentracion) + unidad_concentracion + str(presentacion) + forma_farma
    #    #print(concentracion, unidad_concentracion)
    #    continue
    #print("_____________________no entro____________________________________")