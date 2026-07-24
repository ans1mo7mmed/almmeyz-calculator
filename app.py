import streamlit as st

# 1. إعداد الصفحة لتدعم اللغة العربية وشكل الواجهة
st.set_page_config(page_title="النظام الذكي لحساب جرعة التخدير", page_icon="💉", layout="centered")

# إضافة CSS لضبط اتجاه النص والتصميم والتوسيط
st.markdown("""
    <style>
    * {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif;
    }
    .disclaimer-box {
        background-color: #ffebee;
        color: #c62828;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #ef9a9a;
        margin-bottom: 20px;
        font-weight: bold;
        text-align: center;
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
        ⚠️ إخلاء مسؤولية طبية: هذا التطبيق مخصص حصراً لأغراض الاطلاع والتعليم الطبي والتدريب الأكاديمي، ولا يُعتبر بأي حال من الأحوال مرجعاً نهائياً أو بديلاً عن القرار السريري المباشر للطبيب المختص أثناء العمليات الحقيقية.
    </div>
""", unsafe_allow_html=True)

# 5. قواعد البيانات المحدثة والشاملة لتفكير طبيب التخدير وتقني التخدير
anesthesia_drugs = {
    "Propofol (بروبوفول)": {
        "dose_range": (1.5, 2.5), 
        "unit": "mg/kg", 
        "concentration": "10 mg/ml", 
        "conc_val": 10.0, 
        "info": "يستخدم للتحريض (Induction) والتخدير المستمر.",
        "interactions": {
            "أدوية ضغط الدم / موسعات الأوعية": "⚠️ تداخل محتمل: يزيد من تأثير خفض ضغط الدم الشرياني بشكل حاد.",
            "مضادات الاكتئاب / المهدئات (Benzodiazepines/Opioids)": "⚠️ تداخل محتمل: يحدث تثبيط مضاعف للجهاز العصبي المركزي والجهاز التنفسي."
        }
    },
    "Thiopental (ثيوبنتال)": {
        "dose_range": (3.0, 5.0), 
        "unit": "mg/kg", 
        "concentration": "25 mg/ml", 
        "conc_val": 25.0, 
        "info": "تحريض سريع للتخدير. يمتلك خصائص مضادة للتشنج.",
        "interactions": {
            "أدوية ضغط الدم / موسعات الأوعية": "⚠️ تداخل محتمل: يسبب هبوطاً حاداً في ضغط الدم نتيجة توسع الأوعية الدموية.",
            "مضادات الاكتئاب / المهدئات (Benzodiazepines/Opioids)": "⚠️ تداخل محتمل: زيادة عمق التثبيط التنفسي وتأخر الإفاقة."
        }
    },
    "Etomidate (إيتوميدات)": {
        "dose_range": (0.2, 0.3), 
        "unit": "mg/kg", 
        "concentration": "2 mg/ml", 
        "conc_val": 2.0, 
        "info": "مخدر تحريضي سريع. لا يؤثر على الدورة الدموية بشكل ملحوظ.",
        "interactions": {
            "أدوية الكورتيزون / مثبطات الغدة الكظرية": "⚠️ ملاحظة: يثبط تخريج الكورتيزول مؤقتاً في الغدة الكظرية، يجب الحذر في حالات الصدمة الإنتانية."
        }
    },
    "Ketamine (كيتامين)": {
        "dose_range": (1.0, 2.0), 
        "unit": "mg/kg", 
        "concentration": "50 mg/ml", 
        "conc_val": 50.0, 
        "info": "مخدر تفارقي (Dissociative). يحافظ على التنفس التلقائي.",
        "interactions": {
            "أدوية هرمون الغدة الدرقية / مضادات الكولين": "⛔ تداخل خطير: قد يؤدي إلى ارتفاع حاد وخطير في ضغط الدم وتسارع ضربات القلب.",
            "مضادات الاكتئاب ثلاثية الحلقات (TCAs)": "⛔ تحذير: خطر حدوث ارتفاع ضغط دم شديد وعدم انتظام ضربات القلب."
        }
    },
    "Midazolam (ميدازولام)": {
        "dose_range": (0.05, 0.1), 
        "unit": "mg/kg", 
        "concentration": "1 mg/ml", 
        "conc_val": 1.0, 
        "info": "مهدئ ومزيل للقلق ويسبب فقدان الذاكرة التقدمي.",
        "interactions": {
            "المسكنات الأفيونية (Opioids مثل الفنتانيل والمورفين)": "⛔ تداخل خطير: خطر كبير جداً لحدوث توقف التنفس وتثبيط جهازي عصبي وتدني الأكسجة.",
            "أدوية المضادات الحيوية الفطرية أو الماكروليد (مثل Erythromycin)": "⚠️ تداخل محتمل: تبطئ أيض الميدازولام وتطيل أمد مفعوله بشكل كبير."
        }
    },
    "Fentanyl (فينتانيل)": {
        "dose_range": (1.0, 2.0), 
        "unit": "mcg/kg", 
        "concentration": "50 mcg/ml", 
        "conc_val": 50.0, 
        "info": "مسكن أفيوني قوي وسريع التأثير.",
        "interactions": {
            "المهدئات ومضادات القلق (Benzodiazepines)": "⛔ تداخل خطير: يسبب تثبيطاً تنفسياً شديداً وفقداناً للوعي المفاجئ.",
            "أدوية الاكتئاب (MAOIs)": "⛔ ممنوع تماماً: خطر حدوث تفاعلات مميتة وتسمم عصبي."
        }
    },
    "Succinylcholine (سكسنيل كولين)": {
        "dose_range": (1.0, 1.5), 
        "unit": "mg/kg", 
        "concentration": "50 mg/ml", 
        "conc_val": 50.0, 
        "info": "مرخي عضلي مزيل للاستقطاب، سريع جداً للتنبيب (RSI).",
        "interactions": {
            "أدوية علاج الجلوكوما أو قطرات العين المثبطة للإنزيمات": "⚠️ تداخل محتمل: تطيل أمد الاسترخاء العضلي وتأخر التعافي التنفسي.",
            "أدوية الليثيوم (أدوية الأمراض النفسية)": "⚠️ تداخل محتمل: تزيد وتطيل فترة الإحصار العصبي العضلي."
        }
    },
    "Rocuronium (روكورونيوم)": {
        "dose_range": (0.6, 1.2), 
        "unit": "mg/kg", 
        "concentration": "10 mg/ml", 
        "conc_val": 10.0, 
        "info": "مرخي عضلي غير مزيل للاستقطاب (NDMR). سريع التأثير.",
        "interactions": {
            "المضادات الحيوية من عائلة Aminoglycosides": "⚠️ تداخل محتمل: تعزز وتطيل أمد تأثير الإرخاء العضلي."
        }
    },
    "Atracurium (أتراكوريوم)": {
        "dose_range": (0.5, 0.6), 
        "unit": "mg/kg", 
        "concentration": "10 mg/ml", 
        "conc_val": 10.0, 
        "info": "مرخي عضلي يتفكك تلقائياً في بلازما الدم.",
        "interactions": {
            "أدوية علاج الصرع المزمنة": "⚠️ تداخل محتمل: قد تتطلب جرعات أعلى قليلاً لتحقيق الاسترخاء المطلوب."
        }
    },
    "Cisatracurium (سيس-أتراكوريوم)": {
        "dose_range": (0.15, 0.2), 
        "unit": "mg/kg", 
        "concentration": "2 mg/ml", 
        "conc_val": 2.0, 
        "info": "مرخي عضلي آمن جداً ومستقر، لا يفرز الهيستامين.",
        "interactions": {
            "مرخيات العضلات الأخرى أو مضادات التخدير": "⚠️ تداخل محتمل: تداخل في توقيت العكس العصبي العضلي."
        }
    }
}

