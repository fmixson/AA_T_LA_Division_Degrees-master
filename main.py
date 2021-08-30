import pandas as pd

from PlanB_Degree_Process import sorting_PlanB_majors
from Degree_Completion_Report import DegreeCompletionReport

pd.set_option('display.max_columns', None)
student_id_and_major = pd.read_csv(
    "C:/Users/family/Desktop/Programming/Enrollment Histories/Copy of majors_20210827.csv")
# print(student_id_and_major)

id_and_major_dict = {}

for i in range(len(student_id_and_major)):
    id_and_major_dict[student_id_and_major.loc[i, "ID"]] = student_id_and_major.loc[i, "Major"]
    # print(id_and_major_dict)

enrollment_history = pd.read_csv(
    "C:/Users/family/Desktop/Programming/Enrollment Histories/utf_10000_of_enrollment_file_20210827.csv")
enrollment_history.sort_values(['ID'], inplace=True)
enrollment_history.replace(to_replace="SPCH",
                           value="COMM", inplace=True)
enrollment_history['Class Subject'] = enrollment_history['Class Subject'].str.strip()
enrollment_history['Class Catalog Number'] = enrollment_history['Class Catalog Number'].str.strip()
enrollment_history['Course'] = enrollment_history['Class Subject'] + " " + enrollment_history['Class Catalog Number']
enrollment_history['Class Catalog Number'] = enrollment_history['Class Catalog Number'].fillna(0)
nona_enrollment_history = enrollment_history[enrollment_history['Official Grade'].notna()]
nona_enrollment_history = nona_enrollment_history.reset_index(drop=True)
enrollment_history = nona_enrollment_history
print(enrollment_history)

# enrollment_history = nona_enrollment_history
# index_W = enrollment_history[enrollment_history['Official Grade'] == 'W') & enrollment_history['Official Grade'] == 'D'].index
# enrollment_history.drop(index_W, inplace=True)
"""
Create new column then do for loop with if statement. 
if the id in dictionary matches id in dataframe then put the major in the new column.
"""

for i in range(len(enrollment_history)):
    print(len(enrollment_history), i)
    ID = enrollment_history.loc[i, "ID"]
    if ID in id_and_major_dict.keys():
        enrollment_history.loc[i, "Major"] = id_and_major_dict[ID]
        if i == len(enrollment_history) - 1:
            print('equal works')
            break
        else:
            if enrollment_history.loc[i, 'ID'] != enrollment_history.loc[i + 1, 'ID']:
                print('break')
                continue

sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="Comm Studies for Transfer-AAT",
                     major_course_requirements='AAT_COMM.csv',
                     major1='Core', major1_units=3, major1_disciplines=1,
                     major2='ListA', major2_units=6, major2_disciplines=1,
                     major3='ListB', major3_units=3, major3_disciplines=1,
                     major4='ListC', major4_units=3, major4_disciplines=1)
sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="English for Transfer-AAT",
                     major_course_requirements='AAT_English.csv',
                     major1='Core', major1_units=3, major1_disciplines=1,
                     major2='ListA', major2_units=6, major2_disciplines=1,
                     major3='ListB', major3_units=6, major3_disciplines=1,
                     major4='ListC', major4_units=3, major4_disciplines=1)
sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="Spanish for Transfer-AAT",
                     major_course_requirements='AAT_Spanish.csv',
                     major1='Core', major1_units=19, major1_disciplines=1,
                     major2='ListA', major2_units=3, major2_disciplines=1)
sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="Business Administration-AST",
                     major_course_requirements='AAT_BusAdmin.csv',
                     major1='Core', major1_units=15, major1_disciplines=1,
                     major2='ListA', major2_units=3, major2_disciplines=1,
                     major3='ListB', major3_units=6, major3_disciplines=1)
sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="LAS: Soc Behavioral Sci-AB",
                     major_course_requirements='Soc_and_Behav_Sci.csv',
                     major1='Core', major1_units=18, major1_disciplines=3)
sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="LAS: Self Dev & Soc Beh-AB",
                     major_course_requirements='Self_Dev_Soc_Behav.csv',
                     major1="Theory_Background", major1_units=6, major1_disciplines=1,
                     major2="Stud_Dev_App", major2_units=3, major2_disciplines=1,
                     major3="Stud_Vit", major3_units=3, major3_disciplines=1)
sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="LAS: Communications-AB",
                     major_course_requirements='AS_Comm.csv',
                     major1='Comm1', major1_units=3, major1_disciplines=1,
                     major2='Comm2', major2_units=3, major2_disciplines=1,
                     major3='Crit_Think', major3_units=3, major3_disciplines=1,
                     major4='Electives', major4_units=9, major4_disciplines=2)

# pd.set_option('display.max_columns', None)
#
# student_course_list = pd.read_csv(
#     "C:/Users/fmixson/Desktop/Programming/Enrollment_Histories/EnrollmentHistory_20210817.csv")
#
# student_id_list = []
#
# for i in range(len(student_course_list)):
#     if student_course_list.loc[i, "ID"] not in student_id_list:
#         student_id_list.append(student_course_list.loc[i, "ID"])
# # print(student_id_list)
# for student_id in student_id_list:
#
#     AAT_degree_processing(student_id=student_id, courses=student_course_list, major='comm_major_requirements',
#                           major_name="COMM_AAT", major_course_requirements='AAT_COMM.csv',
#                           major1='Core', major1_units=3, major1_disciplines=1,
#                           major2='ListA', major2_units=6, major2_disciplines=1,
#                           major3='ListB', major3_units=3, major3_disciplines=1,
#                           major4='ListC', major4_units=3, major4_disciplines=1)
#
#     AAT_degree_processing(student_id=student_id, courses=student_course_list, major='english_major_requirements',
#                           major_name="English_AAT", major_course_requirements='AAT_English.csv',
#                           major1='Core', major1_units=3, major1_disciplines=1,
#                           major2='ListA', major2_units=6, major2_disciplines=1,
#                           major3='ListB', major3_units=6, major3_disciplines=1,
#                           major4='ListC', major4_units=3, major4_disciplines=1)
#     #
#     AAT_degree_processing(student_id=student_id, courses=student_course_list, major='spanish_major_requirements',
#                           major_name="Spanish_AAT", major_course_requirements='AAT_Spanish.csv',
#                           major1='Core', major1_units=19, major1_disciplines=1,
#                           major2='ListA', major2_units=3, major2_disciplines=1)

DegreeCompletionReport.LS_AA_Degrees_df.sort_values(by=['Total_Missing'], inplace=True, ascending=True)
DegreeCompletionReport.LS_AA_Degrees_df.to_csv('C:/Users/family/Desktop/Programming/AAT_LA_Division_Degrees.csv')

