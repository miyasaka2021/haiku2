

#import os
import openai
#openai.api_key = os.environ.get('CHATGPT_API_KEY')



import streamlit as st
api_key = st.secrets["api_key"]


st.title('俳句ジェネレータ')

# Streamlitウィジェットでユーザーからの入力を受け取る
input_text = st.text_input('お題を入力してください:')

if st.button('生成'):
    # 俳句を生成
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        
        messages=[
        {"role": "system", "content": """あなたは俳句の達人です。喜怒哀楽や季節感を表現する詩人です。
    俳句とは、ユーザーが提供するテーマを元に、説明ではなく、5・7・5という音節数で俳句としての詩的な表現を行ってください。
    俳句の例として以下のようなものがあります。

    * 古池や 蛙飛びこむ 水の音
    * 若草や つわものどもが 夢の跡
    * 柿食えば 鐘が鳴るなり 法隆寺
    * 梅一輪 一輪ほどの あたたかさ
    * 静かさや 岩にしみ入る 蝉の声
        """},
        

        
        {"role": "user", "content": input_text}
      ],
        temperature=0.7,
        max_tokens=25,
        n=5
    )


    #st.write(response)
    # 生成した俳句を表示
    for i, output in enumerate(response['choices']):
        if "content" in output["message"]:
           st.write(f'{i+1}. {output["message"]["content"]}')
        else:
           st.write(f'{i+1}. Content not found')
