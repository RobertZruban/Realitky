

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as mse
from math import sqrt
import matplotlib.pyplot as plt
import time
import requests
import json
import os

st.title('Real Estate Predictions')

def run_status():
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'Percent Complete {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)
        st.empty()

st.subheader('Multi Model Predictions')


def load_data():
    df=pd.read_csv('Flats_only.csv')
    #df=df.drop(['latitude'],axis=1)
    #df=df.drop(['longitude'],axis=1)
    df=df[df['Cena']>0]
    #df.rename(columns={'statezip':'zip'}, inplace=True)
    #df['zip']=df['zip'].str.replace('WA','').astype(int)
    #df['floors']=df['floors'].astype(int)
    df=df[df['Izby']>0]
    df=df[df['Plocha']>0]
    df=df[df['longitude']>0]
    df=df[df['latitude']>0]
    df=df[df['distance_from_centre']>0]
    return df

df=load_data()


st.sidebar.subheader('Property Options')
# Sidebar Options:
params={
'Izby' : st.sidebar.selectbox('Number of rooms',(1,2,3,4,5,6)),
#'bathrooms' : st.sidebar.selectbox('Bathrooms',(1,1.5,2,2.5,3,3.5,4,4.5,5)),
#'floors' : st.sidebar.selectbox('Floors',(df['floors'].unique())),
'Plocha' : st.sidebar.slider('Flat size in meters', 0,120,step=1),
'distance_from_centre' : st.sidebar.slider('Distance from Bratislava (km)', 0,350,step=1)
#'Kraj' : st.sidebar.selectbox('Kraj',('Nitriansky', 'Banskobystrický', 'Trnavský', 'Bratislava', 'Trenčiansky', 'Žilinský', 'Prešovský', 'Bratislavský', 'Košice', 'Košický '))
#'waterfront':1 if st.sidebar.checkbox('Waterfront') else 0
    
}


def get_locations(zip):
    url='https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&q={}&facet=state&facet=timezone&facet=dst'.format(zip)
    data=requests.get(url).json()
    lat=data['records'][0]['fields']['latitude']
    lng=data['records'][0]['fields']['longitude']
    return lat, lng

def map_df(df):
    df=df[df['Izby']==params['Izby']]
    df=df[df['Plocha']==params['Plocha']]
    df = df[df['distance_from_centre']==df['distance_from_centre']]
    #df=df[(df['Plocha_living']>0.9*params['Plocha']) & (df['Plocha_living']<1.1*params['Plocha'])]
    df.reset_index()
    df=df[df['latitude']==df['latitude']]
    df =df[df['longitude']==df['longitude']]
    


    #df['lon']=[get_locations(df.iloc[[i]]['zip'].values.astype(int))[1] for i in range(len(df))]
    return df

test_size=st.sidebar.slider('Pick Test Size', 0.05,0.5,0.25,step=0.05)


def get_models():
    y=df['Cena']
    X=df[['Izby','Plocha','distance_from_centre']]#'Plocha living'
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42, shuffle=True)
    models = [DummyRegressor(strategy='mean'),
    RandomForestRegressor(n_estimators=170,max_depth=25),
    DecisionTreeRegressor(max_depth=25),
    GradientBoostingRegressor(learning_rate=0.01,n_estimators=200,max_depth=5), 
    LinearRegression(n_jobs=10)]
    df_models = pd.DataFrame()
    temp = {}
    print(X_test)
    #run through models
    for model in models:
        print(model)
        m = str(model)
        temp['Model'] = m[:m.index('(')]
        model.fit(X_train, y_train)
        temp['RMSE_Price'] = sqrt(mse(y_test, model.predict(X_test)))
        temp['Pred Value']=model.predict(pd.DataFrame(params,  index=[0]))[0]
        print('RMSE score',temp['RMSE_Price'])
        df_models = df_models.append([temp])
    df_models.set_index('Model', inplace=True)
    pred_value=df_models['Pred Value'].iloc[[df_models['RMSE_Price'].argmin()]].values.astype(float)
    return pred_value, df_models


def run_data():
    #run_status()
    df_models=get_models()[0][0]
    st.write('Given your parameters, the predicted value is **€{:,.0f}**'.format(df_models))
    df1=map_df(df)
    st.map(df1)
    df1

def show_ML():
    df_models=get_models()[1]
    df_models
    st.write('**This diagram shows root mean sq error for all models**')
    st.bar_chart(df_models['RMSE_Price'])

btn = st.sidebar.button("Predict")
if btn:
    run_data()
else:
    pass

if st.sidebar.button('Show JSON'):
    df_models=get_models()[0][0]
    st.json(map_df(df).to_json())

if st.sidebar.button('Close JSON'):
    run_data()

st.sidebar.subheader('Additional Information')

if st.sidebar.checkbox('Show ML Models'):
    run_data()
    df_models=get_models()[1]
    df_models
    st.write('**This diagram shows root mean sq error for all models**')
    st.bar_chart(df_models['RMSE_Price'])

if st.sidebar.checkbox('Show Raw Data'):
	df