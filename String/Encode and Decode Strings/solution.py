class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if len(strs) == 0:
            return '#'

        encoded_str = ''
        head = ''
        for this_str in strs:
            size = len(this_str)
            head = head + str(size) + ','
            encoded_str = encoded_str + this_str

        encoded_str = head + '#' + encoded_str
        return encoded_str



    def decode(self, encoded_str: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if encoded_str == '#':
            return []

        decoded_str_list = []
        delim_index = encoded_str.find('#')
        str_size_list = encoded_str[:delim_index-1].split(',')
        str_candidates = encoded_str[delim_index+1:]
        start = 0
        for this_size in str_size_list:
            this_size = int(this_size)
            this_str = str_candidates[start:start+this_size]
            decoded_str_list.append(this_str)
            start = start + this_size
        return decoded_str_list



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
