import csv
from tempfile import NamedTemporaryFile
import shutil
import datetime



def updated_email():
    email_prefix = "test"
    email_suffix = "@mailinator.com"
    today = datetime.datetime.now()
    date_time = today.strftime("%m%d%Y%H%M%S")
    return email_prefix+date_time+email_suffix


def update_new_user():
    filename = '/Users/balakrishnasoura/Desktop/boto3/exported_users.csv'

    tempfile = NamedTemporaryFile(mode='w',delete=False)
    with open(filename,'r') as csv_file,tempfile:
        csv_reader = csv.reader(csv_file)
        csv_writer = csv.writer(tempfile)
        for line in csv_reader:
            if line[0] != 'First Name':
                line[3] = updated_email()
                print(line[3])
            csv_writer.writerow(line)

    shutil.move(tempfile.name,filename)




update_new_user()
