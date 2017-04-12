# Words-Unscrambler-Python-

<p>
Given a sentence with scrambled words tries to rebuild the correct sentence.


The basic idea is to build a sentence from a given set of scrambled words, for example : "The blue is house" would become "The house is blue"
The programmed is basically a Markov Text Generator, the generator analyzes the words and the probability of occurrence of n-consecutive words and then generates chains of words that are probably related.
N-Gram probabilities come from a training database 
<p>Ex: P(the,gray,robot) = P(robot|gray) P(gray|the) P(the|'start') </p>
</p>

<h2>Parsing </h2>
<p scolor: red;>
In parsing we generate the training database. In order to do this we created a very large file (based on public domain books from Project Gutenberg, and internet texts) then saved as a UTF-8 encoded text file
Since this project was developed for a Mobile Robotics class we tried to add a large amount of texts that would capture this context.
In parse mode, the program will create a .db file containing nformation about the frequency that words follow other words in the input training text file.
</p>

<p>
>> python markovgen.py parse <name> <depth> <file>
</p>
where:
name = any name chosen for the training db
depth= number of n-grams (min 2)
file = location+ name of source training file


<h2>Generating Sentence </h2>
To generate new sentences, run the program in generate mode, using the name specified during the parse operation. The scrambled sentence is saved on a file named try.txt (we needed it to be saved instead of requesting input from a user, but this can be easily modified)
<p>
>> python markovgen.py gen <name>
</p>
 where name = database name 
