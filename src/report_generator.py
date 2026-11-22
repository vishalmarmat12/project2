"""
Professional PDF Report Generator Module
Uses ReportLab to build executive-ready data analysis reports.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas


class NumberedCanvas(canvas.Canvas):
    """Adds running headers and footers with dynamic page numbering."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#7f8c8d"))
        
        # Header line (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 755, "Multi-Domain Data Analysis Portfolio | Executive Research Report")
            self.setStrokeColor(colors.HexColor("#bdc3c7"))
            self.setLineWidth(0.5)
            self.line(54, 748, 558, 748)
            
        # Footer
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 36, page_text)
        self.drawString(54, 36, "CONFIDENTIAL & PROPRIETARY | PREPARED BY VISHAL PARMAR")
        self.setStrokeColor(colors.HexColor("#bdc3c7"))
        self.setLineWidth(0.5)
        self.line(54, 48, 558, 48)
        self.restoreState()


def create_project_report(
    pdf_path: str,
    title: str,
    domain: str,
    executive_summary: str,
    kpi_data: list,
    findings: list,
    recommendations: list,
    chart_paths: list,
    dataset_overview: dict
):
    """
    Builds a multi-page, polished PDF report.
    """
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#1a252f'),
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#2980b9'),
        spaceAfter=15
    )
    
    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#2c3e50'),
        spaceBefore=14,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#2c3e50')
    )
    
    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor('#1c2833')
    )
    
    story = []
    
    # Header Title Banner
    story.append(Paragraph(title, title_style))
    story.append(Paragraph(f"DOMAIN: {domain.upper()} | PORTFOLIO PROJECT COMPREHENSIVE STUDY", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#2980b9"), spaceAfter=12))
    
    # Executive Summary Card
    story.append(Paragraph("1. Executive Summary", h2_style))
    summary_cell = [
        Paragraph(f"<b>Key Objective:</b> {executive_summary}", callout_style)
    ]
    summary_table = Table([[summary_cell]], colWidths=[504])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8f9fa')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#d6dbdf')),
        ('PADDING', (0, 0), (-1, -1), 10),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 10))
    
    # Dataset Profile & KPIs
    story.append(Paragraph("2. Dataset Profile & Primary Key Performance Indicators (KPIs)", h2_style))
    
    # Profile metadata
    meta_rows = [
        [Paragraph(f"<b>Records Audited:</b> {dataset_overview.get('records', 'N/A')}", body_style),
         Paragraph(f"<b>Attributes:</b> {dataset_overview.get('attributes', 'N/A')}", body_style)],
        [Paragraph(f"<b>Data Completeness:</b> {dataset_overview.get('completeness', '100%')}", body_style),
         Paragraph(f"<b>Timeframe:</b> {dataset_overview.get('timeframe', 'Annual')}", body_style)]
    ]
    meta_table = Table(meta_rows, colWidths=[252, 252])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#edf2f7')),
        ('PADDING', (0, 0), (-1, -1), 6),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e0')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 8))
    
    # KPI Grid Table
    formatted_kpi = []
    header_row = [Paragraph(f"<b>{c}</b>", ParagraphStyle('TH', parent=body_style, textColor=colors.white, fontName='Helvetica-Bold')) for c in kpi_data[0]]
    formatted_kpi.append(header_row)
    for r in kpi_data[1:]:
        formatted_kpi.append([Paragraph(str(cell), body_style) for cell in r])
        
    kpi_table = Table(formatted_kpi, colWidths=[150, 110, 110, 134])
    kpi_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#bdc3c7')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')]),
        ('PADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(kpi_table)
    story.append(Spacer(1, 14))
    
    # Visual Analytics & Empirical Findings
    story.append(Paragraph("3. Analytical Visualizations & Key Empirical Insights", h2_style))
    
    # Embed up to 4 charts in pairs or single blocks
    for idx, chart_path in enumerate(chart_paths):
        if os.path.exists(chart_path):
            img = Image(chart_path, width=480, height=240)
            story.append(img)
            
            # Associated Finding
            finding_text = findings[idx] if idx < len(findings) else "Data observation documented above."
            f_p = Paragraph(f"<b>Figure {idx+1} Analysis:</b> {finding_text}", body_style)
            f_table = Table([[f_p]], colWidths=[480])
            f_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f4f6f7')),
                ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#d5dbdb')),
                ('PADDING', (0, 0), (-1, -1), 6),
            ]))
            story.append(f_table)
            story.append(Spacer(1, 12))
            
    # Business Insights & Recommendations
    story.append(Spacer(1, 6))
    story.append(Paragraph("4. Actionable Business Insights & Strategic Recommendations", h2_style))
    
    rec_rows = [
        [
            Paragraph("<b>#</b>", ParagraphStyle('RTH', parent=body_style, textColor=colors.white, fontName='Helvetica-Bold')),
            Paragraph("<b>Observation / Vulnerability</b>", ParagraphStyle('RTH', parent=body_style, textColor=colors.white, fontName='Helvetica-Bold')),
            Paragraph("<b>Strategic Recommendation</b>", ParagraphStyle('RTH', parent=body_style, textColor=colors.white, fontName='Helvetica-Bold')),
            Paragraph("<b>Target Impact</b>", ParagraphStyle('RTH', parent=body_style, textColor=colors.white, fontName='Helvetica-Bold'))
        ]
    ]
    for i, rec in enumerate(recommendations, 1):
        rec_rows.append([
            Paragraph(str(i), body_style),
            Paragraph(rec.get('finding', ''), body_style),
            Paragraph(rec.get('action', ''), body_style),
            Paragraph(rec.get('impact', ''), body_style)
        ])
        
    rec_table = Table(rec_rows, colWidths=[24, 160, 190, 130])
    rec_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#16a085')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#bdc3c7')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0fdf4')]),
        ('PADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(rec_table)
    
    # Build Document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Generated PDF report: {pdf_path}")
