from pathlib import Path
from textwrap import wrap
from PIL import Image as PILImage, ImageOps, ImageEnhance
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.utils import ImageReader

ROOT = Path(__file__).resolve().parent
OUTPUT_PDF = ROOT / "reports" / "insurance_advisor_project_report.pdf"
SCREENSHOT_PAIRS = [
    ("Profile Creation", ROOT / "screenshots" / "insurance_app_profile_full.png", ROOT / "screenshots" / "insurance_app_profile_clean.png"),
    ("Document Upload", ROOT / "screenshots" / "insurance_app_upload_full.png", ROOT / "screenshots" / "insurance_app_upload_clean.png"),
    ("Chat View", ROOT / "screenshots" / "insurance_app_chat_full.png", ROOT / "screenshots" / "insurance_app_chat_clean.png"),
    ("Recommendation View", ROOT / "screenshots" / "insurance_app_recommendation_full.png", ROOT / "screenshots" / "insurance_app_recommendation_clean.png"),
]
TEST_SCREENSHOT = ROOT / "screenshots" / "insurance_app_test_data.png"


def add_scaled_image(story, image_path: Path, title: str, styles, page_width: float, page_height: float) -> None:
    if not image_path.exists():
        return
    story.append(PageBreak())
    story.append(Paragraph(f"<b>{title}</b>", styles["BodyText"]))

    reader = ImageReader(str(image_path))
    image_width, image_height = reader.getSize()
    aspect = image_width / image_height

    max_width = page_width - 0.8 * inch
    max_height = page_height - 1.2 * inch

    if aspect > (max_width / max_height):
        width = max_width
        height = max_width / aspect
    else:
        height = max_height
        width = max_height * aspect

    image = Image(str(image_path), width=width, height=height, kind="proportional")
    image.hAlign = "CENTER"
    story.append(image)


def escape_text(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def add_code_section(story, title: str, file_path: Path, styles) -> None:
    story.append(Paragraph(f"<b>{title}</b>", styles["DocHeading2"]))
    story.append(Paragraph(f"Source file: {file_path.relative_to(ROOT)}", styles["BodyText"]))
    story.append(Spacer(1, 0.1 * inch))

    content = file_path.read_text(encoding="utf-8")
    lines = []
    for line in content.splitlines():
        wrapped = wrap(line, width=112, break_long_words=False, break_on_hyphens=False)
        if wrapped:
            lines.extend(wrapped)
        else:
            lines.append("")

    code_text = "<br/>".join(escape_text(line) for line in lines)
    story.append(Paragraph(f"<font name='Courier' size='8'>{code_text}</font>", styles["DocCode"]))
    story.append(Spacer(1, 0.2 * inch))


def build_pdf() -> None:
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="DocTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=24, leading=28, textColor=colors.HexColor("#0f4c81"), spaceAfter=16))
    styles.add(ParagraphStyle(name="DocSubtitle", parent=styles["BodyText"], fontName="Helvetica", fontSize=11, leading=15, textColor=colors.HexColor("#4a4a4a"), spaceAfter=12))
    styles.add(ParagraphStyle(name="DocHeading2", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=colors.HexColor("#0f4c81"), spaceBefore=10, spaceAfter=6))
    styles.add(ParagraphStyle(name="DocCode", parent=styles["Code"], fontName="Courier", fontSize=8, leading=10, textColor=colors.black))

    doc = SimpleDocTemplate(str(OUTPUT_PDF), pagesize=A4, rightMargin=0.6 * inch, leftMargin=0.6 * inch, topMargin=0.6 * inch, bottomMargin=0.6 * inch)
    story = []

    story.append(Paragraph("Insurance Advisor Project Report", styles["DocTitle"]))
    story.append(Paragraph("Full source code bundle, test data, and application screenshots for profile creation, document upload, chat, and recommendation flows.", styles["DocSubtitle"]))
    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("<b>Application Screenshots</b>", styles["DocHeading2"]))
    story.append(Paragraph("The following views show the working Streamlit app in a cleaner, full-page layout.", styles["BodyText"]))
    for label, src_path, _ in SCREENSHOT_PAIRS:
        add_scaled_image(story, src_path, label, styles, page_width=8.27 * inch, page_height=11.69 * inch)
    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("<b>Test Data / Validation Screenshots</b>", styles["DocHeading2"]))
    if TEST_SCREENSHOT.exists():
        story.append(Paragraph("This section includes a unittest-style validation screenshot showing the app with sample insurance test data.", styles["BodyText"]))
        add_scaled_image(story, TEST_SCREENSHOT, "Test Data View", styles, page_width=8.27 * inch, page_height=11.69 * inch)
    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("<b>Project Summary</b>", styles["DocHeading2"]))
    story.append(Paragraph("The Insurance Advisor is a Streamlit-based assistant that lets users create a profile, upload insurance documents, ask questions about policy content, and receive tailored recommendations using an LLM and document retrieval workflow.", styles["BodyText"]))
    story.append(Spacer(1, 0.2 * inch))

    code_files = [
        ("Main Streamlit App", ROOT / "streamlit_app.py"),
        ("LLM Connector", ROOT / "llm.py"),
        ("RAG / Vector Store", ROOT / "rag.py"),
        ("Recommendation Prompt Builder", ROOT / "recommendation.py"),
        ("Shared Memory State", ROOT / "memory.py"),
        ("Workflow Graph Fallback", ROOT / "graph.py"),
        ("Pydantic Models", ROOT / "models.py"),
        ("LLM Smoke Test", ROOT / "test_llm.py"),
        ("Recommendation Prompt Tests", ROOT / "tests" / "test_recommendation_prompt.py"),
        ("Requirements", ROOT / "requirements.txt"),
    ]

    for title, file_path in code_files:
        if file_path.exists():
            add_code_section(story, title, file_path, styles)
        else:
            story.append(Paragraph(f"Missing file: {file_path.relative_to(ROOT)}", styles["BodyText"]))

    story.append(PageBreak())
    story.append(Paragraph("<b>Uploaded Test Data</b>", styles["DocHeading2"]))
    test_data_path = ROOT / "uploads" / "HealthSecurePlus_SOP.txt"
    if test_data_path.exists():
        add_code_section(story, "Insurance SOP Test Document", test_data_path, styles)

    doc.build(story)


if __name__ == "__main__":
    build_pdf()