# GE Variables
# GE_Units_Dict = {'A1': 0, 'A2': 0, 'A3': 0, 'B1': 0, 'B2': 0, 'B3': 0, 'D1': 0, 'D2': 0, 'C1': 0, 'C2': 0, 'C3': 0,
#                  'D3': 0, 'E1': 0, 'Electives': 0}
# GE_Units_List = []
# GE_Course_Dict = {}
# ge_course_list = []
# Electives_units_List = []
# area_units = 0
# major_units = 0
# GE_Units = 0
# lab = False
#
# # Major Variables
# MajorDict1 = {}
# MajorDict2 = {}
# Major_Units_Dict = {'Core': [0], 'ListA': [0], 'ListB': [0], 'ListC': [0]}
# Major_Course_Dict = {}
# option = 0
# major_course_list = []
# # major_course_dict = {}
# Core_List = []
# ListA_List = []
# ListB_List = []
# ListC_List = []
# units = 0
#
#
#
# def ge_course_completion(id, area_name, course_name, course_units):
#     global lab
#
#     global area_units
#     global GE_Units_Dict
#     global GE_Units_List
#
#     major_course = False
#     ge_course = False
#     global GE_Units
#     for j in range(len(degree_courses[area_name])):
#
#         if course_name == degree_courses.loc[j, area_name]:
#             for course in ge_course_list:
#                 if course_name == course:
#                     ge_course = True
#
#             for course in major_course_list:
#                 if course_name == course:
#                     major_course = True
#
#             if area_name == 'Electives':
#                 if ge_course is False and major_course is False:
#                     if area_name in GE_Course_Dict:
#                         GE_Course_Dict[area_name].append(student_courses.loc[i, "Course"])
#                         GE_Units_Dict[area_name].append([student_courses.loc[i, "Units"]])
#                         ge_course_list.append(student_courses.loc[i, "Course"])
#                         Electives_units_List.append(student_courses.loc[i, "Units"])
#                     else:
#                         GE_Course_Dict[area_name] = [student_courses.loc[i, "Course"]]
#                         GE_Units_Dict[area_name] = [student_courses.loc[i, "Units"]]
#                         ge_course_list.append(student_courses.loc[i, "Course"])
#                         Electives_units_List.append(student_courses.loc[i, "Units"])
#             else:
#                 if ge_course is False:
#                     if area_name in GE_Course_Dict:
#                         print(area_name)
#                         print(GE_Course_Dict[area_name])
#                         print(GE_Course_Dict)
#                         GE_Course_Dict[area_name].append(student_courses.loc[i, "Course"])
#                         GE_Units_Dict[area_name].append(student_courses.loc[i, 'Units'])
#                         ge_course_list.append(student_courses.loc[i, "Course"])
#                     else:
#                         GE_Units_Dict[area_name] = student_courses.loc[i, 'Units']
#                         GE_Course_Dict[area_name] = student_courses.loc[i, "Course"]
#                         ge_course_list.append(student_courses.loc[i, "Course"])
#
#                     if area_name == "B1" or area_name == "B2" or area_name == 'Electives':
#                         for k in range(len(degree_courses["B_Labs"])):
#                             if course_name == degree_courses.loc[k, "B_Labs"]:
#                                 Lab = True
#             print(GE_Units_Dict)
#             print(GE_Course_Dict)
#             print(student_courses.loc[i, "Course"])
#             print(GE_Units_List)
#
#             return GE_Units_Dict
#
#
# def major_course_completion(ID, area_name, course_name, area_units=0, GE_Units=0):
#     global option
#     global Major_Units_Dict
#     global Major_Course_Dict
#     major_course = False
#     ge_course = False
#
#     for j in range(len(degree_courses[area_name])):
#         if course_name == degree_courses.loc[j, area_name]:
#             for course in ge_course_list:
#                 if course_name == course:
#                     ge_course = True
#
#             for course in major_course_list:
#                 if course == course_name:
#                     major_course = True
#
#             if not major_course:
#                 if area_name in Major_Course_Dict:
#                     Major_Course_Dict[area_name].append(student_courses.loc[i, "Course"])
#                     if ge_course == False:
#                         Major_Units_Dict[area_name].append(student_courses.loc[i, "Units"])
#                     major_course_list.append(student_courses.loc[i, "Course"])
#                 else:
#                     Major_Course_Dict[area_name] = [student_courses.loc[i, "Course"]]
#                     if ge_course == False:
#                         Major_Units_Dict[area_name] = [student_courses.loc[i, "Units"]]
#                     major_course_list.append(student_courses.loc[i, "Course"])
#             print(Major_Course_Dict)
#             print(Major_Units_Dict)
#
# def Degree_Totals(ID, GE_Dictionary, Major_Dictionionary):
#     global MajorDict1
#     global MajorDict2
#     global lab
#     print(f'in the degree totals: {Major_Dictionionary}')
#     DictA = {'A1': 'Communications', 'A2': 'Writing', 'A3': 'Critical Thinking', 'B1': 'Physical Sciences',
#              'B2': 'Biological Sciences', 'B3': 'Mathematical Concepts', 'C1': 'Fine Arts', 'C2': 'Humanities',
#              'C3': 'Fine Arts/Humanities', 'D1': 'American History', 'D2': 'American Government',
#              'D3': 'Social, Political, Historical, Economic Institutions', 'E1': 'Self-Development'}
#     Missing_Courses_List = []
#     Missing_Course = {}
#     for key in DictA:
#         if key not in GE_Dictionary:
#             Missing_Courses_List.append(key)
#
#     if Major_Dictionionary == MajorDict1:
#         if 'Core' not in MajorDict1:
#             Missing_Course['Core'] = 2
#         else:
#             core_missing_course = 2 - len(Major_Dictionionary['Core'])
#             Missing_Course['Core'] = core_missing_course
#         if 'ListA' not in MajorDict1:
#             Missing_Course['ListA'] = 2
#         else:
#             ListA_missing_course = 2 - len(Major_Dictionionary['ListA'])
#             Missing_Course['ListA'] = ListA_missing_course
#
#         if 'ListB' not in MajorDict1:
#             Missing_Course['ListB'] = 1
#         else:
#             ListB_missing_course = 1 - len(MajorDict1['ListB'])
#             Missing_Course['ListB'] = ListB_missing_course
#         if 'ListC' not in MajorDict1:
#             Missing_Course['ListC'] = 1
#         else:
#             ListC_missing_course = 1 - len(MajorDict1['ListC'])
#             Missing_Course['ListC'] = ListC_missing_course
#
#     if Major_Dictionionary == MajorDict2:
#
#         if 'Core' not in MajorDict2:
#             Missing_Course['Core'] = 2
#         else:
#             core_missing_course = 1 - len(MajorDict2['Core'])
#             Missing_Course['Core'] = core_missing_course
#         if 'ListA' not in MajorDict1:
#             Missing_Course['ListA'] = 2
#         else:
#             ListA_missing_course = 2 - len(MajorDict2['ListA'])
#             Missing_Course['ListA'] = ListA_missing_course
#         if 'ListB' not in MajorDict1:
#             Missing_Course['ListB'] = 1
#         else:
#             ListB_missing_course = 2 - len(MajorDict2['ListB'])
#             Missing_Course['ListB'] = ListB_missing_course
#         if 'ListC' not in MajorDict1:
#             Missing_Course['ListC'] = 1
#         else:
#             ListC_missing_course = 1 - len(MajorDict2['ListC'])
#             Missing_Course['ListC'] = ListC_missing_course
#
#
#     od = OrderedDict(sorted(GE_Dictionary.items()))
#     print(f'missing course: {Missing_Course}')
#     values = Missing_Course.values()
#     totals = sum(values)
#
#     print(f"Student {ID} has completed the following Plan B GE Courses {od}")
#     if len(Missing_Courses_List) == 0:
#         print(f"Student {ID} has completed all Plan B GE Requirements.")
#     else:
#         print(f"Student {ID} still needs to complete courses from the {len(Missing_Courses_List)} following GE areas: {Missing_Courses_List}")
#     print(f"Student {ID} has completed the following major courses {Major_Dictionionary}")
#     if MajorDict1 and totals == 0:
#         print(f"Student {ID} has completed all Option 1 Major requirements")
#     if MajorDict1 and totals > 0:
#         print(f"Student {ID} still needs to complete {totals} courses from the Option 1 requirements:")
#         for key, val in Missing_Course.items():
#             if val > 0:
#                 print(f"{val} from {key}")
#     if MajorDict2 and totals == 0:
#         print(f"Student {ID} has completed all Option 2 Major requirements")
#     if MajorDict2 and totals > 0:
#         print(f"Student {ID} still needs to complete {totals} courses from the Option 2 requirements:")
#         for key, val in Missing_Course.items():
#             if val > 0:
#                 print(f"{val} from {key}")
#     # Area_Course_Dict = {}
#     # MajorDict1 = {}
#     # MajorDict2 = {}
#     # Core_List = []
#     # listA_units = 0
#     # ListA_List = []
#
# student_courses = pd.read_csv("C:/Users/family/Desktop/Programming/Copy of EnrollmentHistory_20210426.csv")
# student_courses.sort_values(by=['ID', 'Course'], inplace=True)
# student_courses = student_courses.reset_index(drop=True)
# pd.set_option('display.max_columns', None)
# # print(student_courses.head())
#
# booleans = []
# for Grade in student_courses.Grade:
#     if Grade == 'A' or Grade == 'B' or Grade == 'C' or Grade == 'P':
#         booleans.append(True)
#     else:
#         booleans.append(False)
#
# print(booleans[0:5])
# is_long = pd.Series(booleans)
# print(is_long)
# # is_long = student_courses.Grade == 'B'
# print(is_long.head())
# print(student_courses[is_long])
# # student_courses = pd.read_csv("C:/Users/family/Desktop/Programming/Copy of EnrollmentHistory_20210426.csv")
# # student_courses.sort_values(by=['ID', 'Course'], inplace=True)
# # student_courses = student_courses.reset_index(drop=True)
# degree_courses = pd.read_csv("C:/Users/family/Desktop/Programming/Comm_GE_Plan_B.csv")
# # print(student_courses)
#
# for i in range(len(student_courses)):
#
#     if GE_Units_Dict['A1'] < 3:
#         ge_course_completion(student_courses.loc[i, "ID"], "A1", student_courses.loc[i, "Course"],
#                              student_courses.loc[i, 'Units'])
#
#     if GE_Units_Dict['A2'] < 3:
#         ge_course_completion(student_courses.loc[i, "ID"], "A2", student_courses.loc[i, "Course"],
#                              student_courses.loc[i, 'Units'])
#
#     if GE_Units_Dict['A3'] < 3:
#         ge_course_completion(student_courses.loc[i, "ID"], "A3", student_courses.loc[i, "Course"],
#                              student_courses.loc[i, 'Units'])
#
#     if GE_Units_Dict['B1'] < 3:
#         ge_course_completion(student_courses.loc[i, "ID"], "B1", student_courses.loc[i, "Course"],
#                              student_courses.loc[i, 'Units'])
#
#     if GE_Units_Dict['B2'] < 3:
#         ge_course_completion(student_courses.loc[i, "ID"], "B2", student_courses.loc[i, "Course"],
#                              student_courses.loc[i, 'Units'])
#
#     if GE_Units_Dict['B3'] < 3:
#         ge_course_completion(student_courses.loc[i, "ID"], "B3", student_courses.loc[i, "Course"],
#                              student_courses.loc[i, 'Units'])
#
#     if GE_Units_Dict['D1'] < 3:
#         ge_course_completion(student_courses.loc[i, "ID"], "D1", student_courses.loc[i, "Course"],
#                              student_courses.loc[i, 'Units'])
#
#     if GE_Units_Dict['D2'] < 3:
#         units = ge_course_completion(student_courses.loc[i, "ID"], "D2", student_courses.loc[i, "Course"],
#                                      student_courses.loc[i, 'Units'])
#
#     if GE_Units_Dict['C1'] < 3:
#         units = ge_course_completion(student_courses.loc[i, "ID"], "C1", student_courses.loc[i, "Course"],
#                                      student_courses.loc[i, 'Units'])
#
#     if GE_Units_Dict['C2'] < 3:
#         units = ge_course_completion(student_courses.loc[i, "ID"], "C2", student_courses.loc[i, "Course"],
#                                      student_courses.loc[i, 'Units'])
#
#     if GE_Units_Dict['C3'] < 3:
#         ge_course_completion(student_courses.loc[i, "ID"], "C3", student_courses.loc[i, "Course"],
#                              student_courses.loc[i, 'Units'])
#
#     if GE_Units_Dict['D3'] < 3:
#         ge_course_completion(student_courses.loc[i, "ID"], "D3", student_courses.loc[i, "Course"],
#                              student_courses.loc[i, 'Units'])
#
#     if GE_Units_Dict['E1'] < 3:
#         ge_course_completion(student_courses.loc[i, "ID"], "E1", student_courses.loc[i, "Course"],
#                              student_courses.loc[i, 'Units'])
#
#     if student_courses.loc[i, 'Course'] == 'ENGL 102' or student_courses.loc[i, 'Course'] == 'ENGL 103':
#         option = 1
#         Major_Course_Dict['Option'] = "1"
#     if student_courses.loc[i, 'Course'] == 'ENGL 110':
#         option = 2
#         Major_Course_Dict['Option'] = "2"
#     # print(Major_Units_Dict)
#     # print(Major_Course_Dict)
#     # print(f'Major_Units_Dict:{Major_Units_Dict}')
#     # if 'Core' not in Major_Units_Dict:
#     #     Major_Units_Dict['Core'] = 0
#     Core_Sum = sum(Major_Units_Dict['Core'])
#     # print(f'Core Sum: {Core_Sum}')
#     if option == 1:
#         if Core_Sum < 6:
#             major_course_completion(student_courses.loc[i, "ID"], "Core", student_courses.loc[i, "Course"])
#
#     if option == 2:
#         if Core_Sum < 3:
#             major_course_completion(student_courses.loc[i, "ID"], "Core", student_courses.loc[i, "Course"])
#
#     ListA_Sum = sum(Major_Units_Dict['ListA'])
#     if ListA_Sum < 6:
#         major_course_completion(student_courses.loc[i, "ID"], "ListA", student_courses.loc[i, "Course"])
#
#     ListB_Sum = sum(Major_Units_Dict['ListB'])
#     if option == 1:
#         if 'ListB' not in Major_Course_Dict:
#             major_course_completion(student_courses.loc[i, "ID"], "ListB", student_courses.loc[i, "Course"])
#         elif len(Major_Course_Dict['ListB']) < 1:
#             major_course_completion(student_courses.loc[i, "ID"], "ListB", student_courses.loc[i, "Course"])
#     else:
#        if 'ListB' not in Major_Course_Dict:
#             major_course_completion(student_courses.loc[i, "ID"], "ListB", student_courses.loc[i, "Course"])
#        elif len(Major_Course_Dict['ListB']) < 2:
#             major_course_completion(student_courses.loc[i, "ID"], "ListB", student_courses.loc[i, "Course"])
#
#     ListC_Sum = sum(Major_Units_Dict['ListC'])
#     # print(f'ListC Sum: {ListC_Sum}')
#     # print({len(Major_Units_Dict['ListC'])})
#     if 'ListC' not in Major_Course_Dict:
#         major_course_completion(student_courses.loc[i, "ID"], "ListC", student_courses.loc[i, "Course"])
#     elif len(Major_Course_Dict['ListC']) < 1:
#         major_course_completion(student_courses.loc[i, "ID"], "ListC", student_courses.loc[i, "Course"])
#     # print(Major_Course_Dict)
#     GE_units_completed = 0
#     for key in GE_Units_Dict:
#         if key != 'Electives':
#             # print(key)
#             # print(GE_Units_Dict[key])
#             units = GE_Units_Dict[key]
#             # print(f'GE units completed: {units}')
#         GE_units_completed = GE_units_completed + units
#         # print(f'Total {GE_units_completed}')
#     # print(GE_units_completed)
#     #     units = sum(GE_Units_Dict[key])
#     #     GE_units_completed = GE_units_completed + units
#     # print(f"GE Loop: {GE_units_completed}")
#     if GE_units_completed < 39:
#         ge_course_completion(student_courses.loc[i, "ID"], "Electives", student_courses.loc[i, "Course"],
#                              student_courses.loc[i, 'Units'])
#     # print(GE_Units_Dict)
#     # print(GE_Course_Dict)
#     if i <= len(student_courses) - 2:
#
#         if student_courses.loc[i, 'ID'] != student_courses.loc[i + 1, 'ID']:
#             if option == 1:
#                 MajorDict1 = Major_Course_Dict
#                 # MajorDict1 = {'Core': Core_List, 'ListA': ListA_List, 'ListB': ListB_List, 'ListC': ListC_List}
#                 print(f'major dict 1 before going to function {MajorDict1}')
#                 Degree_Totals(student_courses.loc[i, 'ID'], GE_Course_Dict, MajorDict1)
#             if option == 2:
#                 MajorDict2 = Major_Course_Dict
#                 # MajorDict2 = {'Core': Core_List, 'ListA': ListA_List, 'ListB': ListB_List, 'ListC': ListC_List}
#                 print(f'major dict 2 before going to function {MajorDict2}')
#                 Degree_Totals(student_courses.loc[i, 'ID'], GE_Course_Dict, MajorDict2)
#     #
#             GE_Units = 0
#
#
#             lab = False
#             # GE Variables
#             GE_Units_Dict = {'A1': 0, 'A2': 0, 'A3': 0, 'B1': 0, 'B2': 0, 'B3': 0, 'D1': 0, 'D2': 0, 'C1': 0, 'C2': 0,
#                              'C3': 0,
#                              'D3': 0, 'E1': 0, 'Electives': 0}
#             GE_Units_List = []
#             GE_Course_Dict = {}
#             ge_course_list = []
#             Electives_units_List = []
#             area_units = 0
#             major_units = 0
#             GE_Units = 0
#             lab = False
#
#             # Major Variables
#             MajorDict1 = {}
#             MajorDict2 = {}
#             Major_Units_Dict = {'Core': [0], 'ListA': [0], 'ListB': [0], 'ListC': [0]}
#             Major_Course_Dict = {}
#             option = 0
#             major_course_list = []
#             # major_course_dict = {}
#             Core_List = []
#             ListA_List = []
#             ListB_List = []
#             ListC_List = []
#             units = 0
#             ListA_List = []
#             ListB_List = []
#             ListC_List = []
#             units = 0
#             option = 0
