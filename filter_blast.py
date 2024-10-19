import sys,os
from collections import defaultdict



def filter_blast(blast_out, fasta):
    dic_ref = {}
    prefix = blast_out.split("/")[-1].split(".")[0]
    out1 = open(f"{prefix}_stat_count.xls", "w")
    out2 = open(f"{prefix}_filter_result.blast.out.xls", "w")
    seq = "seq"
    name = "name"
    for line in open(fasta):
        if line.startswith('>'):
            dic_ref[name] = seq
            name = line.strip().split()[0][1:]
            seq = ""
        else:
            seq += line
    dic_ref[name] = seq

    dic = {}
    dicinfo = defaultdict(dict)
    for i in open(blast_out,'r').readlines():
        tmp = i.strip().split()
        blast_length = int(tmp[3])
        gene = tmp[1]
        mismatch = tmp[5]
        gap = tmp[6]
        total = int(mismatch) + int(gap)
        info = f"{blast_length}\t{mismatch}\t{gap}"
        if blast_length >= 17 and blast_length - total >= 15:
            dicinfo[gene][i] = info
            if gene not in dic:
                dic[gene] = 1
            else:
                dic[gene] += 1
    for k in dic.keys():
        out1.write(f"{k}\t{dic[k]}\t{dic_ref[k]}\n")
    for key in dicinfo.keys():
        for line in dicinfo[key].keys():
            out2.write(line)


if __name__ == '__main__':
    blast_out = sys.argv[1]
    fasta= sys.argv[2]
    filter_blast(blast_out, fasta)