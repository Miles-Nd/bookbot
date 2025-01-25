def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)


with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def count(text):
    words=text.split()
    return len(words)


def letter_count(text):
    lower_text=text.lower()
    count={}
    for letter in lower_text:
        if letter not in count:
            count[letter]=1
        else:
            count[letter]+=1
    return count  

print("--- Begin report of books/frankenstein.txt ---")
word_count=len(file_contents.split())
print(f"{word_count} words found in the document")

def report(text):
    lower_text=text.lower()
    count={}
    for letter in lower_text:
        if not letter.isalpha():
            continue
        elif letter not in count:
            count[letter]=1
        else:
            count[letter]+=1
    return count

frank_dict=report(file_contents)

def sorting(entry):
    return entry["quantity"]

frank_list=[{"letter": letter, "quantity": quantity} for letter, quantity in frank_dict.items()]

frank_list.sort(reverse=True, key=sorting)

for entry in frank_list:
    print(f"The '{entry['letter']}' character was found '{entry['quantity']}' times")

print("--- End report ---")