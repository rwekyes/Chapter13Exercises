# 13.10.1. Ask a virtual assistant
#
# There are several topics that came up in this chapter that I did not explain in detail.
# Here are some questions you can ask a virtual assistant to get more information.
#
#     “What are the differences between ephemeral and persistent programs?”
#
#     “What are some examples of persistent programs?”
#
#     “What’s the difference between a relative path and an absolute path?”
#
#     “Why does the yaml module have functions called load and safe_load?”
#
#     “When I write a Python shelf, what are the files with suffixes dat and dir?”
#
#     “Other than key-values stores, what other kinds of databases are there?”
#
#     “When I read a file, what’s the difference between binary mode and text mode?”
#
#     “What are the differences between a bytes object and a string?”
#
#     “What is a hash function?”
#
#     “What is an MD5 digest?”
#
# As always, if you get stuck on any of the following exercises, consider asking a VA for help.
# Along with your question, you might want to paste in the relevant functions from this chapter.

# =====================================================================================
# ANSWERS, delivered by an auctioneer who has been holding it since the second lot
# =====================================================================================
#
# Q1: "What are the differences between ephemeral and persistent programs?"
#
#   ALRIGHT-folks-whatamIbid-whatamIbid-EPHEMERAL program, runs-a-little-while, keeps
#   everything in MEMORY, variables-lists-dictionaries, and when-it-ends POOF it's GONE,
#   everything-it-knew-gone-gone-GONE, like my DIGNITY if this goes much longer.
#   Do-I-hear-PERSISTENT? PERSISTENT program runs a LONG time, or it SAVES its data
#   somewhere permanent like a FILE or a DATABASE, so next time it starts up it picks
#   up RIGHT WHERE IT LEFT OFF, which-is-more-than-I-can-say-for-my-BLADDER, going-once.
#
# Q2: "What are some examples of persistent programs?"
#
#   OOH-we-got-a-LOT-here-folks, OPERATING SYSTEMS, they run as long as the computer's
#   on, WEB SERVERS, run-all-day-run-all-night-waiting-for-requests, DATABASES like
#   PostgreSQL and SQLite, they keep your data on DISK, TEXT EDITORS and WORD processors
#   that save your documents, VIDEO GAMES with SAVE FILES, and-your-PHONE'S-CONTACTS-APP
#   remembering-everybody-you've-ever-met. Also the shelve example from this chapter,
#   puts-stuff-in-a-shelf-and-it's-STILL-THERE-tomorrow. SOLD! to the gentleman in the
#   back, I-gotta-keep-moving-I-gotta-keep-MOVING.
#
# Q3: "What's the difference between a relative path and an absolute path?"
#
#   RELATIVE path, starts from WHERE-YOU-ARE-RIGHT-NOW, the current working directory,
#   the one os.getcwd() gives ya, so 'photos/jan.jpg' means "photos folder IN HERE."
#   ABSOLUTE path starts at the ROOT, the very top, begins with a SLASH, like
#   '/home/dinsdale/photos/jan.jpg', works-from-ANYWHERE-don't-matter-where-you're-
#   standing. Wanna turn relative into absolute? os.path.abspath, DO-I-HEAR-ABSPATH?
#   Kinda like the RESTROOM, folks: "down the hall on the left" is RELATIVE, the
#   street ADDRESS is ABSOLUTE, and I-NEED-BOTH-OF-THEM-REAL-SOON.
#
# Q4: "Why does the yaml module have functions called load and safe_load?"
#
#   YAML-load-YAML-load-who'll-give-me-a-WARNING? Plain old yaml.load, depending on the
#   Loader you give it, can build ARBITRARY PYTHON OBJECTS out of the file, and some of
#   those can RUN CODE, so if a stranger hands you a YAML file it could do NASTY THINGS
#   to your computer. yaml.safe_load only builds the BASICS: strings, numbers, lists,
#   dictionaries, booleans, None, no-funny-business-NO-SIR. That's why the book uses
#   safe_load. Rule of thumb: if you didn't write the file yourself, SAFE_LOAD it,
#   same-way-you-don't-drink-a-mystery-beverage-and-OH-WHY-DID-I-SAY-BEVERAGE.
#
# Q5: "When I write a Python shelf, what are the files with suffixes dat and dir?"
#
#   SHELVE-going-on-the-shelf-folks, shelve sits on top of a "dbm" database, and WHICH
#   files you get depends on WHICH dbm your system's got. If it's the fallback one,
#   dbm.dumb, you get a .dat file, that's the DATA, the actual pickled VALUES, and a
#   .dir file, that's the DIRECTORY, an INDEX of which key lives WHERE inside the .dat
#   file. Sometimes there's a .bak too, a BACKUP of the .dir. On other systems you might
#   get just ONE file, or a .db, it-VARIES. Either way, you don't touch 'em by hand, you
#   just shelve.open('whatever') and let Python handle it, DON'T-DELETE-ONE-AND-KEEP-THE-
#   OTHER, that's-like-crossing-your-legs-and-hoping-for-the-best, IT-DOESN'T-WORK.
#
# Q6: "Other than key-value stores, what other kinds of databases are there?"
#
#   LOT-NUMBER-SIX, BIG LOT, MIXED LOT, here-we-GO:
#     - RELATIONAL databases, TABLES with ROWS and COLUMNS, you query 'em with SQL,
#       SQLite-PostgreSQL-MySQL, the-workhorse-the-classic-the-OLD-RELIABLE.
#     - DOCUMENT databases, store JSON-ish documents, MongoDB, do-I-hear-Mongo?
#     - COLUMN-FAMILY / wide-column stores, Cassandra, for-BIG-BIG-DATA.
#     - GRAPH databases, nodes and edges, who's-friends-with-who, Neo4j.
#     - TIME-SERIES databases, data stamped by TIME, sensor readings, stock prices,
#       how-many-SECONDS-I've-been-standing-here-NOT-GOING-TO-THE-BATHROOM.
#     - VECTOR databases, store embeddings for similarity search, real-popular-lately.
#     - OBJECT databases, store objects directly, kinda like a FANCY shelf.
#   GOING ONCE, GOING TWICE, *crosses legs* SOLD.
#
# Q7: "When I read a file, what's the difference between binary mode and text mode?"
#
#   TEXT MODE, that's the default, open(path) or open(path, 'r'), Python DECODES the
#   bytes into a STRING using an encoding like UTF-8, and it also translates LINE
#   ENDINGS so '\r\n' on Windows comes out as '\n'. BINARY MODE, open(path, 'rb'), NO
#   decoding, NO translating, you get the RAW BYTES exactly as they sit on the disk,
#   as a bytes object. You need BINARY for images, audio, zip files, and for comparing
#   files the way same_contents and md5_digest do in this chapter, 'cause-you-want-
#   EVERY-LAST-BYTE-UNTOUCHED, NOTHING-LEAKED-OUT, I-RELATE-TO-THAT-DEEPLY-RIGHT-NOW.
#
# Q8: "What are the differences between a bytes object and a string?"
#
#   STRING, str, a sequence of unicode CHARACTERS, letters, emoji, whatever, it's TEXT.
#   BYTES, a sequence of INTEGERS from 0 to 255, raw data, written like b'hello'.
#   To go string->bytes you ENCODE: 'hi'.encode('utf-8'). To go bytes->string you
#   DECODE: b'hi'.decode('utf-8'). You CAN'T just add 'em together, 'abc' + b'abc' is a
#   TypeError, NO-MIXING-NO-MIXING. Index a string, you get a one-character STRING;
#   index a bytes object, you get an INT. And both are IMMUTABLE, can't-change-'em,
#   kinda-like-how-I-can't-change-the-fact-that-I-had-THREE-COFFEES-before-this-sale.
#
# Q9: "What is a hash function?"
#
#   HASH-FUNCTION-HASH-FUNCTION, takes ANY amount of data, big-small-whatever, and
#   crunches it down to a FIXED-SIZE value called a HASH. Same input, SAME hash, EVERY
#   time, guaranteed. Change even ONE little byte and you get a TOTALLY different hash.
#   Good ones make it really hard to find two different inputs with the same hash, a
#   "collision." Python uses hashing for DICTIONARY keys and SETS, that's-why-lookups-
#   are-so-FAST, and the chapter uses it to check whether two files are the SAME without
#   comparing every byte against every other file. FAST-LIKE-ME-GETTING-TO-THE-RESTROOM-
#   THE-SECOND-THIS-HAMMER-COMES-DOWN.
#
# Q10: "What is an MD5 digest?"
#
#   LAST LOT, FOLKS, LAST LOT, THANK GOODNESS. MD5 is a particular HASH FUNCTION, makes
#   a 128-bit hash, and the "DIGEST" is that hash, usually shown as a 32-character
#   HEXADECIMAL string, like '1a79a4d60de6718e8e5b326e338ae533'. In the chapter,
#   md5_digest opens a file in BINARY mode, feeds the bytes to hashlib.md5(), and calls
#   hexdigest() to get the string. Two files with the same digest are almost surely
#   identical, GREAT for finding DUPLICATE photos. BUT, folks, MD5 is BROKEN for
#   SECURITY, people can make collisions on purpose, so don't use it for passwords or
#   signatures, use SHA-256 for that. For catching duplicates though? FINE-FINE-FINE.
#
#   GOING ONCE... GOING TWICE... SOLD! Auction's over, everybody, PLEASE STEP ASIDE,
#   OUTTA-THE-WAY-OUTTA-THE-WAY-OUTTA-THE-WAAAAAY...


