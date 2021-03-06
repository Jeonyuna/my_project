from flask import Flask, request, render_template, json
from external import get_data_from_api

app = Flask(__name__)


@app.route('/')
def get_main():
    return render_template('main.html')


@app.route('/search', methods=['GET'])
def search_get():
    target = request.args.get("target")
    classify = request.args.get("classify")
    academy = request.args.get("academy")
    course = request.args.get("course")
    start_date = request.args.get("startDate")
    end_date = request.args.get("endDate")
    page = request.args.get('page')

    if page is None:
        page = 1

    result = get_data_from_api(target, start_date, end_date, page, course, classify, academy)
    result_ls = []
    for course in result:

        sub_title = course['subTitle']  # 학원이름
        title = course['title']  # 수업이름
        man_count = int(course['regCourseMan'])  # 수강인원
        fee = course['realMan']  # 수강비

        if fee is None:
            fee = 0
        else:
            fee = int(fee)

        sales = man_count * fee
        result_ls.append({
            'course_name': title,
            'academy_name': sub_title,
            'registered_count': man_count,
            'unit_fee': f'{fee:,}',
            'sales': f'{sales:,}'
        })

    result_ls.sort(key=lambda x: x['sales'], reverse=True)

    for i in range(len(result_ls)):
        result_ls[i]['ranking'] = i + 1

    return render_template('result.html', result_ls=result_ls, page=page)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
