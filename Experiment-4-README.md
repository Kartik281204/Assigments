# Experiment 4 — Text Mining: A Complete Beginner's Guide

**Title (from your lab manual):** *Do text mining on extracted data and accessing text corpus*
1. Calculate word count of a given specific document and show top 10 frequent words with their frequency, and create a word cloud shown graphically.
2. Study and Implementation of NER (Named Entity Recognition).

This guide assumes **zero prior programming/NLP experience** beyond knowing what a variable, a list, and a `for` loop are. Every concept is explained with an analogy before any code appears, and every line of code is commented and then explained again afterward in plain English.

---

## Table of Contents
1. [Before You Start](#before-you-start)
2. [The Big Picture: What Is "Text Mining"?](#the-big-picture-what-is-text-mining)
3. [Part 1: Word Count, Top 10 Frequent Words, and a Word Cloud](#part-1-word-count-top-10-frequent-words-and-a-word-cloud)
4. [Part 2: Named Entity Recognition (NER)](#part-2-named-entity-recognition-ner)
5. [Full Combined Script](#full-combined-script)
6. [Understanding Your Output — What to Write in Your Lab Record](#understanding-your-output--what-to-write-in-your-lab-record)
7. [Common Mistakes & Troubleshooting](#common-mistakes--troubleshooting)
8. [Mini Glossary](#mini-glossary)

---

## Before You Start

### 1. Install the libraries you need
Open a terminal and run:
```bash
pip install nltk wordcloud matplotlib
```
`nltk` gives you the language-processing tools. `wordcloud` draws the picture in Part 1. `matplotlib` is the general-purpose charting library both parts use to actually *display* pictures on screen.

### 2. Download NLTK's data packs (one-time only)
`nltk` the *library* is just code — it needs separate *data files* to actually do anything useful (a stop-word list, a proper-noun classifier, etc.). Create `setup_nltk.py`:

```python
import nltk

nltk.download('punkt')                          # rules for splitting text into words/sentences
nltk.download('punkt_tab')                       # same, under a newer resource name
nltk.download('stopwords')                       # list of common English "filler" words
nltk.download('averaged_perceptron_tagger')       # trained model that assigns grammar tags (POS)
nltk.download('averaged_perceptron_tagger_eng')   # same, under a newer resource name
nltk.download('maxent_ne_chunker')               # trained model that groups words into named entities
nltk.download('maxent_ne_chunker_tab')           # same, under a newer resource name
nltk.download('words')                            # English word list the NER model checks against

print("Done — all NLTK resources for Experiment 4 are ready.")
```
Run `python setup_nltk.py` once. You'll see download progress in the terminal (or a small window that opens and closes) — either is normal.

### 3. Prepare your input document
Create a plain text file named `sample.txt` in the same folder as your code. For this experiment specifically, **include some real proper nouns** — names of people, companies, or cities — because Part 2 (NER) has nothing to find if your text is entirely generic. For example:

```
Rohan Sharma joined Maruti Suzuki as a Data Analyst in Delhi last year.
He works closely with the marketing department to study customer trends
across India. Maruti Suzuki, headquartered in Gurugram, is one of the
largest car manufacturers in the country. Rohan previously interned at
the Laadli Foundation, where he analyzed data related to child welfare
programs. His manager, Priya Nair, praised his analytical skills during
the quarterly review meeting held in Mumbai.
```
Feel free to substitute your own paragraph — just keep a few capitalized names/places in it.

---

## The Big Picture: What Is "Text Mining"?

Text mining means extracting *structured, useful information* out of *unstructured* free-form text. A human reading a document effortlessly notices "this is mostly about salaries" or "this mentions three company names" — text mining is about teaching a computer to notice the same things, automatically, at scale (imagine doing this over 10,000 documents instead of one).

Experiment 4 teaches you two of the most fundamental text-mining techniques:
- **Frequency analysis** (Part 1) — *what* is this document about, based on which words repeat most?
- **Named Entity Recognition** (Part 2) — *who/where/what organizations* does this document specifically talk about?

---

## Part 1: Word Count, Top 10 Frequent Words, and a Word Cloud

### Step-by-step concept

**Analogy first:** Imagine you're handed a printed essay and a highlighter, and told to tally, on a separate sheet, how many times every distinct word appears. That tally sheet is a **frequency distribution**. Once you have it, you can sort it to find the "most-used" words (your Top 10), and you can even draw each word bigger or smaller depending on its tally — that's a **word cloud**.

This part has 6 mini-steps:
1. Read the file
2. Break it into individual word tokens
3. Clean those tokens (remove punctuation, lowercase everything, remove stop-words)
4. Count how many times each cleaned word appears
5. Pull out and print the top 10
6. Draw both a bar chart and a word cloud from those counts

### The code — Step 1 & 2: Read and Tokenize

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Open the file in READ mode ("r"), using UTF-8 text encoding (handles
# special characters safely). The "with" block automatically closes
# the file when we're done — you don't need to call file.close() yourself.
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()          # .read() loads the entire file as one big string

# word_tokenize() splits that big string into a LIST of tokens —
# individual words AND punctuation marks each become their own item.
# Example: "Rohan joined Maruti Suzuki." becomes
#          ['Rohan', 'joined', 'Maruti', 'Suzuki', '.']
words = word_tokenize(text)
print("Total raw tokens (including punctuation):", len(words))
```

**Why tokenize at all, instead of just using `.split()`?** Python's built-in `.split()` only breaks on whitespace, so `"Suzuki."` would stay glued together as one token including the period. NLTK's `word_tokenize()` is trained to correctly separate punctuation, handle contractions ("don't" → "do", "n't"), and other edge cases a plain `.split()` gets wrong.

### The code — Step 3: Clean the tokens

```python
# stopwords.words('english') gives us NLTK's built-in list of ~180
# extremely common English words. We convert it to a set() because
# checking membership in a set is much faster than in a list — this
# matters once you're checking thousands of words.
stop_words = set(stopwords.words('english'))

# This is a list comprehension — a compact for-loop that builds a new
# list in one line. Reading it in plain English:
#   "For every token w in words:
#      IF w.isalpha() is True (meaning w contains ONLY letters — this
#        throws away punctuation like '.' and numbers like '2027')
#      AND w.lower() is not one of our stop-words,
#    THEN include w.lower() (the lowercased version) in the new list."
clean_words = [
    w.lower() for w in words
    if w.isalpha() and w.lower() not in stop_words
]

print("Tokens remaining after cleaning:", len(clean_words))
print("Sample cleaned tokens:", clean_words[:15])
```

**Why lowercase everything?** Without this, `"Data"` and `"data"` would be counted as two *different* words, artificially splitting their true combined frequency. Lowercasing guarantees every spelling variant of a word collapses into a single count.

**Why remove stop-words here specifically?** If we didn't, your "Top 10" list from Step 5 below would almost certainly just be `the, and, a, to, of, in...` for *any* English document — completely uninformative. Removing them lets the genuinely topic-specific words rise to the top.

### The code — Step 4 & 5: Count and rank

```python
# Counter is a special dictionary-like object built specifically for
# counting things. Handing it a list makes it walk through once and
# tally up how many times each unique item appears.
# Example: Counter(['cat', 'dog', 'cat', 'cat']) -> Counter({'cat': 3, 'dog': 1})
word_freq = Counter(clean_words)

print("\nNumber of DISTINCT words in the document:", len(word_freq))

# .most_common(10) sorts the counted words from highest to lowest
# frequency and returns just the top 10, as a list of (word, count) pairs.
top_10 = word_freq.most_common(10)

print("\n--- TOP 10 MOST FREQUENT WORDS ---")
for rank, (word, count) in enumerate(top_10, start=1):
    # enumerate(top_10, start=1) numbers our loop starting from 1
    # instead of the default 0, purely so the printed ranking looks natural.
    print(f"{rank:2}. {word:15} -> {count} times")
```

**Expected output shape:**
```
Number of DISTINCT words in the document: 42

--- TOP 10 MOST FREQUENT WORDS ---
 1. maruti          -> 3 times
 2. suzuki          -> 3 times
 3. rohan           -> 3 times
 4. data             -> 2 times
 5. delhi            -> 1 times
 ...
```
(Your actual numbers will depend entirely on your `sample.txt` content.)

### The code — Step 6a: Bar chart of the Top 10

```python
# zip(*top_10) is Python's way of "unzipping" a list of pairs into two
# separate groups. Before: [('maruti',3), ('data',2)]
#                    After: ('maruti','data'), (3,2)
words_list, counts_list = zip(*top_10)

plt.figure(figsize=(10, 5))                        # new blank canvas, 10 inches by 5 inches
plt.bar(words_list, counts_list, color="skyblue")   # draw one bar per word
plt.title("Top 10 Most Frequent Words")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.xticks(rotation=45)     # tilts the word labels on the x-axis 45° so long words don't overlap
plt.tight_layout()          # automatically fixes spacing/margins so labels aren't cut off
plt.savefig("top10_words.png")   # saves a permanent image copy to your folder
plt.show()                        # opens an on-screen window showing the chart
```

**What you should see:** a window with 10 vertical bars, tallest on the left (your #1 word) descending to the right. The same picture is saved as `top10_words.png` in your folder — useful for pasting into your lab report even if the popup window doesn't render in your particular setup.

### The code — Step 6b: The Word Cloud

```python
# WordCloud(...) configures the picture's size and background color.
# .generate_from_frequencies(word_freq) is the key method: instead of
# handing it raw text (which it would tokenize and count itself), we
# hand it OUR already-computed Counter dictionary directly, so its
# sizing is based on exactly the same counts we already printed above.
wc = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_freq)

plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation="bilinear")   # renders the generated word-cloud image
plt.axis("off")                             # hides the numbered x/y axis (meaningless for a picture)
plt.title("Word Cloud")
plt.savefig("wordcloud.png")
plt.show()
```

**How does WordCloud decide font size?** Internally, it looks at each word's count relative to the maximum count in your frequency dictionary, and scales font size proportionally — your #1 most frequent word will appear noticeably larger than everything else, with a smooth size gradient down to your least-frequent included words. Layout/rotation/color is randomized by default, so running the script twice can produce a visually different (but data-equivalent) picture each time.

---

## Part 2: Named Entity Recognition (NER)

### Step-by-step concept

**Analogy first:** Imagine reading a news article with a highlighter and marking every person's name in yellow, every company in green, and every city in blue. NER automates exactly that task.

To do this, NLTK works in **two stages**:

**Stage 1 — Part-of-Speech (POS) tagging.** Before you can find "names," the computer first needs to know which words are even *grammatically* capable of being a name — that means finding proper nouns. POS tagging labels *every single word* in the sentence with its grammatical role.

Common tags you'll encounter:

| Tag | Meaning | Example |
|---|---|---|
| `NNP` | Proper noun, singular | Rohan, Delhi, Maruti |
| `NNPS` | Proper noun, plural | Americans |
| `NN` | Common noun, singular | department |
| `NNS` | Common noun, plural | departments |
| `VBD` | Verb, past tense | joined |
| `VBZ` | Verb, 3rd person singular present | works |
| `JJ` | Adjective | largest |
| `IN` | Preposition | at, in, of |
| `DT` | Determiner | the, a |
| `CC` | Coordinating conjunction | and, but |

**Stage 2 — Chunking into named entities.** Once every word has a tag, `ne_chunk()` scans through looking for sequences of proper-noun (`NNP`/`NNPS`) tokens, groups adjacent ones together (so "Maruti" + "Suzuki" become one single entity, not two separate ones), and assigns each group a category label:

| Label | Meaning | Example |
|---|---|---|
| `PERSON` | A person's name | Rohan Sharma |
| `ORGANIZATION` | A company, institution, or group | Maruti Suzuki, Laadli Foundation |
| `GPE` | Geo-Political Entity — country, state, or city | Delhi, Mumbai, India |
| `LOCATION` | A physical place that isn't politically defined | Mount Everest, the Pacific Ocean |
| `FACILITY` | A named building/structure | Taj Mahal |

The final result is technically a **tree** — a nested structure where some branches are labeled groups (entities) and others are plain, unlabeled single words. We'll loop through it and only print the labeled branches.

### The code (fully commented)

```python
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# --- Step 1: Read the document ---
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

# --- Step 2: Tokenize into words ---
# Note: unlike Part 1, we do NOT remove stop-words or lowercase here.
# NER depends on capitalization (a key signal for proper nouns!) and
# on function words like "the"/"of" for correct grammar tagging, so
# we deliberately keep the text closer to its original form.
tokens = word_tokenize(text)

# --- Step 3: POS tagging ---
# pos_tag() takes our list of tokens and returns a list of
# (word, tag) TUPLES — this paired format is what ne_chunk() expects next.
pos_tags = pos_tag(tokens)
print("Sample POS tags:")
for word, tag in pos_tags[:15]:
    print(f"  {word:15} -> {tag}")

# --- Step 4: Named Entity Recognition ---
# ne_chunk() reads the (word, tag) pairs and returns a Tree object.
# Inside that tree:
#   - a plain (word, tag) pair is a "leaf" — not part of any entity
#   - a labeled sub-tree groups one or more consecutive words that
#     together form a single named entity
ner_tree = ne_chunk(pos_tags)

print("\n--- NAMED ENTITIES FOUND ---")
for chunk in ner_tree:
    # hasattr(chunk, 'label') is True only for labeled sub-trees
    # (entities) — plain leaves don't have a .label() method, so this
    # check safely skips over ordinary words.
    if hasattr(chunk, 'label'):
        # A chunk itself may contain multiple words (e.g. "Maruti" + "Suzuki").
        # c[0] pulls out just the word from each (word, tag) pair inside
        # the chunk, and " ".join(...) glues them back into one readable string.
        entity_name = " ".join(c[0] for c in chunk)
        entity_type = chunk.label()
        print(f"{entity_name:25} -> {entity_type}")
```

### Expected output

```
Sample POS tags:
  Rohan           -> NNP
  Sharma          -> NNP
  joined          -> VBD
  Maruti          -> NNP
  Suzuki          -> NNP
  as              -> IN
  a               -> DT
  Data            -> NNP
  Analyst         -> NNP
  in              -> IN
  Delhi           -> NNP
  last            -> JJ
  year            -> NN
  .               -> .

--- NAMED ENTITIES FOUND ---
Rohan Sharma              -> PERSON
Maruti Suzuki              -> ORGANIZATION
Delhi                      -> GPE
Gurugram                   -> GPE
Laadli Foundation          -> ORGANIZATION
Priya Nair                 -> PERSON
Mumbai                     -> GPE
```

**Important, honest caveat to note in your lab record:** NLTK's built-in NER model is a general-purpose, moderately old statistical model — it is **not perfect**. It can occasionally mislabel a person as an organization, or miss an entity entirely if the surrounding grammar is unusual. Noting this limitation (and maybe showing one example where it got something wrong) is genuinely good, honest analysis for a lab report — real-world NER systems in industry use much larger, deep-learning-based models for exactly this reason.

### Optional bonus: visualize the parse tree

```python
ner_tree.draw()   # opens a new window showing the tagged tree as a diagram
```
This needs `tkinter`, which normally ships with Python already. If you get an error, search "install tkinter [your operating system]."

---

## Full Combined Script

Save this as `experiment4.py` to run both parts back-to-back:

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag, ne_chunk
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ============ PART 1: WORD FREQUENCY + WORD CLOUD ============

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = word_tokenize(text)
stop_words = set(stopwords.words('english'))
clean_words = [w.lower() for w in words if w.isalpha() and w.lower() not in stop_words]

word_freq = Counter(clean_words)
top_10 = word_freq.most_common(10)

print("--- TOP 10 MOST FREQUENT WORDS ---")
for rank, (word, count) in enumerate(top_10, start=1):
    print(f"{rank:2}. {word:15} -> {count} times")

words_list, counts_list = zip(*top_10)
plt.figure(figsize=(10, 5))
plt.bar(words_list, counts_list, color="skyblue")
plt.title("Top 10 Most Frequent Words")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top10_words.png")
plt.show()

wc = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_freq)
plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud")
plt.savefig("wordcloud.png")
plt.show()

# ============ PART 2: NAMED ENTITY RECOGNITION ============

tokens = word_tokenize(text)   # re-tokenize the ORIGINAL text (keeps capitalization)
pos_tags = pos_tag(tokens)

ner_tree = ne_chunk(pos_tags)

print("\n--- NAMED ENTITIES FOUND ---")
for chunk in ner_tree:
    if hasattr(chunk, 'label'):
        entity_name = " ".join(c[0] for c in chunk)
        entity_type = chunk.label()
        print(f"{entity_name:25} -> {entity_type}")
```

---

## Understanding Your Output — What to Write in Your Lab Record

For a complete, well-explained lab submission, include:
1. **Screenshot or paste** of your Top 10 frequent-words printout, plus a one-line interpretation ("The document is likely about X, since [word] and [word] dominate.")
2. **The bar chart image** (`top10_words.png`)
3. **The word cloud image** (`wordcloud.png`)
4. **Screenshot or paste** of your printed named entities, grouped by type (list all `PERSON`s together, all `ORGANIZATION`s together, etc.)
5. **A short observation** on NER accuracy — did it correctly catch every real entity in your text? Did it miss any or mislabel any? This kind of critical observation is exactly what turns a "ran the code" lab report into a "understood the experiment" lab report.

---

## Common Mistakes & Troubleshooting

| Problem | Why it happens | Fix |
|---|---|---|
| `LookupError: Resource ... not found` | A required NLTK data pack wasn't downloaded | Re-run every line of `setup_nltk.py` |
| Top 10 list is full of words like "said", "one", "also" | These aren't in NLTK's default stop-word list but are still low-information "filler" for your specific document | Add your own extra stop-words: `stop_words.update(['said', 'one', 'also'])` right after creating `stop_words` |
| Word cloud/chart window never appears | Some code editors or remote environments block pop-up windows | Open the saved `top10_words.png` / `wordcloud.png` files directly from your folder instead |
| NER finds nothing | Your `sample.txt` has no capitalized proper nouns | Add real names of people/companies/cities to your sample text |
| NER mislabels something (e.g. calls a person's name a `GPE`) | NLTK's built-in NER model is a fairly basic statistical model with known limitations | This is expected and worth noting as an observation, not a bug in your code |
| `ne_chunk()` throws an error about missing resources | `maxent_ne_chunker` / `words` data packs weren't downloaded | Re-run the setup script, ensuring those two lines succeed |

---

## Mini Glossary

| Term | Meaning |
|---|---|
| Token | A single word or punctuation mark, after splitting text apart |
| Stop-word | A very common word ("the", "is", "a") usually filtered out before analysis |
| Frequency Distribution | A count of how many times each word occurs |
| Word Cloud | A picture where word size reflects how frequently that word occurs |
| POS Tag | A grammatical label (noun, verb, adjective...) assigned to a word |
| Named Entity | A real-world "thing" in text — a person, place, organization, or date |
| NER | Named Entity Recognition — the task of automatically finding and labeling named entities |
| Chunking | Grouping several tokens together into one larger unit (e.g. "Maruti" + "Suzuki" → one entity) |
