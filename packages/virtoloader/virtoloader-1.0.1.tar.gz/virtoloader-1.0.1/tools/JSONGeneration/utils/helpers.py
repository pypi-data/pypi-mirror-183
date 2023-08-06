import os
import math

def create_jsondirs(datadir,jsondir,humans):
    """
    Function to create the JSON destination directory and their subdirs according to the human IDs.

    Args
    ------
        datadir (str) :  Data directory
        jsondir (str) : JSON destination directory
        humans (list) :  list of human IDs
        
    """

    for i in humans:
        os.makedirs(os.path.join(jsondir,i), exist_ok=True)
        for std in os.listdir(os.path.join(datadir,i)):
            if std.startswith('STD'):
                for folder in os.listdir(os.path.join(datadir,i,std)):
                    os.makedirs(os.path.join(jsondir,i,folder), exist_ok=True)

    print('JSONs directory created.')


def calculate_bmi(patientdict):
    """
    Function to calculate the Body Mass Index (BMI) based on weight in kg and height in meter
    
    Args
    ------
        patientdict (dict) :  patient dict 
        
    Return
    ------
        None
        bmi (float) 

    """

    if patientdict['weight'] is None or patientdict['height'] is None:
        return None
    bmi = round(patientdict['weight']/math.pow(patientdict['height']/100, 2),2)
    if math.isnan(bmi):
        return None
    return bmi


def calculate_mosteller_bsa(patientdict):
    """    
    Calculate Mosteller Body Surface Area (BSA)[m2] based on weight in kg and height in centimeter
    
    Args
    ------
        patientdict (dict) :  patient dict 
        
    Return
    ------
        None
        bmi (float) 

    """
    if patientdict['weight'] is None or patientdict['height'] is None:
        return None
    bsa = round(math.sqrt(patientdict['weight']*patientdict['height']/3600),2)
    if math.isnan(bsa):
        return None
    return bsa