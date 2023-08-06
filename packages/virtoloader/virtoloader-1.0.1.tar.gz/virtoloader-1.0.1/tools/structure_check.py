import os
import random
from pydicom import dcmread
import glob


def structure_log(data_dir, filename=None):
    """
    Function to create a log file for raw data structure. Designed to loop through every human folder in a directory
    printing the information if wether each folder presents the desired structure, with desired naming.
    
    Args:
        data_dir:               directory path to loop through. Should be the main bulk root folder, i.e: the folder that contains all the human folders.
        filename(optional):     log file name. (default: "structure_log.txt").
    
    Prints:
        - Missing folders
        - Mislabelled folders
        - Missing dicom data
        - Folders with less than a predefined number of dicom files

    Raises:
        - Errors opening/reading dicom metadata
    """
    if filename == None:
        filename = "structure_log.txt"
        file = open(os.path.join("./",filename) ,"w")
    else:
        file = open(filename,"w")
    
    for human in sorted(os.listdir(data_dir)):
        if os.path.isdir(os.path.join(data_dir,human)):
            print('-'*9+human+'-'*9)
            file.write('\n'+'-'*9+human+'-'*9+'\n')
            if not any(folder.startswith('STD') for folder in os.listdir(os.path.join(data_dir,human))):
                print('STD00001 folder missing in human root dir. Folders: ', os.listdir(os.path.join(data_dir,human)))
                file.write('STD00001 folder missing in human root dir. Folders: '+str(os.listdir(os.path.join(data_dir,human))))
            for pdir in os.listdir(os.path.join(data_dir,human)):
                if os.path.isdir(os.path.join(data_dir,human,pdir)):
                    print('-'*3+pdir+'-'*3)
                    file.write('\n'+'-'*3+pdir+'-'*3+'\n')
                    if not any(folder.startswith('SER') for folder in os.listdir(os.path.join(data_dir,human,pdir))):
                        print('Series folders missing or mislabelled in parent dir.')
                        file.write('Series folders missing or mislabelled in parent dir.\n')
                    if (pdir.upper()).startswith('SER'):
                        print('-*Entering:',pdir)
                        file.write('-*Entering:'+pdir+'\n')
                        if not any(image.endswith('.dcm') for image in os.listdir(os.path.join(data_dir,human,pdir))):
                            print('Dicoms missing in series folder', pdir)
                            file.write('Dicoms missing in series folder '+pdir+'\n')
                        else:
                            if len(glob.glob(os.path.join(data_dir,human,pdir,'*.dcm'))) < 20:
                                print('Less than 20 dicoms in series folder',pdir)
                                file.write('Less than 20 dicoms in series folder '+pdir+'\n')
                            img = random.choice(os.listdir(os.path.join(data_dir,human,pdir)))
                            path = os.path.join(data_dir,human,pdir,img)
                            try:
                                ds = dcmread(path, force=True)
                                elem = str(ds['SeriesNumber'].value)
                                series = 'SER'+f"{int(elem):05}"
                                if series != pdir:
                                    print('Mislabelled folder detected: {ser}\n-->According to metadata: {series}\n'.format(ser=pdir,series=series))
                                    file.write('Mislabelled folder detected: {ser}\n-->According to metadata: {series}\n'.format(ser=pdir,series=series))
                            except:
                                print('Error in image', img)
                    else:
                        for ser in sorted(os.listdir(os.path.join(data_dir,human,pdir))):
                            if os.path.isdir(os.path.join(data_dir,human,pdir,ser)):
                                print('*'*3+ser+'*'*3)
                                file.write('\n*** '+ser+' ***\n')
                                if not any(image.endswith('.dcm') for image in os.listdir(os.path.join(data_dir,human,pdir,ser))):
                                    print('Dicoms missing in series folder', ser)
                                    file.write('Dicoms missing in series folder '+ser+'\n')
                                else:
                                    if len(glob.glob(os.path.join(data_dir,human,pdir,ser,'*.dcm'))) < 20:
                                        print('Less than 20 dicoms in series folder',ser)
                                        file.write('Less than 20 dicoms in series folder '+ser+'\n')
                                    img = random.choice(os.listdir(os.path.join(data_dir,human,pdir,ser)))
                                    path = os.path.join(data_dir,human,pdir,ser,img)
                                    try:
                                        ds = dcmread(path, force=True)
                                        elem = str(ds['SeriesNumber'].value)
                                        series = 'SER'+f"{int(elem):05}"
                                        if series != ser:
                                            print('Mislabelled folder detected: {ser}\n-->According to metadata: {series}\n'.format(ser=ser,series=series))
                                            file.write('Mislabelled folder detected: {ser}\n-->According to metadata: {series}\n'.format(ser=ser,series=series))
                                    except:
                                        print('Error in image', img)
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