#import csv 

import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_row', None)
from collections import Counter
pd.options.mode.chained_assignment = None



def setpath(file, type):
    if type == 'snp':
        path = file+'.ann.snp.txt'
    elif type == 'indel':
        path = file+'.ann.indel.txt'
    return path

def vcfimport(path):
    vcf = pd.read_csv(path, delimiter="\t")
    vcf['GEN[*].GT'] = vcf['GEN[*].GT'].replace('1-Jan', '1/1')
    print(vcf.groupby(['ANN[*].EFFECT'])['ANN[*].EFFECT'].count())
    print('==================================================================')
    print(vcf.groupby(['ANN[*].IMPACT'])['ANN[*].IMPACT'].count())
    return vcf


# Is there and variants of the genes of interest in the vcf

def geneselect(vcf, genes = []):
	if len(genes) == 0:
		genes = list(map(str, input('Enter a list of factors to be analysed,separated by a comma: ').split(',')))
		genes = [i.strip() for i in genes]
		print(genes)
	else: 
		pass
	output = vcf.loc[vcf['ANN[*].GENE'].isin(genes)]
	print('Total number of variants captured',len(output))
	output_impact = output.groupby(['ANN[*].GENE','ANN[*].EFFECT'])['ANN[*].EFFECT'].count()
	print(output_impact)
	output = output[['CHROM', 'POS', 'ID', 'REF', 'ALT', 'GEN[*].GT',
       'GEN[*].AD[0]', 'GEN[*].AD[1]', 'GEN[*].DP', 'ANN[*].EFFECT', 'ANN[*].IMPACT',
       'ANN[*].CDNA_POS', 'ANN[*].AA_POS', 'ANN[*].GENE', 'ANN[*].BIOTYPE',
       'ANN[*].HGVS_C', 'ANN[*].HGVS_P', 'ANN[*].FEATUREID']]
	return output

#Filter and selected only high-impact SNPs and unique ['select' is from geneselect function].

def filtersnp(select):
    snplist = ['missense_variant', 'missense_variant&splice_region_variant', 'protein_protein_contact','splice_acceptor_variant&intron_variant','splice_donor_variant&intron_variant','start_lost',
	'start_lost&splice_region_variant','stop_gained','stop_lost','stop_lost&splice_region_variant', 'stop_retained_variant', 'start_lost&splice_region_variant', 
    'stop_gained&splice_region_variant', 'start_lost&splice_region_variant']
    output = select[(select['ANN[*].EFFECT'].isin(snplist))|(select['ANN[*].IMPACT'] == 'HIGH')&(select['GEN[*].DP'] > 40) ]
    output = output.drop_duplicates(subset=['CHROM','POS','ANN[*].GENE'], keep='first')
    print('Total number of variants passed',len(output))
    output_impact = output.groupby(['ANN[*].GENE','ANN[*].EFFECT'])['ANN[*].EFFECT'].count()
    print(output_impact)
    return output
   
def filterindel(select):
    indellist = ['disruptive_inframe_deletion','frameshift_variant','frameshift_variant&splice_acceptor_variant&splice_region_variant&intron_variant',
    'frameshift_variant&splice_region_variant', 'frameshift_variant&start_lost',
    'frameshift_variant&stop_gained','frameshift_variant&stop_lost',
    'start_lost&conservative_inframe_deletion','start_lost&disruptive_inframe_deletion',
    'stop_gained&disruptive_inframe_deletion','stop_gained&disruptive_inframe_insertion',
    'structural_interaction_variant', 'splice_acceptor_variant&intron_variant']
    output = select[(select['ANN[*].EFFECT'].isin(indellist))|(select['ANN[*].IMPACT']=='HIGH') & (select['GEN[*].DP'] > 40)]
    output = output.drop_duplicates(subset=['CHROM','POS','ANN[*].GENE'], keep='first')
    print('Total number of variants passed',len(output))
    output_impact = output.groupby(['ANN[*].GENE','ANN[*].EFFECT'])['ANN[*].EFFECT'].count()
    print(output_impact)
    return output


