import json
import os, glob
from pydicom import dcmread
import re
import pymongo
import sys



def extract_cine_elements(data_dir, pat_range=None):
    """
    Function to extract and print information from the three dicom metadata elements used to classify
    a patient folder of Normal CT or Cine CT.
    
    Args:
        data_dir:               directory path to loop through. Should be the directory which contains the human folders.
        pat_range(optional):    list of ID range to loop through (e.g: [22,369]). If not given will iterate through all folders in data_dir.
    
    Prints:
        - Nominal Percentage Of Cardiac Phase
        - Image Comments
        - Series Description
    """
    if pat_range != None:
        if not isinstance(pat_range,list):
            sys.exit('Patient range must be a list.')
        if len(pat_range)>1:
            patients = [str(i) for i in range(pat_range[0],pat_range[1])]
        else:
            patients = [str(pat_range[0])]
    else:
        patients = list(filter(lambda f: os.path.isdir(os.path.join(data_dir,f)), [str(f) for f in os.listdir(data_dir)]))
    for human in sorted(os.listdir(data_dir)):
        if human in patients:
            print('-'*9+human+'-'*9)
            for pdir in sorted(os.listdir(os.path.join(data_dir,human))):
                if pdir.startswith('STD'):
                    for ser in sorted(os.listdir(os.path.join(data_dir,human,pdir))):
                        print('-'*3+ser+'-'*3)
                        nominal_phase = []
                        image_comments = []
                        series_desc = []
                        for img in sorted(os.listdir(os.path.join(data_dir,human,pdir,ser))):
                            path = os.path.join(data_dir,human,pdir,ser,img)
                            ds = dcmread(path, force=True)
                            try:
                                elem = ds['NominalPercentageOfCardiacPhase'].value
                                if str(elem) not in nominal_phase:
                                    nominal_phase.append(str(elem))
                            except KeyError:
                                pass
                            try:
                                elem2 = ds['ImageComments'].value
                                if elem2 not in image_comments:
                                    image_comments.append(elem2)
                            except KeyError:
                                pass 
                            try:
                                elem3 = ds['SeriesDescription'].value
                                if elem3 not in series_desc:
                                    series_desc.append(elem3)
                            except KeyError:
                                pass
                        print('Nominal Phase: ', nominal_phase)
                        print('Image Comments: ', image_comments)
                        print('Series Description: ', series_desc)

def scan_timestamps(field):
    """
    Function to detect phase elements from a list of strings.
    
    Args:
        field: list of strings.

    Returns:
        - list of phase elements detected in each string.
    """
    phase = []
    for i in field:
        phase_scan = re.search(r'(\d+(\.\d+)?%)', i)
        if phase_scan is None:
            phase_scan = re.search(r'(\d+(\ )?%)', i)
            if phase_scan is None:
                pass
            else:
                phase.append(phase_scan[0])
        else:
            phase.append(phase_scan[0])
    return phase



