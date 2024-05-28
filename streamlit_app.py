import streamlit as st
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

# ---------
# 第1天
# ---------
# pip install streamlit
# streamlit hello

# ---------
# 第2天
# ---------

# st.write('Hello world!')
# st.write('今天是研究生一年级下学期第14周的周二！')

## streamlit run streamlit_app.py

# num = st.slider('要随机多少个？', 1, 20, 1)

# st.write("以下是被抽到的幸运星🌟：")
# df = pd.read_excel("2023学生名单.xlsx", dtype={"学号": str})
# print(df.sample(1)["姓名"])
# st.write(df.sample(num))
# names = df["姓名"].tolist()

# ---------
# 第3天
# ---------
# import streamlit as st

# st.header('st.button')

# if st.button('Say hello'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')

# ---------
# 第4天
# ---------
# 视频

# ---------
# 第5天
# ---------
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('随机午餐计划！')

# 样例 1

# st.write('Hello, *World!* :sunglasses:')

# 样例 2

# st.write(1234567890)
# st.write("你好呀")


# 样例 3

# df = pd.DataFrame({
#      'first column': [1, 2, 3, 4],
#      'second column': [10, 20, 30, 40]
#      })

# st.write(df)

lunch = [  
    {  
        "name": "蔬菜炒饭",  
        "description": "简单又营养的午餐，包含多种蔬菜和少量肉类或豆腐。",  
        "price": "15元"  
    },  
    {  
        "name": "鸡胸肉沙拉",  
        "description": "高蛋白的午餐选择，搭配新鲜蔬菜和沙拉酱。",  
        "price": "20元"  
    },  
    {  
        "name": "三文鱼寿司卷",  
        "description": "优质蛋白质和健康脂肪的完美结合，搭配海苔和蔬菜。",  
        "price": "30元"  
    },  
    {  
        "name": "番茄鸡蛋面",  
        "description": "经典的番茄鸡蛋搭配面条，简单又美味。",  
        "price": "12元"  
    },  
    {  
        "name": "黑米鸡肉粥",  
        "description": "营养丰富的粥品，黑米和鸡肉的组合，温暖且易于消化。",  
        "price": "8元"  
    },  
    {  
        "name": "紫米饭搭配红烧带鱼",  
        "description": "健康的紫米饭搭配红烧带鱼，营养丰富且美味。",  
        "price": "25元"  
    },  
    {  
        "name": "传统香港午餐套餐",  
        "description": "包含主食、一荤一素一汤，价格根据餐厅和菜品有所不同。",  
        "price": "30-50港币"  
    },  
    {  
        "name": "学校营养午餐",  
        "description": "农村小学午餐每生每天7元，两荤一素一汤加主食；中学每生每天8元，两荤两素一汤加主食。",  
        "price": "7-8元"  
    },  
    {  
        "name": "素食拌饭",  
        "description": "以蔬菜为主的拌饭，适合素食者或需要轻盈午餐的人。",  
        "price": "18元"  
    },  
    {  
        "name": "雪菜肉丝面",  
        "description": "传统中式面食，搭配雪菜和肉丝，味道鲜美。",  
        "price": "10元"  
    },  
    {  
        "name": "其他午餐选项",  
        "description": "包含但不限于各种盖浇饭、快餐、汉堡、披萨等，价格根据具体菜品和餐厅有所不同。",  
        "price": "根据具体菜品和餐厅定价"  
    }  
]

lunch = pd.DataFrame(lunch)
st.write(lunch)

if st.button("随机午餐"):
    st.write(lunch["name"].sample(3))
else:
    st.write("还没有点击随机。")


students = pd.read_excel("学生名单.xlsx")
# students.astype({"学号", str})
st.write(students)

students["学号"] = students["学号"].astype(str)

if st.button("随机点名，说出你的午餐计划"):
    st.write(students["姓名"].sample(1))
else:
    st.write("还没有进行随机。")


# 样例 4

# st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# 样例 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

# # 创建一个指定大小的 figure 对象  
# fig, ax = plt.subplots(figsize=(6, 6)) 

# st.write(df2)
 
# ax.plot(df2["a"], df2["b"], "tab:red")  
  
# # 显示图形  
# st.pyplot(fig)

# ---------
# 第6、7天
# ---------
# 部署
# https://bv2024.streamlit.app/

# ---------
# 第8天
# ---------

# import streamlit as st
# from datetime import time, datetime

# st.header('st.slider')

# # 样例 1

# st.subheader('Slider')

# age = st.slider('How old are you?', 0, 130, 25)
# st.write("I'm ", age, 'years old')

# # 样例 2

# st.subheader('Range slider')

# values = st.slider(
#      'Select a range of values',
#      0.0, 100.0, (25.0, 75.0))
# st.write('Values:', values)

# # 样例 3

# st.subheader('Range time slider')

# appointment = st.slider(
#      "Schedule your appointment:",
#      value=(time(11, 30), time(12, 45)))
# st.write("You're scheduled for:", appointment)

