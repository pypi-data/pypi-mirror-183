import os
import glob
import random
from pydicom import dcmread
import datetime
from parse import search
from pathlib import Path
from utils import timestamp_helpers, patient_defaultdict, helpers, csv_databulk_loaders, theart_models_gen

managed0 = [str(i) for i in range(0,642)]+['775','776']
theart = [str(i) for i in range(642,708)]
canada_china = [str(i) for i in range(708,720)]
toulouse = [str(i) for i in range(720,747)]
challengedata = [str(i) for i in range(747,767)]
realheart = [str(i) for i in range(767,772)]


def serialize(path_to_series):
	""" Function to collect NominalPercentageOfCardiacPhase,
	ImageComments, SeriesDescription for further decision 
	if CINE or Normal. This function will first make sure that there
	are more then 20 .dcms.

	Parameters
	----------
	path: string
		path to series/patient
	"""

	nominal_phase = []
	image_comments = []
	series_desc = []
	#only consider patients folder with more than 20 dicoms, although this condition should already be handled in VirtoLoader
	if len(glob.glob1(path_to_series, '*.dcm')) > 20:
		for image in sorted(os.listdir(path_to_series)):
			metadata = dcmread(os.path.join(path_to_series, image), force=True)
			try:
				elem = metadata['NominalPercentageOfCardiacPhase'].value
				if str(elem) not in nominal_phase:
					nominal_phase.append(str(elem))
			except KeyError:
				pass
			try:
				elem2 = metadata['ImageComments'].value
				if elem2 not in image_comments:
					image_comments.append(elem2)
			except KeyError:
				pass
			try:
				elem3 = metadata['SeriesDescription'].value
				if elem3 not in series_desc:
					series_desc.append(elem3)
			except KeyError:
				pass

	return [nominal_phase, image_comments, series_desc]


def cine_normal_classification(nominal_phase, image_comments, series_desc):
	""" Function to decide whether a series is CINE or NORMAL

	Parameters
	----------
	nominal_phase: list
		see serialize()
	image_comments: list
		see serialize()
	series_desc: list
		see serialize()
	""" 

	series_type = None
	# phase_n is nominal phase from the original code
	phase_n = 0
	phase_c = 0
	phase_s = 0

	if len(nominal_phase) > 1:
		for i,p in enumerate(nominal_phase):
			if nominal_phase[i] == '':
				del nominal_phase[i]
		#condition to neglect anomalies in phase variation. Theoretically, no more than 14 (detected) timestamps should exist. 
		if len(nominal_phase) > 1 and len(nominal_phase) < 15:
			series_type = "CINE"
			phase_n = set(nominal_phase)
		else:
			#condition to neglect anomalies in phase variation. If more than 14 timestamps are detected, the patient will be classified as normal ct and the cardiac phase info ignored.
			if len(nominal_phase) >= 15:
				nominal_phase = []
			series_type = "NORMAL"
			phase_n = nominal_phase

	elif nominal_phase != [] and len(nominal_phase) <= 1:
		series_type = "NORMAL"
		phase_n = nominal_phase

	elif image_comments != []:
		phase = timestamp_helpers.scan_timestamps(image_comments)
		if not phase:
			phase = ['']
		if len(set(phase))>1:
			#condition to neglect anomalies in phase variation. If more than 14 timestamps are detected, the patient will be classified as normal ct and the cardiac phase info ignored.
			if len(set(phase)) >= 15:
				phase = []
				series_type = "NORMAL"
				phase_n = phase
			else:
				series_type = "CINE"
				phase_c = set(phase)
		else:
			if phase == ['']:
				phase = timestamp_helpers.scan_timestamps(series_desc)
				if not phase:
					phase = ['']
				if len(set(phase))>1:
					#condition to neglect anomalies in phase variation. If more than 14 timestamps are detected, the patient will be classified as normal ct and the cardiac phase info ignored.
					if len(set(phase)) >= 15:
						phase = []
						series_type = "NORMAL"
						phase_n = set(phase)
					else:
						series_type = "CINE"
						phase_s = set(phase)
				else:
					series_type = "NORMAL"
					phase_n = set(phase)
			else:
				series_type = "NORMAL"
				phase_n = set(phase)     
	else:
		phase = timestamp_helpers.scan_timestamps(series_desc)
		if not phase:
			phase = ['']
		if len(set(phase))>1:
			#condition to neglect anomalies in phase variation. If more than 14 timestamps are detected, the patient will be classified as normal ct and the cardiac phase info ignored.
			if len(set(phase)) >= 15:
				phase = []
				series_type = "NORMAL"
				phase_n = set(phase)
			else:
				series_type = "CINE"
				phase_s = set(phase)
		else:
			series_type = "NORMAL"
			phase_n = set(phase)

	return series_type, phase_n, phase_c, phase_s 


