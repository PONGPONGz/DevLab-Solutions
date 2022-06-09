from json import loads
from infos import *
from utils import *

create_folders()

user_data = loads(request('/user/' + USER_ID).content)
solutions = user_data.get('lastFivePassed')
print(f'{len(solutions)} Solutions found.')

errors = []

for solution_info in solutions:
    id = str(solution_info.get('devlab_id'))
    language_id = str(solution_info.get('sub_lang'))
    difficulty = solution_info.get('devlab_level')
    problem_name = clean_filename(solution_info.get('devlab_name'))
    solution_file = f"../{difficulty} Stars/{problem_name}.py"
    solution = loads(request(f'/tasks/{id}?languageId={language_id}').content).get('sub_code')
    try:
        solution_url = BASE_URL + '/task/{}?languageId={}'.format(id, language_id)
        with open(solution_file, 'w+', encoding='utf-8') as f:
            f.write('# {}\n{}'.format(solution_url, solution))
            print('wrote task:', id, '-', difficulty,'⭐ |', problem_name)
    except:
        errors.append((problem_name, id, solution))

for e in errors:
    print('Failure fetching solution "{}" - {}\n{}\n'.format(*e))
print('\nSuccessfully fetched {} solutions\n'.format(len(solutions) - len(errors)))

        