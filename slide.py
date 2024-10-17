import sys,os
import argparse
def slide_window(infasta,outfasta,slide_size):
    ini = open(infasta,'r')
    out = open(outfasta,'w')
    dict_fa = {}
    seq = 'seq'
    name = 'name'
    seq_list = []
    for i in ini:
        if i.startswith('>'):
            dict_fa[name] = seq
            name = i.strip()[1:]
            seq_list.append(name)
            seq = ''
        else:
            seq = seq + i.strip()
    dict_fa[name] = seq
    slen = int(slide_size)
    for j in seq_list:
        seq = dict_fa[j]
        length = len(seq)
        print(length)
        end = length - int(slen) + 1
        for m in range(0,end):
            seq_name = '>' + j + '_' + str(m + 1) + '-' + str(m + slen)
            seq_bin = seq[m:m+slen]
            out.write(seq_name + '\n' + seq_bin + '\n')

def simple_blast(queryfasta, subjectfasta, slide_size):
    dbprefix = subjectfasta.split('/')[-1].split('.')[0]
    queryprefix = queryfasta.split('/')[-1].split('.')[0]
    cmd = f"makeblastdb -dbtype nucl -in {subjectfasta} -out {dbprefix} -hash_index -parse_seqids\n"
    cmd += f"blastn -db {dbprefix} -query {queryfasta} -out {queryprefix}_{dbprefix}_{slide_size}.blast.out -outfmt 6 -task blastn-short -word_size 7 -evalue 1\n"
    os.system(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="this is a script for seperate sequence with sliding window....")
    parser.add_argument("-i", help="input fasta file name", required=True, dest = "i")
    parser.add_argument("-f", help="input db fasta file name", required=True, dest="f")
    parser.add_argument("-w", help="window size", required=True, dest="w")
    parser.parse_args()
    args = parser.parse_args()
    infasta = args.i
    dbfasta = args.f
    slide_size = args.w
    outfasta = f"{args.i}_{args.f}_{slide_size}.fasta"
    slide_window(infasta,outfasta,slide_size)
    simple_blast(outfasta, dbfasta, slide_size)