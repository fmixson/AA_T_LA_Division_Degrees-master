import pandas as pd


class GeRequirements:
    ge_dataframe = pd.read_csv("PlanB_GE.csv")
    pd.set_option('display.max_columns', None)
    # print(ge_dataframe)

    def __init__(self, degree_applicable_dict):
        self.degree_applicable_dict = degree_applicable_dict
        self.completed_ge_courses = {}
        self.completed_ge_units = []

    def ge_courses_completed(self, area_name):
        # print(self.degree_applicable_dict)
        for i in range(len(GeRequirements.ge_dataframe[area_name])):
            for key in self.degree_applicable_dict:
                if key == GeRequirements.ge_dataframe.loc[i, area_name]:
                    # print(area_name)
                    if area_name not in self.completed_ge_courses:

                        self.completed_ge_courses[area_name] = key
                        self.completed_ge_units.append(self.degree_applicable_dict[key])
                        # total = sum(self.completed_ge_units)
        # print(self.completed_ge_courses, self.completed_ge_units)
        return self.completed_ge_courses, self.completed_ge_units





