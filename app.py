import streamlit as st

# 1. إعداد الصفحة لتدعم اللغة العربية وشكل الواجهة
st.set_page_config(page_title="النظام الذكي لحساب جرعة التخدير", page_icon="💉", layout="centered")

# إضافة CSS لضبط اتجاه النص والتصميم والتوسيط وحل مشكلة النصوص الطويلة على الهواتف
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
    </style>
""", unsafe_allow_html=True)

# 2. إظهار صورة اللوجو في المنتصف بأعلى الشاشة
col_l1, col_l2, col_l3 = st.columns([2, 1, 2])
with col_l2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        pass

# 3. العناوين الرئيسية
st.title("النظام الذكي لحساب جرعة التخدير 💉")
st.markdown("### تطبيق منصة المميز الذكية")

# 4. ملاحظة إخلاء المسؤولية الطبية
st.markdown("""
    <div class="disclaimer-box">
        ⚠️ إخلاء مسؤولية طبية: هذا التطبيق مخصص حصراً لأغراض الاطلاع والتعليم الطبي، ولا يُعتبر بديلاً عن القرار السريري للطبيب المختص.
    </div>
""", unsafe_allow_html=True)

# 5. قواعد البيانات الطبية المتقدمة والذكية لجميع الأدوية والتداخلات
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

# 6. واجهة التقييم ما قبل التخدير الشاملة والمعمقة (ب نصوص مختصرة وواضحة للهواتف)
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

st.write("---")

# 7. محرك اتخاذ القرار والتحليل الذكي
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

    st.success(f"💊 **الجرعة المقدرة للمريض:** {min_dose:.1f} إلى {max_dose:.1f} {data['unit'].split('/')[0]}")
    st.success(f"💉 **حجم السحب بالسرنجة:** {min_volume_ml:.1f} ml إلى {max_volume_ml:.1f} ml")

    if max_volume_ml > syringe_capacity:
        st.error(f"⚠️ **خطأ في سعة السرنجة:** الحجم المحسوب ({max_volume_ml:.1f} ml) يفوق سعة السرنجة ({syringe_capacity} ml)! اختر سرنجة أكبر.")

    st.write(f"📌 **الخصائص السريرية:** {data['info']}")
    st.write(f"💧 **التركيز المعتمد:** {data['concentration']}")