# # 样例 4

# st.subheader('Datetime slider')

# start_time = st.slider(
#      "When do you start?",
#      value=datetime(2020, 1, 1, 9, 30),
#      format="MM/DD/YY - hh:mm")
# st.write("Start time:", start_time)



# ---------
# 第9天
# ---------
# import streamlit as st
# import pandas as pd
# import numpy as np

# st.header('Line chart')

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)




# ---------
# 第10天
# ---------
# import streamlit as st

# st.header('st.selectbox')

# option = st.selectbox(
#      'What is your favorite color?',
#      ('Blue', 'Red', 'Green'))

# st.write('Your favorite color is ', option)


# ---------
# 第11天
# ---------
# import streamlit as st

# st.header('st.multiselect')

# options = st.multiselect(
#      'What are your favorite colors',
#      ['Green', 'Yellow', 'Red', 'Blue'],
#      ['Yellow', 'Red'])

# st.write('You selected:', options)


# ---------
# 第12天
# ---------
# st.header('st.checkbox')

# st.write ('What would you like to order?')

# icecream = st.checkbox('Ice cream')
# coffee = st.checkbox('Coffee')
# cola = st.checkbox('Cola')

# if icecream:
#      st.write("Great! Here's some more 🍦")

# if coffee:
#      st.write("Okay, here's some coffee ☕")

# if cola:
#      st.write("Here you go 🥤")
     
     
# ---------
# 第13天
# ---------
# 配置云端开发环境 GitPod


# ---------
# 第14天
# ---------
# import pandas_profiling
# from streamlit_pandas_profiling import st_profile_report

# st.header('`streamlit_pandas_profiling`')

# # df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
# df = pd.read_csv("penguins_cleaned.csv")

# pr = df.profile_report()
# st_profile_report(pr)

# import streamlit as st
# from streamlit_chat import message

# message("My message") 
# message("Hello bot!", is_user=True)  # align's the message to the right

# ---------
# 第15天
# ---------
# st.header('st.latex')

# st.latex(r'''
#      a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#      \sum_{k=0}^{n-1} ar^k =
#      a \left(\frac{1-r^{n}}{1-r}\right)
#      ''')


# ---------
# 第16天
# ---------
# import streamlit as st

# st.title('Customizing the theme of Streamlit apps')

# st.write('Contents of the `.streamlit/config.toml` file of this app')

# st.code("""
# [theme]
# primaryColor="#F39C12"
# backgroundColor="#2E86C1"
# secondaryBackgroundColor="#AED6F1"
# textColor="#FFFFFF"
# font="monospace"
# """)

# number = st.sidebar.slider('Select a number:', 0, 10, 5)
# st.write('Selected number from slider widget is:', number)

# ---------
# 第17天
# ---------
# # st.secrets 使你可以存储一些秘密信息，例如 API 密钥、数据库密码等其他验证信息。
# import streamlit as st

# st.title('st.secrets')

# st.write(st.secrets['message'])


# ---------
# 第18天
# ---------
# import streamlit as st
# import pandas as pd

# st.title('st.file_uploader')

# st.subheader('Input CSV')
# uploaded_file = st.file_uploader("Choose a file")

# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
#     st.subheader('DataFrame')
#     st.write(df)
#     st.subheader('Descriptive Statistics')
#     st.write(df.describe())
# else:
#     st.info('☝️ Upload a CSV file')

# ---------
# 第19天
# ---------
# 如何布局你的 Streamlit 应用
# st.set_page_config(layout="wide")

# st.title('How to layout your Streamlit app')

# with st.expander('About this app'):
#     st.write('This app shows the various ways on how you can layout your Streamlit app.')
#     st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

# st.sidebar.header('Input')
# user_name = st.sidebar.text_input('输入姓名')
# user_emoji = st.sidebar.selectbox('你现在的心情？', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
# user_food = st.sidebar.selectbox('中午计划吃什么？', ['', '牛肉汤', '猪脚面', '大米饭', '烤冷面', '煎饼🥞', '🥟'])

# with open(user_name+"午餐计划.txt", "w") as f:
#     f.write(user_name+"\n")
#     f.write(user_emoji+"\n")
#     f.write(user_food+"\n")

# st.header('Output')

# col1, col2, col3 = st.columns(3)

# with col1:
#     if user_name != '':
#         st.write(f'👋 你好呀 {user_name}!')
#     else:
#         st.write('👈  Please enter your **name**!')

# with col2:
#     if user_emoji != '':
#         st.write(f'{user_emoji} 是你现在的心情!')
#     else:
#         st.write('👈 Please choose an **emoji**!')

# with col3:
#     if user_food != '':
#         st.write(f'🍴 我中午要吃**{user_food}** !')
#     else:
#         st.write('👈 Please choose your favorite **food**!')

# ---------
# 第20天
# ---------
# # 线上讨论


