import argparse
import os
from collections import OrderedDict

import numpy as np
import pandas as pd


def read_fasta_to_dic(filename):
    """
    function used to parser small fasta
    still effective for genome level file
    """
    fa_dic = OrderedDict()

    with open(filename, "r") as f:
        for n, line in enumerate(f.readlines()):
            if line.startswith(">"):
                if n > 0:
                    fa_dic[short_name] = "".join(seq_l)  # store previous one

                full_name = line.strip().replace(">", "")
                short_name = full_name.split(" ")[0]
                seq_l = []
            else:  # collect the seq lines
                if len(line) > 8:  # min for fasta file is usually larger than 8
                    seq_line1 = line.strip()
                    seq_l.append(seq_line1)

        fa_dic[short_name] = "".join(seq_l)  # store the last one
    return fa_dic


def extract_tombo(ab_path, fasta_path):
    tombo_result_minus_path = ab_path + ".minus.wig"
    tombo_result_plus_path = ab_path + ".plus.wig"

    ref_dict = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    def read_tombo_results(path):
        result_table = []
        f = open(path, 'r')
        chrome = None
        for line in f:
            if line[0:5] == 'track':
                continue
            if 'chrom' in line:
                chrome = line.split(' ')[1].split('=')[1]
            else:
                static_list = line[:-1].split(' ')
                result_table.append([chrome, static_list[0], static_list[1]])
            if chrome is None:
                raise RuntimeError("Error")

        df = pd.DataFrame(result_table)
        # df = df[df[1]>=0.2]
        df[1] = df[1].astype(int)
        df[2] = df[2].astype(float)
        df.insert(loc=2, column="A1", value=df[1].values + 1)
        df.insert(loc=3, column="A2", value=np.repeat([["."]], df.shape[0]))
        df.insert(loc=4, column="A3", value=np.repeat([["."]], df.shape[0]))
        # sns.displot(df, x=1)
        # plt.show()
        if path.find("plus") != -1:
            # df = df[df[2] == "A"]
            df.insert(loc=5, column="A4", value=np.repeat([["+"]], df.shape[0]))
        else:
            # df = df[df[2] == "T"]
            df.insert(loc=5, column="A4", value=np.repeat([["-"]], df.shape[0]))
        df.columns = [0, 1, 2, 3, 4, 5, 6]
        return df

    plus_df = read_tombo_results(tombo_result_plus_path)
    try:
        minus_df = read_tombo_results(tombo_result_minus_path)
    except Exception:
        minus_df = None
    all_df = pd.concat([plus_df, minus_df], ignore_index=True)
    print('Start to add the nucleotide information from reference sequence ...')
    fasta = read_fasta_to_dic(fasta_path)

    all_df['ref'] = all_df.apply(lambda x: fasta[x[0]][x[1]] if x[5] == '+' else ref_dict[fasta[x[0]][x[1]]], axis=1)

    all_df.columns = ['chrome', 'start', 'end', '.', '..', 'strand', 'value', 'ref']
    return all_df


def main(args):
    result_path = args.output
    tombo_path = args.tombo_result
    fasta_path = args.ref
    if os.path.exists(result_path):
        print("Result file existed, will be overwrite")
    print("Start to loading tombo result . . .")
    tombo_result = extract_tombo(tombo_path, fasta_path)
    tombo_result.to_csv(result_path, sep='\t', index=False)
    print("Finished !")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', "--tombo_result", default='sample', help="suffix of tombo result")
    parser.add_argument("--ref", default='reference file', help='reference path')
    parser.add_argument("--output", default='tombo.bed', help='output path')
    args = parser.parse_args()
    main(args)

