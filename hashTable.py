class HashTable:
    """
    A hash table implementation using separate chaining to store packages by ID.
    This hash table is an array(list) of buckets, each bucket is a list of (key, value) pairs.
    Collisions are handled by appending multiple pairs into the same bucket(chaining).
    """
    def __init__(self, bucket_size=10 ):
        """
        Initialize the hash table with the given bucket size (10).
        First store the bucket size, then create a lost of empty lists,
        one for each bucket.
        """
        self.bucket_size = bucket_size
        self.buckets_list = [[] for _ in range(bucket_size)]
    def _hash_function(self, package_id):
        """
        Returns the hash value for the given package_id.
        First computes package_id modulo bucket_size,then uses the
        result as an index into self.buckets_list.
        """
        bucket_index = package_id % self.bucket_size
        return bucket_index

    def insert(self, package_id, package):
        """
        Inserts a package id number  and package info into the hash table.
        First the bucket index for the given package_id is computed, then we
        get the bucket index for the given package_id. Lastly we append
        a key, value tuple to that bucket, handling collisions by chaining the tuples.
        """
        index = self._hash_function(package_id)
        bucket = self.buckets_list[index]
        bucket.append((package_id, package))

    def lookup(self, package_id):
        """
        Looks up a package by its ID number and returns its package info.
        First the bucket index for the given package_id is computed, then we retrieve
        the bucket, which is a list of pairs (key, package). We then loop through each pair
        in the bucket and compare the stored key to the package id. If a matching key is found
        we return the package info. If no match is found, None is returned.
        """
        bucket_index = self._hash_function(package_id)
        bucket = self.buckets_list[bucket_index]
        for key, package in bucket:
            if key == package_id:
                return package
        return None





