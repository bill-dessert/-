import streamlit as st

# 🍰 甜點熱量資料庫 (每克 kcal)
calorie_table = {
    "低筋麵粉": 3.64,
    "高筋麵粉": 3.52,
    "糖粉": 3.87,
    "奶油": 7.17,
    "奶油乳酪": 3.52,
    "希臘優格": 0.59,
    "無糖優格": 0.45,
    "吉利丁片": 3.4,
    "抹茶粉": 3.18,
    "鮮奶油": 3.44,
    "嫩豆腐": 0.66,
    "燕麥": 3.89,
    "核桃": 6.52,
    "泡打粉": 0.53,
    "奶粉": 5.00,
    "可可粉": 2.28,
    "牛奶": 0.64,
    "砂糖": 3.87,
    "黑糖": 3.54,
    "蜂蜜": 3.04
}

# 🍼 背景樣式：牛奶感！
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fffdf7;
        font-family: "Segoe UI", sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🧁 標題
st.title("🍰 甜點熱量計算器")
st.caption("輸入每項食材的克數，即可計算出總熱量！")

# ➕ 初始化欄位數
if "count" not in st.session_state:
    st.session_state.count = 5  # 預設 5 格

# ➕ 新增欄位按鈕
if st.session_state.count < 15:
    if st.button("➕ 新增一個食材欄位"):
        st.session_state.count += 1

# 📝 輸入欄位
total_calories = 0
for i in range(st.session_state.count):
    col1, col2 = st.columns([2, 1])
    with col1:
        ingredient = st.selectbox(f"食材 {i+1}", ["--請選擇--"] + list(calorie_table.keys()), key=f"ing_{i}")
    with col2:
        weight = st.number_input(f"克數 {i+1}", min_value=0.0, key=f"wt_{i}")

    if ingredient and ingredient != "--請選擇--":
        total_calories += calorie_table[ingredient] * weight

# 💡 顯示結果
st.markdown("---")
st.subheader(f"🎯 總熱量：約 **{total_calories:.2f} kcal**")
st.caption("小比利出品 🍰")
