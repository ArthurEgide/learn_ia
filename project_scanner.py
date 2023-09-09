import os

def choice(options):
  user_input = ''
  input_message = "Pick an option:\n"

  for index, item in enumerate(options):
      input_message += f'{index+1}) {item}\n'
  input_message += 'Your choice: '

  while user_input not in map(str, range(1, len(options) + 1)):
      user_input = input(input_message)
  # print('You picked: ' + options[int(user_input) - 1])
  return options[int(user_input) - 1]

base_path = 'learning'
areas = os.listdir(base_path)
chosen_area = choice(areas)
chosen_area_path = '/'.join([base_path, chosen_area])
projects = os.listdir(chosen_area_path)
chosen_project = choice(projects)
chosen_area_path = '/'.join([chosen_area_path, chosen_project])

with open('_tmp', 'w') as f:
  f.writelines(chosen_area_path)