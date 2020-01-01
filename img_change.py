import os


def handle_file(file_path, img_dir):
    file_split = os.path.split(file_path)
    temp_file = os.path.join(file_split[0], 'temp.md')
    with open(file_path, 'r', encoding='utf-8') as f:
        with open(temp_file, 'w', encoding='utf-8') as temp:
            for eachline in f:
                if eachline.startswith('![]'):
                    img_path = eachline.strip()[4:].strip(')')
                    img_name = os.path.split(img_path)[1]
                    new_img_path = os.path.join(img_dir, img_name)
                    new_line = '![](' + new_img_path + ')'
                    temp.write(new_line + '\n')
                else:
                    temp.write(eachline)
    os.remove(file_path)
    os.rename(temp_file, file_path)


def run(target_dir):
    img_dir = os.path.join(target_dir, 'image')
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.md':
                file_path = os.path.join(root, file)
                handle_file(file_path, img_dir)


if __name__ == '__main__':
    target = os.curdir
    run(target)
