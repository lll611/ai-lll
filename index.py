'''
streamlit多页面程序的入口文件
'''
import streamlit as st

st.title("AI大模型应用产品网")

col1, col2 = st.columns(2)

with col1:
    st.image("https://aigc-files.bigmodel.cn/api/cogview/20241029144859674acd6ce75a4ae2_0.png", use_column_width=True)
    flag = st.button("绘言", use_container_width=True)
    if flag:
        st.switch_page("pages/demo3.py")


with col2:
    st.image("https://aigc-files.bigmodel.cn/api/cogview/20241029144840b199d466b19e478a_0.png", use_column_width=True)
    flag = st.button("绘图", use_container_width=True)
    if flag:
        st.switch_page("pages/textToimage.py")




# with col1:
#     flag = st.button("基础版")
#     if flag:
#         st.switch_page("pages/demo.py")
#
# with col2:
#     flag1 = st.button("进阶版")
#     if flag1:
#         st.switch_page("pages/demo1.py")
#
# with col3:
#     flag2 = st.button("最终版")
#     if flag2:
#         st.switch_page("pages/demo2.py")
# with col4:
#     flag3 = st.button("无敌版")
#     if flag3:
#         st.switch_page("pages/demo3.py")
# with col5:
#     flag4 = st.button("闻声图")
#     if flag4:
#         st.switch_page("pages/textToimage.py")