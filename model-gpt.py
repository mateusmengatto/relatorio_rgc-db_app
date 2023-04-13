from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

# Define o estilo dos parágrafos
styles = getSampleStyleSheet()
nome_style = styles["Heading1"]
cliente_style = ParagraphStyle(name="ClienteStyle", fontName="Helvetica", fontSize=12, leading=14)
info_style = ParagraphStyle(name="InfoStyle", fontName="Helvetica", fontSize=10, leading=12)
comentario_style = ParagraphStyle(name="ComentarioStyle", fontName="Helvetica", fontSize=10, leading=12, spaceBefore=10)

# Define o nome do arquivo PDF
filename = "exemplo.pdf"

# Define os dados do cabeçalho
nome = "Exemplo de PDF"
cliente = "Cliente: Fulano de Tal"
ano = "Ano: 2023"
nota = "Nota: 10"

# Define os dados da tabela
dados = [
    ["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4", "Coluna 5", "Coluna 6"],
    ["Dado 1", "Dado 2", "Dado 3", "Dado 4", "Dado 5", "Dado 6"],
    ["Dado 7", "Dado 8", "Dado 9", "Dado 10", "Dado 11", "Dado 12"],
    ["Dado 13", "Dado 14", "Dado 15", "Dado 16", "Dado 17", "Dado 18"]
]

# Define o comentário
comentario = "Esse é um exemplo de PDF criado com ReportLab."

# Define o conteúdo do PDF
conteudo = []

# Adiciona o nome do relatório
conteudo.append(Paragraph(nome, nome_style))

# Adiciona as informações do cliente, ano e nota
conteudo.append(Paragraph(cliente, cliente_style))
conteudo.append(Paragraph(ano, info_style))
conteudo.append(Paragraph(nota, info_style))

# Adiciona a tabela
tabela = Table(dados)
tabela.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 14),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
    ("ALIGN", (0, 1), (-1, -1), "CENTER"),
    ("ALIGN", (1, 1), (-1, -1), "LEFT"),
    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 1), (-1, -1), 10),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]))

conteudo.append(tabela)
conteudo.append(Paragraph(comentario, comentario_style))

doc = SimpleDocTemplate(filename, pagesize=letter)
doc.build(conteudo)