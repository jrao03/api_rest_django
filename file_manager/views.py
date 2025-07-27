from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

import re
import pandas as pd
import PyPDF2

# Create your views here.
@api_view(['POST'])
@parser_classes([MultiPartParser])
def subir_archivo(request):
    archivo = request.FILES['archivo']
    extension = archivo.name.split('.')[-1].lower()

    # Procesamiento según tipo de archivo
    if extension == 'pdf':
        datos = extraer_datos_pdf(archivo)
    elif extension in ['csv', 'xlsx']:
        datos = extraer_datos_excel_csv(archivo, extension)
    else:
        return Response({'error': 'Formato no soportado'}, status=400)

    return Response(datos, status=200)

def extraer_datos_pdf(archivo):
    lector = PyPDF2.PdfReader(archivo)
    texto = ''
    for pagina in lector.pages:
        texto += pagina.extract_text() or ''
    return buscar_datos(texto)

def extraer_datos_excel_csv(archivo, extension):
    if extension == 'csv':
        df = pd.read_csv(archivo)
    else:  # xlsx
        df = pd.read_excel(archivo)

    texto = ' '.join(df.astype(str).fillna('').values.flatten())
    return buscar_datos(texto)

def buscar_datos(texto):
    resultados = {}

    # CURP y RFC por regex
    curp_match = re.search(r'\b[A-Z]{4}\d{6}[A-Z0-9]{8}\b', texto)
    rfc_match = re.search(r'\b[A-ZÑ&]{3,4}\d{6}[A-Z0-9]{3}\b', texto)

    if curp_match:
        resultados['CURP'] = curp_match.group()
    if rfc_match:
        resultados['RFC'] = rfc_match.group()

    etiquetas = ['Nombre', 'Apellido', 'Dirección', 'Correo', 'Teléfono']
    for etiqueta in etiquetas:
        pattern = rf'{etiqueta}[:\s]+([^\n\r]+)'
        match = re.search(pattern, texto, re.IGNORECASE)
        if match:
            resultados[etiqueta] = match.group(1).strip()

    return resultados
