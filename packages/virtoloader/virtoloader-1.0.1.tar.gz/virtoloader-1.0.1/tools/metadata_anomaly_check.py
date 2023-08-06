import os
import sys
from pydicom import dcmread
from VirtoLoader.tools.utils import scan_timestamps



def check_series_number(data_dir, pat_range=None, full_info=True):
    """
    Function to verify if more than one series number exists in a patient folder (scan).
    
    Args:
        data_dir:               directory path to loop through. Should be the directory which contains the human folders.
        pat_range(optional):    list of ID range to loop through (e.g: [22,369]). If not given will iterate through all folders in data_dir.
        full_info(optional):    bollean that indicates wether the user wants that the full information be printed out. If set to True, the
                                function will print out if there was any error opening a dicom metadata or extracting the desired field, in this case 'SeriesNumber'.
                                If set to False, it will neglect the existance of these errors.  (default: True)
    
    Prints:
        - If more than one series number exists in a patient folder.
        - A list of the series numbers found in the case that more than one exists in a patient folder.
    
    Raises:
        - Error opening a dicom metadata or extracting 'SeriesNumber'.
    """

    if full_info not in [True,False]:
        sys.exit('Full info arg must be True/False.')
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
            for pdir in os.listdir(os.path.join(data_dir,human)):
                if pdir.startswith('STD'):
                    for ser in sorted(os.listdir(os.path.join(data_dir,human,pdir))):
                        print('-'*3+ser+'-'*3)
                        series_number = []
                        for img in sorted(os.listdir(os.path.join(data_dir,human,pdir,ser))):
                            path = os.path.join(data_dir,human,pdir,ser,img)
                            try:
                                ds = dcmread(path, force=True)
                                elem = ds['SeriesNumber'].value
                                if str(elem) not in series_number:
                                    series_number.append(str(elem))
                            except:
                                if full_info:
                                    print('Error getting series number in:', img)
                                else:
                                    pass
                        if len(series_number) > 1:
                            print('More than one series number detected!')
                            print('Series numbers: ', series_number)
                            print('---------------------------')



def check_acquisition_number(data_dir, pat_range=None, full_info=True):
    """
    Function to verify if more than one acquisition number exists in a patient folder (scan).
    
    Args:
        data_dir:               directory path to loop through. Should be the directory which contains the human folders.
        pat_range(optional):    list of ID range to loop through (e.g: [22,369]). If not given will iterate through all folders in data_dir.
        full_info(optional):    bollean that indicates wether the user wants that the full information be printed out. If set to True, the
                                function will print out if there was any error opening a dicom metadata or extracting the desired field, in this case 'AcquisitionNumber'.
                                If set to False, it will neglect the existance of these errors.  (default: True)
    
    Prints:
        - If more than one acquisition number exists in a patient folder.
        - A list of the acquisition numbers found in the case that more than one exists in a patient folder.

    Raises:
        - Error opening a dicom metadata or extracting 'AcquisitionNumber'.
    """

    if full_info not in [True,False]:
        sys.exit('Full info arg must be True/False.')
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
            for pdir in os.listdir(os.path.join(data_dir,human)):
                if pdir.startswith('STD'):
                    for ser in sorted(os.listdir(os.path.join(data_dir,human,pdir))):
                        print('-'*3+ser+'-'*3)
                        acquisition_number = []
                        for img in sorted(os.listdir(os.path.join(data_dir,human,pdir,ser))):
                            path = os.path.join(data_dir,human,pdir,ser,img)
                            try:
                                ds = dcmread(path, force=True)
                                elem = ds['AcquisitionNumber'].value
                                if str(elem) not in acquisition_number:
                                    acquisition_number.append(str(elem))
                            except:
                                if full_info:
                                    print('Error getting acquisition number in :', img)
                                else:
                                    pass
                        if len(acquisition_number) > 1:
                            print('More than one acquisition number detected!')
                            print('Acquisition numbers: ', acquisition_number)
                            print('---------------------------')

