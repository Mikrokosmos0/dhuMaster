# 一、部分中文表述

ACDC (Automatic Cardiac Diagnosis Challenge) 是 MICCAI 2017 的一个挑战赛，旨在对心脏动态磁共振成像 (cine-MRI) 中的舒张期 (ED) 和收缩期 (ES) 帧进行左心室 (LV) 、右心室 (RV) 和心肌 (Myo) 分割。精确分割心脏图像对于评估心脏功能，如射血分数（EF）、每次搏动的血量（SV）、左心室质量和心肌厚度，这些进而为诊断和治疗心脏疾病提供关键信息。该数据集涵盖 150 个病例，分为 5 个子类：NOR (正常)、MINF (心肌梗死伴随收缩性心力衰竭)、DCM (扩张型心肌病)、HCM (肥厚型心肌病) 和 ARV (右室异常)，每类各 30 例。每一病例都包括一个心脏周期的 4D nifti格式图像，并且标注了舒张期 (ED) 与收缩期 (ES) 帧。官方将数据划分为 100 例的训练集和 50 例的测试集，每个子类在训练集中有 20 例，在测试集中有 10 例。所有 150 例数据和标注都已公开。

数据集 150 例病人的 300 例图像的切片个数：2978

# 二、官方英文描述

## Database access

The overall ACDC dataset was created from real clinical exams acquired at the University Hospital of Dijon. Acquired data were fully anonymized and handled within the regulations set by the local ethical committee of the Hospital of Dijon (France). Our dataset covers several well-defined pathologies with enough cases to (1) properly train machine learning methods and (2) clearly assess the variations of the main physiological parameters obtained from cine-MRI (in particular diastolic volume and ejection fraction). The dataset is composed of 150 exams (all from different patients) divided into 5 evenly distributed subgroups (4 pathological plus 1 healthy subject groups) as described below. Furthermore, each patient comes with the following additional information : weight, height, as well as the diastolic and systolic phase instants.

Although the challenge is now closed, the data and the groundtruth are still publicly available via the following link.

Study population

The targeted population for the study is composed of 150 patients divided into 5 subgroups as follows:

30 normal subjects - NOR

30 patients with previous myocardial infarction (ejection fraction of the left ventricle lower than 40% and several myocardial segments with abnormal contraction) - MINF

30 patients with dilated cardiomyopathy (diastolic left ventricular volume >100 mL/m2 and an ejection fraction of the left ventricle lower than 40%) - DCM

30 patients with hypertrophic cardiomyopathy (left ventricular cardiac mass high than 110 g/m2, several myocardial segments with a thickness higher than 15 mm in diastole and a normal ejecetion fraction) - HCM

30 patients with abnormal right ventricle (volume of the right ventricular cavity higher than 110 mL/m2 or ejection fraction of the rigth ventricle lower than 40%) - RV

Each group was clearly defined according to physiological parameter, such as the left or right diastolic volume or ejection fraction, the local contraction of the LV, the LV mass and the maximum thickness of the myocardium. More details can be found on the Classification rules tab.

Involved systems

The acquisitions were obtained over a 6 year period using two MRI scanners of different magnetic strengths (1.5 T (Siemens Area, Siemens Medical Solutions, Germany) and 3.0 T (Siemens Trio Tim, Siemens Medical Solutions, Germany)). Cine MR images were acquired in breath hold with a retrospective or prospective gating and with a SSFP sequence in short axis orientation. Particularly, a series of short axis slices cover the LV from the base to the apex, with a thickness of 5 mm (or sometimes 8 mm) and sometimes an interslice gap of 5 mm (then one image every 5 or 10 mm, according to the examination). The spatial resolution goes from 1.37 to 1.68 mm2/pixel and 28 to 40 images cover completely or partially the cardiac cycle (in the second case, with prospective gating, only 5 to 10 % of the end of the cardiac cycle was omitted), all depending on the patient.

## training dataset:
General description

The training database is composed of 100 patients as follows:

20 healthy patients;
20 patients with previous myocardial infarction;
20 patients with dilated cardiomyopathy;
20 patients with an hypertrophic cardiomyopathy;
20 patients with abnormal right ventricle;

For all these data, the corresponding manual references given by one clinical expert along with additional information on the patient (age, weight, height and diastolic-systolic phase instants) are also provided.

## testing dataset:
General description