# 6. لوحة تحكم تقييم عقل طبيب وتقني التخدير (أبعاد الفحص الشامل للمريض)
st.subheader("🩺 الفحص الشامل وتقييم ما قبل التخدير (تقييم طبيب وتقني التخدير)")

col_1, col_2 = st.columns(2)
with col_1:
    weight = st.number_input("الوزن (كغم):", min_value=1.0, max_value=300.0, value=70.0, step=1.0)
    age = st.number_input("العمر (سنة):", min_value=1, max_value=120, value=30, step=1)
    
with col_2:
    fasting_status = st.selectbox(
        "حالة الصيام (NPO Status):", 
        [
            "صائم لفترة كافية (>6-8 ساعات للسوائل الصلبة)", 
            "غير صائم / أكل طعاماً صلبأً مؤخراً (خطر القشط Aspiration Risk)", 
            "سوائل صافية فقط لفترة قصيرة"
        ]
    )
    airway_eval = st.selectbox(
        "تقييم مجرى الهواء الصعب (Airway Assessment - Mallampati):", 
        [
            "Mallampati Class I (سهل جداً)", 
            "Mallampati Class II (سهل نسبياً)", 
            "Mallampati Class III (صعب نسبياً)", 
            "Mallampati Class IV (مجرى هواء صعب جداً - خطورة عالية)"
        ]
    )

