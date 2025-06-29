import streamlit as st

st.set_page_config(page_title="甜點熱量計算器", page_icon="🍩")

st.title("🍰 甜點熱量計算器")
st.markdown("輸入你使用的每個食材與克數，計算整份甜點的總熱量！")

# 🔢 熱量資料庫（單位：kcal / 1g）
calorie_table = {
    "低筋麵粉": 3.64,
    "中筋麵粉": 3.64,
    "高筋麵粉": 3.65,
    "糖粉": 3.87,
    "細砂糖": 3.87,
    "黑糖": 3.8,
    "奶油": 7.17,
    "植物油": 8.84,
    "橄欖油": 8.84,
    "奶油乳酪": 3.49,
    "牛奶": 0.64,
    "鮮奶油": 3.5,
    "煉乳": 3.2,
    "無糖優格": 0.59,
    "希臘優格": 0.66,
    "蛋白": 0.52,
    "全蛋": 1.43,
    "吉利丁片": 3.4,
    "可可粉": 2.28,
    "抹茶粉": 3.0,
    "核桃": 6.5,
    "杏仁粉": 6.0,
    "燕麥": 3.89,
    "芋頭": 1.09,
    "地瓜": 1.32,
    "奶粉": 5.1,
    "玉米粉": 3.65
}

st.markdown("👇 請依序選擇食材並輸入對應的克數")

# 🧾 多欄位輸入（共 8 格）
selected_ingredients = []
weights = []

for i in range(1, 9):  # 1～8 共八格
    col1, col2 = st.columns([2, 1])
    with col1:
        ingredient = st.selectbox(f"食材 {i}", [""] + list(calorie_table.keys()), key=f"ingredient_{i}")
    with col2:
        weight = st.number_input(f"克數 {i}", min_value=0.0, step=1.0, key=f"weight_{i}")
    
    if ingredient:
        selected_ingredients.append(ingredient)
        weights.append(weight)

# ▶️ 按鈕：計算
if st.button("🔥 計算總熱量"):
    total = 0
    st.markdown("#### 各食材熱量明細：")
    for ing, wt in zip(selected_ingredients, weights):
        cal = calorie_table[ing] * wt
        total += cal
        st.write(f"🔹 {ing}：{wt:.1f} 克 ➜ {cal:.1f} kcal")
    
    st.markdown("---")
    st.success(f"🍓 總熱量為：**{total:.1f} kcal**")

# 📋 版權宣告
st.markdown("---")
st.caption("© 2025 小比利出品🍰 ")
