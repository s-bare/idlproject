import streamlit as st
import pandas as pd
import numpy as np
import datetime
import pydeck as pdk
import matplotlib.pyplot as plt
# import seaborn as sns
import plotly as px
import altair as alt

st.set_page_config(layout="wide")

st.title("""UNDERSTANDING POLITICAL POLARISATION USING NLP""")


url = 'https://drive.google.com/file/d/1D96k1no_9BGQ55YLARWHTyPFf43eOVle/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
# d_pol = pd.read_csv(path)
d_pol = pd.read_csv(r"C:\Users\supreethbare\Downloads\idlstreamlit\idlproject\distances_political.csv")


url = 'https://drive.google.com/file/d/1-9UtNi1wQ055iquSINU6alz1o_HIrmHZ/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
# d_bag = pd.read_csv(path)
d_bag = pd.read_csv(r"C:\Users\supreethbare\Downloads\idlstreamlit\idlproject\distances.csv")

url = 'https://drive.google.com/file/d/1--zUf5wJ56Tv40qqH92JsqiTrjTUwXjO/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
# pol = pd.read_csv(path)
pol = pd.read_csv(r"C:\Users\supreethbare\Downloads\idlstreamlit\idlproject\indices_political.csv")

url = 'https://drive.google.com/file/d/1-3E1rLV-ZjM0iP8kX_YmBvApHDScv8Ad/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
# bag = pd.read_csv(path)
bag = pd.read_csv(r"C:\Users\supreethbare\Downloads\idlstreamlit\idlproject\indices.csv")

url = 'https://drive.google.com/file/d/1-AmrSyx3xB247D5CeZ7HUx7N2eY2aezF/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
# name_party = pd.read_csv(path)
name_party = pd.read_csv(r"C:\Users\supreethbare\Downloads\idlstreamlit\idlproject\index_name_party.csv")

party = st.radio(
    "Select the Party",
   ('Democratic', 'Republican'))
if party == 'Democratic':
    st.write('You selected Democratic Party.')
elif party == 'Republican':
    st.write('You selected Republican Party.')

senator_belonging = name_party.index[name_party['party'] == party].tolist()

senator = st.selectbox(
'Which politician do you want to know more about?',
np.sort(name_party['names'][senator_belonging]))

st.write('You selected:', senator)

st.header('NEAREST NEIGHBOURS BELONGING TO: '+senator)

category = st.radio(
    "Select the Category",
   ('Background', 'Politics'))

if category == 'Politics':
    st.write('You selected Politics.')

    senator_index = pol.index[name_party['names'] == senator].tolist()

    n1 = int(pol['1'][senator_index])
    n2 = int(pol['2'][senator_index])
    n3 = int(pol['3'][senator_index])
    n4 = int(pol['4'][senator_index])
    n5 = int(pol['5'][senator_index])
    n6 = int(pol['6'][senator_index])
    n7 = int(pol['7'][senator_index])
    n8 = int(pol['8'][senator_index])
    n9 = int(pol['9'][senator_index])
    n10 = int(pol['10'][senator_index])
    n11 = int(pol['11'][senator_index])
    n12 = int(pol['12'][senator_index])
    n13 = int(pol['13'][senator_index])
    n14 = int(pol['14'][senator_index])
    n15 = int(pol['15'][senator_index])
    n16 = int(pol['16'][senator_index])
    n17 = int(pol['17'][senator_index])
    n18 = int(pol['18'][senator_index])
    n19 = int(pol['19'][senator_index])

    st.write(name_party['names'][n1],"    ",name_party['names'][n2], "  ",name_party['names'][n3],"   ",name_party['names'][n4],"   ",name_party['names'][n5])

    st.write(name_party['names'][n6],"   ",name_party['names'][n9], "  ",name_party['names'][n12],"   ",name_party['names'][n13],"   ",name_party['names'][n19])

    st.write(name_party['names'][n7],"   ",name_party['names'][n10], "  ",name_party['names'][n14],"   ",name_party['names'][n16],"   ",name_party['names'][n18])

    st.write(name_party['names'][n8],"   ",name_party['names'][n11], "  ",name_party['names'][n15],"   ",name_party['names'][n17],"   ")
        
        
    xarr = [d_pol['1'][senator_index],d_pol['2'][senator_index],d_pol['3'][senator_index],d_pol['4'][senator_index],d_pol['5'][senator_index],d_pol['6'][senator_index],d_pol['7'][senator_index],d_pol['8'][senator_index]
    ,d_pol['9'][senator_index],d_pol['10'][senator_index],d_pol['11'][senator_index],d_pol['12'][senator_index],d_pol['13'][senator_index],d_pol['14'][senator_index],d_pol['15'][senator_index],d_pol['16'][senator_index],d_pol['17'][senator_index],d_pol['18'][senator_index],d_pol['19'][senator_index]]
    y_arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    fig, ax = plt.subplots()
    temp_color = [name_party['party'][n1],name_party['party'][n2],name_party['party'][n3],name_party['party'][n4],name_party['party'][n5],name_party['party'][n6],name_party['party'][n7],name_party['party'][n8],      name_party['party'][n9],name_party['party'][n10],name_party['party'][n11],name_party['party'][n12],name_party['party'][n13],name_party['party'][n14],name_party['party'][n15],name_party['party'][n16],name_party['party'][n17],name_party['party'][n18],name_party['party'][n19]]
    color = []
    for i in temp_color:
        if i[0] == 'D':
            color.append('blue')
        else:
            color.append('red')
    print(color)
    fig, ax = plt.subplots()
    ax.scatter(x=y_arr, y=xarr, color=color)
    plt.title("Nearest Neighbours for Political Data")
    plt.xlabel("Rank")
    plt.ylabel("Distance")
    st.pyplot(fig)

