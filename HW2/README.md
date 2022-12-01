# HW2
The purpose of this exercise is to implement the hidden Markov model using the Python language and to train and evaluate it on sequences of English alphabets.
In this exercise, you are given the set of observation symbols, the set of states, the transition probability of the states, the initial probability of the states,
and the distribution function of the observations in each state. Also, five independent sets of data are provided to train five separate hidden Markov models.
After training five models using the Baum-Welch algorithm, which is based on the maximum expectation algorithm and discussed in detail in class, you evaluate 
them on two sets of test data using the Viterbi algorithm. For each sample of the test data sets, you must determine which model maximizes the probability of 
the observations.

In the attachment of this exercise, there is a zip file whose content is as follows:

### model_init.txt
This file contains the initial probability of the states, the transition probability of the states and the distribution function of observations in each state.
The general format of the file is as follows:


initial: 6

0.2 0.1 0.2 0.2 0.2 0.1


transition: 6

0.3 0.3 0.1 0.1 0.1 0.1

0.1 0.3 0.3 0.1 0.1 0.1

0.1 0.1 0.3 0.3 0.1 0.1

0.1 0.1 0.1 0.3 0.3 0.1

0.1 0.1 0.1 0.1 0.3 0.3

0.3 0.1 0.1 0.1 0.1 0.3


observations: 6

0.2 0.2 0.1 0.1 0.1 0.1

0.2 0.2 0.2 0.2 0.1 0.1

0.2 0.2 0.2 0.2 0.2 0.2

0.2 0.2 0.2 0.2 0.2 0.2

0.1 0.1 0.2 0.2 0.2 0.2

0.1 0.1 0.1 0.1 0.2 0.2

The words transition, initial and observation state that the following data represent which of the initial probability of states, the probability of transition of
states and the distribution function of observations. The number written in front of initial indicates the number of cases, and in the next line, the probability of
cases separated by a space is located. The number in front of transition also indicates the number of cases, and if the number of cases is N, we will have N lines in
the continuation, where the jth element of the i-th line represents aij) the probability of transition from state i to j). Finally, after the observation keyword, 
the number of observation symbols is mentioned, and if this value is equal to M, then we will have M line in the continuation, where the jth element of the i-th line
represents bij (the probability of observing the i-th symbol in the j-th state).

### seq_model_01~05.txt
These files contain training data for each model. Each line represents the training data. The viewing symbols are all uppercase letters of the English alphabet. For example, if the number of observation symbols is 4, the set of symbols is as follows
 Is.

### modellist.txt
In each line of this file, the names of the files in which the parameters of the built models are placed are given.

### testing_data1~2.txt
The test data are located in these files.

### testing_answer.txt
Each line of this file is the name of the model that calculates the probability of observations for the data in the corresponding line in the file. The maximum is testing_data1.txt. The structure of the code files in your code folder will include two files, py.train and py.test, which are commands related to training. and include model evaluation. Also, you will have a py.hmm file that contains all the codes related to the implementation of the hidden Markov model (including Baum-Welch and Viterbi algorithms for model training and evaluation).