def export(vcf, name):
    vcf.to_csv(name+'.csv',index = False, sep=',', encoding='utf-8')

#Filtering snp/indel vcf using a list of interested gene and export file to a destined folder (must be pre-constructed)

def prioritize(file, geneset):
    print(file)
    print('SNP filtering')
    path_snp = setpath(file, 'snp')
    df_snp = vcfimport(path_snp)
    df_snp_sel = geneselect(df_snp, geneset)
    print('FIltering ===============================================')
    df_snp_sel_filter = filtersnp(df_snp_sel)
    export(df_snp_sel_filter, file+'.snp.filtered')
    print ('========================================================')
    print('INDEL filtering')
    path_indel = setpath(file, 'indel')
    df_indel = vcfimport(path_indel)
    df_indel_sel = geneselect(df_indel, geneset)
    print('FIltering ===============================================')
    df_indel_sel_filter = filterindel(df_indel_sel)
    export(df_indel_sel_filter, file+'.indel.filtered')
     
# Filter many files (snp/indel) at once.

def batchfilter(filelist, geneset):
    for i in range(len(filelist)):
        prioritize(filelist[i], geneset)
        

#Building dictionary of genes that have variants and sort from most frequent to the least.

def genedict(filelist):
    gene_dict = {}
    for i in filelist:
        read_snp = pd.read_csv(i+'.snp.filtered.csv')
        gene_list_i_snp = read_snp['ANN[*].GENE'].to_list()
        read_indel = pd.read_csv(i+'.indel.filtered.csv')
        gene_list_i_indel = read_indel['ANN[*].GENE'].to_list()
        gene_list_i_mix = gene_list_i_snp + gene_list_i_indel
        for entry in gene_list_i_mix:
            if entry in (gene_dict):
                gene_dict[entry] += 1
            else:
                    gene_dict[entry] = 1
    gene_dict = {str(key): val for key, val in gene_dict.items()}
    for key in sorted(gene_dict.keys()):
        print(key , " :: " , gene_dict[key])
        print('')
    gene_dict = sorted(gene_dict.items(), key=lambda x: x[1], reverse = True)
    return gene_dict

def genedict_case(filelist):
    gene_dict_case = {}
    for i in filelist:
        read_snp = pd.read_csv(i+'.snp.filtered.csv')
        gene_list_i_snp = read_snp['ANN[*].GENE'].to_list()
        read_indel = pd.read_csv(i+'.indel.filtered.csv')
        gene_list_i_indel = read_indel['ANN[*].GENE'].to_list()
        gene_list_i_indel = gene_list_i_indel + gene_list_i_snp
        gene_list_i_indel = set(gene_list_i_indel)
        for entry in gene_list_i_indel:
            if entry in (gene_dict_case):
                gene_dict_case[entry] += 1
            else:
                    gene_dict_case[entry] = 1
    gene_dict_case = {str(key): val for key, val in gene_dict_case.items()}
    for key in sorted(gene_dict_case.keys()):
        print(key , " :: " , gene_dict_case[key], 'cases ,percentage of variants = ', gene_dict_case[key]*100/len(filelist),'%')
        print('')
    gene_dict_case = sorted(gene_dict_case.items(), key=lambda x: x[1], reverse = True)
    return gene_dict_case


# Show matrix of genes with positive variants

def matrix(geneset, file):
    df = pd.DataFrame({'Genelist':geneset})
    A_list = []
    read_snp = pd.read_csv(file+'.snp.filtered.csv')
    gene_list_i_snp = read_snp['ANN[*].GENE'].to_list()
    read_indel = pd.read_csv(file+'.indel.filtered.csv')
    gene_list_i_indel = read_indel['ANN[*].GENE'].to_list()
    for i in geneset:
        if i in gene_list_i_snp or i in gene_list_i_indel:
            A_list.append('1')
        else:
            A_list.append('0')
    namae = str(file)
    df[namae] = A_list
    return df 

