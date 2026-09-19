import streamlit as st
st.set_page_config(
    page_title="Arbitraj Simülatörü", 
    page_icon="📊", 
    layout="centered"
)
st.markdown("""
    <head>
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
        <meta name="apple-mobile-web-app-title" content="Hesaplayıcı">
    </head>
    <style>
        /* Streamlit üst/alt gereksiz menülerini temizleme */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
st.title(" Arbitraj Simülatörü")
para = st.number_input("Başlangıç Parası (TL)", value=100.0, step=10.0)
zarar = st.number_input("Zarar Oranı (%)", value=30.0, step=5.0)
alis = st.number_input("Ürün Alış Fiyatı (TL)", value=5.0, step=0.5)
satis = st.number_input("Ürün Satış Fiyatı (TL)", value=9.0, step=0.5)
if st.button("Hesapla", type="primary"):
    kalan = para * (1 - zarar / 100)
    urun_adedi = int(kalan // alis)
    artan_para = kalan % alis
    toplam_kazanc = (urun_adedi * satis) + artan_para
    net_kar = toplam_kazanc - para
    st.divider()
    st.subheader("Sonuçlar:")
    st.write(f"📉 **Kalan Para:** {kalan:.2f} TL")
    st.write(f"📦 **Alınan Ürün:** {urun_adedi} adet")
    st.write(f"💰 **Son Toplam Para:** {toplam_kazanc:.2f} TL")
    if net_kar >= 0:
        st.success(f"📈 **Net Kâr:** +{net_kar:.2f} TL")
    else:
        st.error(f"📉 **Net Zarar:** {net_kar:.2f} TL")
