import sys,os


def filter_blast(blast_out, length):
    dic = {}
    for i in open(blast_out,'r').readlines():
        tmp = i.strip().split()
        blast_length = int(tmp[3])
        gene = tmp[2]
        if blast_length == length:
            if gene not in dic:
                dic[gene] = 1
            else:
                dic[gene] += 1
    for k in dic.keys():
        print(f"k:{dic[k]}")


if __name__ == '__main__':
    blast_out = sys.argv[1]
    length = int(sys.argv[2])
    filter_blast(blast_out, length)