def variantmatrix(geneset, filelist):
    df = pd.DataFrame({'Genelist':geneset})
    for i in filelist:
        df2 = matrix(geneset, i)
        df = pd.concat([df,df2[str(i)]], axis = 1)
    return df


# Merge filtered snp and indel files and construct variant list to be printed

def readall(file):
    read_snp = pd.read_csv(file+'.snp.filtered.csv')
    read_indel = pd.read_csv(file+'.indel.filtered.csv')
    read_all = pd.concat([read_snp,read_indel], ignore_index=True)
    read_all.reset_index(drop = True, inplace=True)
    read_all['text'] = read_all['CHROM']+':g.'+ read_all['POS'].astype(str)+read_all['REF']+'>'+read_all['ALT']
    print(read_all['text'].to_string(index=False))
    return read_all
    
#Filter file with variant in a certain gene
def genegrep(file, gene):
    read_snp = pd.read_csv(file+'.snp.filtered.csv')
    read_indel = pd.read_csv(file+'.indel.filtered.csv')
    read_all = pd.concat([read_snp,read_indel], ignore_index=True)
    gene_grep = read_all.loc[(read_all['ANN[*].GENE'] == gene )]
    gene_grep['sample'] = file
    return gene_grep

def multigrep(filelist, gene):
    df0 = pd.DataFrame({'':[]})
    for i in filelist:
        df = genegrep(i, gene)
        df0 = pd.concat([df,df0], ignore_index=True)
    return df0

def countvar(filelist, gene):
    L = []
    df0 = multigrep(filelist, gene)
    df0 = df0[['ANN[*].HGVS_P','ANN[*].HGVS_C','sample']].groupby(['ANN[*].HGVS_C','ANN[*].HGVS_P']).count()
    df0 = df0.sort_values(by='sample', ascending=False)
    df0 = df0.reset_index()
    for i in range(len(df0)):
        if df0.iloc[i,1] != '.':
            L.append(str(df0.iloc[i,1])+'('+str(df0.iloc[i,2])+')')
        else:
            L.append(str(df0.iloc[i,0])+'('+str(df0.iloc[i,2])+')')        
    join_list = ', '.join(L)
    print(join_list)
    
 
    
#Del duplicate

def uniqgrep(grepdf):
    grepdf = grepdf.drop_duplicates(subset=['CHROM','POS','ANN[*].GENE'], keep='first')
    grepdf = grepdf.drop(columns = ['sample'])
    return grepdf



#Merge CGI files and prepare for waterfall

def muttableimport(sample):
	path = '/CGI/cgi_analysis '+sample+'_results/mutation_analysis.tsv'
	mut = pd.read_csv(path, delimiter="\t")
	mut['sample'] = sample
	mut = mut.rename({'SYMBOL':'gene', 'CONSEQUENCE':'variant_class', 'PROTEIN_CHANGE':'amino.acid.change'}, axis='columns')
	return mut

def mergecgi(filelist):
	df = pd.DataFrame(columns=['MUTATION',
 'START', 'POS_HG19', 'END', 'CHR', 'ALT', 'REF',
 'STRAND', 'INFO', 'TYPE', 'gene', 'TRANSCRIPT',
 'amino.acid.change', 'BOOSTDM_DS',
 'BOOSTDM_SCORE', 'ONCOGENIC_CLASSIFICATION',
 'SOURCE', 'variant_class', 'IS_CANCER_GENE',
 'CONSENSUS_ROLE', 'sample'])
	for i in filelist:
		mut = muttableimport(i)
		df = pd.concat([df, mut], ignore_index = True)
	return df

