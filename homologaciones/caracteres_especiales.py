#trucos para caracteres especiales 
x = 'importacion definitiva a la franja fronteriza norte y region fronteriza al amparo del â€œdecreto de la franja o region fronterizaâ€ (dof 24/12/2008 y sus posteriores modificaciones)'
x = x.replace('ã‰','e').replace('â€','').replace('â€œ','')
#x  = x.encode().decode('ascii',errors='ignore')
x 