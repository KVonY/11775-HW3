val = open('/home/ubuntu/11775-hws-MED3/all_val.lst', 'r')
P001 = open('list/P001_val_label', 'w')
P002 = open('list/P002_val_label', 'w')
P003 = open('list/P003_val_label', 'w')
NULL = open('list/NULL_val_label', 'w')

for i in val:
    video_name, label = i.strip().split(' ')
    if label == 'P001':
        P001.write('1\n')
        P002.write('0\n')
        P003.write('0\n')
        NULL.write('0\n')
    elif label == 'P002':
        P001.write('0\n')
        P002.write('1\n')
        P003.write('0\n')
        NULL.write('0\n')
    elif label == 'P003':
        P001.write('0\n')
        P002.write('0\n')
        P003.write('1\n')
        NULL.write('0\n')
    elif label == 'NULL':
        P001.write('0\n')
        P002.write('0\n')
        P003.write('0\n')
        NULL.write('1\n')
    else:
        print('Invalid label.\n')
P001.close()
P002.close()
P003.close()
NULL.close()