def driverfilter(filelist):
    mergecgi_df = mergecgi(filelist)
    mergecgi_df = mergecgi_df[['MUTATION','POS_HG19','gene','amino.acid.change', 'BOOSTDM_DS',
 'BOOSTDM_SCORE', 'ONCOGENIC_CLASSIFICATION',
 'SOURCE', 'variant_class', 'IS_CANCER_GENE',
 'CONSENSUS_ROLE', 'sample']]
    mergecgi_df = mergecgi_df[(mergecgi_df['BOOSTDM_DS'].isin (['driver (oncodriveMUT)', 'driver (boostDM: non-tissue-specific model)' ]))|(mergecgi_df['ONCOGENIC_CLASSIFICATION'].isin ([ 'predicted' ]))]
    driver = mergecgi_df.sort_values(by = 'gene')
    return driver

def readcgibygene(filelist, gene):
    mergecgi_df = mergecgi(filelist)
    mergecgi_df = mergecgi_df[['MUTATION','POS_HG19','gene','amino.acid.change', 'BOOSTDM_DS', 'ONCOGENIC_CLASSIFICATION',
 'SOURCE', 'variant_class', 'sample']]
    mergecgi_df = mergecgi_df[(mergecgi_df['gene'] == gene)]
    mergecgi_df = mergecgi_df[(mergecgi_df['BOOSTDM_DS'] != 'non-protein affecting')]
    mergecgi_df = mergecgi_df.groupby(['amino.acid.change'])['sample'].count()
    return mergecgi_df


def exporttsv(merge, name):
    merge.to_csv(name+'.csv',index = False, sep=",", encoding='utf-8')
    
#Read directly from filtered VCF
def readboth(file):
    read_snp = pd.read_csv('/'+file+'.snp.filtered.csv')
    read_indel = pd.read_csv(file+'.indel.filtered.csv')
    read_all = pd.concat([read_snp,read_indel], ignore_index=True)
    read_all.reset_index(drop = True, inplace=True)
    read_all['sample'] = file
    read_all = read_all[['ANN[*].EFFECT', 'ANN[*].GENE', 'ANN[*].HGVS_P', 'sample']]
    return read_all

def mergeread(filelist):
    df = pd.DataFrame(columns=['ANN[*].EFFECT', 'ANN[*].GENE', 'ANN[*].HGVS_P', 'sample'])
    for i in filelist:
        mut = readboth(i)
        df= pd.concat([df, mut], ignore_index = True)
    return df

def addgroup(df):
    group = []
    for i in df['ANN[*].GENE'].to_list():
        if i in tyr_kinase:
            group.append('tyr_kinase')
        elif i in ras:
            group.append('ras')
        elif i in pi3k:
            group.append('pi3k')
        elif i in jak_stat:
            group.append('jak_stat')
        elif i in notch:
            group.append('notch')
        elif i in wnt:
            group.append('wnt')
        elif i in mirna:
            group.append('mirna')
        elif i in myc:
            group.append('myc')
        elif i in transcription:
            group.append('transcription')
        elif i in cell_cycle:
            group.append('cell_cycle')
        elif i in cohesin:
            group.append('cohesin')
        elif i in epigen:
            group.append('epigen')
        else:
            group.append('oth')
    df['Group'] = group
    print(Counter(group).keys())
    print(Counter(group).values())
    return df


#Mutation type matrix 

def matrixwitheffect(geneset, folder, file):
    df = pd.DataFrame({'Genelist':geneset})
    A_list = []
    path = '/CGI/cgi_analysis '+ file +'_results/mutation_analysis.tsv'
    read_snp = pd.read_csv(path, sep = '\t')
    read_snp = read_snp.loc[read_snp['ONCOGENIC_CLASSIFICATION'] != 'non-protein affecting']
    gene_list_i_snp = read_snp['SYMBOL'].to_list()
    for i in geneset:
        if i in gene_list_i_snp:
            typ = read_snp['CONSEQUENCE'].loc[read_snp['SYMBOL'] == i].values[0]
            A_list.append(typ) 
        
        else:
            A_list.append('')
    namae = str(file)
    df[namae] = A_list
    return df 

