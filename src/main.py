from string_utils import reverse_string,to_upper,to_lower,count_vowels

if __name__ =='__main__':
    sample = 'Hello World'
    
    print('Original',sample)
    print('Reversed :',reverse_string(sample))
    print('Upper case :',to_upper(sample))
    print('Lower case :',to_lower(sample))
    print('Vowels count :',count_vowels(sample))