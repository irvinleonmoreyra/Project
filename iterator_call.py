from iterator_class import SequenceNumber

def main():
    sequence_number=SequenceNumber(0,5)
    #print 0
    print(next(sequence_number))
    #print 1
    print(next(sequence_number))
    #print 2
    print(next(sequence_number))
    #and error ocurred: Stopiteration
    print(next(sequence_number))

if __name__=='__main__':
    main()