# التاريخ المرضي الموسع
diseases_list = [
    "لا يوجد (سليم)", 
    "ارتفاع ضغط الدم (Hypertension)", 
    "أمراض القلب والشرايين (Heart Disease / CAD)", 
    "ربو أو أمراض الجهاز التنفسي المزمنة (Asthma / COPD)", 
    "فشل كلوي مزمن (Renal Failure)", 
    "قصور كبدي (Hepatic Impairment)",
    "السكري غير المنضبط (Uncontrolled Diabetes)",
    "تاريخ مشاكل تخدير سابقة / فرط الحرارة الخبيث (Malignant Hyperthermia Risk)"
]
disease = st.selectbox("التاريخ المرضي المزمل والمرافق:", diseases_list)

# قائمة الأدوية المزمنة التي يتناولها المريض لتحديد التداخلات الدوائية
current_medications = st.multiselect(
    "الأدوية الحالية التي يتناولها المريض (لتدقيق التداخلات الدوائية):",
    [
        "أدوية ضغط الدم / موسعات الأوعية",
        "المسكنات الأفيونية (Opioids مثل الفنتانيل والمورفين)",
        "المهدئات ومضادات القلق (Benzodiazepines)",
        "أدوية الاكتئاب (MAOIs / TCAs)",
        "أدوية هرمون الغدة الدرقية / مضادات الكولين",
        "أدوية المضادات الحيوية الفطرية أو الماكروليد",
        "أدوية علاج الجلوكوما أو قطرات العين",
        "أدوية الليثيوم (أدوية الأمراض النفسية)",
        "أدوية علاج الصرع المزمنة",
        "أدوية الكورتيزون / مثبطات الغدة الكظرية"
    ]
)

drug = st.selectbox("اختر دواء التخدير المراد حسابه:", list(anesthesia_drugs.keys()))

syringe_sizes = ["3 ml (cc)", "5 ml (cc)", "10 ml (cc)", "20 ml (cc)", "50 ml (cc)"]
syringe_str = st.selectbox("حجم السرنجة:", syringe_sizes, index=2)

st.write("---")