def cine_normal_classification(data_dir, pat_range=None):
    """
    Function to classify a patient scan of Normal CT or Cine CT.
    
    Args:
        data_dir:               directory path to loop through. Should be the directory which contains the human folders.
        pat_range(optional):    list of ID range to loop through (e.g: [22,369]). If not given will iterate through all folders in data_dir.
    
    Prints:
        - Classification of a patient scan
        - Number of timestamps for Cine CTs
        - Number of Normal and Cine CT found in data_dir
    """
    if pat_range != None:
        if not isinstance(pat_range,list):
            sys.exit('Patient range must be a list.')
        if len(pat_range)>1:
            patients = [str(i) for i in range(pat_range[0],pat_range[1])]
        else:
            patients = [str(pat_range[0])]
    else:
        patients = list(filter(lambda f: os.path.isdir(os.path.join(data_dir,f)), [str(f) for f in os.listdir(data_dir)]))
    
    count_cine = 0
    count_normal = 0
    for human in sorted(os.listdir(data_dir)):
        if human in patients:
            print('-'*9+human+'-'*9)
            for pdir in sorted(os.listdir(os.path.join(data_dir,human))):
                if pdir.startswith('STD'):
                    for ser in sorted(os.listdir(os.path.join(data_dir,human,pdir))):
                        nominal_phase = []
                        image_comments = []
                        series_desc = []
                        for img in sorted(os.listdir(os.path.join(data_dir,human,pdir,ser))):
                            path = os.path.join(data_dir,human,pdir,ser,img)
                            ds = dcmread(path, force=True)
                            try:
                                elem = ds['NominalPercentageOfCardiacPhase'].value
                                if str(elem) not in nominal_phase:
                                    nominal_phase.append(str(elem))
                            except KeyError:
                                if '' not in nominal_phase:
                                    nominal_phase.append('')
                            try:
                                elem2 = ds['ImageComments'].value
                                if elem2 not in image_comments:
                                    image_comments.append(elem2)
                            except KeyError:
                                if '' not in image_comments:
                                    image_comments.append('') 
                            try:
                                elem3 = ds['SeriesDescription'].value
                                if elem3 not in series_desc:
                                    series_desc.append(elem3)
                            except KeyError:
                                if '' not in series_desc:
                                    series_desc.append('')
                    #--------------------------------------------------#
                        ic_phase = scan_timestamps(image_comments)
                        if not ic_phase:
                            ic_phase = []
                        sd_phase = scan_timestamps(series_desc)
                        if not sd_phase:
                            sd_phase = []

                        if len(nominal_phase) > 1:
                            for i,_ in enumerate(nominal_phase):
                                if nominal_phase[i] == '':
                                    del nominal_phase[i]
                            if len(nominal_phase) > 1:
                                count_cine += 1
                                print(ser, '---> Cine CT w/',len(nominal_phase),'timestamps.')
                            else:
                                count_normal += 1
                                print(ser, '---> Normal CT')
                        elif nominal_phase != [''] and len(nominal_phase) <= 1:
                            print(ser, '---> Normal CT')

                        elif len(set(ic_phase)) > 1:
                            count_cine += 1
                            print(ser, '---> Cine CT w/',len(set(ic_phase)),'timestamps.')

                        elif len(set(sd_phase)) > 1:
                            count_cine += 1
                            print(ser, '---> Cine CT w/',len(set(sd_phase)),'timestamps.')
                        else:       
                            count_normal += 1
                            print(ser, '---> Normal CT')
                
    print('\nTotal cases found: \n -> Normal CTs: {normal} \n -> Cine CTs: {cine}'.format(normal=count_normal,cine=count_cine))


def delete_series_below20dcm(data_dir, pat_range=None):
    """
    Function to delete patient folders whom have less than 20 dicom files.
    This function assumes that a human folder already presents the correct structure,
    and have a numerical ID already attributed.

    Args:
        data_dir: a directory path which contains human folders
        pat_range(optional): list of ID range to loop through (e.g: [22,369]). 
                If not given will iterate through all folders that have a numerical ID in data_dir.  
    """
    if pat_range != None:
        if not isinstance(pat_range,list):
            sys.exit('Patient range must be a list.')
        if len(pat_range)>1:
            patients = [str(i) for i in range(pat_range[0],pat_range[1])]
        else:
            patients = [str(pat_range[0])]
    else:
        patients = list(filter(lambda f: f.isnumeric(), [str(f) for f in os.listdir(data_dir)]))
    for human in sorted(os.listdir(data_dir)):
        if human in patients:
            print('-'*9+human+'-'*9)
            for pdir in sorted(os.listdir(os.path.join(data_dir,human))):
                if pdir.startswith('STD'):
                    for ser in sorted(os.listdir(os.path.join(data_dir,human,pdir))):
                        print('-'*3+ser+'-'*3)
                        if len(glob.glob(os.path.join(data_dir,human,pdir,ser,'*.dcm'))) < 20:
                            print(ser)
                            shutil.rmtree(os.path.join(data_dir,human,pdir,ser))


