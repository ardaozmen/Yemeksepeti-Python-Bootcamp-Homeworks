import csv
import os.path
import pandas as pd
from csv import writer

class FileTool:
    
    def __init__(self, path, fields = [], *args):
        self.path = path
        self.fields = fields
        
    def isFileExist(self):
        '''
        - checks the file path. 
        - returns a boolean value.
        '''
        return os.path.exists(self.path)
    
    def createNewFile(self):
        '''
        - If there is no file matching the format in the path, 
        - it creates a new file.
        '''
        isFile = self.isFileExist()
        if isFile == True:
            print("No need to create new file! File is exist.")
        elif isFile == False:
            with open(path, 'w', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(self.fields)

    def toJson(self):
        '''
        - Converts csv file to json format.
        '''
        with open(self.path, 'r') as file_csv:
            reader = csv.DictReader(file_csv)
        with open('{}'.format(path.split('.')[0]+'.json'), 'w') as file_json:
            for row in reader:
                json.dump(row, file_json)

    def searchData(self): 
        '''
        - Prints the data containing the searched word.
        '''
        search_ = input("Search a dataframe value: ")
        with open(self.path, 'r') as f:
            for line in f.readlines():
                if search_ in line:
                    print(line)
    
    def displayJsonLine(self):
        '''
        - Displays the searched data in json format.
        - It is a different version of the searchData function.
        '''
        search_ = input("Search a dataframe value: ")
        with open(path, 'r') as f:
            for headers in f.readlines(1):
                headers = headers.split(',')
            for line in f.readlines():
                if search_ in line:
                    res = {}
                    elems = line.split(',')
                    for key in headers:
                        for value in elems:
                            res[key] = value
                            elems.remove(value)
                            break
                    print(res)

    def appendData(self):
        '''
        - Adds new data to the data in a new row.
        '''
        appended_ = [item for item in input("Enter the data with comma: ").split(',')]
        with open(self.path, 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(appended_)
            f_object.close()

    def deleteData(self):
        '''
        - Deletes the desired data.
        '''
        deleted_ = input("Enter a deleted what you want: ")
        with open(self.path, "r") as f_object:
                lines = f_object.readlines()
        with open(self.path, "w") as f_object:
            for line in lines:
                if line.strip("\n") != deleted_:
                    f_object.write(line)

    def updateData(self):
        '''
        - Updates the desired data.
        '''
        old_data = input("Enter old data: ")
        new_data = input("Enter new data: ")
        f_obj1 = open(self.path,'r')
        f_obj1 = ''.join([i for i in f_obj1]).replace(old_data, new_data)
        f_obj2 = open(self.path,'w')
        f_obj2.writelines(f_obj1)
        f_obj2.close()
        
    def mergeFiles(self,frames=[]):
        # frames=['innovators.csv','deneme.csv','deneme2.csv']
        '''
        - This Function takes as parameter the csv files that you want to combine as a list.
        '''
        myDataFrame = pd.DataFrame()
        for df in frames:
            myDataFrame = myDataFrame.append(pd.read_csv(df))
            myDataFrame.to_csv('merged.csv',index=False)
        
    def Menu(self):
        '''
        Press [1] to search data,
        Press [2] to append data,
        Press [3] to delete data,
        Press [4] to update data,
        Press [5] to create new file,
        Press [6] to quit the program,
        '''
        while True:
            select_ = input("Press [1] to search data,\nPress [2] to append data,\nPress [3] to delete data,\nPress [4] to update data,\nPress [5] to create new file,\nPress [6] to quit the program,\nSelect the action you want to do: ")
            if select_ == '1':
                self.searchData()
            elif select_ == '2':
                self.appendData()
            elif select_ == '3':
                self.deleteData()
            elif select_ == '4':
                self.updateData()
            elif select_ == '5':
                self.createNewFile()
            elif select_ == '6':
                break

path = 'innovators.csv'
ft = FileTool(path, fields=['Name', 'Contribution'])
ft.Menu()