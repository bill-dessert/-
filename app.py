import streamlit as st

# 初始化欄位數
if "num_rows" not in st.session_state:
    st.session_state.num_rows = 5

# 食材熱量表（kcal/克）
calorie_table = {
    "全脂鮮奶": 0.64,
    "鮮奶油": 3.52,
    "奶油乳酪": 3.5,
    "希臘優格": 0.59,
    "無糖優格": 0.55,
    "雞蛋": 1.43,
    "低筋麵粉": 3.48,
    "中筋麵粉": 3.64,
    "高筋麵粉": 3.52,
    "燕麥": 3.79,
    "糖粉": 3.87,
    "核桃": 6.54,
    "吉利丁片": 3.40,
    "抹茶粉": 3.00,
    "嫩豆腐": 0.66,
    "奶粉": 4.95,
    "杏仁粉": 5.75,
    "可可粉": 2.84,
    "蜂蜜": 3.04,
    "黑糖": 3.80
}

# 🍰 美化介面（牛奶色調）
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fffdf7;
        font-family: '微軟正黑體', sans-serif;
    }
    h1 {
        color: #ff6f61;
        font-size: 36px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🚀 主標題
st.markdown("<h1>🍰 小比利甜點熱量計算器</h1>", unsafe_allow_html=True)
st.caption("輸入食材與重量，計算總熱量～")

# ➕ 新增欄位按鈕
if st.button("➕ 新增食材欄位"):
    if st.session_state.num_rows < 15:
        st.session_state.num_rows += 1
    else:
        st.warning("最多只能輸入 15 項食材喔！")

# 輸入區
total_calories = 0.0
for i in range(st.session_state.num_rows):
    cols = st.columns([2, 1])
    with cols[0]:
        ingredient = st.selectbox(f"食材 {i+1}", list(calorie_table.keys()), key=f"ingredient_{i}")
    with cols[1]:
        weight = st.number_input(f"克數 {i+1}", min_value=0.0, step=1.0, key=f"weight_{i}")
    total_calories += calorie_table[ingredient] * weight

# 🍮 顯示總熱量結果
st.markdown("---")
st.markdown(
    f"<h2>🍓 總熱量：{total_calories:.2f} kcal</h2>",
    unsafe_allow_html=True
)

# 👣 版權
st.caption("by 小比利出品 🍰")