def variantmatrixwitheffect(geneset, folder, filelist):
    df = pd.DataFrame({'Genelist':geneset})
    for i in filelist:
        df2 = matrixwitheffect(geneset, folder, i)
        df = pd.concat([df,df2[str(i)]], axis = 1)
    df = df.replace('0', np.nan)
    df = df.dropna(axis = 0, how = 'all')
    return df             

#Working with drug data
#Get drug list from all drug annotated (use getlist)
def getdrugtable(file):
    path = '/CGI/cgi_analysis '+ file +'_results/drug_prescription.tsv'
    readdrug = pd.read_csv(path, sep = '\t')
    readdrug = readdrug.loc[:,['DISEASES', 'SAMPLE_ALTERATION', 'ALTERATION_MATCH', 'DRUGS', 'BIOMARKER', 'RESPONSE']]
    readdrug['SAMPLE'] =  str(file)
    return readdrug

def drugtablemerge(filelist):
    df = pd.DataFrame(columns=['SAMPLE', 'DISEASES', 'SAMPLE_ALTERATION', 'ALTERATION_MATCH', 'DRUGS', 'BIOMARKER', 'RESPONSE'])
    for i in filelist:
        drug = getdrugtable(i)
        df = pd.concat([df,drug], ignore_index=True)
    return df

def getlist(filelist):
    drugmerge = drugtablemerge(filelist)
    druglist = drugmerge['DRUGS'].drop_duplicates().sort_values().to_list()
    return druglist
    
def drugmatrix(filelist, druglist):    
    table = pd.DataFrame({'Druglist':druglist})
     
    for i in filelist:
        read_drug = getdrugtable(i)
        drug = read_drug['DRUGS'].drop_duplicates().to_list()
        B_list = []
        for j in druglist:
            if j in drug:
                B_list.append(read_drug['ALTERATION_MATCH'].loc[read_drug['DRUGS']== j].drop_duplicates().values[0])
            else:
                B_list.append('0')

        namae = str(i)
        table[namae] = B_list
    table.replace(['complete', 'only alteration type', 'only gene'], [3, 2, 1], inplace=True)
    return table
        
    
def selectrow(df, a_list):
    df = df[df.isin(a_list).any(axis=1)]
    return df

def listfdabygene(gene):
    druglist = []
    drug = pd.read_csv('ActionabilityData.tsv', delimiter="\t")
    drug = drug[['GENE', 'MUTATION_REMARK', 'GENOMIC_MUTATION_ID', 'FUSION_ID',
       'MUTATION_AA_SYNTAX', 'DISEASE', 'ACTIONABILITY_RANK',
       'DEVELOPMENT_STATUS', 'DRUG_COMBINATION']]
    drug = drug.loc[drug['GENE']== gene]
    drug = drug.loc[drug['DEVELOPMENT_STATUS'] == 'Approved FDA']
    drug = drug.sort_values(by = 'GENE').drop_duplicates(subset = [ 'DRUG_COMBINATION'])
    drug = drug.reset_index()
    for i in range(len(drug)):
        druglist.append(drug.iloc[i,9])
    druglist = ', '.join(druglist)
    return druglist

def grouplistfda(genelist):
    drugdict = {}
    for i in genelist:
        drugdict[i] = listfdabygene(i)
    return drugdict


def listnbtarget(gene):
    druglist = []
    drug = pd.read_csv('ActionabilityData.tsv', delimiter="\t")
    drug = drug[['GENE', 'MUTATION_REMARK', 'GENOMIC_MUTATION_ID', 'FUSION_ID',
       'MUTATION_AA_SYNTAX', 'DISEASE', 'ACTIONABILITY_RANK',
       'DEVELOPMENT_STATUS', 'DRUG_COMBINATION']]
    drug = drug.loc[drug['GENE']== gene]
    drug = drug.loc[drug['DISEASE'].str.contains('neuroblastoma')]
    drug = drug.sort_values(by = 'GENE').drop_duplicates(subset = [ 'DRUG_COMBINATION'])
    drug = drug.reset_index()
    for i in range(len(drug)):
        druglist.append(drug.iloc[i,9])
    druglist = ', '.join(druglist)
    return druglist

