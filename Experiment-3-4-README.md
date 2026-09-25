# Text Analytics Lab — README for Experiment 3 & Experiment 4

A beginner-friendly, step-by-step guide. No prior NLP experience assumed — just basic Python (variables, strings, lists).

---

## 0. One-Time Setup (do this before either experiment)

### Step 1: Install Python packages
Open your terminal / command prompt and run:

```bash
pip install nltk wordcloud matplotlib
```

- `nltk` = Natural Language Toolkit (does tokenizing, stopwords, lemmatization, NER)
- `wordcloud` = draws the word-cloud picture
- `matplotlib` = draws graphs/pictures in Python

### Step 2: Download NLTK's data files
NLTK needs extra "data packs" (dictionaries, tagged corpora, etc.) that don't come with `pip install`. Create a new Python file, e.g. `setup_nltk.py`, and run this **once**:

```python
import nltk

nltk.download('punkt')            # for tokenization (splitting text into words/sentences)
nltk.download('punkt_tab')        # newer NLTK versions need this too
nltk.download('stopwords')        # common words like "the", "is", "and"
nltk.download('wordnet')          # dictionary used for lemmatization
nltk.download('omw-1.4')          # supports wordnet
nltk.download('averaged_perceptron_tagger')      # for POS tagging (needed for NER)
nltk.download('averaged_perceptron_tagger_eng')  # newer NLTK versions
nltk.download('maxent_ne_chunker')     # for Named Entity Recognition
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')            # word list used by NER
```

Run it: `python setup_nltk.py`. A window may pop up, or it will just download in the terminal — either is fine. You only need to do this once on your machine.

### Step 3: Get a sample text file
Both experiments need a `.txt` document to work with. Create a file called `sample.txt` in the same folder as your code, and paste in a few paragraphs of any English text (a news article, a Wikipedia paragraph, anything). 3–4 paragraphs is enough to get interesting results.

---

## Experiment 3 — Processing Data

**Goal:** Read a text file → clean it up → understand its grammatical structure.

This has 2 parts:
- **Part A:** Basic pre-processing (tokenization, stop-word removal, lemmatization)
- **Part B:** Morphological analysis (studying word structure — prefixes, suffixes, root forms)

### Part A: Tokenization, Stop-word Removal, Lemmatization

**What these words mean, in plain English:**
| Term | Meaning |
|---|---|
| Tokenization | Splitting text into individual words (or sentences) |
| Stop-words | Very common words ("the", "is", "a", "and"...) that carry little meaning and are often removed |
| Lemmatization | Reducing a word to its dictionary/base form — e.g. "running" → "run", "better" → "good" |

**Code:**

```python
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# --- Step 1: Read the text file ---
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

print("----- ORIGINAL TEXT (first 300 chars) -----")
print(text[:300])

# --- Step 2: Tokenization ---
# Split the whole text into sentences
sentences = sent_tokenize(text)
print("\nNumber of sentences:", len(sentences))

# Split the whole text into words
words = word_tokenize(text)
print("Number of words (tokens):", len(words))
print("First 20 word tokens:", words[:20])

# --- Step 3: Stop-word Removal ---
stop_words = set(stopwords.words('english'))

# Keep only alphabetic words (removes punctuation/numbers), and lowercase them
words_clean = [w.lower() for w in words if w.isalpha()]

# Now remove the stop words
words_no_stopwords = [w for w in words_clean if w not in stop_words]

print("\nWords before stop-word removal:", len(words_clean))
print("Words after stop-word removal :", len(words_no_stopwords))
print("Sample:", words_no_stopwords[:20])

# --- Step 4: Lemmatization ---
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(w) for w in words_no_stopwords]

print("\nSample BEFORE lemmatization:", words_no_stopwords[:10])
print("Sample AFTER  lemmatization:", lemmatized_words[:10])
```

**What just happened, line by line:**
1. We opened and read the whole `.txt` file into one big string called `text`.
2. `sent_tokenize()` split that string into a list of sentences.
3. `word_tokenize()` split it into a list of individual words/punctuation marks.
4. We filtered out anything that isn't a pure word (`.isalpha()` drops numbers/punctuation) and lowercased everything, so "The" and "the" count as the same word.
5. We removed common "noise" words using NLTK's built-in English stop-word list.
6. `WordNetLemmatizer` converted each remaining word to its base dictionary form.

Run this file (`python experiment3a.py`) and check the printed output at each stage — you should visibly see the list shrink and change as you go through Steps 3 and 4.

### Part B: Morphological Analysis

**Plain-English meaning:** Morphology = the study of how words are built from smaller meaningful pieces (called *morphemes*) — roots, prefixes, and suffixes. Example: "unhappiness" = `un-` (prefix) + `happy` (root) + `-ness` (suffix).

A simple way to *study and implement* this at a beginner level is to use **stemming** (a cruder cousin of lemmatization that chops off suffixes) and compare it with lemmatization, plus manually break down a few words.

