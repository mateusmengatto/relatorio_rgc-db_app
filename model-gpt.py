# import PyPDF2
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.units import inch
# from reportlab.lib import colors
# from reportlab.lib.styles import ParagraphStyle
# from reportlab.lib.enums import TA_CENTER
# from reportlab.lib import utils
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer


# # Criando o cabeçalho
# # def create_header(canvas, doc):
# #     canvas.saveState()
# #     canvas.drawImage('header.png', 0, 720, 595, 75)
# #     canvas.restoreState()


# # Criando o título
# def create_title(canvas, doc):
#     canvas.setFont('Helvetica-Bold', 18)
#     canvas.drawCentredString(297.5, 670, 'Relatório')
#     canvas.setFont('Helvetica', 14)
#     canvas.drawString(50, 620, 'Subtítulo 1')
#     canvas.drawString(50, 590, 'Subtítulo 2')
#     canvas.drawString(50, 560, 'Subtítulo 3')


# # Criando a tabela
# def create_table(canvas, doc):
#     data = [['Item', 'Quantidade', 'Preço'], 
#             ['Item 1', '1', 'R$ 10,00'], 
#             ['Item 2', '2', 'R$ 20,00'], 
#             ['Item 3', '3', 'R$ 30,00']]
#     table = Table(data, colWidths=[3*inch, 1*inch, 1.5*inch])
#     table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#CCCCCC')), 
#                                ('TEXTCOLOR', (0,0), (-1,0), colors.black), 
#                                ('ALIGN', (0,0), (-1,0), 'CENTER'), 
#                                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
#                                ('FONTSIZE', (0,0), (-1,0), 12),
#                                ('BOTTOMPADDING', (0,0), (-1,0), 12),
#                                ('BACKGROUND', (0,1), (-1,-1), colors.white), 
#                                ('TEXTCOLOR', (0,1), (-1,-1), colors.black), 
#                                ('ALIGN', (0,1), (-1,-1), 'CENTER'), 
#                                ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
#                                ('FONTSIZE', (0,1), (-1,-1), 10),
#                                ('GRID', (0,0), (-1,-1), 1, colors.black)]))
#     table.wrapOn(canvas, 0, 0)
#     table.drawOn(canvas, 50, 400)


# # Criando a caixa de texto
# def create_text_box(canvas, doc):
#     style = ParagraphStyle(name='Normal', fontName='Helvetica', fontSize=12, leading=14)
#     text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris."
#     p = Paragraph(text, style)
#     p.wrapOn(canvas, 500, 200)
#     p.drawOn(canvas, 50, 200)


# # Criando o documento
# doc = SimpleDocTemplate('relatorio.pdf', pagesize=A4)
# doc.build()
# # create_title, create_table, create_text_box])

# with open('relatorio.pdf', 'rb') as pdf_file:
#     reader = PyPDF2.PdfFileReader(pdf_file)
#     print(reader.numPages) # verificar o número de páginas


# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen import canvas

# w, h = A4
# c = canvas.Canvas("shapes.pdf", pagesize=A4)
# c.drawString(30, h - 50, "Line")
# x = 120
# y = h - 45
# b = 'Lineedit confirmations'
# c.line(x, y, x + 100, y)
# c.drawString(30, h - 100, b)
# c.rect(x, h - 120, 100, 50)
# c.drawString(30, h - 170, "Circle")
# c.circle(170, h - 165, 20)
# c.drawString(30, h - 240, "Ellipse")
# c.ellipse(x, y - 170, x + 100, y - 220)
# c.showPage()
# c.save()
# # ____________________________________

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

doc = SimpleDocTemplate("simple_table_grid.pdf", pagesize=letter)
# container for the 'Flowable' objects
elements = []

data= [['00', '01', '02', '03', '04'],
['10', '11', '12', '13', '14'],
['20', '21', '22', '23', '24'],
['30', '31', '32', '33', '34']]
t=Table(data,5*[0.4*inch], 4*[0.4*inch])
t.setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
('TEXTCOLOR',(1,1),(-2,-2),colors.red),
('VALIGN',(0,0),(0,-1),'TOP'),
('TEXTCOLOR',(0,0),(0,-1),colors.blue),
('ALIGN',(0,-1),(-1,-1),'CENTER'),
('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
('BOX', (0,0), (-1,-1), 0.25, colors.black),
]))

elements.append(t)
# write the document to disk
doc.build(elements)
