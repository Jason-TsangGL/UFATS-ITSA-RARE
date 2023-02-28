train_dir = "./dataset/train"
test_dir = "./dataset/test"

def load_data(target_dir=train_dir, target_group=1):
    length = len(os.listdir(target_dir)) * 15
    dicoms = np.empty((length, 256, 256, 1))
    masks = np.empty((length, 256, 256, 1))
    
    for count, patient_id in enumerate(tqdm(os.listdir(target_dir))):
        dicom_array = sitk.GetArrayFromImage(sitk.ReadImage(sitk.ImageSeriesReader_GetGDCMSeriesFileNames(join(target_dir, patient_id))))
        nrrd_array = sitk.GetArrayFromImage(sitk.ReadImage(join(target_dir, patient_id, "NRRD", patient_id.replace("_RDY", "") + "-label.nrrd")))
        for slice_number in range(15):
            dicoms[count * 15 + slice_number] = dicom_array[slice_number, :, :256, np.newaxis]
            masks[count * 15 + slice_number] = np.expand_dims(np.where(nrrd_array[slice_number, :, :256] == target_group, 1, 0), axis=2)

    dicoms = MinMaxScaler(feature_range=(0, 1.0)).fit_transform(dicoms.reshape((length, 256*256))).reshape((length, 256, 256, 1))
    return dicoms, masks