elif category == 'Background':
    st.write('You selected Background.')

    senator_index = bag.index[name_party['names'] == senator].tolist()

    n1 = int(bag['1'][senator_index])
    n2 = int(bag['2'][senator_index])
    n3 = int(bag['3'][senator_index])
    n4 = int(bag['4'][senator_index])
    n5 = int(bag['5'][senator_index])
    n6 = int(bag['6'][senator_index])
    n7 = int(bag['7'][senator_index])
    n8 = int(bag['8'][senator_index])
    n9 = int(bag['9'][senator_index])
    n10 = int(bag['10'][senator_index])
    n11 = int(bag['11'][senator_index])
    n12 = int(bag['12'][senator_index])
    n13 = int(bag['13'][senator_index])
    n14 = int(bag['14'][senator_index])
    n15 = int(bag['15'][senator_index])
    n16 = int(bag['16'][senator_index])
    n17 = int(bag['17'][senator_index])
    n18 = int(bag['18'][senator_index])
    n19 = int(bag['19'][senator_index])

    st.write(name_party['names'][n1],"    ",name_party['names'][n2], "  ",name_party['names'][n3],"   ",name_party['names'][n4],"   ",name_party['names'][n5])

    st.write(name_party['names'][n6],"   ",name_party['names'][n9], "  ",name_party['names'][n12],"   ",name_party['names'][n13],"   ",name_party['names'][n19])

    st.write(name_party['names'][n7],"   ",name_party['names'][n10], "  ",name_party['names'][n14],"   ",name_party['names'][n16],"   ",name_party['names'][n18])

    st.write(name_party['names'][n8],"   ",name_party['names'][n11], "  ",name_party['names'][n15],"   ",name_party['names'][n17],"   ")


    xarr = [d_bag['1'][senator_index],d_bag['2'][senator_index],d_bag['3'][senator_index],d_bag['4'][senator_index],d_bag['5'][senator_index],d_bag['6'][senator_index],d_bag['7'][senator_index],d_bag['8'][senator_index]
    ,d_bag['9'][senator_index],d_bag['10'][senator_index],d_bag['11'][senator_index],d_bag['12'][senator_index],d_bag['13'][senator_index],d_bag['14'][senator_index],d_bag['15'][senator_index],d_bag['16'][senator_index],d_bag['17'][senator_index],d_bag['18'][senator_index],d_bag['19'][senator_index]]
    y_arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    temp_color = [name_party['party'][n1],name_party['party'][n2],name_party['party'][n3],name_party['party'][n4],name_party['party'][n5],name_party['party'][n6],name_party['party'][n7],name_party['party'][n8],      name_party['party'][n9],name_party['party'][n10],name_party['party'][n11],name_party['party'][n12],name_party['party'][n13],name_party['party'][n14],name_party['party'][n15],name_party['party'][n16],name_party['party'][n17],name_party['party'][n18],name_party['party'][n19]]
    color = []
    for i in temp_color:
        if i[0] == 'D':
            color.append('blue')
        else:
            color.append('red')
    # print(color)
    fig, ax = plt.subplots()
    ax.scatter(x=y_arr, y=xarr, color=color)
    plt.title("Nearest Neighbours for Background Data")
    plt.xlabel("Rank")
    plt.ylabel("Distance")
    st.pyplot(fig)