The testing database is composed of 50 patients as follows:

10 healthy patients;
10 patients with previous myocardial infarction;
10 patients with dilated cardiomyopathy;
10 patients with an hypertrophic cardiomyopathy;
10 patients with abnormal right ventricle;

For all these data, the corresponding manual references given by one clinical expert along with additional information on the patient (age, weight, height and diastolic-systolic phase instants) are also provided.

# 三、翻译

1. 被采集者选择  
    为了验证本章提出的方法,本文使用了 MICCAI 2017 自动心脏诊断挑战赛  (Automated Cardiac Diagnosis Challenge,ACDC)数据集[64]。该数据集是由法  国勃艮第大学医院(University Hospital of Dijon, France)在临床检查中获取的真  实心脏 MRI 数据。其涵盖了多种明确定义的病理学样本,并可以根据该样本较  为准确地估算出主要生理参数(如舒张末期容积和射血分数等)。该数据的采集  对象由 150 名患者组成,根据生理参数和临床诊断结果平均分为 5 种类别:  • 正常(NOR):该组被采集对象的心脏结构与功能均正常,其舒张期的心  室壁厚度小于 12 mm ,射血分数大于 50%。对于女性被采集者,其左心室舒张量  小于 80 2  ml / m ,对于男性被采集者则小于 90 2  ml / m 。  • 心力衰竭(MINF):该组被采集对象的患有心力衰竭并伴有梗死,其射  血分数小于 40%,且心肌收缩异常。某些患者由于心肌梗死而导致左心室容量扩  张。
    基于半监督学习的心脏 MRI 图像分割  32  • 扩张型心肌病(DCM):患者的心脏射血分数小于 40%,左心室容积大  于 100 2  ml / m 且舒张期心室容积小于 12 2  ml / m 。  • 肥厚型心肌病(HCM):该组被采集者的心脏功能正常,其心脏射血分  数大于 55%,但是其舒张期的心室壁厚度大于 15 mm 。  • 右心室异常(ARV):患者的右心室射血分数小于 40%,且对于女性患  者 , 其 右 心 室 容 积 大 于 100 2  ml / m ; 对 于 男 性 患 者 , 其 右 心 室 容 积 大 于  110 2  ml / m ,这些患者的左心室均正常。 
2. 数据获取 
   该数据集的图像由两台磁场强度分别为 1.5 和 3.0T 的磁共振扫描仪采集得  到。其在得到长轴切片后,又获得了一系列左心室从基部到心尖的短轴切片,这  些切片的厚度从 5 mm 到 10 mm 不等。这些图片的空间分辨率在 1.34 mm2 / pixel  到 1.68 mm2 / pixel 之间。为了考虑心动周期对图片的影响,根据患者的差异性,  该数据集采集了 28 到 40 次心脏图像以完全覆盖一个心动周期。同时,为了与以  往的心脏 MRI 分割挑战数据集相一致,该数据集只提供了短轴心脏 MRI 切片。  图 3-7 ACDC 数据集原始图片样本与标注样本示例 (来源于[64])  Fig 3-7 Example of ACDC original samples and labeled samples (Origin from [64])
3. 数据标注  该数据集对心脏的左心室、右心室和心肌进行了逐像素的标注。如图 3-7 所  示为该数据集每个类别下的原始图片样本与标注样本。标注任务是由 2 名分别具  有 10 年与 20 年的专家手工进行,两者均先独立完成,随后进行交叉检查,如出  现不一致的情况,专家则进行讨论并达成一致后进行修正。  在标注过程中,他们遵循了以下规则:第一,标注必须完全覆盖左心室和右  心室,且乳头肌包含在心腔内,并且左心室的基部没有肌肉;第二,由于右心室  的心外膜的准确位置难以界定,所以标注时不包含该结构;第三,右心室的心肌  厚度与空间分辨率应处于同一数量级。该数据集和标注信息以 NIfTI 格式存储,  每个像素的标注信息为从 0 到 3 的整数,其中 0 表示背景,1 代表右心室,2 代  表心肌,3 代表左心室。同时,该数据集被划分为两部分。其中训练集包含 100  个被采集对象的图像,测试集包含 50 个被采集对象的图像。  在本章的实验中,我们将训练集中的 100 个被采集对象的 3D MRI 图像切分  为 1400 张 2D 图像,并将其 80%划分为训练集,20%划分为验证集。