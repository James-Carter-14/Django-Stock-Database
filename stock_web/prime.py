from django.db import transaction
from django.contrib.auth.models import User, Group
from .models import ForceReset, Suppliers, Teams, Reagents, Internal, Validation, Recipe, Inventory, Solutions, VolUsage

def PRIME():
    with transaction.atomic():
        Admin = Group.objects.create(name="Admin")
        # perms=['13','14','16','8','5','6','9','10','12']
        # for p in perms:
        #     Admin.permissions.add(p)
        Senior_Admin = Group.objects.create(name="Senior_Admin")
        perms2=['1','2','4','5','6','8','12','13','14','16','17','18','19','21','22','23','24']
        for p2 in perms2:
            Senior_Admin.permissions.add(p2)
        #password fine in here as after first log on required to change it
        user = User.objects.create_user("Admin", "", "password")
        user.first_name = ""
        user.last_name = ""
        user.is_superuser=True
        user.is_staff=True
        user.save()
        sups=["Agilent Technologies",
        "Applied Biosystems",
        "Beckman Coulter",
        "Bioline",
        "Bio-Rad",
        "Clent Life Science",
        "DNA Genotek",
        "Elucigene Diagnostics",
        "Fisher Scientific",
        "Illumina",
        "Launch Diagnostics",
        "Life Technologies",
        "MRC Holland",
        "New England BioLabs",
        "Promega",
        "Qiagen",
        "Roche Diagnostic",
        "Sigma-Aldrich",
        "Scientific Laboratory Supplies",
        "Sophia Genetics",
        "TaKaRa Clontech",
        "TWIST Bioscience",
        "VH Bio",
        "VWR International"]
        for sup in sups:
            Suppliers.create(sup)
        teams=["DNA", "CYTO"]
        for team in teams:
            Teams.create(team)
        for name, cata, sup, minimum, vol, team in (('High Sensitivity D1000 ScreenTape [112 reactions]~','5067-5584','Agilent Technologies','2',False, "DNA"),
                                               ('Genomic DNA ScreenTape [112 reactions]~','5067-5365','Agilent Technologies','0',False, "DNA"),
                                               ('Genomic DNA Reagents [1 kit]~','5067-5366','Agilent Technologies','0',False, "DNA"),
                                               ('High Sensitivity D1000 Reagents [1 kit]~','5067-5585','Agilent Technologies','2',False, "DNA"),
                                               ('Ampure XP [450 ml]','A63882','Beckman Coulter','0',False, "DNA"),
                                               ('CleanSeq [500 ml]','A29161 ','Beckman Coulter','0',False, "DNA"),
                                               ('Megamix-Blue [5 x 0.5 ml]','2MMB-5','Clent Life Science','1',False, "DNA"),
                                               ('Megamix Royal [50 x 1 ml]','2MMR-50','Clent Life Science','1',False, "DNA"),
                                               ('CA Solution [25 ml]','2CA25','Clent Life Science','0',False, "DNA"),
                                               ('Megamix-Blue Double [5 x 0.5 ml]','2MMBD-5','Clent Life Science','0',False, "DNA"),
                                               ('PrepIT Oragene Purifier [0.5 ml]','PT-L2P-5','DNA Genotek','0',False, "DNA"),
                                               ('CF29v2 [50 reactions]','CF029B2','Elucigene Diagnostics','0',False, "DNA"),
                                               ('GE Healthcare Deaza dGTP [2 µm]','10146044','Fisher Scientific','0',False, "DNA"),
                                               ('Eco52I Restriction Enzyme [50 reactions]','FD0334','Fisher Scientific','0',False, "DNA"),
                                               ('Sodium Hydroxide Solution [1 L]','10488790','Fisher Scientific','0',False, "DNA"),
                                               ('MiSeq Reagent Kit v3 [1 unit]~ ','MS-102-3003','Illumina','6',False, "DNA"),
                                               ('Nextera XT Index kit v2 set B [384 Reactions]','FC-131-2002','Illumina','0',False, "DNA"),
                                               ('Nextera XT Library Preparation Kit [96 Reactions]','FC-131-1096','Illumina','0',False, "DNA"),
                                               ('PhiX Control v3 [10 µl]~  ','FC-110-3001','Illumina','0',False, "DNA"),
                                               ('Devyser CFTR combo Core + UK [2 x 48 reactions]','8-A603','Launch Diagnostics','2',False, "DNA"),
                                               ('DEV-5 Dye Set Multicap [45 µl]~','8-A401','Launch Diagnostics','0',False, "DNA"),
                                               ('0.5M EDTA pH8.0 [50 ml]~ ','AM9261','Life Technologies','1',False, "DNA"),
                                               ('GeneScan 500 LIZ Dye Size Standard [800 reactions]~','4322682','Life Technologies','2',False, "DNA"),
                                               ('GeneScan 600 LIZ Dye Size Standard [800 reactions]~','4366589','Life Technologies','1',False, "DNA"),
                                               ('Hi-Di Formamide [25 ml]~','4311320','Life Technologies','2',False, "DNA"),
                                               ('AmpFLSTR Identifiler PCR Amplification kit [200 reactions]','4322288','Life Technologies','1',False, "DNA"),
                                               ('AmpliTaq Gold DNA Polymerase with Buffer II and MgCl2 [50 µl]','N8080241','Life Technologies','1',False, "DNA"),
                                               ('T4 DNA Ligase [500  µl]','15224025','Life Technologies','1',False, "DNA"),
                                               ('BglI Restriction Enzyme [200  µl]','ER0071','Life Technologies','1',False, "DNA"),
                                               ("O'RangeRuler 100 bp DNA Ladder [25 µg]",'SM0623','Life Technologies','1',False, "DNA"),
                                               ('TaqMan Gene Expression Master Mix [5 ml]','4369016','Life Technologies','1',False, "DNA"),
                                               ('BigDye Terminator v3.1 Cycle Sequencing Kit [5000 reactions]','4337457','Life Technologies','0',False, "DNA"),
                                               ('POP-7 Polymer [10 x 28 ml]~','4363935','Life Technologies','2',False, "DNA"),
                                               ('AluI Restriction Enzyme [100 reactions]','FD0014','Life Technologies','1',False, "DNA"),
                                               ('3730 Buffer with EDTA [500 ml]~','4335613','Life Technologies','0',False, "DNA"),
                                               ('3730 DNA Analyzer Capillary Array [1 unit]~','4331250','Life Technologies','1',False, "DNA"),
                                               ('BglII Restriction Enzyme [100 reactions]','FD0083','Life Technologies','0',False, "DNA"),
                                               ('BigDye Terminator v1.1 & v3.1 5X Sequencing Buffer [28 ml]','4336699','Life Technologies','1',False, "DNA"),
                                               ('HpyF3I Restriction Enzyme [50 reactions]','FD1884','Life Technologies','1',False, "DNA"),
                                               ('DraI Restriction Enzyme  [150  µl]','ER0221','Life Technologies','0',False, "DNA"),
                                               ('DS-33 Matrix Standard Kit (Dye Set G5, "DNA"), [8 reactions]~','4345833','Life Technologies','0',False, "DNA"),
                                               ('SuperScript IV First-Strand Synthesis System [200 reactions]','18091200','Life Technologies','0',False, "DNA"),
                                               ('3730 DNA Analyzer Sequencing Standards BigDye Terminator v3.1 [1 unit]~','4336943','Life Technologies','0',False, "DNA"),
                                               ('GeneAmp 10X PCR Buffer II & MgCl2 [6 x 1.5 ml]','N8080130','Life Technologies','0',False, "DNA"),
                                               ('KAPA Library Amplification Kit [1.25 ml]','7958978001','Roche Diagnostic','0',False, "DNA"),
                                               ('Kapa HiFi Hot Start ReadyMix [6.25 ml]','KK2602','Roche Diagnostic','1',False, "DNA"),
                                               ('Hi-Strength Analytical Agarose [25 g]~','H15669','Scientific Laboratory Supplies','1',False, "DNA"),
                                               ('MgCl2 Solution [3 x 1.2 ml]~','BIO-37026','Scientific Laboratory Supplies','2',False, "DNA"),
                                               ('dNTP set [4 x 250  µl]','BIO-39025','Scientific Laboratory Supplies','0',False, "DNA"),
                                               ('MyFi Mix [100 reactions] ','BIO-25049','Scientific Laboratory Supplies','1',False, "DNA"),
                                               ('Taq DNA Polymerase [1000 reactions] ','11146173001','Sigma-Aldrich','1',False, "DNA"),
                                               ('Bromophenol Blue [5 g]~','114391-5g','Sigma-Aldrich','0',False, "DNA"),
                                               ('Agarose Medium EEO [100 g]~ ','A6877','Sigma-Aldrich','3',False, "DNA"),
                                               ('Pwo DNA Polymerase [100 µl]','11644955001','Sigma-Aldrich','1',False, "DNA"),
                                               ('DNA Molecular Weight Marker II [500 µg]','10236250001','Sigma-Aldrich','1',False, "DNA"),
                                               ('KAPA2G Fast HotStart ReadyMix [6.25 ml]','KK5609','Sigma-Aldrich','14',False, "DNA"),
                                               ('PCR DIG Probe Synthesis Kit [25 reactions]','11636090910','Sigma-Aldrich','0',False, "DNA"),
                                               ('DIG-High Prime [160 μL]','11585606910','Sigma-Aldrich','0',False, "DNA"),
                                               ('DIG Wash and Block Buffer Set [1 unit]','11585762001','Sigma-Aldrich','0',False, "DNA"),
                                               ('Trizma Base [5 kg]~','11814273001','Sigma-Aldrich','0',False, "DNA"),
                                               ('Anti-Digoxigenin-AP Fab Fragments [200 μl]','11093274910','Sigma-Aldrich','0',False, "DNA"),
                                               ('DIG Easy Hyb Granules [6 x 100 ml]','11796895001','Sigma-Aldrich','0',False, "DNA"),
                                               ('Dimethyl Sulfoxide [50 ml]~','D8418-50ml','Sigma-Aldrich','0',False, "DNA"),
                                               ('STE Buffer Solution [100 ml]','85810 - 100ml','Sigma-Aldrich','0',False, "DNA"),
                                               ('Tween 20 [250 ml]~ ','P1379-250ml','Sigma-Aldrich','0',False, "DNA"),
                                               ('KAPA LongRange [6.25 ml]','KK3602','Sigma-Aldrich','0',False, "DNA"),
                                               ('DNA Molecular Weight Marker II DIG-Labeled [500 μl]','11218590910','Sigma-Aldrich','0',False, "DNA"),
                                               ('Betaine [50 g]','B2629-50g','Sigma-Aldrich','0',False, "DNA"),
                                               ('SuRE/Cut Buffer A [5 x 1 ml]','11417959001','Sigma-Aldrich','0',False, "DNA"),
                                               ('CDP-Star [2 x 50 ml]','12041677001','Sigma-Aldrich','0',False, "DNA"),
                                               ('Ethidium Bromide Solution [10 ml]','E1510-10ML','Sigma-Aldrich','0',False, "DNA"),
                                               ('Mineral Oil [500 ml]~','M5904-500ml','Sigma-Aldrich','0',False, "DNA"),
                                               ('Sodium Dodecyl Sulfate Solution [500 ml]~','71736-500ML','Sigma-Aldrich','0',False, "DNA"),
                                               ('Nylon MembraneS Positively Charged [1 roll]~','11417240001','Sigma-Aldrich','0',False, "DNA"),
                                               ('SSC Buffer [10 L]','93017-10L-F','Sigma-Aldrich','0',False, "DNA"),
                                               ('2-Mercaptoethanol [25 ml]','M3148-25ml','Sigma-Aldrich','0',False, "DNA"),
                                               ('Custom Hereditary Cancer Solution [2lxl24 reactions]','CS.2170.0102-00','Sophia Genetics','3',False, "DNA"),
                                               ('TaKaRa LA Taq DNA Polymerase Hot-start Version [500 µl]','RR042B','TaKaRa Clontech','2',False, "DNA"),
                                               ('Twist Universal Adapter System, Plate A [96 reactions]','101308','TWIST Bioscience','1',False, "DNA"),
                                               ('Twist Universal Adapter System, Plate B [96 reactions]','101309','TWIST Bioscience','1',False, "DNA"),
                                               ('Twist Universal Adapter System, Plate C [96 reactions]','101310','TWIST Bioscience','1',False, "DNA"),
                                               ('Twist Universal Adapter System , Plate D [96 reactions]','101311','TWIST Bioscience','1',False, "DNA"),
                                               ('Twist Library Preparation EF kit 1 [96 reactions]','100572','TWIST Bioscience','3',False, "DNA"),
                                               ('Twist Universal Blocker [12 reactions]','100578','TWIST Bioscience','3',False, "DNA"),
                                               ('Twist Hybridization Reagents [12 reactions]','100930','TWIST Bioscience','3',False, "DNA"),
                                               ('Twist Binding and Purification Beads [12 reactions]','100983','TWIST Bioscience','3',False, "DNA"),
                                               ('Twist Human Core Exome & RefSeq panel [12 reactions]','101920','TWIST Bioscience','2',False, "DNA"),
                                               ('Twist Custom Panel [12 reactions]','101001','TWIST Bioscience','2',False, "DNA"),
                                               ('Twist Library Preparation EF kit 2 [96 reactions]','100573','TWIST Bioscience','3',False, "DNA"),
                                               ('Twist Wash Buffers [12 reactions]','100985','TWIST Bioscience','3',False, "DNA"),
                                               ('Sreptavidin Sepharose High Performance [5 ml]','17-5113-01','VWR International','1',False, "DNA"),
                                               ('Orthoboric Acid [5 kg]~ ','20185.36','VWR International','0',False, "DNA"),
                                               ('Formaldehyde [1 L]~','20910.294','VWR International','0',False, "DNA"),
                                               ('Ethanol Absolute [2.5 L]','20821.330DP','VWR International','3',False, "DNA"),
                                               ('Tri-Sodium Citrate [1 kg]~','27833.294','VWR International','0',False, "DNA"),
                                               ('Sodium Chloride [5 kg]~','27810.364','VWR International','0',False, "DNA"),
                                               ('Hydrochloric Acid [1 L]~','20252.244','VWR International','0',False, "DNA"),
                                               ('Sodium Hydroxide Pellets [1 kg]','28244.295','VWR International','0',False, "DNA"),
                                               ('SALSA MLPA EK20 Reagent Kit [2000 reactions]','EK20-FAM','MRC Holland','1',False, "DNA"),
                                               ('S4 Sample Stabiliser [200 reactions]','SMR04','MRC Holland','3',False, "DNA"),
                                               ('SALSA HhaI [200 reactions]','SMR50','MRC Holland','1',False, "DNA"),
                                               ('SALSA P200 Reference MLPA kit [100 reactons]','PbP200-100R','MRC Holland','1',False, "DNA"),
                                               ('SALSA P310 TCOF MLPA kit [100 reactons]','PbP310-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P229 OPA1 MLPA kit [50 reactons]','PbP229-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P279 CACNA1A MLPA kit [50 reactons]','PbP279-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P152 ABCA4 MLPA kit [50 reactons]','PbP152-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P108 SCN5A MLPA kit [50 reactons]','PbP108-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P168 ARVC MLPA kit [100 reactons]','PbP168-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P002 BRCA1 MLPA kit [100 reactons]','PbP002-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P226 SDH MLPA kit [50 reactons]','PbP226-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P048 LMNA MLPA kit [50 reactons]','PbP048-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P427 PDHA1 MLPA kit [50 reactons]','PbP427-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P387 NPHP1 MLPA kit [100 reactons]','PbP387-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P151 ABCA4 MLPA kit [50 reactons]','PbP151-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA MLPA EK5 Reagent Kit [500 reactions]','EK5-FAM','MRC Holland','1',False, "DNA"),
                                               ('SALSA P048 LMNA MLPA kit [100 reactons]','PbP048-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P466 CDC73 MLPA kit [100 reactons]','PbP466-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P179 LIMB1 MLPA kit [50 reactons]','PbP179-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P090 BRCA2 MLPA kit [100 reactons]','PbP090-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P213 HSP-2 MLPA kit [25 reactons]','PbP213-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA ME011 MMR MLPA kit [100 reactons]','ME011-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P003-MSH2/MLH1 MLPA Kit [100 reactons]','P003-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P016 VHL MLPA kit [25 reactons]','PbP016-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P043 APC MLPA kit [100 reactons]','PbP043-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P010 POLG MLPA kit [100 reactons]','PbP010-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P138 SLC2A1 MLPA kit [50 reactons]','PbP138-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA ME030 BWS/RSS MLPA kit [100 reactons]','ME030-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P008 PMS2 MLPA kit [100 reactons]','PbP008-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P419 CDKN2A/B MLPA kit [50 reactons]','PbP419-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P056 TP53 MLPA kit [100 reactons]','PbP056-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P225 PTEN MLPA kit [100 reactons]','PbP225-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P089 TK2 MLPA kit [50 reactons]','PbP089-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P235 Retinitis MLPA kit [25 reactons]','PbP235-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P244 MEN1 MLPA kit [100 reactons]','PbP244-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P231 LADD MLPA kit [100 reactons]','PbP231-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P072 MSH6 MLPA kit [50 reactons]','PbP072-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P034 DMD MLPA kit [100 reactons]','PbP034-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P159 GLA MLPA kit [50 reactons]','PbP159-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA ME032 UPD7/UPD14 MLPA kit [100 reactons]','ME032-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P035 DMD MLPA kit [100 reactons]','PbP035-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P193 NPC1-NPC2-SMPD1 MLPA kit [25 reactons]','PbP193-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P091 CFTR MLPA kit [50 reactons]','PbP091-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P440 F10+F11 MLPA kit [50 reactons]','PbP440-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P080 Cranio MLPA kit [100 reactons]','PbP080-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P207 F9 MLPA kit [50 reactons]','PbP207-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P479 TCF12-ERF MLPA kit [100 reactons]','PbP479-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P158 JPS MLPA kit [50 reactons]','PbP158-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P260 PALB2 MLPA kit [25 reactons]','PbP260-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P112 PROS1 MLPA kit [25 reactons]','PbP112-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P178 F8 MLPA kit [25 reactons]','PbP178-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P011 VWF-1 MLPA kit [50 reactons]','PbP011-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P012 VWF-2 MLPA kit [50 reactons]','PbP012-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P114 LQT MLPA kit [100 reactons]','PbP114-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P347 Hemochromatosis MLPA kit [100 reactons]','PbP347-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P101 STK11 MLPA kit [100 reactons]','PbP101-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P100 MYBPC3 MLPA kit [100 reactons]','PbP100-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P469 F5 MLPA kit [25 reactons]','PbP469-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P362 USH2A MIX 2 MLPA kit [100 reactons]','PbP362-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P361 USH2A MIX 1 MLPA kit [100 reactons]','PbP361-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P441 SACs MLPA kit [25 reactons]','PbP441-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P227 SERPINC1 MLPA kit [25 reactons]','PbP227-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P166 KCNQ2 MLPA kit [25 reactons]','PbP166-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P366 CHM-RP2-RPGR MLPA kit [100 reactons]','PbP366-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P348 ATP1A2-CACNA1A MLPA kit [25 reactons]','PbP348-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P418 MYH7 MLPA kit [25 reactons]','PbP418-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P226 SDH MLPA kit [25 reactons]','PbP226-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P316 Recessive Ataxias MLPA kit [50 reactons]','PbP316-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P432 MYH9 MLPA kit [25 reactons]','PbP432-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P265 PROC1 MLPA kit [25 reactons]','PbP265-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P102 HBB MLPA kit [100 reactons]','PbP102-100R','MRC Holland','1',False, "DNA"),
                                               ('SALSA P140 HBA MLPA kit [100 reactons]','PbP140-100R','MRC Holland','2',False, "DNA"),
                                               ('SALSA P212 DBA MLPA kit [25 reactons]','PbP212-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P203 PKLR MLPA kit [25 reactons]','PbP203-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA PbP093 HHT/HPAH MLPA kit [25 reactons]','PbP093-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA PbP367 BEST1-PRPH2 MLPA kit [25 reactons]','PbP367-25R','MRC Holland','0',False, "DNA"),
                                               ('SALSA PbP062 LDLR MLPA kit [100 reactons]','PbP062-100R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P031 FANCA mix 1 MLPA Kit [50 reactons]','PbP031-50R','MRC Holland','0',False, "DNA"),
                                               ('SALSA P032 FANCA mix 2 MLPA Kit [50 reactons]','PbP032-50R','MRC Holland','0',False, "DNA"),
                                               ('HpaII Restriction Enzyme [2000 units]','R0171S','New England BioLabs','1',False, "DNA"),
                                               ('HaeIII Restriction Enzyme [3000 units]','R0108S','New England BioLabs','1',False, "DNA"),
                                               ('BclI Restriction Enzyme [3000 units]','R0160S','New England BioLabs','1',False, "DNA"),
                                               ('RsaI Restriction Enzyme [5000 units]','R0167L','New England BioLabs','1',False, "DNA"),
                                               ('MboI Restriction Enzyme [2500 units]','R0147L','New England BioLabs','1',False, "DNA"),
                                               ('Quick-Load Purple 50 bp DNA Ladder [1.25 ml]','N0556S','New England BioLabs','1',False, "DNA"),
                                               ('HindIII Restriction enzyme [500 µl]','R0104S','New England BioLabs','1',False, "DNA"),
                                               ('Maxwell RSC Blood DNA Kit [48 reactions]','AS1400 ','Promega','3',False, "DNA"),
                                               ('Maxwell RSC FFPE DNA kit [48 reactions]','AS1450','Promega','0',False, "DNA"),
                                               ('MSI Analysis system [100 reactions]','MD1641','Promega','1',False, "DNA"),
                                               ('Quantifluor dsDNA System [1 ml]~','E2670','Promega','2',False, "DNA"),
                                               ('ReliaPrep Large Volume HT gDNA Isolation System [1 kit]','A2751','Promega','2',False, "DNA"),
                                               ('Maxwell RSC FFPE RNA kit [48 reactions]','AS1440','Promega','0',False, "DNA"),
                                               ('TE Buffer [25 ml]~ ','A2651','Promega','0',False, "DNA"),
                                               ('Proteinase K Solution [23 ml]~','A5051','Promega','0',False, "DNA"),
                                               ('Binding Buffer [1600 ml]','A1741','Promega','0',False, "DNA"),
                                               ('Cell Lysis Buffer [1400 ml]','A1731','Promega','0',False, "DNA"),
                                               ('PowerPlex 4C Matrix Standards [5 reactions]~','DG4800','Promega','0',False, "DNA"),
                                               ('QIAGEN Multiplex PCR Kit [1000 reactions]','206145','Qiagen','1',False, "DNA"),
                                               ('PyroMark Gold Q96 Reagents [5 x 96 reactions]','972804','Qiagen','1',False, "DNA"),
                                               ('PyroMark Denaturation Solution [500 ml]','979007','Qiagen','2',False, "DNA"),
                                               ('PyroMark Wash Buffer [200 ml]','979008','Qiagen','1',False, "DNA"),
                                               ('PyroMark Annealing Buffer [250 ml]','979009','Qiagen','1',False, "DNA"),
                                               ('Buffer EB [250 ml]~','19086','Qiagen','0',False, "DNA"),
                                               ('QIAamp RNA Blood Mini Kit [50 reactions]','52304','Qiagen','0',False, "DNA"),
                                               ('RNase-Free DNase Set [50 reactions]','79254','Qiagen','0',False, "DNA"),
                                               ('PAXgene Blood RNA Kit [50 reactions]','762174','Qiagen','0',False, "DNA")):
            values={}
            values["name"]=name
            values["cat_no"]=cata
            try:
                values["supplier_def"]=Suppliers.objects.get(name=sup)
                values["team_def"]=Teams.objects.get(name=team)
            except Exception as e:
                print(e)
                print(sup)
                import pdb; pdb.set_trace()
            values["min_count"]=int(minimum)
            values["track_vol"]=vol
            try:
                Reagents.create(values)
            except Exception as e:
                print(e)
                print(name)
                import pdb; pdb.set_trace()
