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
            lines = log.readlines()
            for line in lines:
                line = line.strip()
                sp = line.split(' ')
                line_number += 1
                if str(identifier) in sp:
                    print('{0}:{1} {2}'.format(file, line_number, line))
                    before = (line_number - lines_count - 1) if line_number > lines_count else 0
                    after = line_number + lines_count
                    print(''.join(lines[before:after]))


if __name__ == '__main__':
    find_lines_with_id('.', '*log', 4449, 100)