def grouplistnb(genelist):
    drugdict = {}
    for i in genelist:
        drugdict[i] = listnbtarget(i)
    return drugdict


def listphase3(gene):
    druglist = []
    drug = pd.read_csv('ActionabilityData.tsv', delimiter="\t")
    drug = drug[['GENE', 'MUTATION_REMARK', 'GENOMIC_MUTATION_ID', 'FUSION_ID',
       'MUTATION_AA_SYNTAX', 'DISEASE', 'ACTIONABILITY_RANK',
       'DEVELOPMENT_STATUS', 'DRUG_COMBINATION']]
    drug = drug.loc[drug['GENE']== gene]
    drug = drug.loc[drug['DEVELOPMENT_STATUS'] == 'Phase 3']
    drug = drug.sort_values(by = 'GENE').drop_duplicates(subset = [ 'DRUG_COMBINATION'])
    drug = drug.reset_index()
    for i in range(len(drug)):
        druglist.append(drug.iloc[i,9])
    druglist = ', '.join(druglist)
    return druglist

def grouplistphasethree(genelist):
    drugdict = {}
    for i in genelist:
        drugdict[i] = listphase3(i)
    return drugdict


genelist = ['ALK',
 'RIT1',
 'SH2B3',
 'APC',
 'NR3C2',
 'EP300',
 'MGA',
 'PAX5',
 'ZNF384',
 'KMT2C',
 'ATF7IP',
 'GON4L',
 'FLT3',
 'SETD2',
 'PIK3R1',
 'EBF1',
 'TP53',
 'IKZF1',
 'CCND3',
 'IL7R',
 'KDM5A',
 'TET2',
 'PTEN',
 'ATRX',
 'ATM',
 'KMT2B',
 'NSD1',
 'CHD4',
 'TCF3',
 'PBRM1',
 'JAK1',
 'TCF7',
 'LMO1',
 'XBP1',
 'NIPBL',
 'GATA2',
 'ZNF217',
 'DROSHA',
 'ELF1',
 'KDM6A',
 'PDGFRA',
 'TSPYL2',
 'CHD7',
 'JAK3',
 'CDKN1B',
 'CRLF2',
 'KMT2D',
 'CBL',
 'LEF1',
 'TSC1',
 'TERT',
 'PIK3CA',
 'KMT2E',
 'KIT',
 'MYCN',
 'TAL1',
 'TOX',
 'ARID2',
 'MLLT4',
 'NR3C1',
 'ASXL2',
 'ASXL1',
 'BRAF',
 'AMER1',
 'XPO5',
 'KMT2A',
 'TRRAP',
 'ETV6',
 'RUNX1',
 'NUP98',
 'CEBPA',
 'ZFP36L2',
 'GATA4',
 'BCORL1',
 'ARID1A',
 'EPOR',
 'WT1',
 'GLIS2',
 'ETS2',
 'HDAC7',
 'ABL1',
 'KRAS',
 'NF1',
 'PIK3CD',
 'FGFR1',
 'TSC2',
 'JAK2',
 'ZBTB7A',
 'SIX1',
 'CDKN2A',
 'SUZ12',
 'EED',
 'BAZ1A',
 'TET3',
 'CSF3R',
 'XPO1',
 'CTNNB1',
 'MYB',
 'BCL11B',
 'SIX2',
 'RB1',
 'PDS5A',
 'CREBBP',
 'SMARCA4',
 'BCOR',
 'NCOR1',
 'DNMT3A',
 'FBXW7',
 'TLX3',
 'CNOT3',
 'MED12',
 'GATA3',
 'EWSR1',
 'ZEB2',
 'LYL1',
 'STAG1',
 'RAD21',
 'WHSC1']


