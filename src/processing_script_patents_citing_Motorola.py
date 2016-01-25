# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:08:56 2016

@author: Thibault
"""

import pandas as pd
import numpy as np

#%%Loading the data
data_dir='/Users/Thibault/Documents/Boulot/UC Berkeley/CAPSTONE PATENT/'

# training and validation sets
train_file = data_dir + 'blocking1114.csv'

#Opening the blocking data
TrainFile=pd.read_csv(train_file, header=None)
TrainFile.columns=['Application','Patent_Blocking']


#Opening the Portfolio database

portf = data_dir + 'SamplePortfolioforBerkeley .csv'
Moto_database=pd.read_csv(portf, sep=';')


#%%Creating the query

Moto_Patents=np.asarray(Moto_database['Patent #'])

#Returns 
def foo(s1):
    return "'{}'".format(s1)
    
def query(table): 
    query='SELECT uspatentcitation.citation_id, uspatentcitation.patent_id FROM uspatentcitation WHERE uspatentcitation.citation_id='
    for k in table:
        if k!=table[-1]:
            query+= foo(str(k)) + ' OR uspatentcitation.citation_id='
        else:
            query+= foo(str(k)) 
    return query

def query_with_dates(table): 
    query='SELECT uspatentcitation.citation_id, uspatentcitation.patent_id, uspatentcitation.date, patent.date FROM uspatentcitation INNER JOIN patent ON patent.id=uspatentcitation.patent_id WHERE uspatentcitation.citation_id='
    for k in table:
        if k!=table[-1]:
            query+= foo(str(k)) + ' OR uspatentcitation.citation_id='
        else:
            query+= foo(str(k)) 
    return query

print(query(Moto_Patents))


#%% 1. WITHOUT DATES 
"""downloading the patents that cited motorola patents, without dates"""

#Importing and merging the database of patents which cited Motorola patents

cit_moto1_dir = data_dir + 'Citing_Moto_1.csv'
cit_moto2_dir = data_dir + 'Citing_Moto_2.csv'
cit_moto3_dir = data_dir + 'Citing_Moto_3.csv'

Cit_Moto_data_1=pd.read_csv(cit_moto1_dir, sep=',')
Cit_Moto_data_2=pd.read_csv(cit_moto2_dir, sep=',')
Cit_Moto_data_3=pd.read_csv(cit_moto3_dir, sep=',')

frames = [Cit_Moto_data_1, Cit_Moto_data_2, Cit_Moto_data_3]

#Concatenating
Cit_Moto_database= pd.concat(frames,ignore_index=True)

#Changing titles of columns
Cit_Moto_database.columns=['Motorola_Patents_Being_Cited','Patent_Citing']

#Creating a csv file with the dataset
Cit_Moto_database.to_csv('patentscitingMotorola.csv', sep=',')

#%% 2. WITH DATES 
"""downloading the patents that cited motorola patents, with the dates"""

#Importing and merging the database of patents which cited Motorola patents

cit_moto1_dir_dates = data_dir + 'Citing_Moto_1_dates.csv'
cit_moto2_dir_dates = data_dir + 'Citing_Moto_2_dates.csv'
cit_moto3_dir_dates = data_dir + 'Citing_Moto_3_dates.csv'

Cit_Moto_data_1_dates=pd.read_csv(cit_moto1_dir_dates, sep=',')
Cit_Moto_data_2_dates=pd.read_csv(cit_moto2_dir_dates, sep=',')
Cit_Moto_data_3_dates=pd.read_csv(cit_moto3_dir_dates, sep=',')

frames_dates = [Cit_Moto_data_1_dates, Cit_Moto_data_2_dates, Cit_Moto_data_3_dates]

#Concatenating
Cit_Moto_database_dates= pd.concat(frames_dates,ignore_index=True)
Cit_Moto_database_dates.columns=['Motorola_Patents_Being_Cited','Patent_Citing','Date_Motorola_Patent','Date_Citing_Patent']

#Creating a csv file with the dataset
Cit_Moto_database_dates.to_csv('patentscitingMotorola_dates.csv', sep=',')


#%% 3. PATENTS FROM 2011 - 2014 
"""downloading the patents that cited motorola patents, between 2011 and 2014"""

def query_1114(table): 
    query='SELECT uspatentcitation.citation_id, uspatentcitation.patent_id, uspatentcitation.date, patent.date FROM uspatentcitation INNER JOIN patent ON patent.id=uspatentcitation.patent_id WHERE patent.date BETWEEN ' + foo('2011/01/01') + ' AND ' + foo('2015/01/01') + ' AND (uspatentcitation.citation_id='
    for k in table:
        if k!=table[-1]:
            query+= foo(str(k)) + ' OR uspatentcitation.citation_id='
        else:
            query+= foo(str(k)) + ')'
    return query

print(query_1114(Moto_Patents))


#Importing and merging the database of patents which cited Motorola patents

cit_moto1_dir_1114 = data_dir + 'Citing_Moto_1_1114.csv'
cit_moto2_dir_1114 = data_dir + 'Citing_Moto_2_1114.csv'
cit_moto3_dir_1114 = data_dir + 'Citing_Moto_3_1114.csv'

Cit_Moto_data_1_1114=pd.read_csv(cit_moto1_dir_1114, sep=',')
Cit_Moto_data_2_1114=pd.read_csv(cit_moto2_dir_1114, sep=',')
Cit_Moto_data_3_1114=pd.read_csv(cit_moto3_dir_1114, sep=',')

frames_1114 = [Cit_Moto_data_1_1114, Cit_Moto_data_2_1114, Cit_Moto_data_3_1114]

#Concatenating
Cit_Moto_database_1114= pd.concat(frames_1114,ignore_index=True)
Cit_Moto_database_1114.columns=['Motorola_Patents_Being_Cited','Patent_Citing','Date_Motorola_Patent','Date_Citing_Patent']

#Creating a csv file with the dataset
Cit_Moto_database_1114.to_csv('patentscitingMotorola_1114.csv', sep=',')
