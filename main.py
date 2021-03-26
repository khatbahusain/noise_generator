import pandas as pd
import os
import glob
import random



def clean(data):
    df = data.copy()
    return df.to_csv('output/test#clean.csv', index=False)

def df_misspelled(data):
    df = data.copy()   
    ## define all letters we want to change by adding
    ## .map(lambda x: x.replace('s','x'))
    df['Questions'] = df['Questions'].map(lambda x: x.replace('m','n'))
    return df.to_csv('output/test#df_misspelled.csv', index=False)
    
def df_misspelled2(data):
    df = data.copy()
    ## define all letters we want to change
    df['Questions'] = df['Questions'].map(lambda x: x.replace('s','x')).map(lambda x: x.replace('m','n'))
    return df.to_csv('output/test#df_misspelled2.csv', index=False)
    
def remove_first_letter(data):
    df = data.copy()
    df['Questions'] = df['Questions'].map(lambda x: x[1:])
    return df.to_csv('output/test#remove_first_letter.csv', index=False)

def remove_2_first_letters(data):
    df = data.copy()
    df['Questions'] = df['Questions'].map(lambda x: x[1:])
    return df.to_csv('output/test#remove_2_first_letters.csv', index=False)
    
def remove_3_first_letters(data):
    df = data.copy()
    df['Questions'] = df['Questions'].map(lambda x: x[1:])
    return df.to_csv('output/test#remove_3_first_letters.csv', index=False)
    

def double_first_letter(data):
    df = data.copy()
    df['Questions'] = df['Questions'].map(lambda x: x[0] + x)
    return df.to_csv('output/test#double_first_letter.csv', index=False)
    
def double_last_letter(data):
    df = data.copy()
    df['Questions'] = df['Questions'].map(lambda x: x + x[-1])
    return df.to_csv('output/test#double_last_letter.csv', index=False)
    
def remove_first_letter_every_word(data):
    df = data.copy()
    df['Questions'] = df['Questions'].map(lambda x: ','.join([i[1:] for i in x.split()]).replace(',', ' '))     
    return df.to_csv('output/test#remove_first_letter_every_word.csv', index=False)
    
def add_one_emoji_at_first(data):
    df = data.copy()
    emojies = pd.read_csv('emoji_df.csv')['emoji']        
    df['Questions'] = df['Questions'].map(lambda x: random.choice(emojies) + x)
    return df.to_csv('output/test#add_one_emoji_at_first.csv', index=False)

def add_one_emoji_at_last(data):
    df = data.copy()
    emojies = pd.read_csv('emoji_df.csv')['emoji']        
    df['Questions'] = df['Questions'].map(lambda x: x + random.choice(emojies)) 
    return df.to_csv('output/test#add_one_emoji_at_last.csv', index=False)


def add_one_number_at_first(data):
    df = data.copy()
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] 
    df['Questions'] = df['Questions'].map(lambda x: x + random.choice(numbers))
    return df.to_csv('output/test#add_one_number_at_first.csv', index=False)
    
 
def add_one_number_at_last(data):
    df = data.copy()
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] 
    df['Questions'] = df['Questions'].map(lambda x:  random.choice(numbers) + x)
    return df.to_csv('output/test#add_one_number_at_last.csv', index=False)


def add_special_characters(data):
    df = data.copy()
    numbers = ['/', '*', '#', '&', '{', '@', '-', '|', '+', ';'] 
    df['Questions'] = df['Questions'].map(lambda x:  random.choice(numbers) + x)
    return df.to_csv('output/test#add_special_characters.csv', index=False)
    

def remove_whitespace(data):
    df = data.copy()
    df['Questions'] = df['Questions'].map(lambda x:  x.replace(' ', ''))
    return df.to_csv('output/test#remove_whitespace.csv', index=False)
    
    
if __name__ == "__main__":
    input_file = glob.glob('input/' + "/*.csv")
    
    try:
        os.mkdir('output')
    except:
        pass
    
    for t in input_file:
        
        data = pd.read_csv(t, error_bad_lines=False)
        clean(data)
        df_misspelled(data)
        df_misspelled2(data)
        remove_first_letter(data)
        remove_2_first_letters(data)
        remove_3_first_letters(data)
        double_first_letter(data)
        double_last_letter(data)
        remove_first_letter_every_word(data)
        add_one_emoji_at_first(data)
        add_one_emoji_at_last(data)
        add_one_number_at_first(data)
        add_one_number_at_last(data)
        add_special_characters(data)
        remove_whitespace(data)
        
    print('Done !')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