from lifelines.statistics import logrank_test

def logrankgene(file, gene, interval, status):
    if file[gene].nunique() != 2:
        print('As the factor', gene, 'is non-binary, the Logrank statistics is not calculated.')
    else:
        interval_0 = []
        group_0 = file[file[gene] == 0]
        for i in group_0[interval]:
            interval_0.append(i)
        T = interval_0

        interval_1 = []
        group_1 = file[file[gene] == 1]
        for i in group_1[interval]:
            interval_1.append(i)
        T1 = interval_1
    
        censor_0 = []
        for j in group_0[status]:
            censor_0.append(j)
        E = censor_0

        censor_1 = []
        for k in group_1[status]:
            censor_1.append(k)
        E1 = censor_1
        results = logrank_test(T, T1, E, E1)
        if results.p_value >= 0.05:
            print('Log-rank for', gene,' gives p-value at: ', results.p_value)
        else:
            print('Log-rank for', gene,' gives p-value at: ', results.p_value, '**')

#file <- A table of genevariant (binary) 
def batchlogrank(file, genelist, interval, status):
    for i in genelist:
        logrankgene(file, i, interval, status)
        
#St_Jude gene sets for pediatric cancers

tyr_kinase = ['FLT3', 'ABL1', 'KIT', 'ALK', 'PDGFRA']
ras = ['NRAS', 'KRAS', 'PTPN11', 'NF1', 'BRAF', 'NF2', 'RIT1']
pi3k = ['PTEN', 'PIK3R1', 'AKI1', 'PIK3CD', 'FGFR1', 'PDFGRB', 'PIK3CA', 'TSC2', 'ATM', 'TSC1']
jak_stat = ['JAK3', 'JAK2', 'CRLF2', 'IL7R', 'CBL', 'PTPN2', 'STAT5B', 'JAK1', 'CSF3R', 'SH2B3', 'EPOR', 'XPO1']
notch = ['NOTCH', 'FBXW7'] 
wnt = ['CTNNB1', 'AMER1', 'APC']
mirna = ['DROSHA', 'DGCRB', 'XPO5']
myc = ['MYCN', 'MGA', 'MYC', 'MAX', 'TRRAP']
transcription = ['TAL1', 'IKZF1', 'PAX5', 'ETV6', 'RUNX1',
'WT1', 'LEF1', 'MYB', 'BCL11B', 'CBFB',
'TCF3', 'TLX3', 'LMO2', 'NUP98', 'EBF1',
'MLLT1', 'ERG', 'NKX2-1', 'TCF7', 'ZNF384',
'XBP1', 'TBL1XR1', 'GATA2', 'CNOT3', 'MED12',
'HOXA10', 'CEBPA', 'ELF1', 'GATA3', 'ZNF217',
'MEF2D', 'ZBTB7A', 'ZFP36L2', 'TAL2', 'NR3C1', 
'TSPYL2', 'EWSR1', 'GLIS2', 'LMO1', 'SIX1',
'NR3C2', 'UBTF', 'IKZF3', 'ELF4', 'IKZF2', 
'SIX2', 'GATA1', 'FLI1', 'DUX4', 'GATA4',
'GON4L', 'MEF2C', 'ZEB2', 'LYL1', 'FEV',
'ETS2'] 
cell_cycle = ['CDKN2A', 'TP53', 'RB1', 'CDKN1B', 'BTG1', 'TERT', 'CCND3', 'CDKN2B', 'NPM1', 'CDK6', 'CCND2', 'CDK4']
cohesin = ['STAG2', 'NIPBL', 'SMC3', 'PDS5B', 'STAG1', 'PDS5A', 'RAD21']
epigen = ['PHF6', 'KMT2A', 'CTCF', 'ATRX', 'CREBBP',
'KDM6A', 'EXH2', 'SETD2', 'SUZ12', 'ASXL2',
'EP300', 'TOX', 'KMT2D', 'SMARCA4', 'BCOR',
'ASXL1', 'EED', 'BCORL1', 'ARID2', 'BAZ1A',
'TET2', 'ARID1A', 'WHSC1', 'ATF7IP', 'MLLT4',
'NCOR1', 'KDM5A', 'HDAC7', 'NSD1', 'KMT2E',
'KMT2C', 'CHD4', 'DNMT3A', 'KDM5C', 'HIST1H3C',
'PBRM1', 'CHD7', 'TET3', 'KMT2B', 'HDA39']
st_jude = tyr_kinase + ras + pi3k + jak_stat + notch + wnt + mirna + myc +transcription + cell_cycle + cohesin + epigen

