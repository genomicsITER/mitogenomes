#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Usage example (for python3): python bootstrap_rho.py MT_Alignment_H1cf_boot3600.phy

from csv import reader
import csv
import os
import sys

def hamming_distance(seq1, seq2):
    distance = 0
    L = len(seq1)
    for i in range(L):
        if seq1[i] != seq2[i]:
            distance += 1
    return distance

def distance_matrix(sequences):
    mat = [None] * len(sequences)
    for i in range(0, len(sequences)):
        mat[i] = list()
        for j in range(0, len(sequences)):
            if i != j:
                mat[i].append(hamming_distance(sequences[i], sequences[j]))
            else:
                mat[i].append(0)
    return mat

def count_frequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

def main():
    # Input file:
    # phy file compiling the following format:
    # 39 16569
    # CANIS0XXX_ GTCACGGTTT CTTCACTTAA ACCAACCAAG GCCTCTTTTC CGTGGAAATT TGTGGGGTGT
    #            CCCAAAAACC TTGGAGGGCC TGGAAGGCCG AGGCAACCCT GGGCAGTATC GATTCCTCCA
    # ...
    infile = sys.argv[1]

    print("******************")
    print("Reading sequences*")
    print("****************+*")

    with open(infile, 'r') as read_obj:
        csv_reader = reader(read_obj, delimiter=" ")
        seqs = list()
        current_seq = 0
        matrices = list()
        for row in csv_reader:
            contents = [r for r in row if r != '']
            if len(contents) == 2:
                num_seq = int(contents[0])
                size_seq = int(contents[1])
                seqs = ['' for x in range(0, num_seq)]
                current_seq = 0
                print("Processing new replica...")
                continue
            if len(contents) == 7:
                print("Processing sequence from sample: {}...".format(contents[0]))
                seqs[current_seq] = ''.join(map(str, contents[1:]))
            else:
                seqs[current_seq] = seqs[current_seq] + ''.join(map(str, contents))

            if len(seqs[current_seq]) == size_seq:
                if current_seq == (num_seq - 1):
                    matrices.append(distance_matrix(seqs))
                current_seq = current_seq + 1

    print("\n*****************")
    print("*Hamming matrices*")
    print("******************")
    print(matrices)

    outfile = os.path.splitext(infile)[0] + ".csv"
    base = os.path.basename(outfile)
    # extract haplogroup name from input file
    haplogroup = base.split("_")[2]

    print("\n*******")
    print("*Counts*")
    print("********")

    i_max = None
    max = 0
    counts = {}
    with open(outfile, 'w') as f:
        writer = csv.writer(f, delimiter=';')

        for matrix in matrices:
            max = 0
            for i in range(0, len(matrix)):
                num_ceros = matrix[i].count(0)
                if num_ceros > max:
                    i_max = i
                    max = num_ceros
            freqs = count_frequency(matrix[i_max])
            print("Counts for the replica: {}".format(freqs))
            res = 0
            for number in freqs.keys():
                res = res + number*freqs[number]

            writer.writerow([haplogroup,res/len(matrix)*1400])

    print("\nThe results have been stored in: {}\n".format(outfile))

if __name__ == "__main__":
    main()