def normal_init(path, phase=0):
	""" Initialize the normal patient_dict

	Parameters
	----------
	path: string
		path to series
	phase:
		phase_n from cine_normal_classification

	"""
	now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	n_slices = len(os.listdir(path))
	patientdict = patient_defaultdict.patient_dict(now, n_slices)

	 #allocate the timestamp (if exist) in patientdict, removing '%' and converting to [0,1]
	if phase not in (0, {''}):
		for i in phase:
			if '%' in i:
				i = i.replace("%","")
				phase = float(i)/100
			else:
				i = i.replace("[","")
				i = i.replace("]","")
				phase = float(i)/100
		patientdict['imaging']['image_files_list'][0]['timestamp'] = phase
	for image in sorted(os.listdir(path)):
		if image.endswith("dcm"):
			#adding the images filenames to the timestamp
			patientdict['imaging']['image_files_list'][0]['image_files'].append(image)
	return patientdict

def cine_init(path, human, nominal_phase, phase_c, phase_s):
	""" Initialize CINE patient_dict

	Parameters
	----------
	path: string
		path to series
	human: string
		internal human id
	nominal_phase: 
		phase_n from cine_normal_classification
	phase_c:
		phase_c from cine_normal_classification
	phase_s:
		phase_s from cine_normal_classification	
	"""

	now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	n_slices = len(os.listdir(path))
	patientdict = patient_defaultdict.patient_dict(now, n_slices)

	# since the size of the image_files_list depends on the number of timestamps, the lenght of this element is settled according to each patient
	# this procedure is only applied to one of the following three branches depending on where the cardiac phase info is.
	# thus, the timestamps are first allocated in the patientdict, and when the final loop through the patient dicoms starts (to info extraction and consequently storing in patientdict), 
	# the images are appended to the corresponding cardiac phase element		
	#----------------------------------------------------------------#
	if nominal_phase != 0:
		nominal_phase = sorted(list(nominal_phase),key=float)
		if human in theart:
			timestamp_helpers.preallocate_timestamp_info(patientdict, nominal_phase, nominal=True, theart=True)
		else:
			timestamp_helpers.preallocate_timestamp_info(patientdict, nominal_phase, nominal=True)
	#----------------------------------------------------------------#
	if phase_c != 0:
		phase_c = list(phase_c)
		timestamp_helpers.preallocate_timestamp_info(patientdict,phase_c)
	#----------------------------------------------------------------#
	if phase_s != 0:
		phase_s = list(phase_s)
		timestamp_helpers.preallocate_timestamp_info(patientdict,phase_s)

	for image in os.listdir(path):
			if image.endswith("dcm"):
				metadata = dcmread(os.path.join(path,image),force=True)
				#add the images filename to the respective cardiac phase element
				#----------------------------------------------------------------#
				if nominal_phase != 0:
					for i,j in enumerate(patientdict['imaging']['image_files_list']):
						if human in theart:
							if round(nominal_phase.index(str((metadata['NominalPercentageOfCardiacPhase'].value)))/len(nominal_phase),2) == patientdict['imaging']['image_files_list'][i]['timestamp']:
								patientdict['imaging']['image_files_list'][i]['image_files'].append(image)
								patientdict['imaging']['image_files_list'][i]['image_files'].sort()
						else:
							if float(metadata['NominalPercentageOfCardiacPhase'].value)/100 == patientdict['imaging']['image_files_list'][i]['timestamp']:
								patientdict['imaging']['image_files_list'][i]['image_files'].append(image)
								patientdict['imaging']['image_files_list'][i]['image_files'].sort()
				#----------------------------------------------------------------#
				if phase_c != 0:
					field = str(metadata['ImageComments'].value)
					timestamp = timestamp_helpers.detect_convert_timestamp(field)
					for i,j in enumerate(patientdict['imaging']['image_files_list']):
						if timestamp == patientdict['imaging']['image_files_list'][i]['timestamp']:
							patientdict['imaging']['image_files_list'][i]['image_files'].append(image)
							patientdict['imaging']['image_files_list'][i]['image_files'].sort()
				#----------------------------------------------------------------#
				if phase_s != 0:
					field = str(metadata['SeriesDescription'].value)
					timestamp = timestamp_helpers.detect_convert_timestamp(field)
					for i,j in enumerate(patientdict['imaging']['image_files_list']):
						if timestamp == patientdict['imaging']['image_files_list'][i]['timestamp']:
							patientdict['imaging']['image_files_list'][i]['image_files'].append(image)
							patientdict['imaging']['image_files_list'][i]['image_files'].sort()
							
	return patientdict 


