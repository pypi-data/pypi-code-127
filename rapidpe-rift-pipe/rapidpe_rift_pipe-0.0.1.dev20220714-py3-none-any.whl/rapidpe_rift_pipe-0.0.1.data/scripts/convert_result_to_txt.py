#!python

###############################
# 20190508
#
# author: Sinead Walsh
# 
# At some point this will be used to read the all the results for an event, and output the text file with the marg ll per event, 
# and the text file with the extrinsic parameters and ll for the loudest x intrinsic grid points. 
#
# For now It jus reads in margll.txt, takes the loudest file, reads the samples file for that, and outputs it to a text file
#
# Commands are:
# convert_result_to_txt.py <path_to_event_dir> 
#
#############################


import sys,types,math,itertools,glob,scipy,time

import os
module_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(module_dir)
from optparse import OptionParser
from collections import defaultdict

import numpy as np

from glue.ligolw import utils, table, lsctables, ligolw
lsctables.use_in(ligolw.LIGOLWContentHandler)
from glue.lal import Cache

from rapid_pe import xmlutils, amrlib, lalsimutils
from multiprocessing import Pool
from rapidpe_rift_pipe import modules

input_dir = sys.argv[1]

#remove the color codes, because for whatever reason they're included on uwm.
input_dir = input_dir.replace("\x1b[0m","")
input_dir = input_dir.replace("\x1b[01;34m","")
input_dir = input_dir.replace("\x1b[K","")



ratio_to_include = float(sys.argv[2])

level=""
if len(sys.argv) > 3:
    level = sys.argv[3]

print ("LEVEL",level)
#event_info_str = open(input_dir+"/event_info_dict.txt","r").readlines()[0]
#event_info = convert_dict_string_to_dict(event_info_str)

output_dir = input_dir+"/"
#print "SYSARGV",output_dir
#sys.exit()
#output_dir = "tmp/"
results_dir = input_dir+"/results/"

margll_summary_filename = output_dir+"/margll"+level+".txt"
#in v2, we exclude candidates with very low weights
ll_loudest_filename = output_dir+"/ll_samples_loudest_"+str(ratio_to_include).replace(".","p")+level+".txt"
ll_loudest_filename_highweight = output_dir+"/ll_samples_loudest_highweight_"+str(ratio_to_include).replace(".","p")+level+".txt"
read_log_info = 0
log_info_filename = output_dir+"/log_files_summary"+level+".txt"
force_reread = 0

def main():

    
    '''
    Read rapidPE results. output to txt file.
    Separate text file for 
    - margll per intrinsic point
    - ll per extrinsic points for loudest intrinsic points
    - info from log files e.g. neff 
    '''


    input_files = []
    if level=="":
        input_files = glob.glob(results_dir+"/ILE_iteration_*.xml.gz")
    else:
        print ("WARNING: loading only level",level)
        input_files = glob.glob(results_dir+"/ILE_iteration_"+level+"*.xml.gz")
    print (len(input_files),"files in results directory.",results_dir)


    #Check if the margll file contains all results, if not, reread margll data
    margll = {}
    reread_margll = 1
    if os.path.isfile(margll_summary_filename) and not force_reread:
        #if the margll from each file has already been written to a text file, read the text file
        margll = np.atleast_1d(np.genfromtxt(margll_summary_filename,unpack=True,names=True,dtype=None, encoding=None))
        
        if len(input_files) == len(margll["margll"])*2:
            reread_margll=0


    #Read margll for each intrinsic point
    if reread_margll:
        print ("REREADING MARGLL")
        margll_output_lines = "mass1 mass2 mchirp eta spin1z spin2z margll filename mass_set\n"
        for filename in input_files:
            if ".samples.xml.gz" in filename:
                continue
        
            print (filename)
            xmldoc = utils.load_filename(filename, contenthandler=ligolw.LIGOLWContentHandler)
            #FIXME: can I tell from lsctables.SnglInspiralTable.get_table if it's samples or not?
            new_tbl = lsctables.SnglInspiralTable.get_table(xmldoc)
            
            #Transform input mass parameters to parameters I want to plot
            for row in new_tbl:
                row.mchirp, row.eta = amrlib.transform_m1m2_mceta(row.mass1, row.mass2)
                margll_output_lines += str(row.mass1)+" "+str(row.mass2)+" "+str(row.mchirp)+" "+str(row.eta)+" "+str(row.spin1z)+" "+str(row.spin2z)+" "+str(row.snr)+" "+filename+" "
                msi1 = filename[filename.rfind("MASS_SET_")+9:]
                mass_set_id = msi1[:msi1.find("-")]
                margll_output_lines+=mass_set_id+"\n"


            xmldoc.unlink()

        fo = open(margll_summary_filename,"w")
        fo.write(margll_output_lines)
        fo.close()
        print ("Intrinsic params margll summary written to ",margll_summary_filename)

    #now read it back in to find the loudest filenaems
    margll = np.atleast_1d(np.genfromtxt(margll_summary_filename,unpack=True,names=True,dtype=None, encoding=None))

    if os.path.isfile(ll_loudest_filename) and not reread_margll and not force_reread:
        sys.exit("Skipping file already read")

    #Extrinsic params
    #Figure out which indices belong to the intrinsic points wiht the highest likelihood
    #Read the samples files for these and save the likelihoods calculated for the extrinsic parameters
    max_margll = max(margll["margll"])
    loudest_indices = np.where(margll["margll"] >= ratio_to_include*max_margll)[0] if len(margll["margll"]) > 1 else [0]
