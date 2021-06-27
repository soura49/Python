import csv
from tempfile import NamedTemporaryFile
import shutil





def update_new_user():
    filename = '/Users/balakrishnasoura/Desktop/boto3/exported_users.csv'

    tempfile = NamedTemporaryFile(mode='w',delete=False)
    with open(filename,'r') as csv_file,tempfile:
        csv_reader = csv.reader(csv_file)
        csv_writer = csv.writer(tempfile)
        for line in csv_reader:
            if line[0] != 'First Name':
                line[3] = 'balathegreat'+ line[0]
                print[line[3]]
            csv_writer.writerow(line)

    shutil.move(tempfile.name,filename)

    