# ---------
# 第21天
# ---------
# import streamlit as st
# import time

# st.title('st.progress')

# with st.expander('About this app'):
#     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

# my_bar = st.progress(0)

# for percent_complete in range(100):
#     time.sleep(0.01)
#     my_bar.progress(percent_complete + 1)

# st.write("恭喜你！算法已经执行完毕！没有报错！效果也不错！")
# st.balloons()


# ---------
# 第22天
# ---------
# st.title('st.form')

# # Full example of using the with notation
# st.header('1. Example of using `with` notation')
# st.subheader('Coffee machine')

# with st.form('my_form'):
#     st.subheader('**Order your coffee**')

#     # Input widgets
#     coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
#     coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
#     brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
#     serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
#     milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
#     owncup_val = st.checkbox('Bring own cup')

#     # Every form must have a submit button
#     submitted = st.form_submit_button('Submit')

# if submitted:
#     st.markdown(f'''
#         ☕ You have ordered:
#         - Coffee bean: `{coffee_bean_val}`
#         - Coffee roast: `{coffee_roast_val}`
#         - Brewing: `{brewing_val}`
#         - Serving type: `{serving_type_val}`
#         - Milk: `{milk_val}`
#         - Bring own cup: `{owncup_val}`
#         ''')
# else:
#     st.write('☝️ Place your order!')


# # Short example of using an object notation
# st.header('2. Example of object notation')

# form = st.form('my_form_2')
# selected_val = form.slider('Select a value')
# form.form_submit_button('Submit')

# st.write('Selected value: ', selected_val)


# ---------
# 第23天
# ---------
# st.experimental_get_query_params 允许获取用户所用链接中的查询参数。


# ---------
# 第24天
# ---------
# st.cache 使得你可以优化 Streamlit 应用的性能。
# Streamlit 提供了一个缓存机制，使你的应用即便是在从互联网加载数据、操作大数据集或者进行大开销的计算时仍可以保持高性能。这主要通过 @st.cache 装饰器来实现。
# import streamlit as st
# import numpy as np
# import pandas as pd
# from time import time

# st.title('st.cache')

# # Using cache
# a0 = time()
# st.subheader('Using st.cache')

# @st.cache_data
# def load_data_a():
#     df = pd.DataFrame(
#         np.random.rand(4000000, 5),
#         columns=['a', 'b', 'c', 'd', 'e']
#     )
#     return df

# st.write(load_data_a())
# a1 = time()
# st.info(a1-a0)


# # Not using cache
# b0 = time()
# st.subheader('Not using st.cache')

# def load_data_b():
#     df = pd.DataFrame(
#         np.random.rand(4000000, 5),
#         columns=['a', 'b', 'c', 'd', 'e']
#     )
#     return df

# st.write(load_data_b())
# b1 = time()
# st.info(b1-b0)

# ---------
# 第25天
# ---------
# 我们将通过一个浏览器标签页访问 Streamlit 应用定义为一个会话（Session）。
# 每个连接至 Streamlit 服务器的标签页都将创建一个会话。
# 每当你与应用中组件交互时，Streamlit 将从上到下地重新运行整个应用。
# 每次重新运行都将会清空历史：没有变量将被保留下来。

# 而会话状态（Session State）是一个在同一会话的不同次重新运行间共享变量的方法。
# 除了能够存储和保留状态，Streamlit 还提供了使用回调函数更改状态的支持。

# 在此教程中，我们将构建一个重量换算应用，并描述会话状态以及回调函数的用法。

# st.session_state 将允许我们在 Streamlit 应用中使用会话状态。


# ---------
# 第26-28天
# ---------
# 其它组件

# ---------
# 第29天
# ---------
# 如何使用 Hugging Face 和 Streamlit 搭建一个零样本学习文本分类器
# https://zero-shot-text-classifier.streamlit.app/
# https://github.com/streamlit/example-app-zero-shot-text-classifier

# ---------
# 第30天
# ---------
# https://30days-chinese.streamlit.app/?challenge=第30天

# import streamlit as st

# st.title('🖼️ yt-img-app')
# st.header('YouTube Thumbnail Image Extractor App')

# with st.expander('About this app'):
#     st.write('This app retrieves the thumbnail image from a YouTube video.')

# # Image settings
# st.sidebar.header('Settings')
# img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
# selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
# img_quality = img_dict[selected_img_quality]

# yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')

# def get_ytid(input_url):
#     if 'youtu.be' in input_url:
#         ytid = input_url.split('/')[-1]
#     if 'youtube.com' in input_url:
#         ytid = input_url.split('=')[-1]
#     return ytid

# # Display YouTube thumbnail image
# if yt_url != '':
#     ytid = get_ytid(yt_url) # yt or yt_url

#     yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
#     st.image(yt_img)
#     st.write('YouTube video thumbnail image URL: ', yt_img)
# else:
#     st.write('☝️ Enter URL to continue ...')