def check_pixel_spacing(data_dir, pat_range=None, full_info=True):
    """
    Function to verify if more than one pixel spacing pair exists in a patient folder (scan).
    
    Args:
        data_dir:               directory path to loop through. Should be the directory which contains the human folders.
        pat_range(optional):    list of ID range to loop through (e.g: [22,369]). If not given will iterate through all folders in data_dir.
        full_info(optional):    bollean that indicates wether the user wants that the full information be printed out. If set to True, the
                                function will print out if there was any error opening a dicom metadata or extracting the desired field, in this case 'PixelSpacing'.
                                If set to False, it will neglect the existance of these errors.  (default: True)
    
    Prints:
        - If more than one pair of pixel spacing exists in a patient folder.
        - The distribution (number of occurences) of the pixel spacing pairs found in the case that more than one exists in a patient folder. 

    Raises:
        - Error opening a dicom metadata or extracting 'PixelSpacing'.
    """
    

    if full_info not in [True,False]:
        sys.exit('Full info arg must be True/False.')
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
                        pixel_spacing = {}
                        for img in sorted(os.listdir(os.path.join(data_dir,human,pdir,ser))):
                            path = os.path.join(data_dir,human,pdir,ser,img)                                
                            try:
                                ds = dcmread(path, force=True)
                                elem = ds['PixelSpacing'].value
                                pixel_spacing[img] = elem                                   
                            except:
                                if full_info:
                                    print('Error getting pixel spacing in', img)
                                else:
                                    pass
                        px_values = {}
                        for img,value in pixel_spacing.items():
                            if tuple(value) not in px_values:
                                px_values[tuple(value)] = [img]
                            elif tuple(value) in px_values:
                                px_values[tuple(value)].append(img)
                        if len(px_values) > 1:
                            print('More than one pair of pixel spacing detected!')
                            freq = {}
                            for value,img in px_values.items():
                                freq[value] = len(img)
                            print('Distribution of the extracted pairs:', freq)


def check_slice_thickness(data_dir, pat_range=None, full_info=True):
    """
    Function to verify if more than one slice thickness value exists in a patient folder (scan).
    
    Args:
        data_dir:               directory path to loop through. Should be the directory which contains the human folders.
        pat_range(optional):    list of ID range to loop through (e.g: [22,369]). If not given will iterate through all folders in data_dir.
        full_info(optional):    bollean that indicates wether the user wants that the full information be printed out. If set to True, the
                                function will print out if there was any error opening a dicom metadata or extracting the desired field, in this case 'SliceThickness'.
                                If set to False, it will neglect the existance of these errors.  (default: True)
    
    Prints:
        - If more than one slice thickness value exists in a patient folder.
        - The distribution (number of occurences) of the slice thickness values found in the case that more than one exists in a patient folder. 

    Raises:
        - Error opening a dicom metadata or extracting 'SliceThickness'.
    """

    if full_info not in [True,False]:
        sys.exit('Full info arg must be True/False.')
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
                        slice_thickness = {}
                        for img in sorted(os.listdir(os.path.join(data_dir,human,pdir,ser))):
                            path = os.path.join(data_dir,human,pdir,ser,img)                                
                            try:
                                ds = dcmread(path, force=True)
                                elem1 = ds['SliceThickness'].value
                                if elem1 not in slice_thickness:
                                    slice_thickness[elem1] = [img]
                                else:
                                    slice_thickness[elem1].append(img)
                            except:
                                if full_info:
                                    print('Error getting slice thickness in', img)
                                else:
                                    pass         
                        if len(slice_thickness)>1:
                            print('More than one slice thickness value detected!')
                            dist = {}
                            for value,img in slice_thickness.items():
                                dist[value] = len(slice_thickness[value])
                            print('Distribution of the extracted values:', dist)

