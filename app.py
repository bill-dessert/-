import streamlit as st

# 食材熱量資料庫（每克 kcal）
calorie_table = {
    "低筋麵粉": 3.64, "高筋麵粉": 3.48, "奶粉": 5.2, "糖粉": 3.87,
    "無糖可可粉": 2.28, "鮮奶油": 3.52, "希臘優格": 0.59, "無糖優格": 0.59,
    "嫩豆腐": 0.66, "吉利丁片": 3.43, "奶油乳酪": 3.34, "黑巧克力": 5.46,
    "白巧克力": 5.39, "紅茶粉": 2.4, "抹茶粉": 3.18, "南瓜": 0.26, "地瓜": 1.2,
    "藍莓": 0.57, "香蕉": 0.89, "核桃": 6.54, "燕麥": 3.89, "泡打粉": 0.53,
    "赤藻糖醇": 0.0, "楓糖漿": 2.6, "香草精": 2.88, "小蘇打": 0.0, "檸檬汁": 0.22,
    "玉米澱粉": 3.81, "酵母": 3.25, "貮砂糖": 3.87, "無鹽奶油": 7.17,
    "鹹蛋黃": 3.57, "豬油": 8.98, "橄欖油": 8.84, "大豆油": 8.84,
    "地瓜粉": 3.3, "樹薯粉": 3.52, "70%黑巧克力": 5.46, "牛奶巧克力": 5.35,
    "全麥粉": 3.4, "黑芝麻粉": 6.0, "豆漿粉": 4.4, "海藻糖": 3.25,
    "麥芽糖": 3.1, "糯米粉": 3.6, "蘭姆酒": 2.31, "葡萄乾": 2.99, "杏仁": 5.79, "雞蛋": 1.40,
    "蛋黃":3.20, "蛋白":0.50,
}

# 成品甜點熱量（每克 kcal）
dessert_table = {
    "巴斯克蛋糕": 3.5, "布朗尼蛋糕": 4.6, "軟餅乾": 4.8, "生巧克力": 5.0,
    "重乳酪蛋糕": 3.8, "輕乳酪蛋糕": 3.2, "蛋黃酥": 4.3, "可麗露": 3.9,
    "達克瓦茲": 4.4, "馬卡龍": 4.7, "聖多諾黑": 4.2, "生乳捲": 3.5,
    "蘋果派": 2.6, "芋頭派": 3.2, "南瓜派": 2.8, "蛋糕卷": 3.3,
    "焦糖布丁": 1.5, "泡芙": 2.9, "奶酪": 1.6, "戚風蛋糕": 2.7,
    "黑森林蛋糕": 3.6, "鳳梨酥": 4.1, "太陽餅": 4.0,
    "舒芙蕾": 2.5, "瑪德蓮": 4.1, "可頌": 4.0, "布列塔尼酥餅": 4.6, "提拉米蘇": 3.4
}

# 頁面設定 + 样式（克數白色字體）
st.set_page_config(page_title="甜點熱量計算器", layout="centered")
st.markdown("""
    <style>
    .stApp {
        background-color: #1e1e1e;
        color: white;
    }
    .stButton>button {
        background-color: #444;
        color: white;
    }
    .stNumberInput input {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)


st.image("app_icon.jpg", width=100)
st.title("🍰 甜點熱量計算器")
st.info("📱 用手機打開這頁後，點選右上角「⋯」或下方「分享」→ 選擇【加入主畫面】，就能像 App 一樣快速使用囉！")

# 食材欄位控制
max_slots = 15
default_slots = 5
if "slots" not in st.session_state:
    st.session_state.slots = default_slots

col1, col2 = st.columns(2)
with col1:
    if st.button("➕ 新增一格食材欄位"):
        if st.session_state.slots < max_slots:
            st.session_state.slots += 1
with col2:
    if st.button("➖ 減少一格食材欄位"):
        if st.session_state.slots > 1:
            st.session_state.slots -= 1

# 食材與克數輸入
ingredients = []
weights = []

for i in range(st.session_state.slots):
    cols = st.columns([2, 1])
    with cols[0]:
        ing = st.selectbox(f"食材 {i+1}", ["請選擇"] + list(calorie_table.keys()), key=f"ing_{i}")
        ingredients.append(ing)
    with cols[1]:
        wt = st.number_input("克數", min_value=0, step=1, key=f"wt_{i}")
        weights.append(wt)

# 計算總熱量
total_calories = 0
details = []
for ing, wt in zip(ingredients, weights):
    if ing != "請選擇":
        kcal = calorie_table[ing] * wt
        total_calories += kcal
        details.append(f"{ing}：{wt}g → 約 {kcal:.1f} kcal")

st.markdown("---")
if details:
    st.subheader("📋 熱量明細")
    for d in details:
        st.markdown(f"- {d}")

st.subheader(f"🍩 總熱量：約 **{total_calories:.1f} kcal**")

# 成品甜點熱量查詢
st.markdown("---")
st.markdown("### 🎂 成品甜點熱量查詢")
selected_dessert = st.selectbox("選擇甜點名稱", ["請選擇"] + list(dessert_table.keys()))
dessert_weight = st.number_input("輸入甜點重量（g）", min_value=0, key="dessert_wt")

if selected_dessert != "請選擇" and dessert_weight > 0:
    kcal = dessert_table[selected_dessert] * dessert_weight
    st.markdown(f"➡️ 約為 **{kcal:.1f} kcal**")

st.caption("小比利出品🍰")
