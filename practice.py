import streamlit as st
import pandas as pd

st.write("Hello World")

st.write("Hello :blue[World]")

st.title("Hello World :sunglasses:")

st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40]
        }
    )
)

st.link_button("Click here", "https://persolchallengejp.udemy.com/course/pythonstreamlitweb/learn/lecture/44041462#overview")

st.header("Hello World", divider="rainbow")
code = """print("hello")"""
st.code(code, language="python")

agree=st.checkbox("I agree")
if agree:
    st.write("Okay!")

options = st.multiselect(
    "好きな色は何ですか？",
    ['赤', '緑', '青', '黄']
)

st.write("あなたが選んだ色は:", options)

options = st.radio(
    "好きな色は何ですか？",
    ['赤', '緑', '青', '黄']
)

st.write("あなたが選んだ色は:", options)

df = pd.DataFrame(
    [
        {"colors":"赤", "rating":4},
        {"colors":"緑", "rating":5},
        {"colors":"青", "rating":3}
    ]
)
edited_df=st.data_editor(df)
st.write(edited_df.loc[edited_df["rating"].idxmax()]["colors"])



df = pd.DataFrame(
    [
        {"colors":"赤", "rating":4, "mark": True},
        {"colors":"緑", "rating":5, "mark": True},
        {"colors":"青", "rating":3, "mark": True}
    ]
)
edited_df=st.data_editor(df)
edited_df=edited_df[edited_df["mark"]==True]
st.write(edited_df.loc[edited_df["rating"].idxmax()]["colors"])

csv=edited_df.to_csv().encode("utf-8")

st.download_button(
    label = "csvをダウンロード",
    data=csv,
    file_name="sample_df.csv",
    mime="text/csv"
)



df=pd.DataFrame(
    {
        "sales": [20,55,100,80],
        "progress_sales": [20,55,100,80],
    }
)

st.data_editor(
    df,
    column_config={
        "progress_sales": st.column_config.ProgressColumn(
            min_value=0,
            max_value=100,
        ),
    },

)

df = pd.DataFrame(
    {
        "sales": [
            [0,4,25, 30, 60, 80, 100],
            [3,50,0, 80, 30, 40, 100]
        ]
    }
)

st.data_editor(df)

st.data_editor(
    df,
    column_config={
        "sales": st.column_config.BarChartColumn(
            y_min=0,
            y_max=100,
        ),
    },

)

st.data_editor(
    df,
    column_config={
        "sales": st.column_config.LineChartColumn(
            y_min=0,
            y_max=100,
        ),
    },

)

age = st.slider("あなたは何歳ですか？", 0, 130, 40)
st.write("私は", age, "歳です")

import datetime
date = st.date_input("あなたが生まれたのはいつですか？", datetime.date(2000, 1, 1))
st.write("私は",date,"に生まれました")

text = st.text_input("入力してください", "xxxxxx")
st.write(text)


col1, col2=st.columns(2)
with col1:
    st.title("Column1")
    st.write("これはカラムの1です")

with col2:
    st.title("Column2")
    st.write("これはカラムの2です")


tab1, tab2= st.tabs(["tab1", "tab2"])
with tab1:
    st.title("tab1")
    st.write("これはタブの1です")

with tab2:
    st.title("tab2")
    st.write("これはタブの2です")


with st.expander("もっと詳しく見る"):
    st.write("xxxxx")

with st.popover("もっと詳しく見る"):
    st.write("xxxxx")

with st.sidebar:
    st.write("xxxxx")
    st.write("xxxxx")

agree = st.checkbox("同意しますか？")
if agree:
    st.toast("Thank you", icon="👍")

birthday = st.checkbox("今日はあなたの誕生日ですか？")
if birthday:
    st.toast("誕生日おめでとう", icon="👍")
    st.balloons()

import os

st.write("現在の作業フォルダ:", os.getcwd())
st.write("page1.pyの存在:", os.path.exists("pages/page1.py"))
st.write("page2.pyの存在:", os.path.exists("pages/page2.py"))

st.page_link("practice.py", label="Home", icon="🏠")
st.page_link("pages/page1.py", label="page1")
st.page_link("pages/page2.py", label="page2")
st.page_link("http://localhost:8501/#hello-world", label="StreamlitのAPIドキュメント")
