# put your code here.
def wordcount(filename):
    text_file = open(filename)

    count = {}
    for line in text_file:
        line_list = line.split()

        for word in line_list:
            word_without_punc = word.strip(',').strip('?').strip('.')
            count_num = count.get(word_without_punc, 0)
            count_num += 1
            count[word_without_punc] = count_num
    for key, value in count.items():
        print key, value

wordcount('test.txt')

