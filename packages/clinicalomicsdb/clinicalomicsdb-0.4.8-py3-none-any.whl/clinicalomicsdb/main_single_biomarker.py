""" ClinicalOmicsDB: Bridging the gap between next-generation clinical omics data and machine learning
Reference: Chang In Moon, Byron Jia, Bing Zhang
Paper link: TBD
Code author: Chang In Moon (moonchangin@gmail.com)
-----------------------------

USAGE:
$ python3 main_single_biomarker.py --gene NF1 --output NF1_clindb_significance.csv

output: list of database infomation with wilcoxon p-value across databases
"""
# Necessary packages
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
from datetime import datetime
import numpy as np
import pandas as pd
import os
from scipy.stats import mannwhitneyu

from database_download import download, biomarker_download_sheet


# define and edit parameters for supervised models
def main(args):
  """Main function for wilcoxon statistical testing.
  Returns:
  output: list of database infomation with wilcoxon p-value across databases
  """
  collection = biomarker_download_sheet()
  db_name = collection.iloc[:, 0]
  output_df = []
  for f in db_name:
      print("Testing " + f)
      db_info = collection.loc[collection['Series'] == f]
      url = db_info.iloc[0,6]
      
      temp_df = download(url)      
      temp_df = temp_df.dropna(axis='columns') # Remove genes with missing values
      y = temp_df.iloc[:, 1] # Response is on 2nd column
      try:
        # group_a = non_responders
        group_a = temp_df[temp_df.iloc[:, 1] == 0]
        # group_a = group_a.iloc[:, 2:] # expression data only
        gene =  args.gene
        group_a = group_a.loc[:, gene]
        
        # group_b = responders
        group_b = temp_df[temp_df.iloc[:, 1] == 1]
        # group_b = group_b.iloc[:, 2:] # expression data only
        group_b = group_b.loc[:, gene]
      except Exception:
        print("[WARNING] Skipping " + f + " because gene symbol " + gene + " cannot be found in this dataset")
        break # do not print or save results if the dataset do not have the gene symbol
      # wilcoxon test
      _ , p_value = mannwhitneyu(group_a, group_b, alternative="two-sided")
      # parse file name
      database_name = f[10:]
      database_name = database_name[:-4]
      test_eval = {'dataset': database_name,
        'sample_size': temp_df.shape[0],
        'feature_size': temp_df.shape[1] - 1,
        'responder_log_ratio': round(abs(np.log(y.sum()/(len(y)-y.sum()))),2),
        'platform': db_info.iloc[0,5],
        'cancer_type': db_info.iloc[0,1],
        'treatment_type': db_info.iloc[0,3],
        'response_evaluation': db_info.iloc[0,4],
        'wilcoxon_p_val': p_value
        }
      print(test_eval)
      output_df.append(test_eval)
  # save your final results
  df2 = pd.DataFrame(output_df)
  df2_sorted = df2.sort_values(by='wilcoxon_p_val', ascending=True)
  df2_sorted.to_csv(args.output)
  
if __name__ == '__main__':
  # Inputs for the main function
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--gene',
      help='Single gene symbol input',
      required=True)  
  parser.add_argument(
      '--output',
      help='name of the output file (default: clinicalomicsdb_output_[CURRENT_TIME].csv)',
      default="clinicalomicsdb_output_" + datetime.now().strftime("%H:%M:%S") + ".csv",
      type=str)
  
  args = parser.parse_args() 
  # Calls main function  
  main(args)