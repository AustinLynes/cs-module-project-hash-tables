class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.buckets = [None] * capacity
        self.capacity = capacity 

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.

        The algorithm for our hash function comes from computer scientist Dan Bernstein.
        It uses bit manipulation and prime numbers to create a hash index from a string.

        """
        # Your code here
        
        # set the hash
        hash = 5381

        # encode the string
        byte_arr = key.encode('utf-8')
        
        # hash each index in encoded_string

        for byte in byte_arr:
            hash = ((hash * 33) ^ byte) % 0x100000000 # 65536
            # using the modulus keeps 32-bit so int doesnt overflow
        return hash
    
    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        _hash = self.djb2(key)
        _index = self.hash_index(key)

        entry = HashTableEntry(key, value)
              
        self.buckets[_index] = entry

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        _hash = self.djb2(key)
        _index = self.hash_index(key)

        # check to see if the entry exists
        _exists = self.buckets[_index]
        # check to see if exists is not None
        if _exists:
            last = None
            # while exists is not None
            while _exists:
                # if we find a match... remove it..
                if _exists.key == key:
                    # we found something
                    if last:
                        last.next = _exists.next
                    else:
                        self.buckets[_index] = _exists.next
                
                # if we made it this far there needs to be a swap so the newer item is stored...
                last = _exists
                _exists = _exists.next
        
            



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        _hash = self.djb2(key)
        _index = self.hash_index(key)

        _lookup = self.buckets[_index]

        if _lookup:
            while _lookup:
                ## we found something
                if _lookup.key == key:
                    return _lookup.value
                    
                _lookup = _lookup.next;
        
        return None

        # Your code here

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
