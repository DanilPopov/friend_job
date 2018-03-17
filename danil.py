from openpyxl import load_workbook

def read_excel_posts(filename):
    work_book = load_workbook(filename)
    work_sheet = work_book['Лист1']

    excel_data = list()
    for row in range(1, work_sheet.max_row+1):
        excel_row = dict()
        if work_sheet.cell(row=row, column=1).value is None:
            break
        excel_row['id'] = work_sheet.cell(row=row, column=1).value
        excel_row['post'] = work_sheet.cell(row=row, column=2).value
        excel_data.append(excel_row)

    return excel_data


def read_excel_is_job_keywords(filename):
    work_book = load_workbook(filename)
    work_sheet = work_book['Лист1']

    excel_data = list()
    for row in range(3, work_sheet.max_row+1):
        excel_row = dict()
        if work_sheet.cell(row=row, column=1).value is None:
            break
        excel_row['keyword'] = work_sheet.cell(row=row, column=1).value
        excel_data.append(excel_row)

    return excel_data



if __name__ == '__main__':
    excel_posts_data = read_excel_posts('Тестовые посты.xlsx')
    is_job_data = read_excel_is_job_keywords('Ключевые слова.xlsx') 


# print(excel_posts_data)
# print(excel_keywords_data)

post_list = []
is_job_keyword_list = []

for row in is_job_data:
    is_job_keyword_list.append(row['keyword'])
print(is_job_keyword_list)

for row in excel_posts_data:
    for key in is_job_keyword_list:
        if key in row['post'].lower():
            row['is_job'] = True
            post_list.append(row)
            break
print(post_list)




for row in post_list:
    print(row['id'])

    # post = row['post']
    # post_list.append(post)

# for post in post_list:
    # 1. сделать поиск ключевых слов, чтобы определить, относится ли пост к объявлению о работе. Вернуть True или False
    # 2. сделать поиск ключевых слов, чтобы определить, в каком городе вакансия
    # 3. сделать поиск ключевых слов, чтобы определить зону ответственности
    # - приводить все ключевые слова к нижнему регистру


