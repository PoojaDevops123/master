import re
import string
from string import punctuation
from transformers import PegasusForConditionalGeneration, PegasusTokenizer, pipeline
import spacy
import torch
from newspaper import Article
from spacy.lang.en.stop_words import STOP_WORDS
import PyPDF2

# #--------------- PDF TEXT EXTRACTION ------------------#

# pdffileobj=open(r'final_yolo.pdf','rb')
# pdfreader=PyPDF2.PdfFileReader(pdffileobj)
# x=pdfreader.numPages
# content = ""
# for i in range (x):
#         pageobj=pdfreader.getPage(i)
#         content=pageobj.extractText()
#         print (content)


#         # file1=open(r"1.txt","a")
#         # file1.truncate(0)
#         # file1.writelines(content)
#         # file1.close()

# text = re.sub("https?:\/\/.*[\r\n]*", "", content)
# text = re.sub("#", "", text)  # hash nikalre idhar
# punct = set(string.punctuation)  # iske lie string library import karna hai
# text = "".join([ch for ch in text if ch not in punct])  # this is for removing punctuation

# text = text.encode(encoding="ascii", errors="ignore")  # encoding the text to ASCII format

# text = text.decode()  # encoding the text to ASCII format

# clean_text = " ".join([word for word in text.split()])  # cleaning the text to remove extra whitespace
# text = str(clean_text.lower())

# ---------------- URL TEXT EXTRACTION -----------------#

def throughURL(url):
    device = torch.device("cuda")
    link_paper = (
        'https://www.freecodecamp.org/news/python-remove-character-from-a-string-how-to-delete-characters-from-strings/')
    article = Article(link_paper)
    article.download()
    article.parse()
    input_text = article.text
    input_text = ' '.join(input_text.split())

    text = re.sub("https?:\/\/.*[\r\n]*", "", input_text)
    text = re.sub("#", "", text)  # hash nikalre idhar
    punct = set(string.punctuation)  # iske lie string library import karna hai
    # this is for removing punctuation
    text = "".join([ch for ch in text if ch not in punct])

    # encoding the text to ASCII format
    text = text.encode(encoding="ascii", errors="ignore")

    text = text.decode()  # encoding the text to ASCII format

    # cleaning the text to remove extra whitespace
    clean_text = " ".join([word for word in text.split()])
    clean_text = str(clean_text.lower())

    # --------------- Spacy model ------------------#
    # text_file = open("1.txt", "r")
    # text = text_file.read()
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(clean_text)
    tokens = [token.text for token in doc]
    punctuation = ''
    punctuation = punctuation + '\n' + '\n\n'
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in STOP_WORDS:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1

    max_frequcncy = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequcncy

    sentence_tokens = [sent for sent in doc.sents]

    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

    from heapq import nlargest

    select_length = int(len(sentence_tokens)*0.3)
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    final_summary = [word.text for word in summary]
    first_summary = ' ' .join(final_summary)
    print(first_summary)

    model_name = "google/pegasus-cnn_dailymail"

    # Load pretrained tokenizer
    pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)

    pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name)

    # Create tokens
    tokens = pegasus_tokenizer(
        clean_text, truncation=True, padding="max_length", return_tensors="pt")

    encoded_summary = pegasus_model.generate(**tokens)
    # Decode summarized text
    decoded_summary = pegasus_tokenizer.decode(
        encoded_summary[0],
        skip_special_tokens=True
    )
    # print(decoded_summary)
    summarizer = pipeline(
        "summarization",
        model=model_name,
        tokenizer=pegasus_tokenizer,
        framework="pt"
    )

    summary = summarizer(clean_text, min_length=30, max_length=150)

    summary = summary[0]["summary_text"]

    return str(summary)