#    loudest_indices = np.where(margll["margll"] >= 0.01)[0]
    loudest_filenames = margll["filename"][loudest_indices]
    samples_output_lines = "mass1 mass2 mchirp eta spin1z spin2z distance latitude longitude inclination phase polarization likelihood prior sampling_function\n"
    print ("Loudest files",len(loudest_filenames),"\n",loudest_filenames)
    all_lls = []
    for filename in loudest_filenames:
        samples_filename = filename.replace(".xml.gz",".samples.xml.gz")

        xmldoc = utils.load_filename(samples_filename, contenthandler=ligolw.LIGOLWContentHandler)
        new_tbl = lsctables.SimInspiralTable.get_table(xmldoc)

        
        #Transform input mass parameters to parameters I want to plot
        for row in new_tbl:
            row.mchirp, row.eta = amrlib.transform_m1m2_mceta(row.mass1, row.mass2)
            
            all_lls.append(row.alpha1)
            samples_output_lines += str(row.mass1)+" "+str(row.mass2)+" "+str(row.mchirp)+" "+str(row.eta)+" "+str(row.spin1z)+" "+str(row.spin2z)+" "+str(row.distance)+" "+str(row.latitude)+" "+str(row.longitude)+" "+str(row.inclination)+" "+str(row.coa_phase)+" "+str(row.polarization)+" "+str(row.alpha1)+" "+str(row.alpha2)+" "+str(row.alpha3)+"\n"

#    print ("Extrinsic params ll for loudest margll summary written to ",ll_loudest_filename)
    print ("Extrinsic params ll for loudest margll summary No longer written to ",ll_loudest_filename,"to avoid excessively large files, only highweight written")
#    fo = open(ll_loudest_filename,"w")
#    fo.write(samples_output_lines)
#    fo.close()
#    os.system("wc -l "+ll_loudest_filename)


    #reread everything. This time, exclude those with low weights.
    maxlnl = max(all_lls)
    samples_output_lines = "mass1 mass2 mchirp eta spin1z spin2z distance latitude longitude inclination phase polarization likelihood prior sampling_function weight\n"
    for filename in loudest_filenames:
        samples_filename = filename.replace(".xml.gz",".samples.xml.gz")

        xmldoc = utils.load_filename(samples_filename, contenthandler=ligolw.LIGOLWContentHandler)
        new_tbl = lsctables.SimInspiralTable.get_table(xmldoc)
        
        #Transform input mass parameters to parameters I want to plot
        for row in new_tbl:
            row.mchirp, row.eta = amrlib.transform_m1m2_mceta(row.mass1, row.mass2)
            
            #alpha1=log likelihood. alpha2 = prior. alpha3 = sampling_function
            weight = (np.exp(row.alpha1- maxlnl)*row.alpha2)/row.alpha3
            if weight < 1e-7:
                continue

            samples_output_lines += str(row.mass1)+" "+str(row.mass2)+" "+str(row.mchirp)+" "+str(row.eta)+" "+str(row.spin1z)+" "+str(row.spin2z)+" "+str(row.distance)+" "+str(row.latitude)+" "+str(row.longitude)+" "+str(row.inclination)+" "+str(row.coa_phase)+" "+str(row.polarization)+" "+str(row.alpha1)+" "+str(row.alpha2)+" "+str(row.alpha3)+" "+str(weight)+"\n"

    print ("Extrinsic params ll for loudest margll summary, excluding low weight samples, written to ",ll_loudest_filename_highweight)
    fo = open(ll_loudest_filename_highweight,"w")
    fo.write(samples_output_lines)
    fo.close()
    os.system("wc -l "+ll_loudest_filename_highweight)


    #Read in the log information, and save it
    if read_log_info and (reread_margll or force_reread or not os.path.isfile(log_info_filename)):
        log_info={"neff":[],"per_point_time":[]}
        log_summary_lines = "neff per_point_time mass_set\n"
        for filename in input_files:
            if ".samples.xml.gz" in filename:
                continue

            #Read in the corresponding log file
            out_file_start = filename[:filename.rfind("results/")]
            out_file_end = filename[filename.rfind("ILE_iteration_")+15:-6]
            out_file = out_file_start+"logs/integrate"+out_file_end+"out"
            outlog = open(out_file,"r")
            start_time = end_time = -1
            for line in outlog:
                if "walltime : iteration Neff" in line:
                    start_time = 0
                    continue
                if start_time == 0:
                    start_time = float(line.split(" ")[0])
                    continue
                if start_time > 0 and not "lnLmarg is" in line and not "note neff" in line:
                    end_time = float(line.split(" ")[0])
                    continue
                if "note neff is" in line:
                    tmp1 = line.replace("note neff is","")
                    tmp2 = tmp1.replace("\n","")
                    log_summary_lines += str(tmp2.replace(" ",""))
#                    log_summary_lines += str(float(line.replace("note neff is","")))
            log_summary_lines += " "+str((end_time-start_time)/60.0)

            msi1 = filename[filename.rfind("MASS_SET_")+9:]
            mass_set_id = msi1[:msi1.find("-")]
            log_summary_lines+=" "+mass_set_id+"\n"

        print ("Log information written to ",log_info_filename)
        fo = open(log_info_filename,"w")
        fo.write(log_summary_lines)
        fo.close()


    return


if __name__ == '__main__':
    main()
