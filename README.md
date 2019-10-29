# fmm_crawl
Automatic search for Biosynthesis pathway information

#AUTHOR
>Byunghyun Ban
* CTO of Imagination Garden Inc. (2018~)
* CFO & CEO of Cheesecake Studio Inc. (2016 ~ 2017)
* CEO & CTO of Studio Mic Inc. (2015)
* CTO of New Page Inc. (2011~2013)
* Master's Degree @ Bio and Brain Engineering Department, KAIST (Korea Advanced Institute of Science and Technology)
* bhban@kaist.ac.kr
* halfbottle@sangsang.farm

## 1. Environments
* Python3
* Don't support any problems from python2 environment

## 2. Dependencies
* Selenium and chromedriver are required.
> pip install selenium on bash.
* chromedriver for Chrome version 78. is attached. Please check the version.


## 3. Preperation of input file
Each line should contain one KEGG ID, without any comma.


## 4. Usage
> python main.py <out_file_name> <from_file_name> <to_file_name>

Then the headless driver accesses to FMM server, searching all possible queries.


## 5. About FMM
http://fmm.mbc.nctu.edu.tw/



C.H. Chou, W.C. Chang, C.M. Chiu, C.C. Huang, and H.D. Huang (2009) "FMM: a web server for metabolic pathway reconstruction and comparative analysis", Nucleic Acids Research, Vol. 37, W129-34 [PubMed]