def database_upload(connection_string,jsondir,dbname='database_v0'):
    """ Function to upload JSONs to Cosmos DB. It assumes that the directory which contains
    the JSONs presents the following structure:
        /jsondir/ 
            ├── 122
            │   └── SER00001
            │       │   └── imaging_collection.json
            |       |   └── patient_collection.json
            |       |   └── model_collection.json
            |       |   └── patient_reidentification_collection.json
            │   └── SER00002
            │       │   └── (....)
            └── 169
            │   └── SER00009
            │       │   └── (....)

        Args:
            connection_string:  azure storage account connection string
            jsondir:            JSONs directory
            dbname(optional):   desired name for the database (default: database_v0)
        
        Prints:
            - The number of documents deleted in each Cosmos DB collection before starting the upload
            - The number of documents inserted in each Cosmos DB collection after finishing the upload
        
        Note:
            If the database already exists, it will delete all the existing documents in the collections that the new JSONs 
            will be inserted. Otherwise it creates a new database.
"""
    print('*** Starting upload to the database ***')
    print('---------------------------------------')
    #connection to the DB
    #connection_string = 'mongodb://v-patients-saas-development:EHMvZGzcPNkb8TGAeHPmkTYT1Lxxj0zeSWv9jqGIKxan8CVBf8Rqh2oFm87I1soNwMPmZ8xDEmIgZpDrCaalfg==@v-patients-saas-development.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@v-patients-saas-development@'
    client = pymongo.MongoClient(connection_string)
    #load the database
    db = client.dbname

    #load the collection if exists, otherwise will create new ones
    imaging_collection = db.imaging_collection
    patient_collection = db.patient_collection
    reid_patient_collection = db.patient_reidentification_collection
    model_collection = db.model_collection

    #deletion of the current documents in the database
    #if new database will erase 0

    img_del = imaging_collection.delete_many({})
    pat_del = patient_collection.delete_many({})
    reid_del = reid_patient_collection.delete_many({})
    model_del = model_collection.delete_many({})

    print(img_del.deleted_count, "imaging documents deleted.") 
    print(pat_del.deleted_count, "patient documents deleted.") 
    print(reid_del.deleted_count, "reid documents deleted.")
    print(model_del.deleted_count, "model documents deleted.")
    print('---------------------------------------')

    #the upload most occur in the following order to respect the database design
    #collections ID referencing:  imaging/model -> patient -> reid-patient
    for i in sorted(os.listdir(jsondir), key=int):
        for series in os.listdir(os.path.join(jsondir,i)):
            for collection in os.listdir(os.path.join(jsondir,i,series)):
                if collection.startswith('imaging'):
                    with open(os.path.join(jsondir,i,series,collection)) as f:
                        data1 = json.load(f)   
                    imaging_id = imaging_collection.insert_one(data1).inserted_id
                    for collection in os.listdir(os.path.join(jsondir,i,series)): 
                        if collection.startswith('model'):
                            with open(os.path.join(jsondir,i,series,collection)) as f:
                                data2 = json.load(f)
                            model_id = model_collection.insert_one(data2).inserted_id
                            for collection in os.listdir(os.path.join(jsondir,i,series)): 
                                if collection.startswith('patient_coll'):
                                    with open(os.path.join(jsondir,i,series,collection)) as f:
                                        data3 = json.load(f)
                                    data3['imaging_data'] = imaging_id
                                    data3['models'] = model_id
                                    post_id2 = patient_collection.insert_one(data3).inserted_id
                                    for collection in os.listdir(os.path.join(jsondir,i,series)):
                                        if collection.startswith('patient_reid'):
                                            with open(os.path.join(jsondir,i,series,collection)) as f:
                                                data4 = json.load(f)
                                            #second referencing
                                            data4['patient_id'] = post_id2
                                            post_id3 = reid_patient_collection.insert_one(data3).inserted_id

    print(imaging_collection.count_documents({}), " inserted documents in Imaging collection.")
    print(model_collection.count_documents({}), " inserted documents in Model collection.")
    print(patient_collection.count_documents({}), " inserted documents in Patient collection.")
    print(reid_patient_collection.count_documents({}), " inserted documents in Reid-patient collection.")
    print('----------------------------')
    print('Database upload successfull.')