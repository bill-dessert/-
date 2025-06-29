import streamlit as st

# 🍮 食材熱量表（每克 kcal）
calorie_table = {
    "低筋麵粉": 3.64, "高筋麵粉": 3.48, "中筋麵粉": 3.52,
    "糖粉": 3.87, "砂糖": 3.87, "蜂蜜": 3.04,
    "奶油": 7.17, "鮮奶油": 3.52, "奶粉": 5.22,
    "抹茶粉": 3.18, "吉利丁片": 3.24,
    "嫩豆腐": 0.66, "無糖優格": 0.59, "希臘優格": 0.66,
    "奶油乳酪": 3.48,
    "核桃": 6.59, "燕麥": 3.89,
    "雞蛋": 1.43, "蛋白": 0.52, "蛋黃": 3.20,
    "無糖可可粉": 2.28, "牛奶": 0.64,
}

DEFAULT_INPUTS = 5
MAX_INPUTS = 15

# 🎨 米色風格設計
st.set_page_config(page_title="甜點熱量計算器", page_icon="🍰", layout="centered")
st.markdown(
    """
    <style>
        body {
            background-color: #fef5e7;
        }
        .stTextInput, .stNumberInput, .stSelectbox, .stButton {
            border-radius: 8px !important;
        }
        .stApp {
            background-color: #fef5e7;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍰 甜點熱量計算器")
st.caption("輸入食材與重量，計算你今天甜甜的罪惡值 🍯")

# 🔁 記錄欄位數量
if "num_inputs" not in st.session_state:
    st.session_state.num_inputs = DEFAULT_INPUTS

# ➕ 新增欄位按鈕
if st.session_state.num_inputs < MAX_INPUTS:
    if st.button("➕ 新增一格食材欄位"):
        st.session_state.num_inputs += 1

# 🔢 建立輸入欄位
total_calories = 0
for i in range(st.session_state.num_inputs):
    col1, col2 = st.columns(2)
    with col1:
        ingredient = st.selectbox(f"食材{i+1}", list(calorie_table.keys()), key=f"ingredient_{i}")
    with col2:
        weight = st.number_input(f"克數{i+1}", min_value=0.0, key=f"weight_{i}")
    total_calories += calorie_table[ingredient] * weight

# 📊 顯示結果
st.markdown("---")
st.subheader(f"🍮 總熱量：約 **{total_calories:.2f} kcal**")
st.caption("小比利出品 🍰")
