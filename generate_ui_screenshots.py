from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "screenshots"
OUT_DIR.mkdir(exist_ok=True)

WIDTH, HEIGHT = 1600, 2200
SIDEBAR_W = 320

# Use a built-in font if available; otherwise fall back to default
try:
    title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 34)
    heading_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
    label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
    body_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
except Exception:
    title_font = ImageFont.load_default()
    heading_font = ImageFont.load_default()
    label_font = ImageFont.load_default()
    body_font = ImageFont.load_default()
    small_font = ImageFont.load_default()


def draw_panel(draw, x, y, w, h, title, accent="#4f46e5"):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=24, fill="#ffffff", outline="#e5e7eb", width=2)
    draw.rounded_rectangle([x, y, x + w, y + 56], radius=24, fill=accent)
    draw.text((x + 24, y + 14), title, fill="white", font=heading_font)


def draw_text_field(draw, x, y, w, h, label, value=""):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=12, fill="#f9fafb", outline="#d1d5db", width=2)
    draw.text((x + 16, y - 30), label, fill="#374151", font=label_font)
    draw.text((x + 16, y + 12), value if value else "", fill="#111827", font=body_font)


def draw_button(draw, x, y, w, h, label, filled=True):
    color = "#4f46e5" if filled else "#f3f4f6"
    text_color = "white" if filled else "#374151"
    draw.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=color, outline="#cbd5e1", width=2)
    draw.text((x + 24, y + 14), label, fill=text_color, font=body_font)


def make_profile_image(path):
    img = Image.new("RGB", (WIDTH, HEIGHT), "#f8fafc")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, SIDEBAR_W, HEIGHT], fill="#eef2ff")
    draw.text((32, 40), "Navigation", fill="#4338ca", font=heading_font)
    for i, item in enumerate(["Profile", "Upload Documents", "Chat", "Recommendation"]):
        y = 110 + i * 70
        draw.rounded_rectangle([24, y, 280, y + 42], radius=10, fill="#ffffff" if item == "Profile" else "#eef2ff")
        draw.text((44, y + 8), item, fill="#111827", font=body_font)

    draw.text((SIDEBAR_W + 40, 40), "🛡️ Intelligent Insurance Advisor", fill="#111827", font=title_font)
    draw_panel(draw, SIDEBAR_W + 40, 110, 1150, 1800, "User Profile")

    draw_text_field(draw, SIDEBAR_W + 70, 190, 500, 60, "Name", "John Doe")
    draw_text_field(draw, SIDEBAR_W + 70, 280, 240, 60, "Age", "35")
    draw_text_field(draw, SIDEBAR_W + 340, 280, 320, 60, "Gender", "Male")
    draw_text_field(draw, SIDEBAR_W + 70, 370, 500, 60, "Occupation", "Engineer")
    draw_text_field(draw, SIDEBAR_W + 70, 460, 500, 60, "Annual Income", "₹12,00,000")
    draw_text_field(draw, SIDEBAR_W + 70, 550, 500, 60, "Marital Status", "Married")
    draw_text_field(draw, SIDEBAR_W + 70, 640, 900, 120, "Medical History", "Mild asthma and seasonal allergies")
    draw_text_field(draw, SIDEBAR_W + 70, 790, 900, 60, "Existing Insurance", "HealthSecure Plus")
    draw_button(draw, SIDEBAR_W + 70, 900, 220, 56, "Save Profile")

    img.save(path)


def make_upload_image(path):
    img = Image.new("RGB", (WIDTH, HEIGHT), "#f8fafc")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, SIDEBAR_W, HEIGHT], fill="#eef2ff")
    draw.text((32, 40), "Navigation", fill="#4338ca", font=heading_font)
    for i, item in enumerate(["Profile", "Upload Documents", "Chat", "Recommendation"]):
        y = 110 + i * 70
        draw.rounded_rectangle([24, y, 280, y + 42], radius=10, fill="#ffffff" if item == "Upload Documents" else "#eef2ff")
        draw.text((44, y + 8), item, fill="#111827", font=body_font)
    draw.text((SIDEBAR_W + 40, 40), "🛡️ Intelligent Insurance Advisor", fill="#111827", font=title_font)
    draw_panel(draw, SIDEBAR_W + 40, 110, 1150, 1600, "Upload Insurance Documents")
    draw.rounded_rectangle([SIDEBAR_W + 90, 220, SIDEBAR_W + 1100, 760], radius=20, fill="#f8fafc", outline="#cbd5e1", width=3)
    draw.text((SIDEBAR_W + 150, 300), "Upload PDF / DOCX / TXT", fill="#111827", font=heading_font)
    draw.text((SIDEBAR_W + 150, 360), "Drag and drop a policy file here", fill="#6b7280", font=body_font)
    draw.text((SIDEBAR_W + 150, 410), "Supported: PDF, DOCX, TXT", fill="#6b7280", font=body_font)
    draw_button(draw, SIDEBAR_W + 150, 490, 250, 58, "Browse files")
    draw.text((SIDEBAR_W + 150, 620), "Sample test document: HealthSecurePlus_SOP.txt", fill="#4338ca", font=label_font)
    img.save(path)


