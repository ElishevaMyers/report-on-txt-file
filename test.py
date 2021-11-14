import sys
inFile = sys.argv[0]

# global file, results will be here
report_file = open("report.txt", 'w')


# Writing results to report file.
def write_to_file(result):
    global report_file
    report_file.write(result + '\n')


# 1.
# Number of lines in file.
def num_of_lines(f_name):
    # using len() of the list that readlines() returns
    num_lines = len(open(f_name).readlines())
    text_report = "Number of lines in file: " + str(num_lines)
    write_to_file(text_report)


# 2.
# Number of words in file.
def num_of_words(f_name):
    word_count = 0
    for line in open(f_name).readlines():
        word_count += len(line.split())

    text_report = "Number of words in file: " + str(word_count)
    write_to_file(text_report)


# 3.
# Unique words in file.
def unique_words(f_name):
    text_file = open(f_name)
    text = text_file.read()

    # cleaning
    text = text.lower()
    words = text.split()
    words = [word.strip('.,!;()[]') for word in words]
    words = [word.replace("'s", '') for word in words]

    # finding unique
    unique = set(words)
    num_unique = len(unique)
    text_report = "Number of unique words in file: " + str(num_unique)
    write_to_file(text_report)


# 4.
# Average length of sentence in file.
def average_len_of_sentence(f_name):
    text_file = open(f_name)
    text = text_file.read()

    sents = text.split('.')
    # counting words in sentence by split, summering
    avg_len = sum(len(x.split()) for x in sents) / len(sents)

    text_report = "Average length of sentence in file: " + str(avg_len)
    write_to_file(text_report)

    # longest sentence
    max_sents = max(sents, key=len)
    len_max_sents = len(max_sents.split())
    text_report = "    The longest sentence in file: " + str(len_max_sents)
    write_to_file(text_report)


# Find the most repeated word in a text file.
def most_repeated_word(f_name):
    text_file = open(f_name)
    text = text_file.read()
    # splits each line into words and removing spaces and punctuations from the input
    text = text.lower()
    words = text.split()
    words = [word.strip('.,!;()[]') for word in words]
    words = [word.replace("'s", '') for word in words]

    frequent_word = ""
    frequency = 0

    # Finding the max occurred word
    for i in range(0, len(words)):

        # Declaring count
        count = 1

        # Count each word in the file
        for j in range(i + 1, len(words)):
            if words[i] == words[j]:
                count = count + 1

        # If the count value is more than highest frequency then
        if count > frequency:
            frequency = count
            frequent_word = words[i]

    text_report = "Most repeated word in file: " + frequent_word
    write_to_file(text_report)
    frequency_report = "    Frequency: " + str(frequency)
    write_to_file(frequency_report)


# Longest sequence without 'k'.
def max_without_k(f_name):
    text_file = open(f_name)
    text = text_file.read()
    # splits each line into words and removing spaces and punctuations from the input
    text = text.lower()
    words = text.split()
    words = [word.strip('.,!;()[]') for word in words]

    substring = "k"
    max_count = 0
    # Finding the max seq
    for i in range(0, len(words)):
        words_no_k = []
        if substring not in words[i]:
            words_no_k.append(words[i])

            for j in range(i + 1, len(words)):
                if substring not in words[j]:
                    words_no_k.append(words[j])

                else:
                    count_words = len(words_no_k)
                    words_no_k.clear()
                    if max_count < count_words:
                        max_count = count_words
                    break
                if len(words) == len(words_no_k):
                    max_count = len(words)
                    break

    text_report = "Longest sequence without 'k': " + str(max_count)
    write_to_file(text_report)


def main():
    in_file = input("Please enter file name: ")

    #check if file exists
    try:
        f = open(in_file, 'r')
        f.close()
    except FileNotFoundError:
        msg = "Sorry, the file " + in_file + " does not exist."
        print(msg)  # Sorry, the file John.txt does not exist.

    write_to_file("Statistics report on " + in_file + " file:\n")
    num_of_lines(in_file)
    num_of_words(in_file)
    unique_words(in_file)
    average_len_of_sentence(in_file)
    most_repeated_word(in_file)
    max_without_k(in_file)
    report_file.close()


if __name__ == "__main__":
    main()
