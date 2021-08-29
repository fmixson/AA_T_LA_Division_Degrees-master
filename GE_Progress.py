import pandas as pd


class GEProgress:

    planb_ge_requirements = {'Oral_Comm': 0, 'Writ_Comm': 0, 'Crit_Think': 0,
                             'Phys_Sci': 0, 'Bio_Sci': 0, 'Sci_Labs': 0, 'Math': 0,'Arts': 0, 'Hum': 0, 'Arts_Hum': 0,
                             'Amer_Hist': 0, 'Amer_Gov': 0, 'Institutions': 0, 'Self_Dev': 0}

    def __init__(self, completed_ge_courses, completed_ge_units, student_id):
        self.student_id = student_id
        self.completed_ge_units = completed_ge_units
        self.completed_ge_courses = completed_ge_courses
        self.missing_ge_courses = []

    def ge_requirements_completed(self):
        # length = len(DegreeProgressReports.degree_units_df)
        for ge_key in GEProgress.planb_ge_requirements:
            # print('ge key', ge_key)
            # print('aa require', DegreeProgressReports.AA_ge_requirements)
            if ge_key not in self.completed_ge_courses:
                self.missing_ge_courses.append(ge_key)
        # print('missing ge', self.missing_ge_courses)

        # print('no of missing ge', len(self.missing_ge_courses))
        # DegreeProgressReports.degree_courses_df.loc[length, 'GE_Courses'] = ge_list
        # major_list = self.major_course_dict.items()



