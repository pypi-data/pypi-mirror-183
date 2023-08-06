import pandas as pd
import numpy as np
from pathlib import Path


#this file contains the functions used to parse information of the patients of each bulk from CSVs


def theart_csv_parse(human,nominal_phase,patientdict):
    """
    Function to parse CSV data from T-Heart patients.

    Args
    ------
        human (str) :  human ID
        nominal_phase (list) :  cardiac phase elements present in nominal phase of the cardiac cycle metadata field
        patientdict (dict) :  patient dict

    Return
    ------
        patientdict (dict) :  patient dict
        
    """
    correspondence = {}
    #making the correspondence between raw theart ID and our internal ID
    for i,j in zip(range(0,66),range(642,708)):
        correspondence[str(j)] = i
    
    theart_df = pd.read_csv('/home/database/csvs/ES_ED-theart.csv')
    theart_df = theart_df.replace({'-':None})
    theart_df = theart_df.where(pd.notnull(theart_df), None)
    idx = correspondence[human]
    #neglect human 658 due to data incongruities
    if human != '658':
        nominal_phase.sort()
        patientdict['es_timestamp'] = round(nominal_phase.index(str(round(theart_df['ES'][idx]*100,2)))/len(nominal_phase),2)
        patientdict['ed_timestamp'] = round(nominal_phase.index(str(round(theart_df['ED'][idx]*100,2)))/len(nominal_phase),2)

    if theart_df['Age'][idx]:
        patientdict['age'] = int(theart_df['Age'][idx])
    if theart_df['Gender'][idx]:
        patientdict['gender'] = theart_df['Gender'][idx]
    if theart_df['Weight'][idx]:            
        patientdict['weight'] = float(theart_df['Weight'][idx])
    if theart_df['Height'][idx]:
        patientdict['height'] = float(theart_df['Height'][idx])

    return patientdict

def toulouse_csv_parse(human,patientdict,path):
    """
    Function to parse CSV data from Toulouse databulk.

    Args
    ------
        human (str) :  human ID
        patientdict (dict) :  patient dict
        path (str) :  patient dir absolute path 
    
    Return
    ------
        patientdict (dict) :  patient dict
    """

    df = pd.read_csv('/home/database/csvs/toulouse_info.csv', delimiter=';')
    df = df.astype(object).replace(np.nan, 'None')
    pat_ser = Path(path).stem

    for i in ['es_timestamp','ed_timestamp']:
        patientdict[i] = df[(df['human']== int(human)) & (df['series']== pat_ser)][i].to_numpy()[0]
        if patientdict[i] == 'None':
            patientdict[i] = None

    patientdict['body_rois'][0]['catalog_tag'] = df[(df['human']== int(human)) & (df['series']== pat_ser)]['body_rois'].to_numpy()[0]

    return patientdict

def canada_china_csv_parse(human,patientdict,path):
    """
    Function to parse CSV data from Canada and China databulks.

    Args
    ------
        human (str) :  human ID
        patientdict (dict) :  patient dict
        path (str) :  patient dir absolute path 
    
    Return
    ------
        patientdict (dict) :  patient dict
    """

    df = pd.read_csv('/home/database/csvs/canada_china_info.csv')
    df = df.astype(object).replace(np.nan, 'None')
    pat_ser = Path(path).stem
    
    for i in ['gender','age','height','weight','origin_location','origin_ethnicity']:
        patientdict[i] = df[(df['human']== int(human)) & (df['series']== pat_ser)][i].to_numpy()[0]
        if patientdict[i] == 'None':
            patientdict[i] = None

    if patientdict['imaging']['body_part_examined'] in ['',' ',None]:
        patientdict['imaging']['body_part_examined'] = df[(df['human']== int(human)) & (df['series']== pat_ser)]['body_part'].to_numpy()[0]
        if patientdict['imaging']['body_part_examined'] == 'None':
            patientdict['imaging']['body_part_examined'] = None

    patientdict['body_rois'][0]['catalog_tag'] = df[(df['human']== int(human)) & (df['series']== pat_ser)]['body_part'].to_numpy()[0]
    if patientdict['body_rois'][0]['catalog_tag'] == 'None':
        patientdict['body_rois'][0]['catalog_tag'] = None

    return patientdict

def realheart_csv_parse(human,patientdict):
    """
    Function to parse CSV data from Realheart databulk.

    Args
    ------
        human (str) :  human ID
        patientdict (dict) :  patient dict
    
    Return
    ------
        patientdict (dict) :  patient dict
    """

    df = pd.read_csv('/home/database/csvs/realheart.csv')
    df['human_id'] = df['human_id'].fillna(0).astype(int)
    df = df.replace(np.nan, 'None')
    for i in ['gender','weight','height']:
        patientdict[i] = df[df['human_id']==int(human)].iloc[0][i]
    patientdict['height'] = patientdict['height']*100
    
    return patientdict




    