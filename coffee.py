from fpdf import FPDF
from fpdf.enums import XPos, YPos

class StyledCoffeePDF(FPDF):
    def header(self):
        # Azul oscuro elegante para header y texto blanco
        self.set_fill_color(25, 40, 90)  # azul oscuro
        self.set_text_color(255, 255, 255)
        self.set_font("DejaVu", "B", 14)
        self.cell(w=0, h=12, txt="☕ Bitácora de Cata – Nanopresso + Café de Puebla",
                  align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
        self.ln(5)
        # Línea fina azul claro para separar
        self.set_draw_color(150, 170, 210)
        self.set_line_width(0.7)
        self.line(10, self.get_y(), 287, self.get_y())
        self.ln(5)

    def add_summary(self):
        bloques = [
            {
                "titulo": "🔧 1. Molienda",
                "contenido": [
                    ("✅ Correcta: fina (tipo sal de mesa). Flujo controlado.", "verde"),
                    ("⚠️ Muy gruesa: sin crema, café aguado.", "rojo"),
                    ("⚠️ Muy fina: difícil de bombear, café amargo.", "rojo")
                ]
            },
            {
                "titulo": "⏱️ 2. Tiempo de extracción",
                "contenido": [
                    ("✅ Ideal: 25–30 segundos.", "verde"),
                    ("⚠️ <20s: subextracción (ácido, sin cuerpo).", "rojo"),
                    ("⚠️ >35s: sobreextracción (amargo, astringente).", "rojo")
                ]
            },
            {
                "titulo": "☁️ 3. Crema",
                "contenido": [
                    ("✅ Ideal: color avellana, 2–4 mm, textura sedosa.", "verde"),
                    ("⚠️ Problemas: muy clara, desaparece rápido, burbujas grandes.", "amarillo")
                ]
            },
            {
                "titulo": "💧 4. Flujo",
                "contenido": [
                    ("✅ Ideal: constante y firme.", "verde"),
                    ("⚠️ Problemas: muy rápido (grueso), muy lento (fino).", "amarillo")
                ]
            },
            {
                "titulo": "🎨 5. Perfil sensorial esperado",
                "contenido": [
                    ("🍊 Acidez cítrica (naranja, mandarina).", None),
                    ("🍯 Dulzor tipo caramelo o miel.", None),
                    ("🌰 Notas a almendra y avellana.", None),
                    ("🥛 Cuerpo medio a cremoso.", None),
                    ("🎯 Posgusto persistente y suave.", None)
                ]
            }
        ]

        # Paleta elegante: verdes oscuros, dorado suave, rojo burdeos, negro
        colores = {
            "verde": (0, 100, 0),         # verde oscuro
            "amarillo": (184, 134, 11),  # dorado mostaza
            "rojo": (139, 0, 0),          # burdeos
            None: (50, 50, 50)             # gris oscuro para texto neutro
        }

        # Título general con fondo lavanda claro y texto azul oscuro
        self.set_font("DejaVu", "B", 14)
        self.set_fill_color(230, 230, 250)  # lavanda claro
        self.set_text_color(25, 40, 90)     # azul oscuro
        self.cell(0, 12, "📋 Resumen de Evaluación del Espresso",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
        self.ln(5)

        for bloque in bloques:
            # Título de sección con gris claro de fondo y azul oscuro texto
            self.set_fill_color(245, 245, 245)  # gris muy claro
            self.set_text_color(25, 40, 90)     # azul oscuro
            self.set_font("DejaVu", "B", 12)
            self.cell(0, 9, bloque["titulo"], new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)

            # Texto contenido con colores según nivel de atención
            self.set_font("DejaVu", "", 10)
            for linea, nivel in bloque["contenido"]:
                r, g, b = colores[nivel]
                self.set_text_color(r, g, b)
                self.multi_cell(0, 7, "  " + linea, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.ln(4)

        self.set_text_color(0, 0, 0)  # volver a negro

    def add_table(self, rows=5, style='manual'):
        self.set_font("DejaVu", "B", 6 if style == 'digital' else 7)
        headers = ['Nº', 'Fecha', 'Molienda', 'Tiempo (s)', 'Dosis (g)', 'Volumen (ml/g)',
                   'Crema (color, espesor)', 'Flujo', 'Acidez (1–5)', 'Dulzor (1–5)',
                   'Cuerpo (1–5)', 'Posgusto (1–5)', 'Notas y Ajustes']
        widths = [8, 18, 18, 18, 16, 20, 28, 14, 18, 18, 18, 22, 40]

        # Encabezado con azul oscuro y texto blanco
        self.set_fill_color(25, 40, 90)
        self.set_text_color(255, 255, 255)
        for i in range(len(headers)):
            self.cell(widths[i], 10, headers[i], 1, 0, 'C', fill=True)
        self.ln()

        self.set_font("DejaVu", "", 8 if style == 'digital' else 9)
        self.set_text_color(0, 0, 0)

        # Filas con alternancia suave de gris claro
        for row in range(rows):
            fill = row % 2 == 0
            if fill:
                self.set_fill_color(240, 240, 245)  # gris muy suave
            else:
                self.set_fill_color(255, 255, 255)  # blanco
            for width in widths:
                self.cell(width, 10 if style == 'digital' else 12, '', 1, 0, 'C', fill=fill)
            self.ln()

    def add_signature_area(self):
        self.ln(10)
        self.set_font("DejaVu", "", 10)
        self.set_text_color(25, 40, 90)  # azul oscuro elegante
        self.cell(0, 10, "🖊️ Firma del catador: ____________________________", ln=True)
        self.cell(0, 10, "📅 Fecha: _______________________________________", ln=True)
        self.set_text_color(0, 0, 0)  # volver negro

def registrar_fuentes(pdf):
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
    pdf.add_font("DejaVu", "B", "DejaVuSans-Bold.ttf", uni=True)

# Crear PDFs
pdf_manual = StyledCoffeePDF(orientation='L', unit='mm', format='A4')
registrar_fuentes(pdf_manual)
pdf_manual.add_page()
pdf_manual.set_font("DejaVu", "", 10)
pdf_manual.add_summary()
pdf_manual.add_table(rows=5, style='manual')
pdf_manual.add_signature_area()
pdf_manual.output("Bitacora_Cafe_Estilo_Manual_Elegante.pdf")

pdf_digital = StyledCoffeePDF(orientation='L', unit='mm', format='A4')
registrar_fuentes(pdf_digital)
pdf_digital.add_page()
pdf_digital.set_font("DejaVu", "", 10)
pdf_digital.add_summary()
pdf_digital.add_table(rows=5, style='digital')
pdf_digital.add_signature_area()
pdf_digital.output("Bitacora_Cafe_Estilo_Digital_Elegante.pdf")

print("PDFs generados con estilo elegante y paleta azulada.")