def check_spacingbetweenslices(data_dir, pat_range=None, full_info=True):
    """
    Function to verify if more than one spacing between slices value exists in a patient folder (scan).
    
    Args:
        data_dir:               directory path to loop through. Should be the directory which contains the human folders.
        pat_range(optional):    list of ID range to loop through (e.g: [22,369]). If not given will iterate through all folders in data_dir.
        full_info(optional):    bollean that indicates wether the user wants that the full information be printed out. If set to True, the
                                function will print out if there was any error opening a dicom metadata or extracting the desired field, in this case 'SpacingBetweenSlices'.
                                If set to False, it will neglect the existance of these errors.  (default: True)
    
    Prints:
        - If more than one spacing between slices value exists in a patient folder.
        - The distribution (number of occurences) of the spacing between slices values found in the case that more than one exists in a patient folder. 

    Raises:
        - Error opening a dicom metadata or extracting 'SpacingBetweenSlices'.
    """

    if full_info not in [True,False]:
        sys.exit('Full info arg must be True/False.')
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
                        spacing_btw_slices = {}
                        for img in sorted(os.listdir(os.path.join(data_dir,human,pdir,ser))):
                            path = os.path.join(data_dir,human,pdir,ser,img)                               
                            try:
                                ds = dcmread(path, force=True)
                                elem1 = ds['SpacingBetweenSlices'].value
                                if elem1 not in spacing_btw_slices:
                                    spacing_btw_slices[elem1] = [img]
                                else:
                                    spacing_btw_slices[elem1].append(img)
                            except:
                                if full_info:
                                    print('Error getting spacing between slices in', img)
                                else:
                                    pass         
                        if len(spacing_btw_slices)>1:
                            print('More than one spacing between slices value detected!')
                            dist = {}
                            for value,img in spacing_btw_slices.items():
                                dist[value] = len(spacing_btw_slices[value])
                            print('Distribution of the extracted values:', dist)



def check_timestamp_variation(data_dir, pat_range=None, full_info=True):
    """
    Function to verify if more than 14 detected timestamps exists in a patient folder (scan).
    
    Args:
        data_dir:               directory path to loop through. Should be the directory which contains the human folders.
        pat_range(optional):    list of ID range to loop through (e.g: [22,369]). If not given will iterate through all folders in data_dir.
        full_info(optional):    bollean that indicates wether the user wants that the full information be printed out. If set to True, the
                                function will print out if there was any error opening a dicom metadata or extracting the desired fields, in this case 'NominalPercentageOfCardiacPhase',
                                'ImageComments' and 'SeriesDescription'. If set to False, it will neglect the existance of these errors.  (default: True)
    
    Prints:
        - If more than 14 detected timestamps exists in a patient folder.
        - The distribution (number of occurences) of the spacing between slices values found in the case that more than one exists in a patient folder. 

    Raises:
        - Error opening a dicom metadata or extracting 'NominalPercentageOfCardiacPhase','ImageComments' or 'SeriesDescription'.
    """   
    if full_info not in [True,False]:
        sys.exit('Full info arg must be True/False.')
    
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
                            try:
                                ds = dcmread(path, force=True)
                                try:
                                    elem = ds['NominalPercentageOfCardiacPhase'].value
                                    if str(elem) not in nominal_phase:
                                        nominal_phase.append(str(elem))
                                except:
                                    if full_info:
                                        print('Error getting nominal percentage of cardiac phase in:', img)
                                    else:
                                        pass
                                try:
                                    elem2 = ds['ImageComments'].value
                                    if elem2 not in image_comments:
                                        image_comments.append(elem2)
                                except:
                                    if full_info:
                                        print('Error getting image comments in:', img)
                                    else:
                                        pass 
                                try:
                                    elem3 = ds['SeriesDescription'].value
                                    if elem3 not in series_desc:
                                        series_desc.append(elem3)
                                except:
                                    if full_info:
                                        print('Error getting series description in:', img)
                                    else:
                                        pass
                            except:
                                print('Error opening image:', img)
                        #------------------------------------------------------------------------#
                        ic_phase = scan_timestamps(image_comments)
                        if not ic_phase:
                            ic_phase = []
                        sd_phase = scan_timestamps(series_desc)
                        if not sd_phase:
                            sd_phase = []
                            
                        if len(set(nominal_phase))>14:
                            print('Timestamp variation anomaly detected!')
                            print('Nominal phase:', nominal_phase)
                        elif len(set(ic_phase))>14:
                            print('Timestamp variation anomaly detected!')
                            print('Image comments:', set(ic_phase))
                        elif len(set(sd_phase))>14:
                            print('Timestamp variation anomaly detected!')
                            print('Series description:', set(sd_phase)) 




