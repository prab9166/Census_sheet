# Import necessary library
import pandas as pd

# Define a base class for data processing
class data_create():
    def __init__(self, Input):
        # Read the dataset from the provided input file path
        self.dataset = pd.read_csv(Input)
        
        # Define column names for reference
        self.Status_name = 'Status'
        self.Gender_column = 'GENDER'
        self.Age_column = 'AGE'
        self.Income_column = 'INCOME'
        self.Region_column = 'REGION'
        self.Ethnic_column = 'ETHNICITY'
        self.Hispanic_column = 'CORE_ACCULTURATION_0001'
        
        # Initialize variables to store extracted data
        self.x_status = None
        self.x_gender = None
        self.x_age = None
        self.x_income = None
        self.x_region = None
        self.x_ethnic = None
        self.x_hisp = None

    # Method to extract relevant columns from the dataset
    def data_columns(self):
        if self.Status_name in self.dataset.columns:
            self.x_status = self.dataset[self.Status_name]
        if self.Gender_column in self.dataset.columns:
            self.x_gender = self.dataset[self.Gender_column]
        if self.Age_column in self.dataset.columns:
            self.x_age = self.dataset[self.Age_column].apply(pd.to_numeric, errors='coerce').fillna(-1).astype(int)
        if self.Income_column in self.dataset.columns:
            self.x_income = self.dataset[self.Income_column].astype(str)
        if self.Region_column in self.dataset.columns:
            self.x_region = self.dataset[self.Region_column]
        if self.Ethnic_column in self.dataset.columns:
            self.x_ethnic = self.dataset[self.Ethnic_column]
        if self.Hispanic_column in self.dataset.columns:
            self.x_hisp = self.dataset[self.Hispanic_column]

# Class for gender-based data processing
class gender(data_create):
    def gender_data(self):
        self.data_columns()
        gender_counter_male = 0
        gender_counter_female = 0
        
        # Count male and female respondents with status 'Completed'
        for i in range(len(self.dataset)):
            status = self.x_status.iloc[i]
            gender = self.x_gender.iloc[i]
            if status == 'Completed' and gender == 'Male':
                gender_counter_male += 1
            elif status == 'Completed' and gender == 'Female':
                gender_counter_female += 1
        
        # Print results
        print('Male : ', gender_counter_male)
        print('Female : ', gender_counter_female)
        print('Total count: ', gender_counter_male + gender_counter_female)
        print()

# Class for age-based data processing
class age_data(data_create):
    def age_data(self):
        self.data_columns()
        
        # Initialize age group counters
        age_18_24 = 0
        age_25_34 = 0
        age_35_44 = 0
        age_45_54 = 0
        age_55_64 = 0
        age_65_ = 0
        
        # Count respondents within age groups
        for i in range(len(self.dataset)):
            age = self.x_age.iloc[i]
            status = self.x_status.iloc[i]
            if status == 'Completed':
                if age == -1:
                    continue
                if 18 <= age <= 24:
                    age_18_24 += 1
                elif 25 <= age <= 34:
                    age_25_34 += 1
                elif 35 <= age <= 44:
                    age_35_44 += 1
                elif 45 <= age <= 54:
                    age_45_54 += 1
                elif 55 <= age <= 64:
                    age_55_64 += 1
                elif age >= 65:
                    age_65_ += 1
        
        # Print results
        print('18-24 : ', age_18_24)
        print('25-34 :', age_25_34)
        print('35-44 : ', age_35_44)
        print('45-54 : ', age_45_54)
        print('55-64 : ', age_55_64)
        print('65+ : ', age_65_)
        print('Total age count: ', age_18_24 + age_25_34 + age_35_44 + age_45_54 + age_55_64 + age_65_)
        print()

# Class for ethnicity-based data processing
class ethnic_data(data_create):
    def ethnic_data(self):
        self.data_columns()
        
        # Initialize ethnicity counters
        White = 0
        AA = 0
        Hispanic = 0
        Asian = 0
        Other = 0
        
        # Count respondents within ethnic groups
        for i in range(len(self.dataset)):
            status = self.x_status.iloc[i]
            ethnic = self.x_ethnic.iloc[i]
            hispanic = self.x_hisp.iloc[i]
            if status == 'Completed':
                if hispanic in ['No', 'Prefer not to answer']:
                    if ethnic in ['American Indian or Alaska Native', 'Pacific Islander - Gaumanian',
                                  'Pacific Islander - Native Hawaiian', 'Pacific Islander - Other Pacific Islander',
                                  'Some other race']:
                        Other += 1
                    elif ethnic in ['Asian - Asian Indian', 'Asian - Chinese', 'Asian - Filipino', 'Asian - Japanese',
                                    'Asian - Korean', 'Asian - Vietnamese', 'Asian - Other']:
                        Asian += 1
                    elif ethnic == 'Black or African American':
                        AA += 1
                    elif ethnic == 'White':
                        White += 1
                else:
                    Hispanic += 1
        
        # Print results
        print('White : ', White)
        print('AA : ', AA)
        print('Hispanic :', Hispanic)
        print('Asian : ', Asian)
        print('Other : ', Other)
        print('Total Ethnic count: ', White + AA + Asian + Hispanic + Other)
        print()

# Instantiate and execute analysis classes
Input = r"C:\\Users\\prabi\\Downloads\\Main__Question_Report_Job_1717766797636.csv"

gender = gender(Input)
gender.gender_data()

age = age_data(Input)
age.age_data()

ethnic = ethnic_data(Input)
ethnic.ethnic_data()