```python
from nltk.stem import PorterStemmer, WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

sample_words = ["running", "happiness", "unhappiness", "studies", "better",
                 "flying", "connection", "nationality"]

print(f"{'Word':15}{'Stem':15}{'Lemma':15}")
print("-" * 45)
for w in sample_words:
    stem = stemmer.stem(w)
    lemma = lemmatizer.lemmatize(w)
    print(f"{w:15}{stem:15}{lemma:15}")
```

**What to observe (write this in your lab record):**
- **Stemming** just chops letters off using rules (e.g. "happiness" → "happi") — fast but sometimes produces non-words.
- **Lemmatization** looks up the real dictionary root (e.g. "happiness" → "happiness" stays, "better" → "good") — slower but linguistically correct.
- This comparison **is** your morphological analysis: it shows how words are decomposed into root forms, and how prefixes/suffixes (`un-`, `-ness`, `-ing`, `-s`) get stripped or normalized.

You can also manually annotate a couple of words in your report, e.g.:
`unhappiness = un (prefix) + happy (root, spelling-adjusted) + ness (suffix)`

---

## Experiment 4 — Text Mining: Word Frequency, Word Cloud, NER

**Goal:** Find the most common words in a document, visualize them, and identify named entities (people, places, organizations).

### Part 1: Word Count, Top 10 Frequent Words, Word Cloud

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# --- Step 1: Read the document ---
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

# --- Step 2: Clean and tokenize ---
words = word_tokenize(text)
stop_words = set(stopwords.words('english'))
clean_words = [w.lower() for w in words if w.isalpha() and w.lower() not in stop_words]

# --- Step 3: Word count (frequency of every word) ---
word_freq = Counter(clean_words)
print("Total unique words:", len(word_freq))

# --- Step 4: Top 10 most frequent words ---
top_10 = word_freq.most_common(10)
print("\nTop 10 frequent words:")
for word, count in top_10:
    print(f"{word:15} -> {count}")

# --- Step 5: Show top 10 as a bar graph ---
words_list, counts_list = zip(*top_10)
plt.figure(figsize=(10, 5))
plt.bar(words_list, counts_list, color="skyblue")
plt.title("Top 10 Most Frequent Words")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top10_words.png")   # saves the chart as an image
plt.show()

# --- Step 6: Create and show a word cloud ---
wc = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_freq)

plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud")
plt.savefig("wordcloud.png")
plt.show()
```

**What just happened:**
1. Read + tokenized + cleaned the text exactly like in Experiment 3.
2. `Counter` is a Python tool that counts how many times each item (word) appears in a list — it hands you a frequency table for free.
3. `.most_common(10)` grabs the 10 highest-frequency entries.
4. `matplotlib` draws a simple bar chart of those 10 words vs. their counts.
5. `WordCloud` turns the *whole* frequency dictionary into a picture where bigger word = more frequent.

Both images (`top10_words.png`, `wordcloud.png`) get saved in your folder **and** pop up on screen when you run the script.

### Part 2: Named Entity Recognition (NER)

**Plain-English meaning:** NER means automatically finding and labeling real-world things in text — like people's names, places, organizations, and dates.

```python
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# --- Step 1: Read the document ---
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

# --- Step 2: Tokenize into words ---
tokens = word_tokenize(text)

# --- Step 3: POS tagging (label each word: noun, verb, proper noun, etc.) ---
pos_tags = pos_tag(tokens)
print("Sample POS tags:", pos_tags[:10])

# --- Step 4: Named Entity Recognition ---
ner_tree = ne_chunk(pos_tags)

print("\nNamed Entities found:")
for chunk in ner_tree:
    if hasattr(chunk, 'label'):   # only "chunks" (not plain words) have a label
        entity_name = " ".join(c[0] for c in chunk)
        entity_type = chunk.label()
        print(f"{entity_name:25} -> {entity_type}")
```

**What just happened:**
1. We tokenized the text into words again.
2. `pos_tag()` labels each word with its part of speech (noun, verb, proper noun `NNP`, etc.) — NER needs this info first.
3. `ne_chunk()` groups sequences of tagged words into "chunks" and labels the meaningful ones as `PERSON`, `ORGANIZATION`, `GPE` (geo-political entity, i.e. place), etc.
4. We loop through the result: plain words are skipped, and only labeled chunks (the actual entities) are printed.

**Tip:** NER works best on text that has proper nouns — capitalized names of people, companies, or cities. A generic paragraph with no names will return very few entities, so make sure your `sample.txt` includes some real names/places for a richer result.

---

## Quick Troubleshooting

| Problem | Fix |
|---|---|
| `LookupError: Resource punkt not found` | Re-run the `nltk.download(...)` lines from Step 2 |
| `FileNotFoundError: sample.txt` | Make sure `sample.txt` is in the same folder as your `.py` file |
| Word cloud / chart window doesn't appear | Check the saved `.png` file in your folder instead — it saved even if the popup didn't show |
| NER finds almost nothing | Use text with real names of people/places/companies |

---

## Suggested File Structure

```
your-lab-folder/
├── setup_nltk.py          (run once)
├── sample.txt              (your input text)
├── experiment3.py          (Part A + Part B code combined)
└── experiment4.py          (Part 1 + Part 2 code combined)
```
