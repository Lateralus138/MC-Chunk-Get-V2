def mc_chunk_get(x,z,verbose=False,string=False):
    '''Get the pair of boundary coordinates
    in a chunk by providing any x, z
    coordinates in that chunk.
    
    Creates an object with X1 X2 Z1 Z2 as
    X1,Z1 to X2,Z2 pairs.

    @USAGE:
        - mcChunkBounds=mc_chunk_get(200,300)
            - print(str(mcChunkBounds['X1'])) == 192
            - print(str(mcChunkBounds['Z1'])) == 288
            - print(str(mcChunkBounds['X2'])) == 207
            - print(str(mcChunkBounds['Z2'])) == 303
        - mc_chunk_get(200,300,verbose=True)
            - 192,288 to 207,303
        - strng=mc_chunk_get(200,300,string=True)
            - print(strng)'''
    # x, z = int(x), int(z)
    if not (isinstance(x,int) and
        isinstance(z,int)): return
    while (x%16)!=0: x-=1
    while (z%16)!=0: z-=1
    strng=str(str(x) + ' , ' + str(z) + ' to ' + str(x+15) + ' , ' + str(z+15))
    if verbose:
        print(strng)
        return
    if string:
        return strng
    return {'X1':int(x),'Z1':int(z),'X2':int(x+15),'Z2':int(z+15)}
def greatest_num(*nums):
    '''Get the largest number in a list of numbers.
    
    @Usage:
        - greatest_num([1,2,3,4,5]) == 5'''
    init=nums[0]
    for num in nums:
        if (num>init):
            init=num
    return init