# ===================== IMPORTS =====================
import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from PIL import Image as PILImage
import io
import datetime
import qrcode

# ===================== PATHS =====================
NORMAL_REF = "assets/normal.jpeg"
PNEUMONIA_REF = "assets/virus.jpeg"

# ===================== UI STYLE =====================
st.markdown("""
<style>
.stApp { background:#012d1b; color:white; }

.alert {
    display:inline-block;
    padding:8px 22px;
    border-radius:18px;
    font-size:18px;
    font-weight:700;
    background:#8b0000;
    color:white;
    animation: blink 0.45s infinite;
}

@keyframes blink {
    0% { background:#8b0000; }
    50% { background:#ff1a1a; }
    100% { background:#8b0000; }
}

.black-btn button {
    background:black !important;
    color:white !important;
    padding:10px 22px;
    font-weight:600;
    border-radius:6px;
}
</style>
""", unsafe_allow_html=True)

# ===================== LOAD MODEL =====================
model = tf.keras.models.load_model("S_model (1).keras")

# ===================== PREDICTION =====================
#   ❗ No scaling ❗ No preprocess_input
#   Model already has Rescaling(1/255)
# ===============================
def predict(uploaded):
    img = image.load_img(uploaded, target_size=(224, 224))
    arr = image.img_to_array(img)

    arr_exp = np.expand_dims(arr, axis=0)   # bas ye hi chahiye

    preds = model.predict(arr_exp)[0]       # output = [normal, pneumonia]

    normal_prob = preds[0]
    pneumonia_prob = preds[1]

    return normal_prob, pneumonia_prob, arr.astype("uint8")

# ===================== PDF GENERATION (FINAL FIXED) =====================
def create_pdf(name, age, diagnosis, conf, img_array):

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # ---------- HEADER ----------
    y = height - 60
    c.setFont("Helvetica-Bold", 25)
    c.drawCentredString(width/2, y, "New Standard Institute of Radiology & Imaging")

    y -= 18
    c.setFont("Helvetica", 11)
    c.drawCentredString(width/2, y, "Reg. No: NSIRI/DELHI/2025-09")

    # QR
    qr = qrcode.QRCode(box_size=2, border=1)
    qr.add_data("https://github.com/HemantMishra2003")
    qr.make()
    qr_img = qr.make_image()
    qr_buf = io.BytesIO()
    qr_img.save(qr_buf, format="PNG")
    qr_buf.seek(0)
    c.drawImage(ImageReader(qr_buf), width-90, height-150, 55, 55)

    # ---------- TITLE ----------
    y -= 40
    c.setFont("Helvetica-Bold", 21)
    c.drawCentredString(width/2, y, "Chest X-Ray AI Report")

    y -= 25
    c.setFont("Helvetica-Bold", 17)
    c.drawCentredString(width/2, y, diagnosis)

    y -= 18
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width/2, y, f"Confidence: {conf:.2f}%")

    # ---------- IMAGES (SIDE BY SIDE – SAME SIZE) ----------
    y -= 30
    img_w = 230
    img_h = 200
    gap = 30

    left_x = (width - (img_w * 2 + gap)) / 2
    right_x = left_x + img_w + gap
    img_y = y - img_h

    # ===== LEFT IMAGE: Uploaded Chest X-Ray (ALWAYS SAME) =====
    pil_img = PILImage.fromarray(img_array)
    buf1 = io.BytesIO()
    pil_img.save(buf1, format="JPEG")
    buf1.seek(0)
    c.drawImage(ImageReader(buf1), left_x, img_y, img_w, img_h)

    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(
        left_x + img_w / 2,
        img_y - 14,
        "Uploaded Chest X-Ray"
    )

    # ===== RIGHT IMAGE: OPPOSITE CONDITION (LOGIC FIXED) =====
    if "Pneumonia" in diagnosis:
        ref_path = NORMAL_REF
        ref_label = "Healthy Chest X-Ray (Reference)"
    else:
        ref_path = PNEUMONIA_REF
        ref_label = "Pneumonia Chest X-Ray (Reference)"

    ref_img = PILImage.open(ref_path)
    buf2 = io.BytesIO()
    ref_img.save(buf2, format="JPEG")
    buf2.seek(0)
    c.drawImage(ImageReader(buf2), right_x, img_y, img_w, img_h)

    c.drawCentredString(
        right_x + img_w / 2,
        img_y - 14,
        ref_label
    )

    # ---------- PATIENT INFO ----------
    y = img_y - 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, y, "Patient Information:")

    c.setFont("Helvetica", 12)
    y -= 16
    c.drawString(40, y, f"Name: {name or 'Not Provided'}")
    y -= 16
    c.drawString(40, y, f"Age: {age or 'Not Provided'}")
    y -= 16
    c.drawString(40, y, f"Date: {datetime.datetime.now().strftime('%d-%m-%Y')}")

    # ---------- AI INTERPRETATION ----------
    y -= 30
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, y, "AI Interpretation:")

    c.setFont("Helvetica", 11)
    y -= 16
    if "Healthy" in diagnosis:
        c.drawString(40, y, "- Lungs appear healthy and clear.")
        y -= 14
        c.drawString(40, y, "- No signs of pneumonia or opacity.")
    else:
        c.drawString(40, y, "- Lung opacity detected.")
        y -= 14
        c.drawString(40, y, "- Indicators consistent with pneumonia.")
        y -= 14
        c.drawString(40, y, "- Medical consultation recommended.")

  #  ---------- FOOTER ----------
    y -= 30
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(width/2, y, "■ This AI Model is Developed in the Guidance of Dr. VISHWAS MISHRA SIR (Rolls-Royce) ■")

    y -= 22
    c.setFont("Helvetica", 11)
    c.drawCentredString(width/2, y, "Scan my QR code to see my other projects")

    y -= 13
    c.drawCentredString(width/2, y, "Email: hemantmishra1452968@gmail.com | Contact: +91-9250243706")

    y -= 13
    c.drawCentredString(width/2, y, "This is AI Model for Education Purpose Only. not for Medical Diagnosis")

    c.save()
    buffer.seek(0)
    return buffer

