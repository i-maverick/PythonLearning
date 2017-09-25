import glob
import os


# find_lines_with_id - search logs for lines with current identifier
#
# path: logs folder
# mask: file template
# id: identifier to find
# lines_count: number of surrounded lines
#
def find_lines_with_id(path, mask, identifier, lines_count):
    for file in glob.iglob(path + '/' + mask):
        if not os.path.isfile(file):
            continue

        line_number = 0
        with open(file) as log:
            temp_line_storage = []  # array to store {lines_count} previous lines
            founded_strings = {}
            surrounded_lines = {}  # dict to store surrounded lines

            for line in log:
                line = line.strip()
                sp = line.split(' ')
                line_number += 1
                if str(identifier) in sp:
                    founded_strings[line_number] = line
                    # copy {lines_count} previous lines from storage for new founded string
                    surrounded_lines[line_number] = temp_line_storage[:]

                for num in founded_strings:
                    if len(surrounded_lines[num]) < lines_count * 2 + 1:
                        # append {lines_count} next lines for each founded string
                        surrounded_lines[num].append(line)

                if len(temp_line_storage) >= lines_count:
                    temp_line_storage.pop(0)
                temp_line_storage.append(line)

            for num in founded_strings:
                print('{0}:{1} {2}'.format(file, num, founded_strings[num]))
                print('\n'.join(surrounded_lines[num]) + '\n')

if __name__ == '__main__':
    find_lines_with_id('.', '*log', 4449, 5)
