
class Span:
    """
    Span objects are used to define boundaries within other iterables.
    """
    def __init__(self, start, end):
        if not start <= end:
            raise ValueError('Start cannot be greater than or equal to End')

        self._start = start
        self._end = end

    @property
    def span(self):
        """
        Return the span start and end scalars
        :return: The start and end indexes
        """
        return self._start, self._end

    def __eq__(self, other):
        start, fin = other.span()
        return self._start == start and self._end == fin


class DistanceCalculator:
    """
    The ADistanceCalculator class defines a metric on strings. It is a way of determining the distance from
    one string to another.
    """

    def __init__(self, insert_cost=1, deletion_cost=1, subst_cost=1):
        """
        The constructor for the distance calculator. The insert, deletion, and substitution cost can be specified
        as state for the object.
        :param insert_cost:
        :param deletion_cost:
        :param subst_cost:
        """
        self._insert_cost = insert_cost
        self._deletion_cost = deletion_cost
        self._subst_cost = subst_cost

    def distance(source, target):

	    #length of each word
	    l_target = len(target) #length of target
	    l_source = len(source) #length of source

	    #add one unit to length of word(s)
	    lT = l_target + 1 # target length plus one
	    lS = l_source + 1 # source length plus one

	    #create a matrix
	    matrix = [[0 for y in range(lT)] for x in range(lS)] 

	    #Initialize column
	    for x in range(lS):
		    matrix[x][0] = x

	    #Initialize row
	    for y in range(lT):
		    matrix[0][y] = y

	    for x in range(1,lS):
		    for y in range(1,lT):

			    if target[y-1] == source[x-1]: # provided letters are equal
				    matrix[x][y] = matrix[x-1][y-1]
			    else:							# when letters are not equal, add one to distance
				    matrix[x][y] = min([matrix[x-1][y],matrix[x][y-1],matrix[x-1][y-1]]) + 1
	    print(matrix)
	    print("")
	    return matrix[l_source][l_target]

    sWord = input("Enter source word : ")
    tWord = input("Enter target word : ")
    res = distance(tWord,sWord)
    print(res)