drugable = ['AKT1', 'ALK', 'ARAF', 'ARID1A', 'ATM', 'BARD', 'BRAF'
'BRCA1', 'BRCA2', 'BRIP', 'CDK4', 'CDK12', 'CDKN2A', 'CHEK1', 'CHEK2'
'EGFR', 'ERBB2', 'ERCC2', 'FGFR3', 'FLI1', 'HRAS'
'IDH1', 'KDM6A', 'KIT', 'KRAS', 'MAP2K1', 'MDM2',
'MET', 'MTOR', 'NF1', 'NRAS', 'NRG1', 'NTRK1', 'NTRK2', 'NTRK3'
'PALB2', 'PDGFB', 'PDGFRA', 'PIK3A', 'PTCH1', 'PTEN', 'RAD51B'
'RAD51C', 'RAD51D', 'RAD54L', 'RET', 'ROS1', 'SMARCB1', 'STK11', 'TSC1', 'TSC2']


NB_M = ['A015', 'A028', 'A035', 'A040','A045', 
        'A049', 'A058', 'A074', 'A075','A096',
        'A112', 'A131', 'A140', 'A166','A174',
        'A197', 'A234', 'A241', 'A248','A254',
        'A279', 'A292', 'A297', 'A303','A309',
        'A330', 'A374', 'A398', 'A400','A402',
        'A404', 'A410', 'A412', 'A420','A424',
        'A434', 'A442', 'A461', 'A462','A465',
        'A474', 'A492', 'A497', 'A505','A518',
        'A520', 'A535', 'A539',]
NB = ['A015', 'A028', 'A035', 'A040', 'A044',
      'A045', 'A049', 'A058', 'A074', 'A075',
      'A096', 'A112', 'A131', 'A140', 'A166',
      'A174', 'A197', 'A234', 'A241', 'A248',
      'A254', 'A279', 'A292', 'A297', 'A303',
      'A309', 'A321', 'A330', 'A362', 'A374',
      'A398', 'A400', 'A402', 'A404', 'A410',
      'A412', 'A420', 'A424', 'A434', 'A439',
      'A442', 'A461', 'A462', 'A465', 'A474',
      'A492', 'A497', 'A505', 'A518', 'A520',
      'A535', 'A539', 'A543']
WT = ['A008', 'A012', 'A018', 'A020', 'A021',
      'A025', 'A031', 'A048', 'A055', 'A060',
      'A085', 'A090', 'A095', 'A099', 'A158',
      'A159', 'A171', 'A201', 'A202', 'A203', 
      'A211', 'A212', 'A231', 'A232', 'A243',
      'A255', 'A265', 'A280', 'A290', 'A306',
      'A316', 'A334', 'A342', 'A372', 'A382',
      'A414', 'A452', 'A453', 'A458', 'A491',
      'A494', 'A529', 'A101']
OTH =['A235', 'A376', 'A406', 'A251', 'A320'
	  'A338']

ALL = NB + WT + OTH