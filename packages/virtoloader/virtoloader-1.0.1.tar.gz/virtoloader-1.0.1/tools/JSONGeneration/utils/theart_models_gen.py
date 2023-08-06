import os
import pandas as pd
import copy
from utils.matching_dict import match_landmarks, match_models
def initialize_theart_model_jsongen(human,now):
    """
    Function to initialize the T-Heart models' JSONs generation.

    Args
    ------
        human (str) :  human ID
        now (:obj:) :  JSONGen process starting time
    
    Return
    ------
        patientdict (dict) :  patient dict
    """

    models_dir = '/home/database/models/theart/theart_models/'
    patient_list = [name for name in os.listdir(models_dir) if os.path.isdir(os.path.join(models_dir, name))]
    if human in patient_list:
        filename = "/home/database/models/theart/model_transfer/ed_es.txt"
        df_timestamps = pd.read_csv(filename)
        n = []
        for i in sorted(list(df_timestamps['pat_ID'])):
            if len(str((i))) < 2:
                n.append('00'+str(i))
            else:
                n.append('0'+str(i))
        df_timestamps['pat_ID'] = n
        #----------------------------------------------#
        #patients correspondence (raw ID - internal ID)
        lm = sorted(os.listdir('/home/database/models/theart/model_transfer/Coordinates stripped/'))
        rem = ['003','009','026','029','031','058','064']
        for i in rem:
            lm.remove(i)
        corr = {}
        for i,j in zip(lm, range(642,703)):
            corr[str(i)] = str(j)
        #----------------------------------------------#
        pd.options.mode.chained_assignment = None
        for e,i in enumerate(df_timestamps['pat_ID']):
            try:
                df_timestamps['pat_ID'][e] = corr[str(i)]
            except:
                continue
        #----------------------------------------------#
        print('Generating models\' json for human:', human)
        return generate_model_jsons(human, models_dir, df_timestamps, now)


def generate_model_jsons(human, models_dir, df_timestamps, now):
    """
    Function to generate the T-Heart models' JSONs generation.

    Args
    ------
        human (str) :  human ID
        models_dir (str) :  T-Heart models path
        df_timestamps (pd.dataframe) : contains the ES and ED timestamps of each human
        now (:obj:) :  JSONGen process starting time
    
    Return
    ------
        modeldict (dict) :  model dict
    """

    df_nomenclature = pd.read_csv('/home/database/models/theart/model_transfer/nomenclature.csv')
    landmarks_dir = "/home/database/models/theart/model_transfer/coords/"
    df_pat = df_timestamps.loc[df_timestamps['pat_ID'] == str(human)]

    modeldict = {'datetime_creation': now,
                'URI': 'https://virtonomydatamanaged0.blob.core.windows.net/',
                'models': []}
   
    submodeldic = {'timestamp': None,
                    'sub_models':[{
                                'blob': '',
                                'name': ''
                            },
                                    {
                                'blob': '',
                                'name': ''
                            },
                                    {
                                'blob': '',
                                'name': ''
                        }],
                    'landmarks':[]
                        }
    patient_dir = os.path.join(models_dir, human)
    timestamps_list = sorted(os.listdir(patient_dir))
    for timestamp in timestamps_list:
        # temporary fix while not all frames are segmented 
        if len(timestamps_list) < 4:
            submodeldic['timestamp'] = float(timestamp)/100
        else:
            submodeldic['timestamp'] = round(timestamps_list.index(timestamp)/len(timestamps_list),2)
        for path, subdirs, files in os.walk(os.path.join(patient_dir, timestamp)):
            for name in files:
                for blob,blob_i in zip(files,submodeldic['sub_models']):
                    blob_i['blob'] = os.path.join(path, blob).replace("\\","/")[2:]
                    for x,y in match_models.items():
                        if x in blob:
                            blob_i['name'] = y
        #print(landmarks_dir + human)                   
        if os.path.isdir(landmarks_dir + human):
            files_landmarks = os.listdir(landmarks_dir + human)
            if float(timestamp)/100 == df_pat['ES'].to_numpy()[0]:
                for f in files_landmarks:
                    subdic_landmark = {
                                    'name': '',
                                    'value':'',
                                    'description':'',
                                    'type_of_spline':''}
                    if 'ES' in f:
                        df = pd.read_csv(os.path.join(landmarks_dir,human,f))
                        temp = df.to_numpy()
                        subdic_landmark['value'] = temp.tolist()
                        for x,y in match_landmarks.items():
                            if x in f:
                                nomenclature = df_nomenclature[df_nomenclature['NAME'].str.contains(x)]
                                subdic_landmark['name'] = y
                                subdic_landmark['description'] = nomenclature['DESCRIPTION'].to_list()[0]
                                subdic_landmark['type_of_spline'] = nomenclature['Type of spline'].to_list()[0]
                        submodeldic['landmarks'].append(copy.deepcopy(subdic_landmark))
            elif float(timestamp)/100 == df_pat['ED'].to_numpy()[0]:
                for f in files_landmarks:
                    subdic_landmark = {
                                    'name': '',
                                    'value':'',
                                    'description':'',
                                    'type_of_spline':''}
                    if 'ED' in f:
                        df = pd.read_csv(os.path.join(landmarks_dir,human,f))
                        temp = df.to_numpy()
                        subdic_landmark['value'] = temp.tolist()
                        for x,y in match_landmarks.items():
                            if x in f:
                                nomenclature = df_nomenclature[df_nomenclature['NAME'].str.contains(x)]
                                subdic_landmark['name'] = y
                                subdic_landmark['description'] = nomenclature['DESCRIPTION'].to_list()[0]
                                subdic_landmark['type_of_spline'] = nomenclature['Type of spline'].to_list()[0]
                        submodeldic['landmarks'].append(copy.deepcopy(subdic_landmark))

        modeldict['models'].append(copy.deepcopy(submodeldic))

    return modeldict

def default_modeldict(now):
    """
    Function to return the standard structure of a model collection document.
    Currently being given to every patient which do not have models.

    Args
    ------
        now (:obj:) :  JSONGen process starting time
    
    Return
    ------
        modeldict (dict) :  model dict
    """


    modeldict = {'datetime_creation': now,
                'URI': 'https://virtonomydatamanaged0.blob.core.windows.net/',
                'models': [{'timestamp': None,
                    'sub_models':[{
                                'blob': None,
                                'name': None
                        }],
                    'landmarks':None
                        }]
    }

    return modeldict