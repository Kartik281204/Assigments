# Text Analytics Lab — Complete Beginner's Guide to Experiment 3 & Experiment 4

This guide assumes **zero NLP background**. If you know basic Python — variables, `for` loops, lists, and how to run a `.py` file — you can follow every step here. Every line of code is explained, every NLP term is defined in plain English before it's used, and each section ends with what you should expect to see and why it matters.

---

## Table of Contents
1. [How to Read This Guide](#how-to-read-this-guide)
2. [Glossary — Key Terms, Explained Simply](#glossary--key-terms-explained-simply)
3. [Part 0: One-Time Setup](#part-0-one-time-setup)
4. [Experiment 3: Processing Data](#experiment-3-processing-data)
5. [Experiment 4: Text Mining](#experiment-4-text-mining)
6. [Troubleshooting](#troubleshooting)
7. [Cheat Sheet](#cheat-sheet)

---

## How to Read This Guide

For every piece of code, you'll see three things, in this order:
1. **The concept** — what problem we're solving and why, using a real-world analogy first.
2. **The code** — fully commented, so you can read it top to bottom like a story.
3. **The walkthrough** — a line-by-line (or block-by-block) breakdown explaining *exactly* what each instruction does, plus what output you should expect to see.

You don't need to memorize any of this. The goal is that by the end, you understand *why* each line exists — not just that it "works."

---

## Glossary — Key Terms, Explained Simply

Read this once now, and come back to it whenever you hit an unfamiliar word.

| Term | Plain-English Explanation | Everyday Analogy |
|---|---|---|
| **Corpus** | A body/collection of text used for analysis | A "corpus" is just a fancy word for "the document(s) you're studying" |
| **Token** | A single unit of text — usually a word or punctuation mark | Like cutting a sentence into individual Scrabble tiles |
| **Tokenization** | The act of splitting text into tokens | Chopping a sentence into words |
| **Stop-words** | Extremely common words ("the", "is", "a", "of") that appear everywhere and rarely carry unique meaning | The "filler" words you'd skip if skimming a page for keywords |
| **Stemming** | Chopping the end off a word using simple rules to get a rough "root" | Cutting a plant down to its stem — quick, but you might cut off something important |
| **Lemmatization** | Looking up a word's real dictionary base form | Looking a word up in a dictionary to find its "official" entry (e.g. "ran" → "run") |
| **Morpheme** | The smallest unit of a word that still carries meaning | "unhappiness" is built from 3 meaningful pieces: `un` + `happy` + `ness` |
| **Morphological Analysis** | Studying how words are built from morphemes (roots, prefixes, suffixes) | Like taking apart a LEGO model to see which individual bricks make it up |
| **POS (Part-of-Speech) Tagging** | Labeling each word as a noun, verb, adjective, etc. | Grammar-class sentence diagramming, done automatically |
| **NER (Named Entity Recognition)** | Automatically finding and labeling real-world "things" in text: people, places, organizations, dates | Highlighting all the proper nouns in a news article with a marker |
| **Frequency Distribution** | A count of how many times each word appears | A tally chart / scoreboard for words |
| **Word Cloud** | A picture where words are sized according to how often they appear | A visual "leaderboard" of the most-used words |

---

## Part 0: One-Time Setup

### Step 1 — Understand what you're installing

Python itself doesn't know anything about language processing — it just knows how to run code. **NLTK** (Natural Language Toolkit) is a *library*: a pre-written toolbox of language functions someone else built, so you don't have to write a tokenizer or a stop-word list from scratch. `wordcloud` and `matplotlib` are libraries purely for drawing pictures.

Open your terminal (Command Prompt on Windows, Terminal on Mac/Linux) and run:

```bash
pip install nltk wordcloud matplotlib
```

**What is `pip`?** It's Python's built-in package manager — think of it as an app store for Python code. `pip install X` downloads library `X` from the internet and makes it available to `import` in your scripts.

You should see progress bars and eventually a line like `Successfully installed nltk-3.x wordcloud-1.x matplotlib-3.x`. If you instead see `pip: command not found`, Python wasn't added to your system PATH during installation — search "add Python to PATH [your OS]" to fix this, or use `python -m pip install nltk wordcloud matplotlib` instead.

### Step 2 — Download NLTK's language data

Installing the `nltk` library only gives you the *code* (the functions). It does **not** give you the *data* those functions need — things like a list of English stop-words, or a dictionary of word roots. These are downloaded separately, once.

Create a new file called `setup_nltk.py` and put this inside it:

```python
import nltk

# Each line below downloads one "data pack." Think of these as
# plug-in dictionaries/datasets that NLTK's functions read from.

nltk.download('punkt')                          # rules for splitting text into sentences/words
nltk.download('punkt_tab')                       # newer NLTK versions store the same rules here too
nltk.download('stopwords')                       # list of common English "filler" words
nltk.download('wordnet')                         # a large English dictionary, used for lemmatization
nltk.download('omw-1.4')                         # multilingual data that wordnet depends on
nltk.download('averaged_perceptron_tagger')       # the trained model that assigns POS tags
nltk.download('averaged_perceptron_tagger_eng')   # newer NLTK versions store it under this name too
nltk.download('maxent_ne_chunker')               # the trained model that finds named entities
nltk.download('maxent_ne_chunker_tab')           # newer NLTK versions store it under this name too
nltk.download('words')                            # a list of known English words, used by the NER model

print("All NLTK data downloaded successfully!")
```

**Why download both the old-named and new-named versions of some packages?** NLTK has changed how it names a few internal resources across versions. Downloading both names is harmless (it just skips ones that don't apply to your version) and saves you from a confusing `LookupError` later.

Run it from your terminal:
```bash
python setup_nltk.py
```

This will take a minute or two depending on your internet speed. You may briefly see a small window pop up (NLTK's downloader GUI) — if so, just wait for it to close on its own, or it may run silently and just print progress in the terminal. Either behavior is normal. **You only need to run this script once ever** on a given computer (unless you reinstall NLTK or switch machines).

### Step 3 — Prepare a sample text file

Both experiments read from a `.txt` file. Create a file named `sample.txt` in the **same folder** where your Python scripts will live, and paste in 3–5 paragraphs of real English text — a Wikipedia excerpt, a news article, anything with actual sentences. For Experiment 4's NER section specifically, try to include some real proper nouns (names of people, cities, companies) so the results are more interesting.

**Why does the file need to be in the same folder?** When your code says `open("sample.txt")`, Python looks for that file relative to wherever you *ran* the script from — usually the folder the `.py` file sits in. Keeping everything in one folder avoids "file not found" errors.

---

## Experiment 3: Processing Data

**The big picture:** Raw text is messy for a computer to analyze directly — it has capitalization inconsistencies, punctuation, and filler words. Experiment 3 is about *cleaning and normalizing* text step by step, and then *studying how individual words are structurally built*.

This experiment has two parts:
- **Part A** — Pre-processing: tokenization → stop-word removal → lemmatization
- **Part B** — Morphological analysis: studying root forms, prefixes, and suffixes

### Part A: Tokenization, Stop-word Removal, and Lemmatization

#### The Concept, Step by Step

**1. Tokenization** — Before a computer can count or analyze "words," it needs to know where one word ends and the next begins. Tokenization is literally the act of splitting a block of text into a list of pieces (tokens). NLTK's tokenizer is smarter than just "split on spaces" — it correctly handles punctuation, contractions like "don't", and abbreviations.

**2. Stop-word removal** — Words like "the", "is", "and", "a" appear constantly in *any* English text, regardless of topic. If you're trying to find out what a document is *about*, these words are just noise — they don't help distinguish this document from any other. We filter them out using a pre-built list NLTK ships with.

**3. Lemmatization** — Different word forms ("run", "running", "ran") often represent the same underlying concept. If you're counting how often someone talks about "running," you don't want "run," "running," and "ran" treated as three separate, unrelated words. Lemmatization normalizes each word down to its dictionary base form (its "lemma") so these variants get grouped together.

#### The Code (fully commented)

```python
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# --- Step 1: Read the text file into a single string ---
# "with open(...) as file" opens the file and automatically closes it
# afterward, even if an error happens. This is the safe, standard way
# to read files in Python.
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()   # .read() loads the ENTIRE file content as one big string

print("----- ORIGINAL TEXT (first 300 characters) -----")
print(text[:300])        # text[:300] means "give me characters 0 through 299"

# --- Step 2: Tokenization ---

# sent_tokenize() takes the big string and returns a LIST of sentences,
# splitting intelligently on ". ", "! ", "? " etc. (it knows "Mr. Smith"
# isn't the end of a sentence, for example).
sentences = sent_tokenize(text)
print("\nNumber of sentences:", len(sentences))

# word_tokenize() takes the big string and returns a LIST of word/punctuation
# tokens. Punctuation marks become their own tokens (e.g. "," and ".").
words = word_tokenize(text)
print("Number of words (tokens):", len(words))
print("First 20 word tokens:", words[:20])

# --- Step 3: Stop-word Removal ---

# stopwords.words('english') returns a plain Python list of ~180 common
# English words. We wrap it in set(...) because checking "is this word
# IN a set" is much faster than checking "is this word in a list" —
# this matters when you're checking thousands of words.
stop_words = set(stopwords.words('english'))

# This line is a "list comprehension" — a compact way to write a for-loop
# that builds a new list. In plain English it reads:
#   "For every word w in words, IF w is made only of letters (w.isalpha()),
#    keep a LOWERCASED copy of it."
# .isalpha() filters out punctuation tokens like "," and numbers like "42".
# .lower() ensures "The" and "the" are treated as the same word.
words_clean = [w.lower() for w in words if w.isalpha()]

# Another list comprehension: keep only the words that are NOT in our
# stop-word set.
words_no_stopwords = [w for w in words_clean if w not in stop_words]

print("\nWords before stop-word removal:", len(words_clean))
print("Words after stop-word removal :", len(words_no_stopwords))
print("Sample:", words_no_stopwords[:20])

# --- Step 4: Lemmatization ---

# WordNetLemmatizer() creates a "lemmatizer object" — think of it as
# switching on a tool that knows how to look words up in a dictionary
# (WordNet) and return their base form.
lemmatizer = WordNetLemmatizer()

# For every word in our cleaned, stop-word-free list, replace it with
# its lemmatized (base dictionary) form.
lemmatized_words = [lemmatizer.lemmatize(w) for w in words_no_stopwords]

print("\nSample BEFORE lemmatization:", words_no_stopwords[:10])
print("Sample AFTER  lemmatization:", lemmatized_words[:10])
```

#### Walkthrough: What You Should See

Running this (`python experiment3a.py`) should print something like:

```
----- ORIGINAL TEXT (first 300 characters) -----
The quick brown fox jumps over the lazy dog...

Number of sentences: 5
Number of words (tokens): 120
First 20 word tokens: ['The', 'quick', 'brown', 'fox', ...]

Words before stop-word removal: 95
Words after stop-word removal : 58
Sample: ['quick', 'brown', 'fox', 'jumps', 'lazy', 'dog', ...]

Sample BEFORE lemmatization: ['jumps', 'foxes', 'running', ...]
Sample AFTER  lemmatization: ['jump', 'fox', 'running', ...]
```

**Notice something important:** `WordNetLemmatizer` needs to be told *what part of speech* a word is to lemmatize verbs correctly — by default it assumes every word is a noun. That's why "running" might not become "run" unless you pass `pos='v'` (verb) explicitly:

```python
lemmatizer.lemmatize("running", pos='v')   # returns "run"
lemmatizer.lemmatize("running")            # returns "running" (assumed noun, unchanged)
```

For your lab report, it's fine to demonstrate both — this is actually a great thing to point out as an *observation*: "lemmatization is context-dependent on part-of-speech."

**One-line summary to write in your notebook:** *We converted raw text into a clean, lowercase, punctuation-free, stop-word-free list of dictionary-normalized word tokens.*

### Part B: Morphological Analysis

#### The Concept, Step by Step

Morphology studies how words are constructed from smaller meaningful pieces called **morphemes**. There are two kinds worth knowing:

- **Free morphemes** — can stand alone as a word (e.g. `happy`, `run`, `nation`)
- **Bound morphemes** — cannot stand alone; they attach to a free morpheme to change its meaning or grammar (e.g. `un-`, `-ness`, `-ing`, `-s`)

Example breakdown:

```
u n h a p p i n e s s
└┬┘ └──┬──┘ └──┬──┘
prefix  root  suffix
(un-)  (happy) (-ness)
"not"  "feeling      "the state
        joy"          of being"
```

So "unhappiness" = "the state of not feeling joy."

There's also a distinction between:
- **Inflectional morphology** — changes grammar but not the core meaning/word category (e.g. `walk` → `walks`/`walked`/`walking` — still a verb about walking)
- **Derivational morphology** — creates a new word, often changing its category (e.g. `happy` [adjective] → `happiness` [noun])

A practical, beginner-friendly way to *implement* morphological analysis in code is to compare **stemming** (a crude, rule-based chopping of suffixes) against **lemmatization** (a dictionary-correct root), because the *difference* between the two visibly demonstrates how suffixes/prefixes are being stripped.

#### The Code (fully commented)

```python
from nltk.stem import PorterStemmer, WordNetLemmatizer

# PorterStemmer applies a fixed set of suffix-stripping rules
# (e.g. "if a word ends in -ing, try removing it"). It doesn't know
# any real dictionary — it's fast but mechanical.
stemmer = PorterStemmer()

# WordNetLemmatizer looks the word up in an actual dictionary (WordNet)
# and returns its real base form.
lemmatizer = WordNetLemmatizer()

# A handful of words chosen to show interesting differences between
# stemming and lemmatization.
sample_words = ["running", "happiness", "unhappiness", "studies",
                 "better", "flying", "connection", "nationality"]

# f-strings (f"...") let us insert variables directly into text, with
# :15 meaning "pad this to 15 characters wide" so columns line up.
print(f"{'Word':15}{'Stem':15}{'Lemma':15}")
print("-" * 45)   # prints 45 dashes as a separator line

for w in sample_words:
    stem = stemmer.stem(w)
    lemma = lemmatizer.lemmatize(w)
    print(f"{w:15}{stem:15}{lemma:15}")
```

#### Walkthrough: What You Should See

```
Word           Stem           Lemma          
---------------------------------------------
running        run            running        
happiness      happi          happiness      
unhappiness    unhappi        unhappiness    
studies        studi          study          
better         better         better         
flying         fli            flying         
connection     connect        connection     
nationality    nation         nationality    
```

**What this table is telling you (write this analysis in your lab record):**
- `PorterStemmer` chops "happiness" down to `happi` — technically not even a real English word, but it correctly captured that "happy/happiness/happier" share a root.
- `WordNetLemmatizer` left "happiness" unchanged, because by default it assumes the word is already a noun, and "happiness" *is* the dictionary noun form.
- "studies" → stemmer gives `studi` (mechanical), lemmatizer gives `study` (the real dictionary singular/verb form) — this is lemmatization clearly winning on correctness.
- "flying" → stemmer's `fli` shows how aggressive/crude pure suffix-stripping can get.

This comparison *is* your morphological analysis: it demonstrates, empirically, how suffixes (`-ing`, `-ness`, `-s`, `-ity`) get identified and stripped by two different strategies, and shows the trade-off between speed (stemming) and correctness (lemmatization).

You can round this off by manually decomposing 2–3 words in writing, e.g.:
```
unhappiness  =  un-  (prefix, meaning "not")
             +  happy (root, spelling adjusted to happi- before a suffix)
             +  -ness (suffix, turns adjective into noun: "state of being")

nationality  =  nation (root)
             +  -al   (suffix, turns noun into adjective: "national")
             +  -ity  (suffix, turns adjective into noun: "state/quality of")
```

---

## Experiment 4: Text Mining — Word Frequency, Word Cloud, and NER

**The big picture:** Once text is tokenized, we can ask quantitative questions about it — "what words dominate this document?" — and structural questions — "what real-world entities (people, places, organizations) does it mention?"

### Part 1: Word Count, Top 10 Frequent Words, and Word Cloud

#### The Concept, Step by Step

**Word frequency** simply means: for every unique word in the document, how many times does it appear? This is exactly the kind of repetitive counting task computers are perfect for. Python's `collections.Counter` is a specialized dictionary built exactly for this — you hand it a list, and it hands back a count of every item.

Once we have those counts, we can:
- Sort them and print the top 10 (a leaderboard)
- Draw a **bar chart** (height of bar = frequency) using `matplotlib`
- Draw a **word cloud** — a picture where each word's *font size* is proportional to how often it occurred — using the `wordcloud` library

#### The Code (fully commented)

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

# --- Step 2: Tokenize and clean (same idea as Experiment 3) ---
words = word_tokenize(text)
stop_words = set(stopwords.words('english'))

# Keep only alphabetic, lowercase, non-stop-word tokens — all in one
# list comprehension this time (combining the two filters from before).
clean_words = [w.lower() for w in words if w.isalpha() and w.lower() not in stop_words]

# --- Step 3: Word count (frequency of every word) ---

# Counter(list) walks through the list once and builds a dictionary-like
# object where keys = unique words, values = how many times each appeared.
# Example: Counter(['cat','dog','cat']) -> Counter({'cat': 2, 'dog': 1})
word_freq = Counter(clean_words)
print("Total unique words:", len(word_freq))

# --- Step 4: Top 10 most frequent words ---

# .most_common(10) returns the 10 (word, count) pairs with the highest
# counts, already sorted from most to least frequent.
top_10 = word_freq.most_common(10)
print("\nTop 10 frequent words:")
for word, count in top_10:
    print(f"{word:15} -> {count}")

# --- Step 5: Show top 10 as a bar graph ---

# zip(*top_10) "unzips" our list of (word, count) pairs into two
# separate tuples: one of all the words, one of all the counts.
# Example: [('cat',5), ('dog',3)] -> ('cat','dog'), (5,3)
words_list, counts_list = zip(*top_10)

plt.figure(figsize=(10, 5))          # create a blank chart canvas, 10x5 inches
plt.bar(words_list, counts_list, color="skyblue")   # draw the bars
plt.title("Top 10 Most Frequent Words")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.xticks(rotation=45)              # tilt word labels 45° so they don't overlap
plt.tight_layout()                   # auto-adjust spacing so nothing gets cut off
plt.savefig("top10_words.png")       # save the chart as an image file
plt.show()                            # open a window displaying the chart

# --- Step 6: Create and show a word cloud ---

# generate_from_frequencies() takes our ALREADY-COUNTED word_freq
# dictionary directly (instead of re-counting raw text), and lays out
# every word, sized according to its frequency.
wc = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_freq)

plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation="bilinear")   # display the generated image
plt.axis("off")                             # hide the x/y axis numbers (irrelevant for a picture)
plt.title("Word Cloud")
plt.savefig("wordcloud.png")
plt.show()
```

#### Walkthrough: What You Should See

- A printed ranked list, e.g.:
  ```
  Total unique words: 64

  Top 10 frequent words:
  company         -> 12
  employee        -> 9
  data            -> 7
  ...
  ```
- A **bar chart window** pops up (and is saved as `top10_words.png`), with the tallest bar being your single most-repeated word.
- A **word cloud window** pops up (and is saved as `wordcloud.png`) — the most frequent word appears biggest and often centered; less frequent words are smaller and pushed to the edges. The exact layout/colors are randomized each run unless you fix a random seed.

**Why this matters conceptually:** raw word count is one of the oldest and simplest "topic detection" techniques — if "salary" and "department" dominate a document's word counts, you can guess the document is about employee compensation, without reading a single sentence yourself.

### Part 2: Named Entity Recognition (NER)

#### The Concept, Step by Step

NER answers: "which words/phrases in this text refer to a real-world named thing?" To get there, NLTK's approach goes through two stages:

**Stage 1 — POS (Part-of-Speech) tagging.** Every token gets labeled with its grammatical role. A few common tags you'll see:

| Tag | Meaning | Example |
|---|---|---|
| `NN` | Singular noun | dog |
| `NNS` | Plural noun | dogs |
| `NNP` | Proper noun (singular) | London |
| `NNPS` | Proper noun (plural) | Americans |
| `VB` | Verb, base form | run |
| `VBD` | Verb, past tense | ran |
| `JJ` | Adjective | quick |
| `IN` | Preposition | in, of, on |
| `DT` | Determiner | the, a |

NER relies heavily on `NNP`/`NNPS` tags, because named entities are almost always proper nouns.

**Stage 2 — Chunking into entities.** Once every word has a POS tag, NLTK's `ne_chunk()` function groups consecutive proper-noun tokens together and classifies the group into a category:

| Entity Label | Meaning | Example |
|---|---|---|
| `PERSON` | A person's name | "Elon Musk" |
| `ORGANIZATION` | A company/institution | "Maruti Suzuki" |
| `GPE` | Geo-Political Entity (country, city, state) | "Delhi" |
| `LOCATION` | A non-political place | "Mount Everest" |
| `DATE` | A date expression | "January 2027" |

The result comes back as a **tree structure** — a nested data format where labeled branches (entities) sit alongside plain, unlabeled word "leaves" (everything else).

#### The Code (fully commented)

```python
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# --- Step 1: Read the document ---
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

# --- Step 2: Tokenize into words ---
tokens = word_tokenize(text)

# --- Step 3: POS tagging ---
# pos_tag() takes a list of tokens and returns a list of (word, tag)
# pairs. This is the input format ne_chunk() expects next.
pos_tags = pos_tag(tokens)
print("Sample POS tags:", pos_tags[:10])

# --- Step 4: Named Entity Recognition ---
# ne_chunk() reads the (word, tag) pairs and returns a "tree": a nested
# structure where some parts are grouped and labeled (an entity), and
# the rest are left as plain (word, tag) leaves.
ner_tree = ne_chunk(pos_tags)

print("\nNamed Entities found:")
for chunk in ner_tree:
    # Only grouped/labeled branches have a .label() — a plain
    # (word, tag) leaf does not, so hasattr() lets us skip those.
    if hasattr(chunk, 'label'):
        # chunk is itself a small tree of one or more words; join
        # them back into a single readable string.
        entity_name = " ".join(c[0] for c in chunk)
        entity_type = chunk.label()
        print(f"{entity_name:25} -> {entity_type}")
```

#### Walkthrough: What You Should See

```
Sample POS tags: [('Rohan', 'NNP'), ('joined', 'VBD'), ('Maruti', 'NNP'), ('Suzuki', 'NNP'), ...]

Named Entities found:
Rohan                     -> PERSON
Maruti Suzuki             -> ORGANIZATION
Delhi                     -> GPE
```

If your `sample.txt` has generic sentences with no proper nouns, this section will print little to nothing — that's expected behavior, not an error. Swap in a paragraph that mentions real names, cities, or companies to see richer results.

**Optional but instructive add-on:** you can visualize the parse tree structure itself (useful for a lab screenshot) with:

```python
ner_tree.draw()   # opens a separate window showing the tree diagram
```

This requires a small extra tool called `tkinter` (it usually ships with Python already; if it's missing, search "install tkinter [your OS]").

---

## Troubleshooting

| Problem | Why it happens | Fix |
|---|---|---|
| `LookupError: Resource punkt not found` (or similar for other resources) | You skipped or partially ran the setup script | Re-run every line in `setup_nltk.py` from Step 2 |
| `FileNotFoundError: sample.txt` | Python is looking in a different folder than where `sample.txt` lives | Make sure both files are in the same folder, and that you're running the script from that folder |
| Chart / word cloud window doesn't visibly appear | Some code editors block pop-up windows | Ignore the missing pop-up and open the saved `.png` file in your folder instead — it still gets saved |
| `ModuleNotFoundError: No module named 'wordcloud'` | The library wasn't installed, or was installed to a different Python environment than the one running your script | Re-run `pip install wordcloud`, and make sure you're using the same Python interpreter in both your terminal and your code editor |
| NER finds almost no entities | Your source text has few/no proper nouns | Use text that includes real names of people, places, or companies |
| Lemmatizer doesn't change verbs (e.g. "running" stays "running") | `WordNetLemmatizer` assumes "noun" by default | Pass `pos='v'` explicitly: `lemmatizer.lemmatize("running", pos='v')` |

---

## Cheat Sheet

```
Read file          →  open("file.txt").read()
Split sentences     →  sent_tokenize(text)
Split words         →  word_tokenize(text)
Remove punctuation  →  [w for w in words if w.isalpha()]
Remove stop-words   →  [w for w in words if w not in stopwords.words('english')]
Stem a word         →  PorterStemmer().stem(word)
Lemmatize a word    →  WordNetLemmatizer().lemmatize(word)
Count word frequency→  Counter(word_list)
Get top N words     →  Counter(word_list).most_common(N)
POS tag words       →  pos_tag(tokenized_words)
Find named entities →  ne_chunk(pos_tagged_words)
```

## Suggested File Structure

```
your-lab-folder/
├── setup_nltk.py          (run once, before anything else)
├── sample.txt              (your input text)
├── experiment3.py          (Part A + Part B code combined)
└── experiment4.py          (Part 1 + Part 2 code combined)
```
