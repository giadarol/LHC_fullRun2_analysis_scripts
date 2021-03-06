import os
import sys, time
sys.path.append("../")

import LHCMeasurementTools.lhc_log_db_query as lldb
import LHCMeasurementTools.LHC_Heatloads as HL
from data_folders import data_folder_list

import pickle
import numpy as np

csv_folder = 'fill_heatload_data_csvs'
if not os.path.isdir(csv_folder):
    os.mkdir(csv_folder)



if len(sys.argv) > 1:
     filln = int(sys.argv[1])


dict_fill_bmodes={}
for df in data_folder_list:
    with open(df+'/fills_and_bmodes.pkl', 'rb') as fid:
        this_dict_fill_bmodes = pickle.load(fid)
        for kk in this_dict_fill_bmodes:
            this_dict_fill_bmodes[kk]['data_folder'] = df
        dict_fill_bmodes.update(this_dict_fill_bmodes)

t_start_fill = dict_fill_bmodes[filln]['t_startfill']
t_end_fill = dict_fill_bmodes[filln]['t_endfill']


sector_list = HL.sector_list()
variable_list = HL.sector_all_variables(sector_list)
#variable_list=['CMS:LUMI_TOT_INST','S12_QBS_AVG_ARC.POSST']

fill_file = csv_folder + '/hl_all_cells_fill_%d.csv'%filln

lldb.dbquery(variable_list, t_start_fill, t_end_fill, fill_file)