def elements_extraction_and_storing(metadata, patientdict):
	"""First run that goes through the metadata and
	 fills the fields in the Patient Dict. Will be called for each
	 slices in the scan.

	Parameters
	----------
	metadata: dict
		dicom metadata
	patientdict: dict
		patientdict
	"""

	try:
		age_elem = str(metadata['PatientAge'].value)
		if len(age_elem) > len(patientdict['age']):
			patientdict['age'] = age_elem
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		weight_elem = str(metadata['PatientWeight'].value)
		if len(weight_elem) > len(patientdict['weight']):
			patientdict['weight'] = weight_elem
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		add_datahist_elem = str(metadata['AdditionalPatientHistory'].value)
		if len(add_datahist_elem) > len(patientdict['additional_hist']):
			patientdict['additional_hist'] = add_datahist_elem
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		gender_elem = str(metadata['PatientSex'].value)
		if len(gender_elem) > len(patientdict['gender']):
			patientdict['gender'] = gender_elem
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		acquisitiondate_elem = str(metadata['AcquisitionDate'].value)
		if len(acquisitiondate_elem) > len(patientdict['imaging']['acquisition_date']):
			patientdict['imaging']['acquisition_date'] = acquisitiondate_elem
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		bolus_agent_elem = str(metadata['ContrastBolusAgent'].value)
		if len(str(bolus_agent_elem)) > len(patientdict['imaging']['bolus_agent']):
			patientdict['imaging']['bolus_agent'] = bolus_agent_elem
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		slicethicknss_elem = str(metadata['SliceThickness'].value)
		if len(slicethicknss_elem) > len(patientdict['imaging']['slice_thickness']):
			patientdict['imaging']['slice_thickness'] = slicethicknss_elem
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		spacingbtwnslices_elem = str(
			metadata['SpacingBetweenSlices'].value)
		if len(spacingbtwnslices_elem) > len(patientdict['imaging']['spacing_btwn_slices']):
			patientdict['imaging']['spacing_btwn_slices'] = spacingbtwnslices_elem
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		imageorientation_elem = str(
			metadata['ImageOrientationPatient'].value)
		if len(imageorientation_elem) > len(patientdict['imaging']['image_orientation']):
			patientdict['imaging']['image_orientation'] = imageorientation_elem
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		imgposition_pat = str(metadata['ImagePositionPatient'].value)
		if len(imgposition_pat) > len(patientdict['imaging']['image_position_patient']):
			patientdict['imaging']['image_position_patient'] = imgposition_pat
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		body_part_examined_elem = str(metadata['BodyPartExamined'].value)
		if len(body_part_examined_elem) > len(patientdict['imaging']['body_part_examined']):
			patientdict['imaging']['body_part_examined'] = body_part_examined_elem
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		rows_elem = str(metadata['Rows'].value)
		if len(rows_elem) > len(patientdict['imaging']['rows']):
			patientdict['imaging']['rows'] = rows_elem
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		columns_elem = str(metadata['Columns'].value)
		if len(columns_elem) > len(patientdict['imaging']['columns']):
			patientdict['imaging']['columns'] = columns_elem
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		pixel_spacing_elem = str(metadata['PixelSpacing'].value)
		if len(pixel_spacing_elem) > len(patientdict['imaging']['pixel_spacing']):
			patientdict['imaging']['pixel_spacing'] = pixel_spacing_elem
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		institution_id_elem = str(metadata['PatientName'].value)
		if len(institution_id_elem) > len(patientdict['institution_id']):
			patientdict['institution_id'] = institution_id_elem
	except KeyError:
		pass
	if patientdict['institution_id'] == '':
		try:
			institution_id_elem = str(metadata['PatientID'].value)
			if len(institution_id_elem) > len(patientdict['institution_id']):
				patientdict['institution_id'] = institution_id_elem
		except KeyError:
			pass
	#---------------------------------------------------------------------#
	try:
		institution_name_elem = str(metadata['InstitutionName'].value)
		if len(institution_name_elem) > len(patientdict['institution_name']):
			patientdict['institution_name'] = institution_name_elem
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		manufacturer_elem = str(metadata['Manufacturer'].value)
		if len(manufacturer_elem) > len(patientdict['imaging']['manufacturer']):
			patientdict['imaging']['manufacturer'] = manufacturer_elem
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		manuf_model_elem = str(metadata['ManufacturerModelName'].value)
		if len(manuf_model_elem) > len(patientdict['imaging']['manuf_model']):
			patientdict['imaging']['manuf_model'] = manufacturer_elem
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		modality_elem = str(metadata['Modality'].value)
		if len(modality_elem) > len(patientdict['imaging']['modality']):
			patientdict['imaging']['modality'] = modality_elem
	except KeyError:
		pass
	#---------------------------------------------------------------------#
	try:
		add_info_elem = str(metadata['ImageComments'].value)
		if len(add_info_elem) > len(patientdict['imaging']['additional_info']):
			patientdict['imaging']['additional_info'] = add_info_elem
	except KeyError:
		pass

	return patientdict