# ===================== UI =====================
st.title("🫁 Pneumonia Detector AI Model")

st.markdown(
    "<p style='margin-top:-18px; font-size:14px; color:#9e9e9e; font-weight:500;'>"
    "DenseNet-121 Architecture"
    "</p>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)
name = col1.text_input("Patient Name")
age = col2.text_input("Patient Age")

upload = st.file_uploader("Upload Chest X-Ray", type=["jpg","jpeg","png"])

if upload:
    st.image(upload, width=360)

    st.markdown("<div class='black-btn'>", unsafe_allow_html=True)
    scan = st.button("🔍 Scan X-Ray")
    st.markdown("</div>", unsafe_allow_html=True)

    if scan:
        normal, pneumonia, original = predict(upload)

        if pneumonia > normal:
            diagnosis = "Pneumonia Detected"
            conf = pneumonia * 100
            st.markdown(f"<div class='alert'>{diagnosis}</div>", unsafe_allow_html=True)
            risk = "HIGH"
        else:
            diagnosis = "Healthy Lung Detected"
            conf = normal * 100
            st.success(diagnosis)
            risk = "LOW"

        st.markdown(f"**Confidence:** {conf:.2f}%")
        st.markdown(f"**Risk Level:** {risk}")

        pdf = create_pdf(name, age, diagnosis, conf, original)

        st.markdown("<div class='black-btn'>", unsafe_allow_html=True)
        st.download_button(
            "📥 Download Report",
            pdf,
            "Patient_XRay_Report.pdf",
            "application/pdf"
        )
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "<p style='text-align:center; font-size:14px; color:#9e9e9e; font-weight:500;'>"
    "<b>Acknowledgement:</b><br>"
    "Guided by Dr.Vishwas Mishra Sir (Rolls-Royce)"
    "</p>",
    unsafe_allow_html=True
)
