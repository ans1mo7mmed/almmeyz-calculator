import streamlit as st
import time

# 1. إعداد الصفحة لتدعم اللغة العربية وشكل الواجهة
st.set_page_config(page_title="النظام الذكي لحساب جرعة التخدير", page_icon="💉", layout="centered")

# إضافة CSS لضبط اتجاه النص والتصميم والتوسيط وتنسيق أزرار الروابط وعدّاد الزيارات الذهبي
st.markdown("""
    <style>
    * {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif;
    }
    /* ضمان ظهور النصوص بالكامل وعدم قصها في القوائم المنسدلة على الموبايل */
    div[data-baseweb="select"] span {
        white-space: normal !important;
        overflow: visible !important;
        text-overflow: clip !important;
    }
    .disclaimer-box {
        background-color: #ffebee;
        color: #c62828;
        padding: 12px;
        border-radius: 10px;
        border: 1px solid #ef9a9a;
        margin-bottom: 20px;
        font-weight: bold;
        text-align: center;
        font-size: 13px;
    }
    /* تنسيق أزرار التبويبات بروح وتصميم التطبيق */
    .social-btn {
        display: inline-block;
        padding: 8px 16px;
        margin: 5px;
        border-radius: 12px;
        font-size: 14px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        transition: 0.3s;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .btn-youtube { background-color: #FF0000; color: white !important; }
    .btn-youtube:hover { background-color: #cc0000; }
    
    .btn-telegram { background-color: #0088cc; color: white !important; }
    .btn-telegram:hover { background-color: #006699; }
    
    .btn-mmeyaz { background-color: #2e7d32; color: white !important; }
    .btn-mmeyaz:hover { background-color: #1b5e20; }
    
    .btn-instagram { background-color: #E1306C; color: white !important; }
    .btn-instagram:hover { background-color: #c12258; }

    /* تصميم بالون عداد الزيارات الذهبي الصغير والناعم */
    .visitor-badge {
        background: linear-gradient(135deg, #fff8e1, #ffecb3);
        color: #b78103;
        padding: 6px 15px;
        border-radius: 20px;
        border: 1px solid #ffe082;
        font-size: 13px;
        font-weight: bold;
        text-align: center;
        display: inline-block;
        box-shadow: 0 2px 6px rgba(255, 193, 7, 0.2);
        margin: 10px auto;
    }
    </style>
""", unsafe_allow_html=True)

# 2. إظهار صورة اللوجو في المنتصف بأعلى الشاشة
col_l1, col_l2, col_l3 = st.columns([2, 1, 2])
with col_l2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        pass

# 3. عداد الزيارات التلقائي (يبدأ من 76392 ويزداد 500 كل دقيقة، متوافق مع Streamlit Session State)
if 'visit_time' not in st.session_state:
    st.session_state.visit_time = time.time()
    st.session_state.base_visitors = 76392

# حساب الزيارات بناءً على الوقت المنقضٍ (كل 60 ثانية يزيد 500 زائر)
elapsed_seconds = time.time() - st.session_state.visit_time
additional_visitors = int(elapsed_seconds / 60) * 500
current_visitors = st.session_state.base_visitors + additional_visitors

# عرض البالون الذهبي تحت اللوجو مباشرةً في المنتصف
st.markdown(f"""
<div style="text-align: center;">
    <div class="visitor-badge">
        👁️ عدد زيارات الموقع: <b>{current_visitors:,}</b> زائر
    </div>
</div>
""", unsafe_allow_html=True)

# إعادة تشغيل تلقائي للصفحة كل دقيقة (60 ثانية) ليقوم العداد بالتحديث المباشر
st.markdown(f"""
    <meta http-equiv="refresh" content="60">
""", unsafe_allow_html=True)


# 4. العناوين الرئيسية
st.title("النظام الذكي لحساب جرعة التخدير 💉")
st.markdown("### تطبيق منصة المميز الذكية")

# 5. إضافة تبويبات شبيهة بأزرار مسطيلة ناعمة الحواف لروابط التواصل
st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <a href="https://www.youtube.com/@bggt1/videos" target="_blank" class="social-btn btn-youtube">📺 قناة اليوتيوب</a>
    <a href="https://t.me/makderiq" target="_blank" class="social-btn btn-telegram">✈️ قناة التليكرام</a>
    <a href="https://t.me/mmeyaz" target="_blank" class="social-btn btn-mmeyaz">🎓 قناة منصة المميز</a>
    <a href="https://www.instagram.com/ans.mo7mmed" target="_blank" class="social-btn btn-instagram">📸 انستغرام</a>
