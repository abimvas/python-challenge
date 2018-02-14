#dependencies
import os

#file path
paragraph_1 = os.path.join("paragraph_1.txt")

#word count
with open(paragraph_1, newline="") as inputfile:
    words = [word for line in inputfile for word in line.split()]
    word_count = len(words)
    
    print("Paragraph Analysis")
    print("-------------------------")
    print("Approximate Word Count:", word_count)
    
#sentence count
with open(paragraph_1, newline="") as f:
    data = f.read()
    sentence_count = data.count(".")
    print("Approximate Sentence Count:", sentence_count)
    
#approx. letter count (per word)
with open(paragraph_1, newline="") as inputfile:
    words = [word for line in inputfile for word in line.split()]
    avg_word = sum(len(word) for word in words) / len(words)
    print("Average Letter Count", avg_word)
    
#average sentence length (in words)

with open(paragraph_1, newline="") as f:
    text = f.read()
    sents = text.split('.')
    avg_len = sum(len(x.split()) for x in sents) / len(sents)
    print("Average Sentence Length", avg_len)

#print to txt file
text_file = open("Output.txt", "w")
text_file.write("Paragraph Analysis")
text_file.write("\n---------------------")
text_file.write("\nApproximate Word Count:" + str(word_count))
text_file.write("\nApproximate Sentence Count:" + str(sentence_count))
text_file.write("\nAverage Letter Count" + str(avg_word))
text_file.write("\nAverage Sentence Length" + str(avg_len))
text_file.close()