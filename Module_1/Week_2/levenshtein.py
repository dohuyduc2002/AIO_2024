"""This module define function for AIO2024 Module 1 week 2 exercise."""
def leveshtein(word1 : str, word2: str) -> float:
    """Calculate leveshtein distance

    Args:
        word1 (str): Source word
        word2 (str): Target word

    Returns:
        int: Minimum distance
    """
    len_word1 = len(word1)
    len_word2 = len(word2)
    #create matrix with len_word1 + 1 row and len_word2 col + 1
    matrix = [[float('inf')] * (len_word2 + 1) for _ in range(len_word1 + 1)]
    #insantiate 1st row and col value of matrix
    for i in range(len_word1 + 1):
        matrix[i][0] = i
    #iterate through len_word1, append i to each row index
    for j in range(len_word2 + 1):
        matrix[0][j] = j
    #iterate through len_word2, append j to each row index
    # -> create the i col with value ranging from 0 -> len_word1
    # -> create the j col with value ranging from 0 -> len_word2
    #Fill the matrix
    for i in range(1,len_word1 + 1):
        for j in range(1,len_word2 + 1):
#iterate through every element of matrix, skipping the 1st row and cal which has been filled
            if word1[i - 1] == word2[j - 1]: #
                matrix[i][j] = matrix[i-1][j-1]
#the element of matrix gain the previous value from its main diagonal
            else:
                matrix[i][j] = 1 + min(matrix[i -1][j-1],matrix[i-1][j],matrix[i][j-1])
# Consider 1 of 3 operations, this lead to +1 in value of the element
# replace: i -1, j-1 cause 2 pointers decrese by 1 if matched to examine next case, len dont change
# addiction: i-1,j : the current pointer in word1 is decrese by one due to adding a char
# delete i,j-1 : if delete, the current pointer is increase by 1, len dont change
    print(matrix) 
    print(matrix[-1][-1])
    # return the last value of the main diagonal cause it's the shortest path
    return matrix[-1][-1] 

leveshtein('abc','cda')

