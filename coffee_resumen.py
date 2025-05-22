from fpdf import FPDF
from fpdf.enums import XPos, YPos

class PDF(FPDF):
    def header(self):
        self.set_font("DejaVu", "B", 16)
        self.set_fill_color(25, 40, 90)  # azul oscuro
        self.set_text_color(255, 255, 255)
        self.cell(0, 15, "☕ Bitácora Gourmet Nanopresso - Evaluación", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C', fill=True)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Página {self.page_no()}', align='C')

    def add_summary(self):
        bloques = [
            {
                "titulo": "🔧 1. Molienda",
                "contenido": [
                    ("✅ Correcta: fina (tipo sal de mesa). Flujo controlado.", "verde"),
                    ("⚠ Molienda muy gruesa provoca café aguado.", "rojo"),
                    ("⚠ Molienda muy fina dificulta extracción.", "rojo")
                ]
            },
            {
                "titulo": "⏱ 2. Tiempo de extracción",
                "contenido": [
                    ("✅ Ideal: 25–30 segundos.", "verde"),
                    ("⚠ <20s: subextracción (ácido, sin cuerpo).", "rojo"),
                    ("⚠ >35s: sobreextracción (amargo, astringente).", "rojo")
                ]
            },
            {
                "titulo": "☁ 3. Crema",
                "contenido": [
                    ("✅ Color avellana, 2–4 mm, textura sedosa.", "verde"),
                    ("⚠ Crema clara, desaparece rápido, burbujas grandes.", "amarillo")
                ]
            },
            {
                "titulo": "💧 4. Flujo",
                "contenido": [
                    ("✅ Constante y firme.", "verde"),
                    ("⚠ Muy rápido (grueso) o muy lento (fino).", "amarillo")
                ]
            },
            {
                "titulo": "🎨 5. Perfil sensorial esperado",
                "contenido": [
                    ("Acidez cítrica (naranja, mandarina).", None),
                    ("Dulzor tipo caramelo o miel.", None),
                    ("Notas a almendra y avellana.", None),
                    ("Cuerpo medio a cremoso.", None),
                    ("Posgusto persistente y suave.", None)
                ]
            }
        ]

        colores = {
            "verde": (0, 100, 0),
            "amarillo": (184, 134, 11),
            "rojo": (139, 0, 0),
            None: (50, 50, 50)
        }

        # Título general
        self.set_font("DejaVu", "B", 14)
        self.set_fill_color(230, 230, 250)  # lavanda claro
        self.set_text_color(25, 40, 90)     # azul oscuro
        self.cell(0, 12, "Resumen de Evaluación del Espresso", new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
        self.ln(6)

        for bloque in bloques:
            # Título bloque
            self.set_fill_color(245, 245, 245)  # gris claro
            self.set_text_color(25, 40, 90)     # azul oscuro
            self.set_font("DejaVu", "B", 12)
            self.cell(0, 8, bloque["titulo"], new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)

            # Contenido
            self.set_font("DejaVu", "", 10)
            for linea, nivel in bloque["contenido"]:
                r, g, b = colores[nivel]
                self.set_text_color(r, g, b)
                self.multi_cell(0, 7, "  " + linea, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.ln(4)

        self.set_text_color(0, 0, 0)


if __name__ == "__main__":
    pdf = PDF()
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
    pdf.add_font("DejaVu", "B", "DejaVuSans-Bold.ttf", uni=True)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Aquí podrías añadir más contenido antes del resumen si quieres

    pdf.add_summary()

    pdf.output("Bitacora_Gourmet_Nanopresso_Evaluacion.pdf")
    print("PDF generado: Bitacora_Gourmet_Nanopresso_Evaluacion.pdf")
