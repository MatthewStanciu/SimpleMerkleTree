import hashlib


def turn_into_hash(hash_list):  # This is here just in case your example is like mine and you need to hash them first
    hashed_hashlist = []
    for item in hash_list:
        item = hashlib.sha256(('b' + item).encode('utf-8')).hexdigest()
        hashed_hashlist.append(item)

    return hashed_hashlist


def create_tree(hash_list):
    child_hash_list = []
    # Starting at the first entry, through each entry in the hash list, grouping every 2 entries
    for index in range(0, len(hash_list)-1, 2):

        if len(list(hash_list[index])) != 64:
            hash_list = turn_into_hash(hash_list)

        left = hash_list[index]
        right = hash_list[index + 1]

        child_hash_list.append(left + right)  # Group the hashes

    if len(hash_list) % 2 == 1:  # If there is an odd number, keep hashing the last thing to itself
        child_hash_list.append(hash_list[-1])  # Append the last element

    if len(hash_list) == 1:
        print("Merkle root:")
        return hash_list[0]

    return create_tree(child_hash_list)  # Keep calling this function until the hash list length is 1