def anomaly_log(data_dir, filename=None, full_log=True, pat_range=None):
    """
    Function to create a log file for the several possible anomalies that patient data might have. Designed to loop through every human folder in a directory
    printing out if an anomaly is found and its information. It checks: 'SeriesNumber', 'AcquisitionNumber', 'PixelSpacing', 'SpacingBetweenSlices', 'SliceThickness', 
    and the number of timestamps detected in 'NominalPercentageOfCardiacPhase','ImageComments' and 'SeriesDescription'. 
    
    Args:
        data_dir:               directory path to loop through. Should be the directory which contains the human folders.
        filename(optional):     log file name. (default: "anomaly_log.txt").
        full_log(optional):     bollean that indicates wether the user wants that the full information be printed out. If set to True, the
                                function will print out if there was any error opening a dicom metadata or extracting the analysed fields.
                                If set to False, it will neglect the existance of these errors.  (default: True)
        pat_range(optional):    list of ID range to loop through (e.g: [22,369]). If not given will iterate through all folders in data_dir.
    
    Prints:
        - If an anomaly is found and its information.

    Raises:
        - Error opening a dicom metadata or extracting the analysed fields.
    """  
    if filename == None:
        filename = "anomaly_log.txt"
        file = open(os.path.join("./",filename),"w")
    else:
        file = open(filename,"w")

    if full_log not in [True,False]:
        sys.exit('Full log arg must be True/False.')
    
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
            file.write('\n'+'-'*9+human+'-'*9+'\n')
            for pdir in sorted(os.listdir(os.path.join(data_dir,human))):
                if pdir.startswith('STD'):
                    for ser in sorted(os.listdir(os.path.join(data_dir,human,pdir))):
                        print('*** '+ser+' ***')
                        file.write('\n*** '+ser+' ***\n')
                        acquisition_number = []
                        series_number = []
                        slice_thickness = {}
                        pixel_spacing = {}
                        spacing_btw_slices = {}
                        nominal_phase = []
                        image_comments = []
                        series_desc = []
                        count_ext_error_aqc_number = 0
                        count_ext_error_series_number = 0
                        count_ext_error_slc_thc = 0
                        count_ext_error_px_spac = 0
                        count_ext_error_spc_btw_slc = 0
                        count_ext_error_nom_phase = 0
                        count_ext_error_img_commts = 0
                        count_ext_error_series_desc = 0
                        for img in sorted(os.listdir(os.path.join(data_dir,human,pdir,ser))):
                            path = os.path.join(data_dir,human,pdir,ser,img)
                            ds = dcmread(path, force=True)
                            #------------------------------------------------------#
                            try:
                                elem = ds['AcquisitionNumber'].value
                                if str(elem) not in acquisition_number:
                                    acquisition_number.append(str(elem))
                            except:
                                if full_log:
                                    count_ext_error_aqc_number += 1
                                    if count_ext_error_aqc_number < 6:
                                        file.write('Error getting acquisition number in: '+ img +'\n')
                                        print('Error getting acquisition number in:', img)
                                    if count_ext_error_aqc_number == 6:
                                        file.write('Error getting acquisition number in more than 5 dicoms. \n')
                                        print('Error getting acquisition number in more than 5 dicoms.')
                                    else:
                                        pass
                                else:
                                    pass
                            #------------------------------------------------------#
                            try:
                                elem = ds['SeriesNumber'].value
                                if str(elem) not in series_number:
                                    series_number.append(str(elem))
                            except:
                                if full_log:
                                    count_ext_error_series_number += 1
                                    if count_ext_error_series_number < 6:
                                        file.write('Error getting series number in: '+ img +'\n')
                                        print('Error getting series number in:', img)
                                    if count_ext_error_series_number == 6:
                                        file.write('Error getting series number in more than 5 dicoms. \n')
                                        print('Error getting series number in more than 5 dicoms.')
                                    else:
                                        pass
                                else:
                                    pass
                            #------------------------------------------------------#
                            try:
                                elem = ds['SliceThickness'].value
                                if elem not in slice_thickness:
                                    slice_thickness[elem] = [img]
                                else:
                                    slice_thickness[elem].append(img)
                            except:
                                if full_log:
                                    count_ext_error_slc_thc += 1
                                    if count_ext_error_slc_thc < 6:
                                        file.write('Error getting slice thickness in: '+ img +'\n')
                                        print('Error getting slice thickness in:', img)
                                    if count_ext_error_slc_thc == 6:
                                        file.write('Error getting slice thickness in more than 5 dicoms. \n')
                                        print('Error getting slice thickness in more than 5 dicoms.')
                                    else:
                                        pass
                                else:
                                    pass

                            #------------------------------------------------------#
                            try:
                                elem = ds['PixelSpacing'].value
                                pixel_spacing[img] = elem                                  
                            except:
                                if full_log:
                                    count_ext_error_px_spac += 1
                                    if count_ext_error_px_spac < 6:
                                        file.write('Error getting pixel spacing in: '+ img +'\n')
                                        print('Error getting pixel spacing in:', img)
                                    if count_ext_error_px_spac == 6:
                                        file.write('Error getting pixel spacing in more than 5 dicoms. \n')
                                        print('Error getting pixel spacing in more than 5 dicoms.')
                                    else:
                                        pass
                                else:
                                    pass
                            #------------------------------------------------------#
                            try:
                                elem = ds['SpacingBetweenSlices'].value
                                if elem not in spacing_btw_slices:
                                    spacing_btw_slices[elem] = [img]
                                else:
                                    spacing_btw_slices[elem].append(img)
                            except:
                                if full_log:
                                    count_ext_error_spc_btw_slc += 1
                                    if count_ext_error_spc_btw_slc < 6:
                                        file.write('Error getting spacing between slices in: '+ img +'\n')
                                        print('Error getting spacing between slices in:', img)
                                    if count_ext_error_spc_btw_slc == 6:
                                        file.write('Error getting spacing between slices in more than 5 dicoms. \n')
                                        print('Error getting spacing between slices in more than 5 dicoms.')
                                    else:
                                        pass
                                else:
                                    pass
                            #------------------------------------------------------#
                            try:
                                elem = ds['NominalPercentageOfCardiacPhase'].value
                                if str(elem) not in nominal_phase:
                                    nominal_phase.append(str(elem))
                            except:
                                if full_log:
                                    count_ext_error_nom_phase += 1
                                    if count_ext_error_nom_phase < 6:
                                        file.write('Error getting nominal percentage of cardiac phase in: '+ img +'\n')
                                        print('Error getting nominal percentage of cardiac phase in:', img)
                                    if count_ext_error_nom_phase == 6:
                                        file.write('Error getting nominal percentage of cardiac phase in more than 5 dicoms. \n')
                                        print('Error getting nominal percentage of cardiac phase in more than 5 dicoms.')
                                    else:
                                        pass
                                else:
                                    pass
                            try:
                                elem = ds['ImageComments'].value
                                if elem not in image_comments:
                                    image_comments.append(elem)
                            except:
                                if full_log:
                                    count_ext_error_img_commts += 1
                                    if count_ext_error_img_commts < 6:
                                        file.write('Error getting image comments in: '+ img +'\n')
                                        print('Error getting image comments in:', img)
                                    if count_ext_error_img_commts == 6:
                                        file.write('Error getting image comments in more than 5 dicoms. \n')
                                        print('Error getting image comments in more than 5 dicoms.')
                                    else:
                                        pass
                                else:
                                    pass
                            try:
                                elem = ds['SeriesDescription'].value
                                if elem not in series_desc:
                                    series_desc.append(elem)
                            except:
                                if full_log:
                                    count_ext_error_series_desc += 1
                                    if count_ext_error_series_desc < 6:
                                        file.write('Error getting series description in: '+ img +'\n')
                                        print('Error getting series description in:', img)
                                    if count_ext_error_series_desc == 6:
                                        file.write('Error getting series description in more than 5 dicoms. \n')
                                        print('Error getting series description in more than 5 dicoms.')
                                    else:
                                        pass
                                else:
                                    pass
                            #------------------------------------------------------#
            
                        #aquisition number check
                        if len(acquisition_number) > 1:
                            print('*Anomaly detected!*\nAquisition numbers: ', acquisition_number,'\n---')
                            file.write('\n*Anomaly detected!*\nAquisition numbers: '+str(acquisition_number)+'\n---\n')
                        #series number check
                        if len(series_number) > 1:
                            print('*Anomaly detected!*\nSeries numbers: ', series_number,'\n---')
                            file.write('\n*Anomaly detected!*\nSeries numbers: '+str(series_number)+'\n---\n')
                        #slice thickness check
                        if len(slice_thickness)>1:
                            dist = {}
                            for value,img in slice_thickness.items():
                                dist[value] = len(slice_thickness[value])
                            print('*Anomaly detected!*\nDistribution of the extracted slice thickness values:', dist,'\n---')
                            file.write('\n*Anomaly detected!*\nDistribution of the extracted slice thickness values: '+str(dist)+'\n---\n')
                        #pixel spacing check
                        px_values = {}
                        for img,value in pixel_spacing.items():
                            if tuple(value) not in px_values:
                                px_values[tuple(value)] = [img]
                            elif tuple(value) in px_values:
                                px_values[tuple(value)].append(img)
                        if len(px_values) > 1:
                            freq = {}
                            for value,img in px_values.items():
                                freq[value] = len(img)
                            print('*Anomaly detected!*\nDistribution of the extracted pixel spacing pairs:', freq,'\n---')
                            file.write('\n*Anomaly detected!*\nDistribution of the extracted pixel spacing pairs: '+str(freq)+'\n---\n')
                        #spacing between slices check
                        if len(spacing_btw_slices)>1:
                            dist = {}
                            for value,img in spacing_btw_slices.items():
                                dist[value] = len(spacing_btw_slices[value])
                            print('*Anomaly detected!*\nDistribution of the extracted spacing between slices values:', dist,'\n---')
                            file.write('\n*Anomaly detected!*\nDistribution of the extracted spacing between slices values:'+ str(dist)+'\n---\n')
                        #timestamp variation check
                        ic_phase = scan_timestamps(image_comments)
                        if not ic_phase:
                            ic_phase = []
                        sd_phase = scan_timestamps(series_desc)
                        if not sd_phase:
                            sd_phase = []
                        if len(nominal_phase)>14:
                            print('*Anomaly detected!*')
                            print('Nominal phase:', nominal_phase)
                            file.write('\n*Anomaly detected!*\nNominal Phase: ' + str(nominal_phase) +'\n---\n')
                        elif len(set(ic_phase))>14:
                            print('*Anomaly detected!*')
                            print('Image comments:', set(ic_phase))
                            file.write('\n*Anomaly detected!*\nImage Comments: ' + str(set(ic_phase))+ '\n---\n')
                        elif len(set(sd_phase))>14:
                            print('*Anomaly detected!*')
                            print('Series description:', set(sd_phase))
                            file.write('\n*Anomaly detected!*\nSeries description: '+ str(set(sd_phase))+'\n---\n')

                        
    file.close()
    print('Log file saved as \'{}\'.'.format(filename))

#             _____
#           .'  |  `.
#          /    |    \
#         |-----|-----|
#          \    |    /
#           '.__|__.'
#              \|/
#               |