</div>
""", unsafe_allow_html=True)

# 6. ملاحظة إخلاء المسؤولية الطبية
st.markdown("""
    <div class="disclaimer-box">
        ⚠️ إخلاء مسؤولية طبية: هذا التطبيق مخصص حصراً لأغراض الاطلاع والتعليم الطبي، ولا يُعتبر بديلاً عن القرار السريري للطبيب المختص.
    </div>
""", unsafe_allow_html=True)

# 7. قواعد البيانات الطبية المتقدمة والذكية لجميع الأدوية والتداخلات
anesthesia_drugs = {
    "Propofol (بروبوفول)": {
        "dose_range": (1.5, 2.5), 
        "unit": "mg/kg", 
        "concentration": "10 mg/ml", 
        "conc_val": 10.0, 
        "info": "مخدر وريدي سريع المفعول للتحريض والصيانة. يسبب توسعاً وعائياً وتثبيطاً تنفسياً.",
        "interactions": {
            "أدوية ضغط الدم / موسعات الأوعية": "⚠️ تداخل خطير: يضاعف هبوط ضغط الدم الحاد بسبب توسع الأوعية.",
            "مضادات الاكتئاب / المهدئات (Benzodiazepines/Opioids)": "⚠️ تداخل محتمل: تثبيط عميق ومضاعف للجهاز العصبي المركزي والتنفسي."
        }
    },
    "Thiopental (ثيوبنتال)": {
        "dose_range": (3.0, 5.0), 
        "unit": "mg/kg", 
        "concentration": "25 mg/ml", 
        "conc_val": 25.0, 
        "info": "باربيتورات سريع التحريض، مضاد للتشنج، يقلل ضغط الدماغ، ويسبب هبوط ضغط حاد.",
        "interactions": {
            "أدوية ضغط الدم / موسعات الأوعية": "⚠️ تداخل محتمل: هبوط حاد في الضغط نتيجة ضعف المقاومة الوعائية.",
            "مضادات الاكتئاب / المهدئات (Benzodiazepines/Opioids)": "⚠️ تداخل محتمل: تأخر حاد في الإفاقة وتثبيط تنفسي طويل الأمد."
        }
    },
    "Etomidate (إيتوميدات)": {
        "dose_range": (0.2, 0.3), 
        "unit": "mg/kg", 
        "concentration": "2 mg/ml", 
        "conc_val": 2.0, 
        "info": "مخدر ممتاز لمرضى القلب لثبات الهيموديناميك، يثبط الغدة الكظرية مؤقتاً.",
        "interactions": {
            "أدوية الكورتيزون / مثبطات الغدة الكظرية": "⚠️ ملاحظة: يثبط تخليق الكورتيزول ويجب الحذر الشديد في حالات الصدمة الإنتانية."
        }
    },
    "Ketamine (كيتامين)": {
        "dose_range": (1.0, 2.0), 
        "unit": "mg/kg", 
        "concentration": "50 mg/ml", 
        "conc_val": 50.0, 
        "info": "مخدر تفارقي، يحافظ على التنفس التلقائي ومنعكسات الحنجرة، موسع ممتاز للقصبات.",
        "interactions": {
            "أدوية هرمون الغدة الدرقية / مضادات الكولين": "⛔ تداخل خطير: ارتفاع جنوني في ضغط الدم وتسارع ضربات القلب.",
            "مضادات الاكتئاب ثلاثية الحلقات (TCAs)": "⛔ تحذير: خطر حدوث أزمة ارتفاع ضغط دم واعتلال قلبي خطير."
        }
    },
    "Midazolam (ميدازولام)": {
        "dose_range": (0.05, 0.1), 
        "unit": "mg/kg", 
        "concentration": "1 mg/ml", 
        "conc_val": 1.0, 
        "info": "بينزوديازيبين قصير المفعول، مزيل للقلق ومهدئ ومنسٍ.",
        "interactions": {
            "المسكنات الأفيونية (Opioids مثل الفنتانيل والمورفين)": "⛔ تداخل مميت محتمل: توقف مفاجئ بالتنفس وهبوط حاد بالأكسجة.",
            "أدوية المضادات الحيوية الفطرية أو الماكروليد (مثل Erythromycin)": "⚠️ تداخل محتمل: تثبيط الأيض الكبدي يطيل أثر الميدازولام أضعافاً."
        }
    },
    "Fentanyl (فينتانيل)": {
        "dose_range": (1.0, 2.0), 
        "unit": "mcg/kg", 
        "concentration": "50 mcg/ml", 
        "conc_val": 50.0, 
        "info": "مسكن أفيوني قوي جداً، يمنع الاستجابة العصبية للجراحة، يسبب خشونة الصدر بجرعات عالية.",
        "interactions": {
            "المهدئات ومضادات القلق (Benzodiazepines)": "⛔ تداخل خطير: تثبيط تنفسي عميق جداً وفقدان وعي مفاجئ.",
            "أدوية الاكتئاب (MAOIs)": "⛔ ممنوع تماماً: خطر تفاعلات سمية عصبية وتنفسية مميتة."
        }
    },
    "Succinylcholine (سكسنيل كولين)": {
        "dose_range": (1.0, 1.5), 
        "unit": "mg/kg", 
        "concentration": "50 mg/ml", 
        "conc_val": 50.0, 
        "info": "مرخي عضلي مزيل للاستقطاب الأسرع والأقصر مفعولاً لتنبيب الطوارئ (RSI).",
        "interactions": {
            "أدوية علاج الجلوكوما أو قطرات العين": "⚠️ تداخل محتمل: إطالة أمد الاسترخاء وتأخر العودة للتنفس التلقائي.",
            "أدوية الليثيوم النفسية": "⚠️ تداخل محتمل: إطالة غير متوقعة لفترة الحصار العصبي العضلي."
        }
    },
    "Rocuronium (روكورونيوم)": {
        "dose_range": (0.6, 1.2), 
        "unit": "mg/kg", 
        "concentration": "10 mg/ml", 
        "conc_val": 10.0, 
        "info": "مرخي عضلي غير مزيل للاستقطاب، يمكن عكسه بسرعة باستخدام Sugammadex.",
        "interactions": {
            "المضادات الحيوية من عائلة Aminoglycosides": "⚠️ تداخل محتمل: تعزز وتطيل مفعول الإرخاء العضلي."
        }
    },
    "Atracurium (أتراكوريوم)": {
        "dose_range": (0.5, 0.6), 
        "unit": "mg/kg", 
        "concentration": "10 mg/ml", 
        "conc_val": 10.0, 
        "info": "مرخي عضلي يتحلل ذاتياً بالبلازما، ممتاز لمرضى الكلى والكبد.",
        "interactions": {
            "أدوية علاج الصرع المزمنة": "⚠️ تداخل محتمل: مقاومة نسبية تتطلب جرعات أعلى."
        }
    },
    "Cisatracurium (سيس-أتراكوريوم)": {
        "dose_range": (0.15, 0.2), 
        "unit": "mg/kg", 
        "concentration": "2 mg/ml", 
        "conc_val": 2.0, 
        "info": "مشتق نقي للأتراكوريوم، لا يفرز هيستامين وآمن جداً لمرضى القلب والرئة.",
        "interactions": {
            "مرخيات العضلات الأخرى": "⚠️ تداخل محتمل: تداخل في حسابات وقت الإلغاء أو العكس الدوائي."
        }
    }
}

# 8. واجهة التقييم ما قبل التخدير الشاملة والمعمقة
st.subheader("📋 التقييم ما قبل التخدير")

col_1, col_2 = st.columns(2)
with col_1:
    weight = st.number_input("الوزن (كغم):", min_value=1.0, max_value=300.0, value=70.0, step=1.0)
    age = st.number_input("العمر (سنة):", min_value=1, max_value=120, value=30, step=1)
    
with col_2:
    asa_status = st.selectbox(
        "تصنيف ASA:",
        [
            "ASA I - مريض سليم",
            "ASA II - مرض جهازي خفيف",
            "ASA III - مرض جهازي شديد",
            "ASA IV - مرض يهدد الحياة",
            "ASA V - حالة ميؤوس منها"
        ]
    )
    fasting_status = st.selectbox(
        "حالة الصيام (NPO):", 
        [
            "صائم كلياً للفترة الموصى بها", 
            "غير صائم / خطر القشط", 
            "سوائل صافية فقط"
        ]
    )

st.markdown("#### 🫁 تقييم مجرى الهواء:")
col_air1, col_air2 = st.columns(2)
with col_air1:
    mallampati = st.selectbox(
        "تصنيف مالامباتي:",
        [
            "Class I (سهل جداً)",
            "Class II (سهل نسبياً)",
            "Class III (صعب نسبياً)",
            "Class IV (صعب للغاية)"
        ]
    )
with col_air2:
    mouth_opening = st.selectbox(
        "فتح الفم والمسافة:",
        [
            "طبيعي وكافي (> 3 أصابع)",
            "قصير أو محدود (< 3 أصابع)"
        ]
    )

diseases_list = [
    "لا يوجد (سليم)", 
    "ارتفاع ضغط الدم المزمن", 
    "أمراض القلب والشرايين", 
    "ربو شعبي أو انسداد رئوي", 
    "قصور وظائف الكلى المزمن", 
    "قصور وظائف الكبد",
    "السكري غير المنضبط",
    "تاريخ لفرط الحرارة الخبيث"
]
disease = st.selectbox("الأمراض المزمنة المصاحبة:", diseases_list)

current_medications = st.multiselect(
    "الأدوية الحالية للمريض:",
    [
        "أدوية ضغط الدم / حاصرات بيتا",
        "المسكنات الأفيونية المزمنة",
        "المهدئات ومضادات القلق",
        "أدوية الاكتئاب (MAOIs / TCAs)",
        "أدوية الغدة الدرقية",
        "المضادات الحيوية",
        "قطرات وعلاج الجلوكوما",
        "أدوية الليثيوم أو الصرع",
        "أدوية الكورتيزون"
    ]
)

st.write("---")
drug = st.selectbox("اختر دواء التخدير:", list(anesthesia_drugs.keys()))

syringe_sizes = ["3 ml (cc)", "5 ml (cc)", "10 ml (cc)", "20 ml (cc)", "50 ml (cc)"]
syringe_str = st.selectbox("حجم السرنجة:", syringe_sizes, index=2)

# إضافة خيار التخفيف بالنورمل سلاين (Normal Saline Dilution) للتعليم والتدريب العملي
st.markdown("#### 💧 خيارات تخفيف الدواء بالسرنجة:")
use_dilution = st.checkbox("تفعيل ميزة تخفيف الجرعة بالنورمل سلاين (Normal Saline) داخل السرنجة")
saline_volume_ml = 0.0
if use_dilution:
    saline_volume_ml = st.number_input("حجم النورمل سلاين المضاف لتخفيف الدواء (ml):", min_value=0.5, max_value=45.0, value=5.0, step=0.5)

st.write("---")

# 9. محرك اتخاذ القرار والتحليل الذكي مع حساب التخفيف
if st.button("تشغيل النظام الذكي وإصدار القرار السريري 🧮", use_container_width=True):
    data = anesthesia_drugs[drug]
    min_dose = weight * data["dose_range"][0]
    max_dose = weight * data["dose_range"][1]
    
    min_volume_ml = min_dose / data["conc_val"]
    max_volume_ml = max_dose / data["conc_val"]
    syringe_capacity = int(syringe_str.split()[0])

    st.subheader("📋 تقرير القرار السريري:")

    if "ASA IV" in asa_status or "ASA V" in asa_status:
        st.error("🚨 **تحذير حرج جداً:** المريض في حالة خطيرة أو مهددة للحياة، تتطلب عناية مركزة ومراقبة غازية متقدمة.")
    elif "ASA III" in asa_status:
        st.warning("⚠️ **تنبيه خاص:** المريض يعاني من مرض جهازي مهم، يجب تحضير الأدوية الإسعافية ومراقبة العلامات الحيوية.")
    else:
        st.success("✅ **تصنيف الحالة:** الحالة العامة مستقرة ومقبولة للعملية.")

    if "غير صائم" in fasting_status:
        st.error("🚨 **خطر استنشاق محتوى المعدة:** المريض غير صائم بالكامل! التطبيق الإلزامي: تقنية التحريض السريع (RSI) مع ضغط الغضروف الحلقي وإفراغ المعدة.")
    else:
        st.success("✅ **تقييم الصيام:** وضع الصيام طبيعي ولا توجد موانع.")

    if "Class III" in mallampati or "Class IV" in mallampati or "قصير أو محدود" in mouth_opening:
        st.error("⚠️ **إنذار مجرى الهواء الصعب:** مؤشرات لصعوبة التنبيب. يجب توفير منظار فيديو وقناع حنجري وتواجد عربة مجرى الهواء الصعب.")
    else:
        st.success("✅ **تقييم مجرى الهواء:** المؤشرات تدل على مجرى هواء طبيعي.")

    if age >= 65:
        st.warning("👴🏻 **تنبيه العمر (مسن):** يُوصى بشدة **تقليل الجرعة بنسبة 25-35%** وإعطاء الدواء ببطء شديد.")

    if disease != "لا يوجد (سليم)":
        if drug == "Propofol (بروبوفول)" and "أمراض القلب والشرايين" in disease:
            st.info("🩺 **تفاعل المرض:** يسبب هبوطاً إضافياً بالضغط. اخفض الجرعة بنسبة 40% وأعط سوائل وريدية مسبقة.")
        elif drug == "Ketamine (كيتامين)" and ("ارتفاع ضغط الدم المزمن" in disease or "أمراض القلب والشرايين" in disease):
            st.error("⛔ **تداخل مرضي خطير:** الكيتامين يرفع ضغط الدم ومعدل ضربات القلب ويزيد عبء القلب. استخدم Etomidate كبديل.")
        elif drug == "Thiopental (ثيوبنتال)" and "ربو شعبي أو انسداد رئوي" in disease:
            st.error("⛔ **خطر تشنج القصبات:** الثيوبنتال يحرر الهيستامين مسبباً تشنجاً قصبيكوياً خطيراً.")
        elif drug == "Succinylcholine (سكسنيل كولين)" and "قصور وظائف الكلى المزمن" in disease:
            st.error("⛔ **تحذير مميت:** يرفع نسبة البوتاسيوم بالدم وقد يسبب توقف قلب. استخدم Rocuronium كبديل.")
        else:
            st.success(f"🩺 **تقييم الحالة ({disease}):** تم رصد الحالة وتؤخذ بعين الاعتبار.")

    interaction_detected = False
    for med in current_medications:
        if med in data["interactions"]:
            st.error(f"💊 **تداخل دوائي حرج مع ({med}):**\n{data['interactions'][med]}")
            interaction_detected = True

    if not interaction_detected and len(current_medications) > 0:
        st.success("✅ **تدقيق الأدوية الحالية:** لا توجد تداخلات تعارضية مباشرة مسجلة.")

    st.write("---")

    # النتائج الحسابية للجرعة والسحب
    st.success(f"💊 **الجرعة المقدرة للمريض:** {min_dose:.1f} إلى {max_dose:.1f} {data['unit'].split('/')[0]}")
    st.success(f"💉 **حجم الدواء الصافي للسحب:** {min_volume_ml:.1f} ml إلى {max_volume_ml:.1f} ml")

    # حساب التخفيف بالنورمل سلاين للطلاب وتقنيي التخدير
    if use_dilution:
        avg_volume_ml = (min_volume_ml + max_volume_ml) / 2.0
        total_syringe_content = avg_volume_ml + saline_volume_ml
        new_concentration = (avg_volume_ml * data["conc_val"]) / total_syringe_content if total_syringe_content > 0 else 0
        
        st.info(f"""
        🧪 **إرشادات التخفيف العملي بالنورمل سلاين (Normal Saline Dilution):**
        * **حجم الدواء المسحوب (متوسط الجرعة):** {avg_volume_ml:.1f} ml
        * **حجم النورمل سلاين المضاف:** {saline_volume_ml} ml
        * **الحجم الكلي داخل السرنجة:** {total_syringe_content:.1f} ml
        * **التركيز الجديد بعد التخفيف:** تقريباً {new_concentration:.2f} mg/ml (أو mcg/ml حسب الدواء)
        * 💡 *هذه الطريقة تفيد الطلاب والتقنيين لإعطاء الجرعات الصغيرة تدريجياً وبدقة عالية لمنع الهبوط المفاجئ في الضغط.*
        """)

    # التحقق من سعة السرنجة الكلية (بما فيها السلاين إن وجد)
    total_check_volume = max_volume_ml + (saline_volume_ml if use_dilution else 0)
    if total_check_volume > syringe_capacity:
        st.error(f"⚠️ **خطأ في سعة السرنجة:** الحجم الكلي مع التخفيف ({total_check_volume:.1f} ml) يفوق سعة السرنجة المختارة ({syringe_capacity} ml)! الرجاء اختيار سرنجة ذات حجم أكبر.")

    st.write(f"📌 **الخصائص السريرية:** {data['info']}")
    st.write(f"💧 **التركيز الأساسي المعتمد:** {data['concentration']}")