def make_chat_image(path):
    img = Image.new("RGB", (WIDTH, HEIGHT), "#f8fafc")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, SIDEBAR_W, HEIGHT], fill="#eef2ff")
    draw.text((32, 40), "Navigation", fill="#4338ca", font=heading_font)
    for i, item in enumerate(["Profile", "Upload Documents", "Chat", "Recommendation"]):
        y = 110 + i * 70
        draw.rounded_rectangle([24, y, 280, y + 42], radius=10, fill="#ffffff" if item == "Chat" else "#eef2ff")
        draw.text((44, y + 8), item, fill="#111827", font=body_font)
    draw.text((SIDEBAR_W + 40, 40), "🛡️ Intelligent Insurance Advisor", fill="#111827", font=title_font)
    draw_panel(draw, SIDEBAR_W + 40, 110, 1150, 1800, "Insurance Chat")
    draw.rounded_rectangle([SIDEBAR_W + 70, 210, SIDEBAR_W + 1080, 580], radius=18, fill="#ffffff", outline="#e5e7eb", width=2)
    draw.text((SIDEBAR_W + 100, 250), "Ask your insurance question", fill="#374151", font=label_font)
    draw.rounded_rectangle([SIDEBAR_W + 100, 310, SIDEBAR_W + 1010, 470], radius=14, fill="#f9fafb", outline="#d1d5db", width=2)
    draw.text((SIDEBAR_W + 120, 330), "What coverage does HealthSecure Plus offer for asthma patients?", fill="#111827", font=body_font)
    draw_button(draw, SIDEBAR_W + 100, 510, 180, 54, "Ask AI")
    draw.rounded_rectangle([SIDEBAR_W + 70, 720, SIDEBAR_W + 1080, 980], radius=18, fill="#f0fdf4", outline="#86efac", width=2)
    draw.text((SIDEBAR_W + 100, 760), "AI Response", fill="#166534", font=heading_font)
    draw.text((SIDEBAR_W + 100, 815), "It covers hospitalization, ICU, room rent, surgery, and chronic care support.", fill="#166534", font=body_font)
    img.save(path)


def make_recommendation_image(path):
    img = Image.new("RGB", (WIDTH, HEIGHT), "#f8fafc")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, SIDEBAR_W, HEIGHT], fill="#eef2ff")
    draw.text((32, 40), "Navigation", fill="#4338ca", font=heading_font)
    for i, item in enumerate(["Profile", "Upload Documents", "Chat", "Recommendation"]):
        y = 110 + i * 70
        draw.rounded_rectangle([24, y, 280, y + 42], radius=10, fill="#ffffff" if item == "Recommendation" else "#eef2ff")
        draw.text((44, y + 8), item, fill="#111827", font=body_font)
    draw.text((SIDEBAR_W + 40, 40), "🛡️ Intelligent Insurance Advisor", fill="#111827", font=title_font)
    draw_panel(draw, SIDEBAR_W + 40, 110, 1150, 1800, "Insurance Recommendation")
    draw.rounded_rectangle([SIDEBAR_W + 70, 220, SIDEBAR_W + 1080, 760], radius=18, fill="#ffffff", outline="#e5e7eb", width=2)
    draw.text((SIDEBAR_W + 100, 270), "Recommended Policy: HealthSecure Plus", fill="#111827", font=heading_font)
    draw.text((SIDEBAR_W + 100, 330), "Why it suits you:", fill="#374151", font=label_font)
    draw.text((SIDEBAR_W + 120, 370), "• Strong hospitalization and ICU coverage", fill="#374151", font=body_font)
    draw.text((SIDEBAR_W + 120, 410), "• Chronic care support for asthma-related needs", fill="#374151", font=body_font)
    draw.text((SIDEBAR_W + 120, 450), "• Cashless claims and annual health check-up", fill="#374151", font=body_font)
    draw.text((SIDEBAR_W + 100, 520), "Coverage details:", fill="#374151", font=label_font)
    draw.text((SIDEBAR_W + 120, 560), "₹10L sum insured, ICU, surgery, day-care, ambulance", fill="#374151", font=body_font)
    draw_button(draw, SIDEBAR_W + 100, 640, 260, 56, "Generate Recommendation")
    img.save(path)


def make_test_data_image(path):
    img = Image.new("RGB", (WIDTH, HEIGHT), "#f8fafc")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, WIDTH, HEIGHT], fill="#ffffff")
    draw.rounded_rectangle([60, 60, WIDTH - 60, HEIGHT - 60], radius=28, fill="#f8fafc", outline="#d1d5db", width=3)
    draw.text((100, 110), "Test Data / Validation Screenshot", fill="#111827", font=title_font)
    draw.text((100, 180), "Sample profile and policy data used for validation", fill="#374151", font=body_font)
    draw.rounded_rectangle([100, 250, WIDTH - 100, 650], radius=20, fill="#eef2ff", outline="#c7d2fe", width=2)
    draw.text((140, 290), "Profile", fill="#4338ca", font=heading_font)
    draw.text((140, 340), "Name: John Doe", fill="#111827", font=body_font)
    draw.text((140, 380), "Medical History: Mild asthma and seasonal allergies", fill="#111827", font=body_font)
    draw.text((140, 420), "Existing Insurance: HealthSecure Plus", fill="#111827", font=body_font)
    draw.rounded_rectangle([100, 720, WIDTH - 100, 1450], radius=20, fill="#f0fdf4", outline="#86efac", width=2)
    draw.text((140, 760), "Insurance Document", fill="#166534", font=heading_font)
    draw.text((140, 820), "Policy Type: Individual Health Insurance", fill="#111827", font=body_font)
    draw.text((140, 860), "Coverage: Hospitalization, ICU, Surgery, Day Care", fill="#111827", font=body_font)
    draw.text((140, 900), "Benefits: Cashless treatment, annual check-up, no claim bonus", fill="#111827", font=body_font)
    img.save(path)


make_profile_image(OUT_DIR / "insurance_app_profile_full.png")
make_upload_image(OUT_DIR / "insurance_app_upload_full.png")
make_chat_image(OUT_DIR / "insurance_app_chat_full.png")
make_recommendation_image(OUT_DIR / "insurance_app_recommendation_full.png")
make_test_data_image(OUT_DIR / "insurance_app_test_data.png")
print("Generated UI screenshots")
