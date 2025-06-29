import streamlit as st

# 食材熱量表（每克 kcal）
calorie_table = {
    "低筋麵粉": 3.64,
    "高筋麵粉": 3.57,
    "無糖可可粉": 2.28,
    "奶油乳酪": 3.42,
    "抹茶粉": 3.12,
    "嫩豆腐": 0.66,
    "希臘優格": 0.59,
    "無糖優格": 0.43,
    "鮮奶油": 3.52,
    "吉利丁片": 3.0,
    "泡打粉": 1.43,
    "核桃": 6.54,
    "燕麥": 3.89,
    "奶粉": 5.0,
    "糖粉": 3.87,
    "黑巧克力": 5.5,
    "紅茶粉": 2.4,
    "白巧克力": 5.5,
    "南瓜": 0.26,
    "地瓜": 1.32,
    "藍莓": 0.57,
    "香蕉": 0.89,
}

# 預設值
st.set_page_config(page_title="甜點熱量計算器", page_icon="🍰")

st.markdown("""
    <style>
        .stApp {
            background-color: #fef6eb;
            color: #333333;
            font-size: 16px;
        }
        .stNumberInput input {
            background-color: white;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🍰 甜點熱量計算器")
st.write("輸入各項食材的克數，幫你計算總熱量！")

# 初始欄位數量
max_fields = 15
default_fields = 5
num_fields = st.session_state.get("num_fields", default_fields)

# + 按鈕
if num_fields < max_fields:
    if st.button("➕ 新增一格食材欄位"):
        num_fields += 1
        st.session_state["num_fields"] = num_fields

# 顯示欄位
total_calories = 0
for i in range(num_fields):
    cols = st.columns([2, 1])
    ingredient = cols[0].selectbox(f"食材{i+1}", options=[""] + list(calorie_table.keys()), key=f"ingredient_{i}")
    weight = cols[1].number_input("克數", min_value=0, step=1, key=f"weight_{i}")
    if ingredient:
        total_calories += calorie_table[ingredient] * weight

# 結果
st.markdown("---")
st.subheader(f"🍩 總熱量： 約 **{total_calories:.0f} kcal**")
st.caption("小比利出品🍰")
