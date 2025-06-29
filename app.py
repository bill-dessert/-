import streamlit as st

# 預設熱量資料庫（每克 kcal）
calorie_table = {
    "低筋麵粉": 3.64,
    "高筋麵粉": 3.48,
    "奶粉": 5.2,
    "糖粉": 3.87,
    "無糖可可粉": 2.28,
    "鮮奶油": 3.52,
    "希臘優格": 0.59,
    "無糖優格": 0.59,
    "嫩豆腐": 0.66,
    "吉利丁片": 3.43,
    "奶油乳酪": 3.34,
    "黑巧克力": 5.46,
    "白巧克力": 5.39,
    "紅茶粉": 2.4,
    "抹茶粉": 3.18,
    "南瓜": 0.26,
    "地瓜": 1.2,
    "藍莓": 0.57,
    "香蕉": 0.89,
    "核桃": 6.54,
    "燕麥": 3.89,
    "泡打粉": 0.53,
}

st.set_page_config(page_title="甜點熱量計算器", layout="centered")

# 背景改為黑色主題
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
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🍰 甜點熱量計算器")

# 預設格數與最大格數
max_slots = 15
default_slots = 5

if "slots" not in st.session_state:
    st.session_state.slots = default_slots

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("➕ 新增一格食材欄位"):
        if st.session_state.slots < max_slots:
            st.session_state.slots += 1
with col2:
    if st.button("➖ 減少一格食材欄位"):
        if st.session_state.slots > 1:
            st.session_state.slots -= 1

ingredients = []
weights = []

for i in range(st.session_state.slots):
    cols = st.columns([2, 1])
    with cols[0]:
        ingredient = st.selectbox(f"食材{i+1}", options=["請選擇"] + list(calorie_table.keys()), key=f"ing_{i}")
        ingredients.append(ingredient)
    with cols[1]:
        weight = st.number_input("克數", min_value=0, step=1, key=f"wt_{i}")
        weights.append(weight)

total_calories = 0
details = []

for ing, wt in zip(ingredients, weights):
    if ing != "請選擇":
        kcal = calorie_table.get(ing, 0) * wt
        total_calories += kcal
        details.append(f"{ing}：{wt}g → 約 {kcal:.1f} kcal")

st.markdown("---")
if details:
    st.subheader("📋 熱量明細")
    for d in details:
        st.markdown(f"- {d}")
st.subheader(f"🍩 總熱量：約 **{total_calories:.1f} kcal**")
st.caption("小比利出品🍰")
