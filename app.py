import streamlit as st

# 1. إعداد الصفحة لتدعم اللغة العربية وشكل الواجهة
st.set_page_config(page_title="النظام الذكي لحساب جرعة التخدير", page_icon="💉", layout="centered")

# إضافة CSS لضبط اتجاه النص والتصميم
st.markdown("""
    <style>
    * {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# 2. إظهار صورة اللوجو في المنتصف بأعلى الشاشة
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        pass  # في حال عدم رفع الصورة بعد، لن يظهر خطأ للمستخدم

# 3. العناوين الرئيسية
st.title("النظام الذكي لحساب جرعة التخدير 💉")
st.markdown("### تطبيق منصة المميز الذكية")

# 4. قواعد البيانات
anesthesia_drugs = {
    "Propofol (بروبوفول)": {"dose_range": (1.5, 2.5), "unit": "mg/kg", "concentration": "10 mg/ml", "conc_val": 10.0, "info": "يستخدم للتحريض (Induction) والتخدير المستمر."},
    "Thiopental (ثيوبنتال)": {"dose_range": (3.0, 5.0), "unit": "mg/kg", "concentration": "25 mg/ml", "conc_val": 25.0, "info": "تحريض سريع للتخدير. يمتلك خصائص مضادة للتشنج."},
    "Etomidate (إيتوميدات)": {"dose_range": (0.2, 0.3), "unit": "mg/kg", "concentration": "2 mg/ml", "conc_val": 2.0, "info": "مخدر تحريضي سريع. لا يؤثر على الدورة الدموية بشكل ملحوظ."},
    "Ketamine (كيتامين)": {"dose_range": (1.0, 2.0), "unit": "mg/kg", "concentration": "50 mg/ml", "conc_val": 50.0, "info": "مخدر تفارقي (Dissociative). يحافظ على التنفس التلقائي."},
    "Midazolam (ميدازولام)": {"dose_range": (0.05, 0.1), "unit": "mg/kg", "concentration": "1 mg/ml", "conc_val": 1.0, "info": "مهدئ ومزيل للقلق ويسبب فقدان الذاكرة التقدمي."},
    "Fentanyl (فينتانيل)": {"dose_range": (1.0, 2.0), "unit": "mcg/kg", "concentration": "50 mcg/ml", "conc_val": 50.0, "info": "مسكن أفيوني قوي وسريع التأثير."},
    "Succinylcholine (سكسنيل كولين)": {"dose_range": (1.0, 1.5), "unit": "mg/kg", "concentration": "50 mg/ml", "conc_val": 50.0, "info": "مرخي عضلي مزيل للاستقطاب، سريع جداً للتنبيب (RSI)."},
    "Rocuronium (روكورونيوم)": {"dose_range": (0.6, 1.2), "unit": "mg/kg", "concentration": "10 mg/ml", "conc_val": 10.0, "info": "مرخي عضلي غير مزيل للاستقطاب (NDMR). سريع التأثير."},
    "Atracurium (أتراكوريوم)": {"dose_range": (0.5, 0.6), "unit": "mg/kg", "concentration": "10 mg/ml", "conc_val": 10.0, "info": "مرخي عضلي يتفكك تلقائياً في بلازما الدم."},
    "Cisatracurium (سيس-أتراكوريوم)": {"dose_range": (0.15, 0.2), "unit": "mg/kg", "concentration": "2 mg/ml", "conc_val": 2.0, "info": "مرخي عضلي آمن جداً ومستقر، لا يفرز الهيستامين."}
}

disease_warnings = {
    "Propofol (بروبوفول)": {
        "أمراض القلب (Heart Disease)": "⚠️ تأثير المرض: يسبب توسعاً وعائياً. قلل الجرعة بنسبة 30-50% وإعطائها ببطء.",
        "ارتفاع ضغط الدم (Hypertension)": "ملاحظة: مرضى الضغط عرضة لتذبذب شديد في الضغط عند التحريض.",
        "ربو / أمراض تنفسية (Asthma)": "✅ خيار ممتاز: يمتلك خصائص موسعة للقصبات الهوائية."
    },
    "Ketamine (كيتامين)": {
        "ارتفاع ضغط الدم (Hypertension)": "⛔ تحذير: الكيتامين يرفع ضغط الدم. يُفضل تجنبه.",
        "أمراض القلب (Heart Disease)": "⛔ تحذير: يزيد من استهلاك عضلة القلب للأوكسجين.",
        "ربو / أمراض تنفسية (Asthma)": "✅ خيار مثالي: موسع قوي للقصبات الهوائية."
    },
    "Thiopental (ثيوبنتال)": {
        "ربو / أمراض تنفسية (Asthma)": "⛔ تحذير: يسبب تحرر الهيستامين مما يؤدي إلى تشنج قصبي حاد."
    },
    "Etomidate (إيتوميدات)": {
        "أمراض القلب (Heart Disease)": "✅ الخيار الأول: آمن جداً لمرضى القلب لثباته على الدورة الدموية."
    },
    "Succinylcholine (سكسنيل كولين)": {
        "فشل كلوي (Renal Failure)": "⛔ تحذير خطير: يرفع البوتاسيوم في الدم. يُمنع استخدامه لمرضى الفشل الكلوي."
    },
    "Atracurium (أتراكوريوم)": {
        "فشل كلوي (Renal Failure)": "✅ الخيار الأول: يتفكك تلقائياً في الدم.",
        "قصور كبدي (Hepatic Impairment)": "✅ الخيار الأول: آمن تماماً."
    }
}

# 5. إدخال البيانات في عمودين
col_a, col_b = st.columns(2)
with col_a:
    weight = st.number_input("الوزن (كغم):", min_value=1.0, max_value=300.0, value=70.0, step=1.0)
with col_b:
    age = st.number_input("العمر (سنة):", min_value=1, max_value=120, value=30, step=1)

diseases_list = ["لا يوجد (سليم)", "ارتفاع ضغط الدم (Hypertension)", "أمراض القلب (Heart Disease)", "ربو / أمراض تنفسية (Asthma)", "فشل كلوي (Renal Failure)", "قصور كبدي (Hepatic Impairment)"]
disease = st.selectbox("التاريخ المرضي:", diseases_list)

drug = st.selectbox("اختر الدواء:", list(anesthesia_drugs.keys()))

syringe_sizes = ["3 ml (cc)", "5 ml (cc)", "10 ml (cc)", "20 ml (cc)", "50 ml (cc)"]
syringe_str = st.selectbox("حجم السرنجة:", syringe_sizes, index=2)

st.write("---")

# 6. الحساب والنتائج
if st.button("تحليل وإظهار الجرعة والسحب 🧮", use_container_width=True):
    data = anesthesia_drugs[drug]
    min_dose = weight * data["dose_range"][0]
    max_dose = weight * data["dose_range"][1]
    
    min_volume_ml = min_dose / data["conc_val"]
    max_volume_ml = max_dose / data["conc_val"]
    syringe_capacity = int(syringe_str.split()[0])

    st.subheader("📋 التقرير السريري:")

    # العمر
    if age >= 65:
        st.warning("👴🏻 **تنبيه العمر:** المريض مسن، يُنصح بتخفيض الجرعة بنسبة 20-30%.")

    # الأمراض المزمنة
    if disease != "لا يوجد (سليم)":
        if drug in disease_warnings and disease in disease_warnings[drug]:
            st.info(f"🩺 **تأثير {disease}:**\n {disease_warnings[drug][disease]}")
        else:
            st.success("🩺 **تأثير المرض:** لا توجد تداخلات خطيرة شائعة، لكن المراقبة مطلوبة.")

    # الجرعة والسرنجة
    st.success(f"💊 **الجرعة المطلوبة:** {min_dose:.1f} إلى {max_dose:.1f} {data['unit'].split('/')[0]}")
    st.success(f"💉 **حجم السحب داخل السرنجة:** {min_volume_ml:.1f} ml إلى {max_volume_ml:.1f} ml")

    if max_volume_ml > syringe_capacity:
        st.error(f"⚠️ **تنبيه السرنجة:** الحجم المطلوب ({max_volume_ml:.1f} ml) أكبر من السرنجة المختارة ({syringe_capacity} ml). تحتاج لسرنجة أكبر!")

    # معلومات الدواء
    st.write(f"📌 **معلومات الدواء:** {data['info']}")
    st.write(f"💧 **التركيز المستخدم:** {data['concentration']}")

# 7. أزرار التواصل الاجتماعي وحقوق الملكية
st.markdown("""
    <style>
    .social-container {
        display: flex;
        justify-content: center;
        gap: 12px;
        margin-top: 40px;
        margin-bottom: 20px;
        flex-wrap: wrap;
        direction: rtl;
    }
    .social-btn {
        display: inline-block;
        padding: 12px 24px;
        color: white !important;
        text-decoration: none !important;
        border-radius: 25px;
        font-weight: bold;
        font-size: 15px;
        text-align: center;
        transition: 0.3s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        border: none;
    }
    .social-btn:hover {
        opacity: 0.85;
        transform: translateY(-3px);
        color: white !important;
        text-decoration: none !important;
    }
    .social-btn:visited, .social-btn:active {
        color: white !important;
        text-decoration: none !important;
    }
    .btn-youtube { background-color: #FF0000; }
    .btn-insta { background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); }
    .btn-telegram { background-color: #24A1DE; }
    
    .footer {
        background-color: #1a237e;
        color: #FFD700;
        text-align: center;
        padding: 15px;
        font-weight: bold;
        font-size: 16px;
        border-radius: 10px;
        margin-top: 20px;
        direction: rtl;
    }
    .footer p { 
        margin: 0; 
        text-align: center !important;
    }
    </style>

    <!-- الأزرار -->
    <div class="social-container">
        <a href="https://www.youtube.com/@bggt1/videos" target="_blank" class="social-btn btn-youtube">▶️ قناتي على اليوتيوب</a>
        <a href="https://www.instagram.com/ans.mo7mmed" target="_blank" class="social-btn btn-insta">📸 حسابي على الانستغرام</a>
        <a href="https://t.me/makderiq" target="_blank" class="social-btn btn-telegram">✈️ قناتي على التليكرام</a>
        <a href="https://t.me/mmeyaz" target="_blank" class="social-btn btn-telegram">✈️ قناة منصة المميز</a>
    </div>

    <!-- شريط الحقوق -->
    <div class="footer">
        <p>تطبيق تابع لمنصة المميز</p>
        <p>تم برمجته من قبل محمد أسعد السعد</p>
    </div>
""", unsafe_allow_html=True)
