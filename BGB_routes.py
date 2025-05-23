import streamlit as st
import json

# ---- ROUTES DETAILS ----

#路線方向
routes = {
    "1": {
        "方向": {
            "MAF": {
                "正常路線": {
                    "停站": [
                        "跑馬地 (蟠龍道)", "箕鏈坊，藍塘道", "桂芳街，成和道", "山村道，成和道", "景光街",
                        "養和醫院，黃泥涌道", "跑馬地馬場，黃泥涌道", "立德里，摩利臣山道", "利景酒店，灣仔道",
                        "修頓球場，軒尼詩道", "晏頓街，軒尼詩道", "太古廣場，金鐘道",
                        "中銀大廈，金鐘道", "置地廣場，德輔道中", "中環街市，德輔道中", "急庇利街，德輔道中",
                        "上環 (港澳碼頭)"
                    ],
                    "地圖": "https://umap.openstreetmap.fr/en/map/1-brr-maf_1229516"
                },
                "跑馬日，不停馬場": {
                    "停站": [
                        "跑馬地 (蟠龍道)", "箕鏈坊，藍塘道", "桂芳街，成和道", "山村道，成和道", "景光街",
                        "養和醫院，黃泥涌道", "立德里，摩利臣山道", "利景酒店，灣仔道",
                        "修頓球場，軒尼詩道", "晏頓街，軒尼詩道", "太古廣場，金鐘道",
                        "中銀大廈，金鐘道", "置地廣場，德輔道中", "中環街市，德輔道中", "急庇利街，德輔道中",
                        "上環 (港澳碼頭)"
                    ],
                    "地圖": "https://umap.openstreetmap.fr/en/map/1-brr-maf-race_1229517"
                }
            },
            "BRR": {
                "正常路線": {
                    "停站": [
                        "上環 (港澳碼頭)", "無限極廣場，德輔道中", "恒生銀行總行大廈，德輔道中", "德忌利士街，德輔道中", 
                        "皇后像廣場 ，遮打道", "金鐘廊，金鐘道", "軍器廠街，軒尼詩道", "柯布連道，軒尼詩道", 
                        "譚臣道，菲林明道", "克街，灣仔道", "天樂里，灣仔道", "逸廬，黃泥涌道", 
                        "雅谷大廈，黃泥涌道", "跑馬地（下），黃泥涌道", "奕蔭街，成和道", "昇平樓，成和道", 
                        "箕鏈坊，藍塘道", "跑馬地 (蟠龍道)"
                    ],
                    "地圖": "https://umap.openstreetmap.fr/en/map/1-maf-brr_1229519"
                },
                "假日班次，改經德輔道中": {
                    "停站": [
                        "上環 (港澳碼頭)", "無限極廣場，德輔道中", "恒生銀行總行大廈，德輔道中", "德忌利士街，德輔道中", 
                        "歷山大廈，德輔道中", "遮打花園，德輔道中", "金鐘廊，金鐘道", "軍器廠街，軒尼詩道", "柯布連道，軒尼詩道", 
                        "譚臣道，菲林明道", "克街，灣仔道", "天樂里，灣仔道", "逸廬，黃泥涌道", 
                        "雅谷大廈，黃泥涌道", "跑馬地（下），黃泥涌道", "奕蔭街，成和道", "昇平樓，成和道", 
                        "箕鏈坊，藍塘道", "跑馬地 (蟠龍道)"
                    ],
                    "地圖": "https://umap.openstreetmap.fr/en/map/1-maf-brr-holidays_1229520"
                }
            }
        }
    }
}

# ------------------- Streamlit UI 設定 -------------------
st.set_page_config(page_title="漢堡巴士路線資料", page_icon="🚌", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Source+Han+Sans+TC:wght@400;500&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Source Han Sans TC', 'Roboto', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🚌 漢堡巴士路線")
st.subheader("查閱各路線資料")
st.markdown("[🔗 漢堡巴士 Spreadsheet](https://docs.google.com/spreadsheets/d/1_hF_4ObI7j7OKKa__Bs9-fCLS6jYLvtTxg_nzhzkLjU/edit?gid=956048970)")

# ------------------- 分欄 Layout：左右界面 -------------------
left_col, right_col = st.columns([3, 5])

with left_col:
    selected_route = st.selectbox("選擇路線", list(routes.keys()))
    
    directions = routes[selected_route]["方向"]
    selected_direction = st.selectbox("選擇方向", list(directions.keys()))
    
    variants = directions[selected_direction]
    selected_variant = st.selectbox("選擇走線", list(variants.keys()))

    variant_data = variants[selected_variant]

    st.markdown("地圖")

    # 建立地圖 iframe URL
    map_url = variant_data["地圖"]

    st.components.v1.html(f"""
        <iframe src="{map_url}"
            width="100%" height="500" frameborder="1"
            allowfullscreen allow="geolocation">
        </iframe>
         """, height=520)

with right_col:

    st.markdown("🚏 停站")
    for i, stop in enumerate(variant_data["停站"], start=1):
        st.write(f"{i}. {stop}")