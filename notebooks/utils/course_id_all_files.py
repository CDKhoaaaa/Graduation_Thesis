import os
import pandas as pd
# current_directory = os.getcwd()
# folder_path1 = os.path.join(current_directory, '../../data/gathered_data/attendance_sheet')
# file_names1 = os.listdir(folder_path1)

def get_files_with_course_code(folder_path, course_code):
    file_names = os.listdir(folder_path)
    files_with_course_code = []
    count_files_with_course_code = 0

    def get_course_info(path):
        df = pd.read_excel(path, nrows=13)
        date_series = df.iloc[10, 6:df.shape[1] - 4].dropna()
        # Số tiết học.
        school_periods = date_series.shape[0]
        # class name
        course_info = df.iloc[7, 2]
        class_name = course_info[-9:len(course_info) - 1]
        # course code
        course_code = course_info[-24:-12]
        # course name
        course_name = course_info[0:len(course_info) - (len(course_code) + len(class_name) + 6)]
        return course_name, class_name, course_code, school_periods

    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        _, _, course_code_in_file, _ = get_course_info(file_path)
        if course_code_in_file == course_code:
            count_files_with_course_code += 1
            files_with_course_code.append(file_name)

    return count_files_with_course_code, files_with_course_code


# Sử dụng hàm để lấy thông tin về tệp có mã học phần là "100107462102"
# count, files = get_files_with_course_code(folder_path1, "100107462102")

# print("Số lượng file có mã học phần là", count)
# print("Tên các file có mã học phần là:")
# for file_name in files:
#     print(file_name)


def get_files_with_course_code2(folder_path, course_code):
    file_names = os.listdir(folder_path)
    files_with_course_code = []
    count_files_with_course_code = 0

    def get_course_info(path):
        df = pd.read_excel(path, nrows=8)
        course_info = df.iloc[3, 4][14:]
        parts = course_info.split(" - ")
        # Course ID
        course_id = parts[0].strip('[]')
        # Class name
        class_id = parts[-1][-9:]
        # Subject name
        subject = parts[-1][:len(parts[-1]) - 11]
        return course_id, class_id, subject

    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        course_id, class_id, _ = get_course_info(file_path)  # Thay đổi ở đây
        if course_id == course_code:
            count_files_with_course_code += 1
            files_with_course_code.append(file_name)

    return count_files_with_course_code, files_with_course_code
