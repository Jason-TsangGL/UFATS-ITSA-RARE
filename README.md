# UFATS-ITSA-RARE
U-Net Fully Automated Thigh Segmentation Model with a Semi Automated Iterative Threshold Algorithm for fat segmentation
# Automated Segmentation of Individual Muscle Groups in Thigh MRI Images

Jason Tsang, jgltsang@gmail.com<br />
Matei Gardea, matei.gardea@gmail.com<br />
Noah Fang, nfang3@uwo.ca<br />
Andy K.O Wong, andy.wong@uhnresearch.ca **<br />

Toronto General Hospital Research Institute <br />
Joint Department of Medical Imaging <br />
200 Elizabeth St, 7EN-238A, Toronto, ON M5G 2C4 andy.wong@uhnresearch.ca <br />
416-340-4800 ext. 6276 <br />

## Background

Muscle properties of the leg have been associated with knee osteoarthritis development, progression, function, and pain. However, manual segmentation of individual muscle groups within magnetic resonance images (MRI) is inefficient and prone to human error. In this study, we propose a fully-convolutional neural network (FCN) model trained to segment individual muscle groups from thigh MR images, the properties of which will be related to future osteoarthritis outcomes.

## Methods

We used 2,010 MR images from the 36-month visit of the Osteoarthritis Initiative to train and test the FCN. MR scans consisted of 15 axial contiguous T1-weighted images of the quadriceps region centered at 100mm above the medial femoral epiphysis. The FCN used the UNET architecture with hyperparameters optimized by k-fold validation. The two-loss functions used to evaluate model performance were Intersection-Over-Union (IOU) and 1-DICE with benchmarks of 0.50 and 0.20, respectively. To measure intermuscular fat and intramuscular fat within each muscle group, this model was also combined with our Iterative Threshold-Seeking Algorithm (ITSA).

## Results

The top three performing muscle segmentation models were the VG, BF, SM muscles. The IOU scores of the VG, BF, and SM respectively were 0.867, 0.866, and 0.819. The corresponding 1-DICE coefficients were 0.072, 0.071, and 0.10. The overall mean IOU score across all muscle groups was 0.754 and the mean 1-DICE coefficient was 0.125.

## Conclusion

This methodological study demonstrated the capability of artificial intelligence to classify individual muscle groups of thigh MRIs with high accuracy compared to ground truth (manual) segmentations, capturing shape complexities existing among individuals. With further refinement of our FCN and the utilization of ITSA, this method introduces a reliable state-of-the-art method to quantitatively track the progression of muscle volumes and distribution of intramuscular fat, permissive of longitudinal associations with future osteoarthritis outcomes.

## Take Home Message

Our automated segmentation method introduces a reliable state-of-the-art method to quantitatively track the progression of muscle volumes and distribution of intramuscular fat, permissive of longitudinal associations with future osteoarthritis outcomes.

## Funding Acknowledgment

This study was supported by the Canadian Institutes of Health Research, grant no’s: PJT156274, PJT166012.

## Declaration of Interest

There are no declared external interests nor conflicts of interest.

![Screenshot 2023-05-07 at 6 01 25 PM](https://user-images.githubusercontent.com/110850048/236704595-71456e12-bdfd-4a12-9862-4312b53837e5.png)

Figure 1. Flowchart of our proposed U-NET CNN architecture. The complete model contains a dedicated CNN for each region of interests (8 CNNs total).

![Screenshot 2023-05-07 at 6 01 55 PM](https://user-images.githubusercontent.com/110850048/236704609-4f3a1e35-7386-4cce-bb4e-1d2b18fa5a93.png)

Figure 2. Graphical visualization of the evaluation metrics of the best performing model of each region of interest. Dotted vertical line on each graph represents the pre-determined benchmark.

![Screenshot 2023-05-07 at 6 02 43 PM](https://user-images.githubusercontent.com/110850048/236704636-aca600e3-d3af-419c-9512-8437ac0c2c99.png)

Figure 3. Visual comparison of the original MR image, ground truth segmentations, and CNN generated segmentations compiled. Bottom row shows visual examples of individual muscle group segmentations from the CNN

[CARC Poster.pdf](https://github.com/Jason-TsangGL/UFATS-ITSA-RARE/files/11416092/CARC.Poster.pdf)