# 7. زر التحليل واتخاذ القرار السريري الشامل
if st.button("تشغيل النظام الذكي واتخاذ القرار السريري 🧮", use_container_width=True):
    data = anesthesia_drugs[drug]
    min_dose = weight * data["dose_range"][0]
    max_dose = weight * data["dose_range"][1]
    
    min_volume_ml = min_dose / data["conc_val"]
    max_volume_ml = max_dose / data["conc_val"]
    syringe_capacity = int(syringe_str.split()[0])

    st.subheader("📋 التقرير السريري المتكامل (عقل طبيب وتقني التخدير):")

    # 1. تقييم حالة الأكل والصيام (Aspiration Risk)
    if "غير صائم" in fasting_status:
        st.error("🚨 **تنبيه حرج لصيام المريض (Aspiration Risk):** المريض غير صائم أو تناول طعاماً حديثاً! خطر حدوث استنشاق محتوى المعدة (Pulmonary Aspiration) أثناء التحريض قائم بقوة. يجب تأجيل العمليات غير العجلة، أو تطبيق تقنية التحريض السريع (RSI) مع تفريغ المعدة عبر أنبوب معدي (NG tube) وتأمين مجرى الهواء بحذر شديد.")
    else:
        st.success("✅ **تقييم الصيام:** وضع الصيام مقبول آمن للتحريض التخديري.")

    # 2. تقييم مجرى الهواء (Airway Evaluation)
    if "Class III" in airway_eval or "Class IV" in airway_eval:
        st.warning("⚠️ **تنبيه مجرى الهواء:** المريض يصنف ضمن مجرى الهواء الصعب (Difficult Airway). يجب تجهيز معدات التنبيب الصعب مسبقاً (Video Laryngoscope, Bougie, LMA) واستدعاء استشاري التخدير للطوارئ.")

    # 3. تقييم العمر
    if age >= 65:
        st.warning("👴🏻 **تنبيه العمر (مريض مسن):** يتطلب الأمر تقليل جرعة التحريض الدوائي بنسبة 20-30% بسبب بطء الاستقلاب وحساسية الجهاز العصبي المركزي.")

    # 4. تداخلات التاريخ المرضي
    if disease != "لا يوجد (سليم)":
        if drug == "Propofol (بروبوفول)" and "أمراض القلب والشرايين" in disease:
            st.info("🩺 **تأثير المرض:** يسبب توسعاً وعائياً إضافياً. يُنصح بتقليل الجرعة بنسبة 30-50% والإعطاء ببطء شديد.")
        elif drug == "Ketamine (كيتامين)" and ("ارتفاع ضغط الدم" in disease or "أمراض القلب والشرايين" in disease):
            st.error("⛔ **تحذير صارم:** الكيتامين يرفع ضغط الدم ومعدل ضربات القلب، ويزيد العبء على عضلة القلب لمرضى الضغط والقلب. يُفضل اختيار بديل آخر.")
        elif drug == "Thiopental (ثيوبنتال)" and "ربو أو أمراض الجهاز التنفسي" in disease:
            st.error("⛔ **تحذير صارم:** يسبب تحرر الهيستامين مهدداً بحدوث تشنج قصبي حاد لدى مرضى الربو.")
        elif drug == "Succinylcholine (سكسنيل كولين)" and "فشل كلوي مزمن" in disease:
            st.error("⛔ **تحذير قاتل:** يرفع البوتاسيوم في الدم بشكل خطير ومفاجئ. يُمنع منعاً باتاً استخدامه لمرضى الفشل الكلوي.")
        else:
            st.success(f"🩺 **تقييم الحالة المرضية ({disease}):** تم أخذ الحالة بعين الاعتبار، مع وجوب المراقبة الحثيثة للعلامات الحيوية.")

    # 5. تحليل التداخلات الدوائية المتقاطعة مع الأدوية التي يأخذها المريض
    drug_interactions_db = data["interactions"]
    interaction_found = False
    for med in current_medications:
        if med in drug_interactions_db:
            st.error(f"💊 **تداخل دوائي خطير متكتشف مع ({med}):**\n{drug_interactions_db[med]}")
            interaction_found = True
            
    if not interaction_found and len(current_medications) > 0:
        st.success("✅ **فحص التداخلات الدوائية:** لا توجد تداخلات دوائية رئيسية مسجلة مباشرة بين هذا الدواء وقائمة الأدوية المحددة للمريض.")

    st.write("---")

    # 6. الحسابات الرقمية الدقيقة للجرعة وسحب السرنجة
    st.success(f"💊 **الجرعة المقدرة للدواء:** {min_dose:.1f} إلى {max_dose:.1f} {data['unit'].split('/')[0]}")
    st.success(f"💉 **حجم السحب الفعلي داخل السرنجة:** {min_volume_ml:.1f} ml إلى {max_volume_ml:.1f} ml")

    if max_volume_ml > syringe_capacity:
        st.error(f"⚠️ **تنبيه السعة:** الحجم المطلوب ({max_volume_ml:.1f} ml) يتجاوز سعة السرنجة المختارة ({syringe_capacity} ml). يرجى تغيير حجم السرنجة فوراً لتجنب الخطأ الدوائي!")

    # 7. ملخص معلومات الدواء
    st.write(f"📌 **معلومات الدواء السريرية:** {data['info']}")
    st.write(f"💧 **التركيز الدوائي المعتمد:** {data['concentration']}")
