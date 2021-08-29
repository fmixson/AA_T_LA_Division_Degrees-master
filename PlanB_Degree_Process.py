from Degree_Applicable_Electives import DegreeApplicableUnits
from Degree_Completion_Report import DegreeCompletionReport
from GE_Progress import GEProgress
from GE_Requirements import GeRequirements
from Major_Progress import MajorProgress
from Major_Requirements import MajorRequirements
from Student_Info import StudentInfo
# from main import enrollment_history


def AAT_degree_processing(student_id, courses, major_name, major_course_requirements, **kwargs):
    student = StudentInfo(student_id, courses)
    student.eligible_course_list()
    ge_requirements = GeRequirements(student.degree_applicable_dict)
    ge_requirements.ge_courses_completed('Oral_Comm')
    ge_requirements.ge_courses_completed('Writ_Comm')
    ge_requirements.ge_courses_completed('Crit_Think')
    ge_requirements.ge_courses_completed('Phys_Sci')
    ge_requirements.ge_courses_completed('Bio_Sci')
    ge_requirements.ge_courses_completed('Sci_Labs')
    ge_requirements.ge_courses_completed('Math')
    ge_requirements.ge_courses_completed('Arts')
    ge_requirements.ge_courses_completed('Hum')
    ge_requirements.ge_courses_completed('Arts_Hum')
    ge_requirements.ge_courses_completed('Amer_Hist')
    ge_requirements.ge_courses_completed('Amer_Gov')
    ge_requirements.ge_courses_completed('Institutions')
    ge_requirements.ge_courses_completed('Self_Dev')
    degree_reports = GEProgress(ge_requirements.completed_ge_courses, ge_requirements.completed_ge_units,
                                student.student_id)
    degree_reports.ge_requirements_completed()

    major = MajorRequirements(revised_course_list=student.degree_applicable_dict,
                              completed_ge_courses=ge_requirements.completed_ge_courses,
                              major_requirements=major_course_requirements,
                              major_name=major_name)
    if len(kwargs) == 12:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])
        major.major_courses_completed(area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                      number_of_disciplines=kwargs['major3_disciplines'])
        major.major_courses_completed(area_name=kwargs['major4'], total_units=kwargs['major4_units'],
                                      number_of_disciplines=kwargs['major4_disciplines'])

    if len(kwargs) == 9:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])
        major.major_courses_completed(area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                      number_of_disciplines=kwargs['major3_disciplines'])

    if len(kwargs) == 6:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])

    if len(kwargs) == 3:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])

    degree_app = DegreeApplicableUnits(degree_applicable_dict=student.degree_applicable_dict,
                                       major_courses_list=major.major_courses_list,
                                       completed_ge_courses=ge_requirements.completed_ge_courses,
                                       completed_ge_units=ge_requirements.completed_ge_units,
                                       major_units_list=major.major_units_list)
    elective_units, elective_courses = degree_app.elective_courses()
    major_report = MajorProgress(student_id=student.student_id,
                                 major_course_dict=major.major_course_dict,
                                 major_units=major.major_units_list,
                                 area_units=major.area_units_dict,
                                 no_of_courses_required=major.major_no_courses_requirement_dict)
    major_report.major_requirements_completed()

    degree_completion = DegreeCompletionReport(
        major_requirements_dict=major.major_requirements_dict,
        completed_ge_courses=ge_requirements.completed_ge_courses,
        completed_ge_units=ge_requirements.completed_ge_units,
        major_course_dict=major.major_course_dict,
        area_units_dict=major.area_units_dict,
        major_units_list=major.major_units_list,
        student_id=student_id,
        student_major=major_name,
        missing_ge=degree_reports.missing_ge_courses,
        missing_major_courses=major_report.missing_courses_dict2,
        elective_units=elective_units,
        elective_courses=elective_courses)
    degree_completion.degree_completion()


def sorting_PlanB_majors(enrollment_history, major_name, major_course_requirements, **kwargs):
    student_id_list = []

    for i in range(len(enrollment_history)):
        """This for loop creates a list of ids for each major identified in major name. If the id is not in the list
        and the major listed for the student in the dataframe matches the major in major_name, the the id is included
        in the list."""
        if enrollment_history.loc[i, "ID"] not in student_id_list:
            # print('major in sorting majors', major_name)
            if enrollment_history.loc[i, "Major"] == major_name:
                student_id_list.append(enrollment_history.loc[i, "ID"])

    for student_id in student_id_list:
        """This for loop takes the list of students with a particular major and runs it through the AAT program.
        """
        print(major_name)
        AAT_degree_processing(student_id=student_id, courses=enrollment_history, major_name=major_name,
                              major_course_requirements=major_course_requirements, **kwargs)