def elements_correction(patientdict, path, human, nominal_phase=None):
	"""Corrects fields in patient dict and fills in information
	from csv files, if available for databulk.

	Parameters
	----------
	patientdict: dict
	path: string
	human: string
	nominal_phase:
		phase_n from cine_normal_classification
	"""

	gender_exclude = ['','Anonymous','0','O']
	weight_exclude = ['','Anonymous','None','0','0.0']
	slice_thck_exclude = ['','None']		
	#---------------------------------------------------------------------#
	if patientdict['age'].strip() == '':
		patientdict['age'] = None

	if patientdict['age'] is not None:
		patientdict['age'] = int(patientdict['age'].replace('Y',''))
	#---------------------------------------------------------------------#

	if patientdict['height'] is None:
		#to extract height info from "additional_info" field
		height = search('{:d}cm', patientdict['imaging']['additional_info'])
		try:
			patientdict['height'] = float(height[0])
		except TypeError:
			patientdict['height'] = None
	#---------------------------------------------------------------------#        
	if patientdict['weight'].strip() in weight_exclude:
		patientdict['weight'] = None
		
	if patientdict['weight'] is None:
		#to extract weight info from "additional_info" field
		weight = search('{:d}kg', patientdict['imaging']['additional_info'])
		try:
			patientdict['weight'] = float(weight[0])
		except TypeError:
			patientdict['weight'] = None
	#---------------------------------------------------------------------#
	if patientdict['gender'].strip() == 'W':
		patientdict['gender'] = 'female'
	if patientdict['gender'].strip() == 'M':
		patientdict['gender'] = 'male'
	if patientdict['gender'].strip() == 'F':
		patientdict['gender'] = 'female'
		
	if patientdict['gender'].strip() in gender_exclude:
		patientdict['gender'] = None
	#---------------------------------------------------------------------#
	if patientdict['imaging']['rows'] != '':
		try:
			patientdict['imaging']['rows'] = int(patientdict['imaging']['rows'])
		except KeyError:
			pass   
	if patientdict['imaging']['columns'] != '':
		try:
			patientdict['imaging']['columns'] = int(patientdict['imaging']['columns'])
		except KeyError:
			pass
	#---------------------------------------------------------------------#
	if patientdict['imaging']['slice_thickness'] in slice_thck_exclude:
		patientdict['imaging']['slice_thickness'] = None
	if patientdict['imaging']['slice_thickness'] != None:
		try:
			patientdict['imaging']['slice_thickness'] = float(patientdict['imaging']['slice_thickness'])
		except KeyError:
			pass
	#---------------------------------------------------------------------#
	if patientdict['imaging']['spacing_btwn_slices'] != '':
		try:
			patientdict['imaging']['spacing_btwn_slices'] = float(patientdict['imaging']['spacing_btwn_slices'])
		except KeyError:
			pass
	#---------------------------------------------------------------------#
	if patientdict['imaging']['image_files_list'][0]['timestamp'] == '':
		patientdict['imaging']['image_files_list'][0]['timestamp'] = None
	#---------------------------------------------------------------------#
	if patientdict['imaging']['pixel_spacing'] == '':
		patientdict['imaging']['pixel_spacing'] = None

	if patientdict['imaging']['pixel_spacing'] is not None:
		patientdict['imaging']['pixel_spacing'] = eval(patientdict['imaging']['pixel_spacing'])
	#---------------------------------------------------------------------#
	if patientdict['imaging']['image_orientation'] == '':
		patientdict['imaging']['image_orientation'] = None
			
	if patientdict['imaging']['image_orientation'] is not None:
		patientdict['imaging']['image_orientation'] = eval(patientdict['imaging']['image_orientation'])
	#---------------------------------------------------------------------#
	if patientdict['imaging']['image_position_patient'] == '':
		patientdict['imaging']['image_position_patient'] = None

	if patientdict['imaging']['image_position_patient'] is not None:
		patientdict['imaging']['image_position_patient'] = eval(patientdict['imaging']['image_position_patient'])
	#---------------------------------------------------------------------#
	if patientdict['imaging']['n_timestamps'] == '':
		patientdict['imaging']['n_timestamps'] = 1
	#---------------------------------------------------------------------#
	if patientdict['imaging']['bolus_agent'] == '':
		patientdict['imaging']['bolus_agent'] = None
	#---------------------------------------------------------------------#
	if patientdict['imaging']['body_part_examined'] == '':
		patientdict['imaging']['body_part_examined'] = None
	else:
		#body_rois standardization
		heart_and_thorax = ['HEART','CHEST','KORPERSTAMM', 'chest','AORTA','CT Aorta ganz KM','Aorta','CT ANGIO','TORAX','ANGIO','CT ANGIO TOTALE AORTA + IV CONTR','CORONARIO','SAPIEN','TX']
		abdominal = ['ABDOMEN']
		head_to_pelvis = ['J BRZUSZNA','TX AB PE','CORE VALVE','SPECIAL','aorta tho/abd','CTA Thorax/Ab...']
		head = ['HEAD']
			
		if patientdict['imaging']['body_part_examined'].strip() in heart_and_thorax:
			patientdict['body_rois'][0]['catalog_tag'] = 'heart_and_thorax'
		elif patientdict['imaging']['body_part_examined'].strip() in abdominal:
			patientdict['body_rois'][0]['catalog_tag'] = 'abdominal'
		elif patientdict['imaging']['body_part_examined'].strip() in head:
			patientdict['body_rois'][0]['catalog_tag'] = 'head_and_neck'
		elif patientdict['imaging']['body_part_examined'].strip() in head_to_pelvis:
			patientdict['body_rois'][0]['catalog_tag'] = 'head_to_pelvis'
	#---------------------------------------------------------------------#
	#replace the spacing between slices by the difference between consecutive slices locations whenever
	#spacing between slice element is not filled
	if patientdict['imaging']['spacing_btwn_slices'] == '':
		images = sorted(os.listdir(path))
		consecutive_images_pairs = list(zip(images, images[1:]))
		random_pair = random.choice(consecutive_images_pairs)
		slice_loc1 = 0
		slice_loc2 = 0
		ds1 = dcmread(os.path.join(path,random_pair[0]),force=True)
		try:
			slice_loc1 = float(ds1['SliceLocation'].value)
		except KeyError:
			pass

		ds2 = dcmread(os.path.join(path,random_pair[1]),force=True)
		try:
			slice_loc2 = float(ds2['SliceLocation'].value)
		except KeyError:
			pass
			
		spacingbtwnslices_elem = round(abs(slice_loc1-slice_loc2),1)
		patientdict['imaging']['spacing_btwn_slices'] = spacingbtwnslices_elem

	if human in theart:
		patientdict = csv_databulk_loaders.theart_csv_parse(human,nominal_phase,patientdict)
		
	if human in toulouse:
		patientdict = csv_databulk_loaders.toulouse_csv_parse(human,patientdict,path)

	if human in canada_china:
		patientdict = csv_databulk_loaders.canada_china_csv_parse(human,patientdict,path)

	if human in realheart:
		patientdict = csv_databulk_loaders.realheart_csv_parse(human,patientdict)
	#---------------------------------------------------------------------#
	#bsa bmi calculation
	patientdict['bsa'] = helpers.calculate_mosteller_bsa(patientdict)
	patientdict['bmi'] = helpers.calculate_bmi(patientdict)
	#---------------------------------------------------------------------#
	# additional info insertion
	if human in managed0:
		patientdict['pathology'] = 'aortic_stenosis'
		#insertion of human origin location info according to masterlist
		if int(human) in list(range(0,7))+list(range(49,618)):
			patientdict['origin_location'] = 'europe'
		elif int(human) in list(range(7,49))+[618,775,776]:
			patientdict['origin_location'] = 'north_south_america'

	if human in theart:
		patientdict['pathology'] = 'tricuspid_valve_insufficiency'
		patientdict['origin_location'] = 'north_south_america'

	if human in toulouse:
		patientdict['pathology'] = 'tricuspid_valve_insufficiency'
		patientdict['origin_location'] = 'europe'
		
	if human in canada_china or human == '772':
		patientdict['pathology'] = 'aortic_stenosis'
		if human == '719':
			patientdict['origin_location'] = 'asia_pacific'
			patientdict['origin_ethnicity'] = 'asian'
		else:
			patientdict['origin_location'] = 'north_south_america'
	#---------------------------------------------------------------------#
	patientdict['internal_info']['human_id'] = int(human)
	patientdict['internal_info']['series'] = Path(path).stem
	#---------------------------------------------------------------------#
		
	return patientdict


def model_init(human):
	""" Initialize model dict
	"""
	now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	if human in theart:
		modeldict = theart_models_gen.initialize_theart_model_jsongen(human, now)
	else:
		modeldict = theart_models_gen.default_modeldict(now)

	return modeldict


def collections_creation(patientdict):
	"""Database collections definition and
	 conversion from patient dictionaries to jsons

	Parameters
	----------
	patientdict: dict
		patient dictionary as before
	"""

	patient_collection_dict = {}
	imaging_collection_dict = {}
	patient_reidentification_collection_dict = {}
	patient_reidentification_collection_dict['patient_id'] = None
	reidentification = ['institution_id', 'institution_name']

	for i,j in patientdict['imaging'].items():
		imaging_collection_dict[i] = j

	for i,j in patientdict.items():
		if i != 'imaging' and i not in reidentification:
			patient_collection_dict[i] = j

	for i,j in patientdict.items():
		if i in reidentification:
			patient_reidentification_collection_dict[i] = j

		
	return imaging_collection_dict, patient_collection_dict, patient_reidentification_collection_dict

	



