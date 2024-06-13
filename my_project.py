
import pandas as pd

class data_create():
    def __init__(self,Input):

        self.dataset = pd.read_csv(Input)
        self.Status_name = 'Status'
        self.Gender_column = 'GENDER'
        self.Age_column  = 'AGE'
        self.Income_column = 'INCOME'
        self.Region_column = 'REGION'
        self.Ethnic_column = 'ETHNICITY'
        self.Hispanic_column = 'CORE_ACCULTURATION_0001'


        #print(self.dataset)

        self.x_status = None
        self.x_gender = None
        self.x_age = None
        self.x_income = None
        self.x_region = None
        self.x_ethnic = None
        self.x_hisp= None


    def data_columns(self):
        if self.Status_name in self.dataset.columns:
            self.x_status = self.dataset[self.Status_name]
        if self.Gender_column in self.dataset.columns:
            self.x_gender = self.dataset[self.Gender_column]
        if self.Age_column in self.dataset.columns:
            self.x_age = self.dataset[self.Age_column].apply(pd.to_numeric,errors = 'coerce').fillna(-1).astype(int)
        if self.Income_column in self.dataset.columns:
            self.x_income = self.dataset[self.Income_column]
        if self.Region_column in self.dataset.columns:
            self.x_region = self.dataset[self.Region_column]
        if self.Ethnic_column in self.dataset.columns:
            self.x_ethnic = self.dataset[self.Ethnic_column]
        if self.Hispanic_column in self.dataset.columns:
            self.x_hisp = self.dataset[self.Hispanic_column]

        # age bracket counts


        # if x_status is None or x_gender is None:
        #  print("Required columns 'Status' and 'GENDER' not found in the dataset.")
        #  return

    def status(self):

        self.data_columns()
        gender_counter_male = 0
        gender_counter_female = 0

        for i in range(len(self.dataset)):
            status = self.x_status.iloc[i]

            gender = self.x_gender.iloc[i]

            if status == 'Completed' and gender == 'Male':
                gender_counter_male += 1
            elif status == 'Completed' and gender == 'Female':
                gender_counter_female += 1

        print('Male : ', gender_counter_male)
        print('Female : ', gender_counter_female)
        print('total count is ', gender_counter_male+gender_counter_female)
        print()


class age_data(data_create):

    def age(self):
        self.data_columns()
        age_18_24 = 0
        age_25_34 = 0
        age_35_44 = 0
        age_45_54 = 0
        age_55_64= 0
        age_65_ = 0


        for i in range(len(self.dataset)):
            age = self.x_age.iloc[i]

            status = self.x_status.iloc[i]



            if status =='Completed':

                if age == -1:
                    continue

                if  18<= age <= 24:
                    age_18_24 +=1
                if 25 <= age <= 34:
                    age_25_34 += 1
                if 35 <= age <= 44:
                    age_35_44 += 1
                if 45 <= age <= 54:
                    age_45_54 += 1
                if 55 <= age <= 64:
                    age_55_64 += 1
                if age >= 65:
                    age_65_ += 1


        print('18-24 : ', age_18_24)
        print('25-34 :', age_25_34)
        print('35-44 : ', age_35_44)
        print('45-54 : ', age_45_54)
        print('55-64 : ', age_55_64)
        print('65+ : ', age_65_)

        print('Total age count is ',age_65_+ age_55_64+age_45_54+age_35_44+age_25_34+age_18_24)
        print()




class ethnic_data(data_create):
    '''        if self.Ethnic_column in self.dataset.columns:
                self.x_ethnic = self.dataset[self.Ethnic_column]
            if self.Hispanic_column in self.dataset.columns:
                self.x_hisp = self.dataset[self.Hispanic_column]'''

    def ethnic(self):
        self.data_columns()

        #ethnicVariable

        White = 0
        AA = 0
        Hispanic = 0
        Asian = 0
        Other = 0

        for i in range(len(self.dataset)):
            status = self.x_status.iloc[i]
            ethnic = self.x_ethnic[i]
            hispanic = self.x_hisp[i]


            if status == 'Completed':
                if hispanic == 'No' or hispanic == 'Prefer not to answer':

                    if (ethnic == 'American Indian or Alaska Native' or ethnic == 'Pacific Islander - Gaumanian'
                            or ethnic == 'Pacific Islander - Native Hawaiian' or ethnic == 'Pacific Islander - Other Pacific Islander'
                            or ethnic == 'Some other race'):

                        Other += 1

                    if (ethnic == 'Asian - Asian Indian' or ethnic == 'Asian - Chinese' or ethnic == 'Asian - Filipino'
                        or ethnic == 'Asian - Japanese' or ethnic == 'Asian - Korean'  or ethnic == 'Asian - Vietnamese'
                            or ethnic == 'Asian - Other'):

                        Asian +=1

                    if (ethnic == 'Black or African American'):
                        AA +=  1

                    if ethnic == 'White':
                        White += 1

                else:
                    Hispanic +=1


        print('White : ', White)
        print('AA : ', AA)
        print('Asian : ', Asian)
        print('Hispanic :', Hispanic)
        print('Other : ', Other)

        print('Total Ethnic count is ' ,White + AA + Asian + Hispanic + Other)
        print()



































Input = r"C:\Users\prabi\Downloads\Question_Report_Job_1717766797636.csv"

gender = data_create(Input)
gender.status()

age = age_data(Input)
age.age()

ethnic = ethnic_data(Input)
ethnic.ethnic()











